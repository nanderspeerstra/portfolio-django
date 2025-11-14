#!/bin/bash
set -e

echo "Applying Kubernetes namespace..."
kubectl apply -f namespace.yaml

echo "Creating Kubernetes secret from .env.prod..."
kubectl delete secret portfolio-env --namespace=portfolio --ignore-not-found
kubectl create secret generic portfolio-env \
  --from-env-file=.env.prod \
  --namespace=portfolio

echo "Applying PersistentVolumeClaim for media..."
kubectl apply -f media-pvc.yaml

echo "Applying PersistentVolumeClaim for SQLite database..."
kubectl apply -f db-pvc.yaml

echo "Deploying application with 'latest' image tag..."
kubectl apply -f deployment.yaml

echo "Applying service..."
kubectl apply -f service.yaml

echo "Applying ingress..."
kubectl apply -f ingress.yaml

echo "Forcing rollout to pull latest image..."
kubectl patch deployment portfolio \
  -n portfolio \
  -p "{\"spec\":{\"template\":{\"metadata\":{\"annotations\":{\"date\":\"$(date +%s)\"}}}}}"

echo "Deployment complete."
