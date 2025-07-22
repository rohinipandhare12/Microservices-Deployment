# MicroKube-Deploy: Deploying and Managing Microservices in a Cloud-Native Environment

This project demonstrates the migration of a monolithic application into a **microservices architecture** using **Docker** and **Kubernetes (Minikube)**. The system simulates a real-world production environment with features such as **autoscaling**, **persistent storage**, and **inter-service communication**.

---

## 📌 Project Objectives

- Containerize and deploy Flask-based microservices  
- Set up and manage a local Kubernetes cluster using Minikube  
- Implement service discovery, autoscaling, and persistent volume handling  
- Simulate a production-like microservices deployment pipeline  

---

## ⚙️ Technology Stack

| Component           | Technology / Tool           |
|---------------------|------------------------------|
| Programming         | Python (Flask)               |
| Orchestration       | Kubernetes (Minikube)        |
| Containerization    | Docker                       |
| Monitoring          | metrics-server               |
| Tools               | kubectl, hey, curl           |
| Services            | NodePort, ClusterIP          |

---

## 🧩 Microservices

- **User Service** — Handles user-related operations (Flask app)  
- **Product Service** — Handles product-related operations (Flask app)  
- **Order Service** — Manages order processing and uses persistent storage (Flask app)  

---

## 🏗️ System Architecture

+----------------------+
| End User / CLI |
+----------+-----------+
|
v
+----------+-----------+
| NodePort Service |
| (Exposes Services) |
+----------+-----------+
|
+----------+-----------+----------+
| | |
v v v
User Product Order Service
Svc Service (Flask App)
(Flask App) (Flask App) |
| |
+--------v--------+ +--------v--------+
| Horizontal Pod | | Persistent Vol. |
| Autoscaler | | + PVC Attached |
+-----------------+ +-----------------+


---

## 🔨 Implementation Steps

### ✅ Step 1: Microservices Development
- Developed 3 Flask-based services: User, Product, and Order

### ✅ Step 2: Dockerfile Creation
- Created `Dockerfile` for each service
- Installed Flask and copied application code

### ✅ Step 3: Build & Push Docker Images

docker build -t <dockerhub-username>/user-service .
docker push <dockerhub-username>/user-service
(Repeat for other services)

✅ Step 4: Kubernetes Setup

minikube start
kubectl get nodes
✅ Step 5: Create Deployments
Wrote Kubernetes Deployment YAMLs for each microservice

kubectl apply -f user-deployment.yaml
✅ Step 6: Configure Services
Used ClusterIP for internal communication

Used NodePort to expose services externally

✅ Step 7: Horizontal Pod Autoscaler

kubectl apply -f metrics-server.yaml
kubectl autoscale deployment product-deployment --cpu-percent=50 --min=1 --max=5
✅ Step 8: Persistent Volume for Order Service
Defined a PersistentVolume and PersistentVolumeClaim

Mounted it to the /data directory in the Order service pod

Verified data retention after pod restarts

✅ Results
✅ All microservices deployed and accessible via NodePort

✅ Product service successfully auto-scaled with hey load generator

✅ Order service retained data via Persistent Volume after pod deletion

✅ Inter-service communication verified (User ↔ Product ↔ Order)


📝 Conclusion
This project demonstrates how to deploy and manage microservices in a cloud-native Kubernetes environment. Key features include:

Modular service design (Flask)

Scalable deployments via HPA

Persistent storage integration

Production-like setup using open-source tools

It reflects practical cloud-native application management skills that are critical in real-world DevOps workflows.


Directory Structure

├── order-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── order-deployment.yaml
│   ├── order-service.yaml
│   └── volume.yaml
├── product-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── product-deployment.yaml
│   ├── product-hpa.yaml
│   └── product-service.yaml
└── user-service/
    ├── app.py
    ├── Dockerfile
    ├── pv-pvc.yaml
    ├── user-deployment.yaml
    └── user-service.yaml







