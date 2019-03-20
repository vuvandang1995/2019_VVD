## Cài đặt EFK
- **Lưu ý: dùng (Helm)[https://github.com/vuvandang1995/2019_VVD/blob/master/Kubernetes/Heml.md] để cài nhé**
```
kubectl create ns kube-logging
helm install --name log-elasticsearch stable/elasticsearch --namespace kube-logging --set master.persistence.enabled=false --set data.persistence.enabled=false
helm install --name log-kibana stable/kibana --namespace kube-logging --set env.ELASTICSEARCH_URL=http://log-elasticsearch-client:9200
helm install --name log-fluent-bit stable/fluent-bit --namespace kube-logging --set backend.type=es --set backend.es.host=log-elasticsearch-client
```
