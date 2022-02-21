# shortlyplus
overkill version of [shortlyyy](https://github.com/sainad2222/shortLY)

## URL Shortener designed with Microservices architecture

### System Architecture
![](https://user-images.githubusercontent.com/44405294/155006296-9a001c67-3479-4346-93dc-7c5a18831d63.png)

### Project structure
- frontend -> **React**
- backend/client -> **Nodejs**
- backend/shortener -> **Python**
- backend/db -> **Go**

### Technologies Used
- **Firestore** Cloud Database(Firebase) for Database
- **React** and **Bootstrap** for Frontend
- **gRPC** as RPC Framework(Alternative to REST)
- **Protocol Buffers** as Data format for communication between services(Alternative to JSON)
- **Docker** for containerization
- **Docker Compose** for container orchestration

### Setup Guide
#### Prerequisites
- Docker
- Docker Compose
1. Clone this repository
  `git clone https://github.com/sainad2222/shortlyplus.git`

2. cd into directory and run 
  `docker-compose up`
 

### TODO
- [ ] Add Redis layer for db service(go server)
