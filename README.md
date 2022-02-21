# shortlyplus
overkill version of [shortlyyy](https://github.com/sainad2222/shortLY)

## URL Shortener designed with Microservices architecture

### System Architecture
![](https://user-images.githubusercontent.com/44405294/155005627-a98039b9-2f9f-4030-a411-1e432cfb0621.png)

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
