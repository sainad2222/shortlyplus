const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("api/api.proto",{})
const grpcObject = grpc.loadPackageDefinition(packageDef)
const proto = grpcObject.main

const client = new proto.Shortener("localhost:50051", grpc.credentials.createInsecure())

client.shortenURL({
    "url": "google.com"}
    ,(err,res) => {
        if(err){
            console.log("ERROR",err)
            return
        }
        console.log("Recived from server "+JSON.stringify(res))
    })
