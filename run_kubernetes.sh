#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=sounditi/prediction-api

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run prediction --image=${dockerpath} --labels="tag=flask-app"

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward prediction-7f7c65ccdd-b7jxm 5001:80 
