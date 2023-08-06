import { createPromiseClient } from "@bufbuild/connect";
import { Greeter } from "./gen/greeter_connect";
import { createGrpcWebTransport } from "@bufbuild/connect-node";

const transport = createGrpcWebTransport({
    baseUrl: "http://localhost:50051",
    httpVersion: "1.1"
});

async function main() {
    const client = createPromiseClient(Greeter, transport);
    const res = await client.hello({ name: "World" });
    console.log(res);
}

main();
