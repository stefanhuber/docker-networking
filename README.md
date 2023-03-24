# Docker Networking Example

## Docker Build

Build docker image for api:

```
cd api
docker build -t example-api .
```

Build docker image for client:

```
cd client
docker build -t example-client .
```

## Create Docker Newtork

```
docker network create example
```

## Docker Run

Start API:

```
docker run --name example-api-1 --network example -d example-api
```

Start Client:

```
docker run --network example -e API_URL="http://example-api-1" -it --rm example-client
```
