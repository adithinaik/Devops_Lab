
# Exercise 3: Scaling Flask App Using Kubernetes ReplicaSets

## Objective
Deploy a Flask-based flash sale application on a single-node Minikube cluster, scale the application using a Kubernetes ReplicaSet, and verify automatic pod recovery.

## Technologies Used
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Application Features
- `/` — Displays a welcome message, pod hostname, and timestamp.
- `/buy?user=Adithi` — Simulates a purchase and identifies the serving pod.
- `/health` — Health endpoint used by Kubernetes probes.

## Kubernetes Configuration
- ReplicaSet: `flashsale-rs`
- Service: `flashsale-svc`
- Initial replicas: 3
- Scaled replicas: 5
- Container port: 5000
- Readiness and liveness probes: `/health`
- Resource requests and limits configured for CPU and memory.

## Implementation

### 1. Build the Docker image
```bash
docker build -t flashsale:1.0 .
```

### 2. Load the image into Minikube
```bash
minikube image load flashsale:1.0
```

### 3. Deploy the ReplicaSet and Service
```bash
kubectl apply -f flashsale-replicaset.yaml
```

### 4. Verify the pods
```bash
kubectl get pods -l app=flashsale
```

### 5. Scale to five replicas
```bash
kubectl scale rs flashsale-rs --replicas=5
```

### 6. Test automatic pod recovery
Delete one pod using its actual name:
```bash
kubectl delete pod <pod-name>
```

Verify that the ReplicaSet creates a replacement:
```bash
kubectl get pods -l app=flashsale
```

### 7. Access the application
```bash
kubectl port-forward service/flashsale-svc 8090:80
```

Open `http://127.0.0.1:8090/` in a browser.

## Results
- The application image was built and loaded into Minikube.
- Three replicas started successfully and were scaled to five.
- All five pods were observed running on the Minikube node.
- Deleting a pod triggered automatic replacement.
- The homepage, purchase endpoint, and health endpoint returned successful responses.
- Ten repeated homepage requests returned valid JSON responses.

## Key Learning
A Kubernetes ReplicaSet maintains the desired number of pod replicas. If a pod is deleted, Kubernetes creates a replacement. A Kubernetes Service provides a stable endpoint for accessing the application.

## Future Improvements
- Verify load distribution across different pods.
- Push the Docker image to Docker Hub.
- Add monitoring and request metrics.
