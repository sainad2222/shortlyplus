#!/bin/bash
protoc -I ../api --go_out=. ../api/api.proto
protoc -I ../api --go-grpc_out=. ../api/api.proto
