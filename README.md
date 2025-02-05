# back-up-service


WEEK-1:

>Created a GCP account and set up google-drive api
>
>Created a python script to backup files from "backupfiles" directory
>
>Created a docker container to run this script with necessary dependencies installed


WEEK-2:

>Created a GCP account and set up google-drive api
>
>Created a python script to backup files from "backupfiles" directory
>
>Created a docker container to run this script with necessary dependencies installed

WEEK-3:

>set up cronjob in kubernetes
>
>set up logging

##command sequence
1. minikube start
2. kubectl apply -f backup_pvc.yaml
3. kubectl apply -f backup_cronjob.yaml
check if running:
kubectl get pods


* * * * * /Users/suyog_k/Desktop/CC/back-up-service/log_jobs.sh
