const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("../api/api.proto",{})
const grpcObject = grpc.loadPackageDefinition(packageDef)
const proto = grpcObject.main

const shortenerClient = new proto.Shortener("shortener:50051", grpc.credentials.createInsecure())
const dbClient = new proto.Database("db:50052", grpc.credentials.createInsecure())

module.exports = {
    shortenerClient: shortenerClient,
    dbClient: dbClient
}
