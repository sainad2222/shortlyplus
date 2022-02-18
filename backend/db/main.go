package main

import (
	"context"
	"db/apiPb"
	"log"
	"net"

	"google.golang.org/grpc"
)

type server struct {
	apiPb.UnimplementedDatabaseServer
}

func (s *server) CheckIfPresent(ctx context.Context, req *apiPb.CheckIfPresentRequest) (*apiPb.CheckIfPresentResponse, error) {
	dbClient, err := SetupDB()
	if err != nil {
		return &apiPb.CheckIfPresentResponse{Error: "Cannot connect to DB client"}, err
	}
	defer dbClient.Close()
	slug := req.GetSlug()
	iter := dbClient.Collection("urls").Where("slug", "==", slug).Documents(ctx)
	docCount := 0
	for {
		_, err := iter.Next()
		if err != nil {
			break
		}
		docCount += 1
	}
	var isPresent bool
	if docCount == 0 {
		isPresent = false
	} else {
		isPresent = true
	}
	return &apiPb.CheckIfPresentResponse{
		IsPresent: isPresent,
	}, nil
}

func (s *server) StoreInDB(ctx context.Context, req *apiPb.StoreInDBRequest) (*apiPb.StoreInDBResponse, error) {
	dbClient, err := SetupDB()
	if err != nil {
		return &apiPb.StoreInDBResponse{Error: "Cannot connect to DB client"}, err
	}
	defer dbClient.Close()
	url := req.GetUrl()
	slug := req.GetSlug()
	log.Println("[INFO]", url, slug)
	_, _, err = dbClient.Collection("urls").Add(ctx, map[string]interface{}{
		"url":  url,
		"slug": slug,
	})
	if err != nil {
		log.Fatalln("[ERROR] cannot insert data into db")
		return &apiPb.StoreInDBResponse{Error: "Cannot insert data into db"}, err
	}
	return &apiPb.StoreInDBResponse{
		IsSuccess: true,
	}, nil
}

func main() {
	log.Println("[INFO] firestore connected")
	lis, err := net.Listen("tcp", ":50052")
	if err != nil {
		log.Fatalln("[ERROR] Cannot listen at given port", err)
	}

	grpcServer := grpc.NewServer()
	apiPb.RegisterDatabaseServer(grpcServer, &server{})

	log.Println("[INFO] started listening on port 50052")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalln("[ERROR] cannot serve on listener", err)
	}
}
