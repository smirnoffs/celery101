Run the web server
```bash
cd celery101/examples/02-send-emails-async-celery
uvicorn main:app --reload
```

Run Redis as a broker
```bash
docker run -d -p 6379:6379 redis
```

Run Celery
```bash
celery -A tasks worker --loglevel=INFO
```
You can also contol number of workers
```
celery -A tasks worker --loglevel=INFO --concurrency=10

Run Flower (Celery Monitoring Tool)
```bash
flower -A tasks --port=5555
```
Now Flower is available on http://localhost:5555/monitor