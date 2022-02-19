package main

import (
	"context"
	"errors"
	"log"

	"cloud.google.com/go/firestore"
	firebase "firebase.google.com/go"
	"google.golang.org/api/option"
)

func SetupDB() (*firestore.Client, error) {
	ctx := context.Background()
	// sa := option.WithCredentialsFile(os.Getenv("FIREBASE_SHORTLYPLUS"))
	sa := option.WithCredentialsFile("shortlyplus.firebase.json")
	app, err := firebase.NewApp(ctx, nil, sa)
	if err != nil {
		log.Fatalln("[ERROR]", err)
		return nil, errors.New("Cannot initialize new firebase app")
	}

	client, err := app.Firestore(ctx)
	if err != nil {
		log.Fatalln("[ERROR]", err)
		return nil, errors.New("Cannot create firestore client")
	}
	return client, nil
}
