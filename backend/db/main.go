package main

import (
	"context"
	"log"
	"net"
	"os"

	"cloud.google.com/go/firestore"

	"db/apiPb"

	"google.golang.org/grpc"
)

type server struct {
	apiPb.UnimplementedDatabaseServer
	dbClient *firestore.Client
	dbErr    error
    collection string
}

func (s *server) createDBClient() {
	dbClient, err := SetupDB()
	s.dbClient = dbClient
	s.dbErr = err
    collection,isEnvSet := os.LookupEnv("DB_COLLECTION")
    if isEnvSet {
        s.collection = collection
    } else {
        s.collection = "urls"
    }
}

func (s *server) CheckIfPresent(ctx context.Context, req *apiPb.CheckIfPresentRequest) (*apiPb.CheckIfPresentResponse, error) {
	log.Println("[INFO] hit checkIfPresent RPC")
	if s.dbErr != nil {
		return &apiPb.CheckIfPresentResponse{Error: "Cannot connect to DB client"}, nil
	}
	slug := req.GetSlug()
	iter := s.dbClient.Collection(s.collection).Where("slug", "==", slug).Documents(ctx)
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
	log.Println("[INFO] hit StoreInDB RPC")
	if s.dbErr != nil {
		return &apiPb.StoreInDBResponse{Error: "Cannot connect to DB client"}, nil
	}
	url := req.GetUrl()
	slug := req.GetSlug()
	_, _, err := s.dbClient.Collection(s.collection).Add(ctx, map[string]interface{}{
		"url":  url,
		"slug": slug,
	})
	if err != nil {
		log.Fatalln("[ERROR] cannot insert data into db")
		return &apiPb.StoreInDBResponse{Error: "Cannot insert data into db"}, nil
	}
	return &apiPb.StoreInDBResponse{
		IsSuccess: true,
	}, nil
}

type shortURL struct {
	Url  string `firestore:"url,omitempty"`
	Slug string `firestore:"slug,omitempty"`
}

func (s *server) FetchURLFromSlug(ctx context.Context, req *apiPb.FetchURLFromSlugRequest) (*apiPb.FetchURLFromSlugResponse, error) {
	log.Println("[INFO] hit FetchURLFromSlug RPC")
	if s.dbErr != nil {
		return &apiPb.FetchURLFromSlugResponse{Error: "Cannot connect to DB client"}, nil
	}
	slug := req.GetSlug()
	iter := s.dbClient.Collection(s.collection).Where("slug", "==", slug).Documents(ctx)
	for {
		doc, err := iter.Next()
		if err != nil {
			return &apiPb.FetchURLFromSlugResponse{Error: "Slug not present in DB"}, nil
		}
		var url shortURL
		if err := doc.DataTo(&url); err != nil {
			return &apiPb.FetchURLFromSlugResponse{Error: "Error converting to struct"}, nil
		}
		return &apiPb.FetchURLFromSlugResponse{URL: url.Url}, nil
	}
}

func main() {
	log.Println("[INFO] firestore connected")
	lis, err := net.Listen("tcp", ":50052")
	if err != nil {
		log.Fatalln("[ERROR] Cannot listen at given port", err)
	}

	grpcServer := grpc.NewServer()
	s := server{}
	s.createDBClient()
	apiPb.RegisterDatabaseServer(grpcServer, &s)

	log.Println("[INFO] started listening on port 50052")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalln("[ERROR] cannot serve on listener", err)
	}
}
