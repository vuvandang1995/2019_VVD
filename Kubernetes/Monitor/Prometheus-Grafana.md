## Prometheus là gì?
- https://github.com/locvx1234/prometheus-notes
## Cài Prometheus + grafana trên K8s
- Tham khảo: https://hub.helm.sh/charts/stable/prometheus-operator?fbclid=IwAR0dtJQxzrS5Dsk5uG0-kanolQCsm8kIjG8Zx4NsyKJElt7jNzM_luvs9Ck
- Cài đặt:

```
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/master/example/prometheus-operator-crd/alertmanager.crd.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/master/example/prometheus-operator-crd/prometheus.crd.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/master/example/prometheus-operator-crd/prometheusrule.crd.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/master/example/prometheus-operator-crd/servicemonitor.crd.yaml
```

`helm install --name my-release stable/prometheus-operator --set prometheusOperator.createCustomResource=false`

- NodePort service này để truy cập vào Prometheus

`kubectl edit svc my-release-prometheus-oper-operator`

- NodePort server này để truy cập Grafana

`kubectl edit svc my-release-grafana`

