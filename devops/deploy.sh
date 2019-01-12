#!/bin/bash

set -e

echo "PUSHING DOCKER IMAGES TO REMOTE"
docker push gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}
docker push gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}

yes | gcloud beta container images add-tag gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:$TRAVIS_COMMIT gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}:$TRAVIS_COMMIT gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}:latest

kubectl config view
kubectl config current-context

echo "DEPLOYING DOCKER IMAGES"

kubectl set image deployment/walshsoft-deployment web=gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:$TAG --record
kubectl set image deployment/walshsoft-deployment nginx=gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}:$TAG --record
