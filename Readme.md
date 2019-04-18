# Guessit API

### Build

```sh
docker build -t guessit .
```

### Launch

```sh
docker run -it --rm -p 127.0.0.1:5000:5000 --name guessit guessit
```

### Use

#### GET

```sh
curl http://localhost:5000/guess/your.filename.mp4
```

#### POST

```sh
curl \
  -H "content-type: application/json" \
  -X POST \
  --data '{"name":"your.filename.mp4"}' \
  http://127.0.0.1:5000/guess
```
