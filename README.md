# Medi-now!

## Deployment steps

* Step 1: Build the [image](https://hub.docker.com/r/team2interiit22/mercari-hms)

```ps1
docker build -t team2interiit22/mercari-hms:0.1.0 .
```

* Step 2: Run the services (assuming image is located in the repository called)

```ps1
kubectl apply -f services/django/
kubectl apply -f services/elasticache/
kubectl apply -f services/postgres/
kubectl apply -f services/postgres/
kubectl apply -f services/rds/
kubectl apply -f services/redis/
```
