# Scale Launch Custom Image Minimal Example

See [here](https://scaleapi.github.io/launch-python-client/guides/custom_docker_images/) for general documentation.

## Setup

To setup the python environment locally, do 

```
pip install -r requirements.txt
pip install -r requirements_client.txt
pip install -e .

```

from the root directory.

You can run 

```
uvicorn server:app --port 5005 --host ::
```

from the root directory as well if you want to test changes locally

## Building/Pushing/Running Locally

To build, run `docker build -f Dockerfile -t $REPO:$TAG .` from the root directory. Pushing the docker image
is functionality we will need to build, but conceptually it is very similar to `docker push`.

To run the image locally:
`docker run -p 5005:5005 --net=host <Image ID> dumb-init -- uvicorn launch_image_minimal_example.server:app --port 5005 --host ::`

You can now make requests locally:
`curl -H "Content-Type: application/json" -d '{"url": "test1"}' http://localhost:5005/predict`

## Deploying to Scale Launch

`launch_image_minimal_example/deploy.py` contains code that demonstrate how one would create a bundle + endpoint using the Launch client.
The code isn't currently functional, but does show the API that we would like to provide for bundle creation. Endpoint creation is not used for the Launch/Nucleus integration