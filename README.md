# Azure Dev Ops Machine Learning

This repository contains a sample Python Flask web application and supporting files for you to build an AI application with DevOps in mind. For an AI application, there are always two streams of work, Data Scientists building machine learning models and App developers building the application and exposing it to end users to consume and test.

The target is to build a continuous integration pipeline for an AI application. 

It should look something like the following when finished:

* The pipeline kicks off for each new commit into Github
* The application securely pulls the latest ML model from an Azure Storage account and packages that as part of the application.
* Takes the latest build and packages it in a Docker container. 
* The container is then deployed using Azure container service (ACS) and images are securely stored in Azure container registry (ACR). Note ACS is running Kubernetes for managing the container cluster but you can choose Docker Swarm or Mesos.
* The deployed application has the app code and ML model packaged as single container.

This process decouples the app developers and data scientists, to make sure that their production app is always running the latest code with latest ML model.

A variation to this could be consuming the ML application as an endpoint instead of packaging it in the app. The goal is ultimately to show how easy it is do devops for an AI application.

Details about the code repository
* flaskwebapp - contains the application code.
* deploy.yaml - used while deploying on Kubernetes ACS cluster.
* downloadblob.sh - script to download pretrained model and supporting files.
