# Exercise 4: Docker Networking

## Objective
To create a custom Docker bridge network and enable communication between a Flask REST API, MySQL, and Redis containers.

## Technologies Used
- Docker
- Python
- Flask
- MySQL
- Redis

## Docker Network
- **Network name:** `my-bridge-net`
- **Driver:** Bridge
- **Subnet:** `172.19.0.0/16`

## Containers

| Container | Service | Port |
|---|---|---|
| `flask` | Flask REST API | 5001 |
| `mysql` | MySQL Database | 3306 |
| `redis` | Redis Cache | 6379 |

## Implementation Steps

### 1. Create the bridge network
```bash
docker network create --driver bridge my-bridge-net
```

### 2. Build the Flask API image
```bash
docker build -t flask-api .
```

### 3. Start the MySQL container
```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=DevopsRoot123! mysql:latest
```

### 4. Start the Redis container
```bash
docker run -d --name redis --network my-bridge-net redis:latest
```

### 5. Start the Flask container
```bash
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

## API Testing

Open the following URL in a browser:

`http://localhost:5001/about`

Expected response:

```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

## Network Connectivity Testing

Commands used inside the Flask container:

```bash
ping -c 5 mysql
ping -c 5 redis
```

Both containers were tested from Flask using ping.

The Flask container was also able to establish TCP connections to MySQL on port 3306 and Redis on port 6379.

## Useful Docker Commands

```bash
docker ps
docker network ls
docker network inspect my-bridge-net
docker logs flask
```

## Key Learnings
- Creating a custom bridge network.
- Connecting multiple containers to the same network.
- Using container names for network communication.
- Publishing a container port to access an API from the host machine.
- Testing connectivity between containers.
