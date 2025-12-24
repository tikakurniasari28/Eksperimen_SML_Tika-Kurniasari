from prometheus_client import start_http_server, Gauge
import time
import random

metrics = {
    "model_mse": Gauge("model_mse", "Mean Squared Error"),
    "model_r2": Gauge("model_r2", "R2 Score"),
    "model_loss": Gauge("model_loss", "Loss"),
    "request_latency": Gauge("request_latency_seconds", "Latency"),
    "request_count": Gauge("request_count", "Request Count"),
    "cpu_usage": Gauge("cpu_usage_percent", "CPU Usage"),
    "memory_usage": Gauge("memory_usage_mb", "Memory Usage"),
    "prediction_value": Gauge("prediction_value", "Prediction Output"),
    "data_drift": Gauge("data_drift_score", "Data Drift"),
    "model_confidence": Gauge("model_confidence", "Confidence")
}

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        metrics["model_mse"].set(random.uniform(0.01, 0.03))
        metrics["model_r2"].set(random.uniform(0.8, 0.95))
        metrics["model_loss"].set(random.uniform(0.1, 0.3))
        metrics["request_latency"].set(random.uniform(0.1, 1.5))
        metrics["request_count"].inc()
        metrics["cpu_usage"].set(random.uniform(30, 70))
        metrics["memory_usage"].set(random.uniform(200, 500))
        metrics["prediction_value"].set(random.uniform(0, 1))
        metrics["data_drift"].set(random.uniform(0, 1))
        metrics["model_confidence"].set(random.uniform(0.7, 0.99))
        time.sleep(5)
