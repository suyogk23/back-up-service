# back-up-service


##command sequence
1. minikube start
2. kubectl apply -f backup_pvc.yaml
3. kubectl apply -f backup_cronjob.yaml
check if running:
kubectl get pods