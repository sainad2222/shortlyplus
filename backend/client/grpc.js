const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("../api/api.proto",{})
const grpcObject = grpc.loadPackageDefinition(packageDef)
const proto = grpcObject.main

const client = new proto.Shortener("shortener:50051", grpc.credentials.createInsecure())

module.exports = client;
