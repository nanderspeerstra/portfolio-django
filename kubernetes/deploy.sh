#!/bin/bash

set -e

echo "Applying Kubernetes namespace..."
kubectl apply -f namespace.yaml

echo "Applying PersistentVolumeClaim for media..."
kubectl apply -f media-pvc.yaml

echo "Deploying application with 'latest' image tag..."
kubectl apply -f deployment.yaml

echo "Applying service..."
kubectl apply -f service.yaml

echo "Applying ingress..."
kubectl apply -f ingress.yaml

echo "Deployment complete."
