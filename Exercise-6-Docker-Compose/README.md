# Exercise 6: Real-Time Operations Monitoring and Alerting

## Project Overview

This project demonstrates real-time monitoring and alerting for a simulated ZAPPTTO delivery service using Python, Docker, Prometheus, and Grafana.

The Python application generates simulated delivery metrics. Prometheus collects these metrics and evaluates alert rules, while Grafana provides dashboards for monitoring delivery operations and performance.

## Objectives

- Develop a Python application that exposes delivery metrics.
- Containerize the application using Docker.
- Run multiple services using Docker Compose.
- Collect and monitor metrics using Prometheus.
- Visualize delivery metrics using Grafana.
- Configure alert rules for pending deliveries and average delivery time.
- Include a Jenkins pipeline definition for configuration validation and image building.

## Technologies Used

- Python
- Docker
- Docker Compose
- Prometheus
- Grafana
- PromQL
- Jenkins

## Project Architecture

1. The Python application generates simulated delivery data.
2. The application exposes metrics on port `8000`.
3. Prometheus scrapes the metrics every 5 seconds.
4. Prometheus evaluates alert rules for delivery conditions.
5. Grafana connects to Prometheus to visualize the metrics.

## Metrics Monitored

| Metric | Description |
|---|---|
| `total_deliveries` | Total simulated deliveries |
| `pending_deliveries` | Number of pending deliveries |
| `on_the_way_deliveries` | Number of deliveries on the way |
| `average_delivery_time_sum` | Cumulative sum of observed delivery times |
| `average_delivery_time_count` | Number of observed delivery times |

The average delivery time is calculated using:

`average_delivery_time_sum / average_delivery_time_count`

## Alert Rules

### High Pending Deliveries
- Condition: `pending_deliveries > 10`
- Duration: 15 seconds
- Severity: Warning

### High Average Delivery Time
- Condition: Average delivery time greater than 30 seconds
- Duration: 15 seconds
- Severity: Critical

These alerts are evaluated by Prometheus using the rules defined in `alert_rules.yml`.

## Project Files

- `delivery_metrics.py` — Generates and exposes delivery metrics.
- `Dockerfile` — Builds the Python metrics container.
- `docker-compose.yml` — Runs the application, Prometheus, and Grafana.
- `prometheus.yml` — Configures metric collection.
- `alert_rules.yml` — Defines monitoring alerts.
- `Jenkinsfile` — Defines pipeline stages for Compose validation and image building.
- `screenshots/` — Evidence of monitoring and visualization.

## How to Run

Run the following commands from this project directory.

### 1. Validate the Docker Compose configuration

```bash
docker compose config --quiet
```

### 2. Build the application image

```bash
docker compose build delivery-metrics
```

### 3. Start the services

```bash
docker compose up -d
```

### 4. Check service status

```bash
docker compose ps
```

### 5. Access the services

- Python metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Prometheus targets: http://localhost:9090/targets
- Prometheus alerts: http://localhost:9090/alerts
- Grafana: http://localhost:3000

### 6. Stop the services

```bash
docker compose down
```

## Testing and Validation

The project was tested by starting the Docker Compose services, checking container status, verifying the Prometheus delivery-service target, querying delivery metrics, viewing Grafana visualizations, and checking the configured alert rules.

The delivery data is simulated for demonstration purposes and does not represent live customer or delivery-system data.

## Future Improvements

- Integrate a production-ready notification channel for alerts.
- Add automated testing to the CI pipeline.
- Configure Jenkins to execute the pipeline automatically.
- Use persistent storage and production-ready deployment settings.
- Replace simulated delivery data with real application metrics.

## Author

Adithi Naik

BMS College of Engineering
