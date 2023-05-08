# Kubernetes commands

## Generate "default" definitions for various objects

```bash
$ kubectl create service clusterip backend-svc --tcp=5040:5000 --dry-run=client -o yaml > cl-svc.yaml
$ kubectl create secret generic backend-sec --dry-run=client -o yaml > sec.yaml
$ kubectl create cm my-cm --dry-run=client -o yaml > cm.yaml
$ kubectl create deployment frontend-deploy --image=nginx --dry-run=client -o yaml  > deploy.yaml
```

## Set up a namespace for the project and set it as default

```bash
$ kubectl create ns movies-app-ns

$ kubectl config current-context
$ kubectl config set-context <curr context> --namespace=movies-app-ns
$ kubectl config view
```

## Deploy to a Kubernetes cluster

```bash
$ kubectl create -f backend\backend-cm.yaml
$ kubectl create -f backend\backend-sec.yaml
$ kubectl create -f backend\backend-deploy.yaml
$ kubectl create -f backend\backend-svc.yaml
$ kubectl get all
$ kubectl describe svc backend-svc
```

## Get the URL to access the app in a minikube cluster

```bash
$ minikube service frontend-svc --url
```

