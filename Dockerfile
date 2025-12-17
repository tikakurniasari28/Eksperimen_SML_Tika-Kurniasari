FROM continuumio/miniconda3:latest

WORKDIR /app

COPY . .

RUN conda env create -f Workflow-CI/MLProject/environment.yml || true

SHELL ["conda", "run", "-n", "mlflow-env", "/bin/bash", "-c"]

# Install mlflow global (jaga2)
RUN pip install mlflow==2.9.2

# Jalankan training MLFlow ketika container dipanggil
CMD ["conda", "run", "-n", "mlflow-env", "mlflow", "run", "Workflow-CI/MLProject"]
