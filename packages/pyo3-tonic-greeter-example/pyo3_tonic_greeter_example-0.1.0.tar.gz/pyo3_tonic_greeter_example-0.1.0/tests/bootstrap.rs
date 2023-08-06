use std::path::PathBuf;

#[test]
fn bootstrap() {
    let protos = &["proto/greeter.proto"];
    let includes = &["proto"];

    let out_dir = PathBuf::from(std::env!("CARGO_MANIFEST_DIR"))
        .join("src")
        .join("generated");

    tonic_build::configure()
        .build_client(false)
        .build_server(true)
        .out_dir(out_dir)
        .compile(protos, includes)
        .unwrap();
}
