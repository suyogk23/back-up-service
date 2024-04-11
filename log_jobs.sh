#!/bin/bash

# Timestamp for log entry
timestamp=$(date +"%Y-%m-%d %T")

# Execute kubectl get jobs and append the output to the log file
kubectl get jobs >> /Users/suyog_k/Desktop/CC/back-up-service/master_log.log

# Add a timestamp to the log entry
echo "----------------------------------------" >> /Users/suyog_k/Desktop/CC/back-up-service/master_log.log
echo "Timestamp: $timestamp" >> /Users/suyog_k/Desktop/CC/back-up-service/master_log.log
echo "----------------------------------------" >> /Users/suyog_k/Desktop/CC/back-up-service/master_log.log

