# Exercise 1: Hello Pod — Kubernetes

## Business Problem

The Zepto storefront needs a web application that can run inside a container and be accessed by customers. In this exercise, Nginx is used to simulate the storefront web server.

## Objective

- Deploy an Nginx container as a Kubernetes Pod.
- Expose the Pod through a NodePort Service.
- Access the Nginx welcome page in a web browser.
- Manage project files using Git and GitHub from the terminal.

## Technologies Used

- Kubernetes
- Minikube
- Docker
- Nginx
- kubectl
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
Exercise-1-Hello-Pod/
├── README.md
├── pod.yaml
└── service.yaml
```

## Prerequisites

- Docker Desktop
- Minikube
- kubectl
- Git
- Visual Studio Code

## Deployment Instructions

### 1. Start the Kubernetes cluster

```bash
minikube start --driver=docker
```

### 2. Deploy the Pod

```bash
kubectl apply -f pod.yaml
```

### 3. Verify the Pod

```bash
kubectl get pods
```

### 4. Create the Service

```bash
kubectl apply -f service.yaml
```

### 5. Verify the Service

```bash
kubectl get services
```

### 6. Access the application

```bash
minikube service hello-k8s
```

The Nginx welcome page should open in a browser if the Pod is running correctly.

## Cleanup

To remove the resources created by this exercise:

```bash
kubectl delete -f service.yaml
kubectl delete -f pod.yaml
```

## Learning Outcome

This exercise demonstrates how to deploy a containerized web server as a Kubernetes Pod and expose it through a Service.
