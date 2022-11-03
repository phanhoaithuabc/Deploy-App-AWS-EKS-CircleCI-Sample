# AWS EKS DEVOPS PROJECT

## Overview
In this project:
- Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines
- Develop a CI/CD pipeline for micro services applications with either blue/green deployment or rolling deployment.
- Develop Continuous Integration steps as you see fit, but must at least include typographical checking (aka “linting”). To make your project stand out, you may also choose to implement other checks such as security scanning, performance testing, integration testing, etc.!
- Pushing the built Docker container to the Docker repository (AWS ECR)
- Deploying these Docker container to a small Kubernetes cluster.

## Run the App:
* Run `make install` to install the necessary dependencies
* Running run.py to run the Python scripts and web app:
    - Run standalone: `python app.py`
    - Deploy to AWS EKS: `./.circleci/config.yml`

## Output:
<img src='images\all-stages-passed-success.png'>
<img src='images\Success-deploy-to-eks-cloudformation.png'>
<img src='images\Success-deploy-to-eks-cluster.png'>
<img src='images\Success-deploy-to-eks-ec2.png'>
<img src='images\Success-deploy-to-eks.png'>