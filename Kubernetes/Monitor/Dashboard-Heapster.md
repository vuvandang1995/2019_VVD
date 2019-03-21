## Cài Heapster
- https://www.cnblogs.com/vincenshen/p/9638162.html
- Hoặc chạy duy nhất file này:

`vim heapster.yaml`

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: system:heapster
rules:
- apiGroups:
  - ""
  resources:
  - events
  - namespaces
  - nodes
  - pods
  - nodes/stats
  verbs:
  - create
  - get
  - list
  - watch
- apiGroups:
  - extensions
  resources:
  - deployments
  verbs:
  - get
  - list
  - watch

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: heapster
  namespace: kube-system

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: heapster
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:heapster
subjects:
- kind: ServiceAccount
  name: heapster
  namespace: kube-system

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: heapster
  namespace: kube-system
spec:
  replicas: 1
  selector:
      matchLabels:
        k8s-app: heapster
  template:
    metadata:
      labels:
        task: monitoring
        k8s-app: heapster
    spec:
      serviceAccountName: heapster
      containers:
      - name: heapster
        # image: k8s.gcr.io/heapster-amd64:v1.5.4 将默认google的官方镜像替换为阿里云镜像，否则你懂得
        image: registry.cn-hangzhou.aliyuncs.com/google_containers/heapster-amd64:v1.5.4
        command:
        - /heapster
        - --source=kubernetes:https://kubernetes.default?useServiceAccount=true&kubeletHttps=true&kubeletPort=10250&insecure=true
---
apiVersion: v1
kind: Service
metadata:
  labels:
    task: monitoring
    # For use as a Cluster add-on (https://github.com/kubernetes/kubernetes/tree/master/cluster/addons)
    # If you are NOT using this as an add-on, you should comment out this line.
    kubernetes.io/cluster-service: 'true'
    kubernetes.io/name: Heapster
  name: heapster
  namespace: kube-system
spec:
  ports:
  - port: 80
    targetPort: 8082
  selector:
    k8s-app: heapster
```
## Cài Dashboard
- Link hướng dẫn gốc: https://github.com/kubernetes/dashboard/blob/master/README.md
- Tạo file `dashboard-admin.yaml` định nghĩa các quyền cho user admin
`vim dashboard-admin.yaml`
- Điền thông tin sau:
```
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-dashboard
  labels:
    k8s-app: kubernetes-dashboard
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kubernetes-dashboard
  namespace: kube-system
```
- Chạy lệnh sau để deploy cái ClusterRoleBinding trên: `kubectl create -f dashboard-admin.yaml`
- Cài Dashboad bằng lệnh sau:
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml`
- **Lúc này, pod Dashboad đã được tạo ra nằm trên namespace kube-system, đọc ở link gốc sẽ hiểu**
- Chạy lệnh sau để sửa cấu hình Dashboard để nat port ra ngoài:
`kubectl -n kube-system edit service kubernetes-dashboard`
- Sau khi chạy lệnh trên, bạn sẽ được ở 1 file config bằng trình soạn thảo `vim`, hãy sửa dòng **type: ClusterIP** thành **type: NodePort** và lưu lại
- Chạy lệnh `kubectl -n kube-system get pods` để xem pod Dashboard là gì. ví dụ:

<img src="https://i.imgur.com/lxrpGDv.png">

- Sau đó chạy lệnh `kubectl -n kube-system get secret` để show ra các secret

<img src="https://i.imgur.com/Mg310Hx.png">
    
- Lựa chọn `kubernetes-dashboard-token...` và chạy lệnh `kubectl -n kube-system describe secret kubernetes-dashboard-token-...` để xem token

<img src="https://i.imgur.com/E3mFvTa.png">

- Chạy lệnh `kubectl -n kube-system get services` để biết port được nat ra ngoài là port nào

<img src="https://i.imgur.com/0UdSbFl.png">

- Sau đó dùng token bên trên và 1 trong các địa chỉ IP của các node trong cụm Cluster để đăng nhập và dashboard, nhớ là https nhé: https://192.168.40.182:30324


