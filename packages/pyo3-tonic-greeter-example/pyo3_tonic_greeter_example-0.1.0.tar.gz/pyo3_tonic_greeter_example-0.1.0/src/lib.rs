use std::net::{Ipv4Addr, SocketAddr};

use pyo3::prelude::*;
use tonic::{transport::Server, Request, Response, Status};
use tonic_web::GrpcWebLayer;
use tower_http::cors;

mod pb {
    include!("generated/greeter.v1.rs");
}

#[pyclass]
#[derive(Debug, Clone)]
struct HelloRequest {
    #[pyo3(get, set)]
    name: String,
}

#[pymethods]
impl HelloRequest {
    #[new]
    fn new(name: String) -> Self {
        Self { name }
    }
}

impl From<pb::HelloRequest> for HelloRequest {
    fn from(request: pb::HelloRequest) -> Self {
        Self { name: request.name }
    }
}

#[pyclass]
#[derive(Debug, Clone)]
struct HelloResponse {
    #[pyo3(get, set)]
    message: String,
}

#[pymethods]
impl HelloResponse {
    #[new]
    fn new(message: String) -> Self {
        Self { message }
    }
}

impl From<HelloResponse> for pb::HelloResponse {
    fn from(response: HelloResponse) -> Self {
        Self {
            message: response.message,
        }
    }
}

struct GreeterService {
    hello: PyObject,
}

#[tonic::async_trait]
impl pb::greeter_server::Greeter for GreeterService {
    async fn hello(
        &self,
        request: Request<pb::HelloRequest>,
    ) -> Result<Response<pb::HelloResponse>, Status> {
        let request = request.into_inner();
        let response = Python::with_gil(|py| {
            self.hello
                .call1(py, (HelloRequest::from(request),))?
                .extract::<HelloResponse>(py)
        })
        .map_err(|e| Status::aborted(e.to_string()))?;
        Ok(Response::new(response.into()))
    }
}

#[pyfunction]
#[pyo3(signature = (hello, port=50051))]
fn serve_greeter(py: Python, hello: PyObject, port: u16) -> PyResult<&PyAny> {
    let addr = SocketAddr::from((Ipv4Addr::UNSPECIFIED, port));
    let service = pb::greeter_server::GreeterServer::new(GreeterService { hello });

    pyo3_asyncio::tokio::future_into_py(py, async move {
        let allow_cors = cors::CorsLayer::new()
            .allow_origin(cors::Any)
            .allow_headers(cors::Any)
            .allow_methods(cors::Any);
        Server::builder()
            .accept_http1(true)
            .layer(allow_cors)
            .layer(GrpcWebLayer::new())
            .add_service(service)
            .serve(addr)
            .await
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
        Ok(())
    })
}

#[pymodule]
fn pyo3_tonic_greeter_example(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<HelloRequest>()?;
    m.add_class::<HelloResponse>()?;
    m.add_function(wrap_pyfunction!(serve_greeter, m)?)?;
    Ok(())
}
