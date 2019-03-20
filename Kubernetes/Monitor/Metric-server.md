## Cài đặt
- Clone repo này về:

`git clone https://github.com/kubernetes-incubator/metrics-server.git`

- Thay thế file `metrics-server/deploy/1.8+/metrics-server-deployment.yaml` bằng nội dung:

```
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: metrics-server
  namespace: kube-system
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: metrics-server
  namespace: kube-system
  labels:
    k8s-app: metrics-server
spec:
  selector:
    matchLabels:
      k8s-app: metrics-server
  template:
    metadata:
      name: metrics-server
      labels:
        k8s-app: metrics-server
    spec:
      serviceAccountName: metrics-server
      volumes:
      # mount in tmp so we can safely use from-scratch images and/or read-only containers
      - name: tmp-dir
        emptyDir: {}
      containers:
      - name: metrics-server
        image: k8s.gcr.io/metrics-server-amd64:v0.3.0
        imagePullPolicy: Always
        command:
        - /metrics-server
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP
        volumeMounts:
        - name: tmp-dir
          mountPath: /tmp
```

- Sau đó:

```
systemctl restart kubelet.service
systemctl restart docker.serivice
```
- Test Metric-server

`kubectl top node`

