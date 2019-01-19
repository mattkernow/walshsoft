#!/bin/bash

set -e

if [[ -z ${DEPLOY_TAG} ]]; then
    echo "PUSHING DOCKER IMAGES TO REMOTE..."
    docker push gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}
    docker push gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}

    yes | gcloud beta container images add-tag gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:$TRAVIS_COMMIT gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:latest
    yes | gcloud beta container images add-tag gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}:$TRAVIS_COMMIT gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}:latest
fi

kubectl config current-context

echo "PERFORM ROLLING UPDATE..."

kubectl set image deployment/walshsoft-deployment web=gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:$TAG --record
kubectl set image deployment/walshsoft-deployment nginx=gcr.io/${PROJECT_NAME}/${NGINX_DOCKER_IMAGE_NAME}:$TAG --record

echo "RUNNING INTEGRATION TESTS POST DEPLOYMENT"
sleep 60
docker run --rm --env POSTCODE_HOST=35.228.129.21 --env POSTCODE_PORT=80 gcr.io/${PROJECT_NAME}/${WEB_DOCKER_IMAGE_NAME}:$TAG /bin/sh -c "pytest --disable-pytest-warnings /code/postcode_api/tests/tests_integration"
