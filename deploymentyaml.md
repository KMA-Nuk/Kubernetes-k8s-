apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-api-deployment
  labels:
    environment: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-api
  template:
    metadata:
      labels:
        app: flask-api
    spec:
      containers:
      - name: flask-api
        image: nghia5/flask-api:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "256Mi"
            cpu: "500m"
          limits:
            memory: "512Mi"
            cpu: "1"
            - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
          resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"