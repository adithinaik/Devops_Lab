
# Exercise 10: Multi-Node Kubernetes Cluster

## Overview
Deployed two Flask applications on a three-node Minikube Kubernetes cluster using Docker images, Deployments, pod anti-affinity, and NodePort Services.

## Applications

### 1. Product Catalog
- Docker image: `product-catalog:latest`
- Replicas: 2
- Endpoint: `GET /products`
- Returns a list of products with their IDs, names, and prices.

### 2. Shopping Cart
- Docker image: `shopping-cart:latest`
- Replicas: 3
- Endpoint: `GET /cart`
- Endpoint: `POST /cart`
- Supports viewing the cart and adding items.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- YAML
- PowerShell

## Kubernetes Resources
- Product Catalog Deployment
- Shopping Cart Deployment
- Product Catalog NodePort Service
- Shopping Cart NodePort Service

Pod anti-affinity was configured to distribute replicas of each application across different nodes.

## Verification
- All 5 application pods reached `Running` status.
- Product Catalog replicas ran on separate nodes.
- Shopping Cart replicas were distributed across all 3 nodes.
- Both NodePort Services were created successfully.
- `GET /products` returned 3 products.
- `GET /cart` returned the cart contents.
- `POST /cart` successfully added a Laptop to the cart.

## Important Note
The Shopping Cart uses an in-memory Python list. Each replica maintains its own separate cart, and the data is not persistent across pod restarts. A shared database would be needed for a production-ready implementation.

## Project Files
- `product_catalog.py`
- `shopping_cart.py`
- `Dockerfile.product`
- `Dockerfile.shopping`
- `product_catalog_deployment.yaml`
- `shopping_cart_deployment.yaml`
- `product_catalog_service.yaml`
- `shopping_cart_service.yaml`
- `README.md`
