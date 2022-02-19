FROM golang:1.16-alpine

WORKDIR /usr/local/app/backend/db

COPY . .

RUN go mod download

RUN go build -o /docker-db

EXPOSE 50052

CMD [ "/docker-db" ]
