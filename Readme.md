# Guessit API

### Build

```
docker build -t gregdel/guessit .
```

### Launch

```
docker run -it --rm -p 127.0.0.1:5000:5000 --name guessit gregdel/guessit
```

### Use

```
curl http://localhost:5000/guess/your.filename.mp4
```
