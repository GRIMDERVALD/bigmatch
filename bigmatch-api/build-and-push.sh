#!/bin/bash

# Script pour builder et pousser l'image Docker

# Configuration - Modifier selon votre registry
REGISTRY_URL="votre-registry.com"  # Ou docker.io pour Docker Hub
IMAGE_NAME="bigmatch-api"
TAG="latest"
FULL_IMAGE_NAME="$REGISTRY_URL/$IMAGE_NAME:$TAG"

echo "🐳 Building Docker image..."
docker build -t $FULL_IMAGE_NAME .

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    
    echo "🚀 Pushing to registry..."
    docker push $FULL_IMAGE_NAME
    
    if [ $? -eq 0 ]; then
        echo "✅ Push successful!"
        echo "Image available at: $FULL_IMAGE_NAME"
    else
        echo "❌ Push failed!"
        exit 1
    fi
else
    echo "❌ Build failed!"
    exit 1
fi