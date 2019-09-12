## Cấu hình cho `nginx-ingress` sử dụng `proxy protocol` với `Haproxy` để có thể lấy real ip Client khi có request vào Haproyx - > ingresss nginx
B1: Cấu hình haproxy:

```
listen application-https
    bind :443
    mode tcp
    balance roundrobin
    server k8s-master01 kmaster01:30443 check send-proxy
    server k8s-master02 kmaster02:30443 check send-proxy
    server k8s-master03 kmaster03:30443 check send-proxy
    server k8s-worker01 kworker01:30443 check send-proxy
    server k8s-worker02 kworker02:30443 check send-proxy
    server k8s-worker03 kworker03:30443 check send-proxy

listen application-http
    bind :80
    mode tcp
    balance roundrobin
    server k8s-master01 kmaster01:30080 check send-proxy
    server k8s-master02 kmaster02:30080 check send-proxy
    server k8s-master03 kmaster03:30080 check send-proxy
    server k8s-worker01 kworker01:30080 check send-proxy
    server k8s-worker02 kworker02:30080 check send-proxy
    server k8s-worker03 kworker03:30080 check send-proxy
```
B2: Enanele `use-proxy-protocol` khi cài nginx-ingress
- sử dụng file sau để install nginx-ingress:

```
controller:
  config:
    use-forwarded-headers: "true"
    compute-full-forwarded-for: "true"
    use-proxy-protocol: true
  extraArgs:
   enable-ssl-passthrough: ""
  metrics:
    enabled: true
    serviceMonitor:
      additionalLabels:
        release: argus
      enabled: true
      namespace: ""
  service:
    nodePorts:
      http: 30080
      https: 30443
    type: NodePort

```
B3: Test
- Deploy app sau để test thử

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: echoserver
  labels:
    app: echoserver
spec:
  selector:
    matchLabels:
      app: echoserver
  template:
    metadata:
      labels:
        app: echoserver
    spec:
      containers:
      - name: echoserver
        image: gcr.io/google-containers/echoserver:1.10
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          protocol: TCP
          containerPort: 8080
        resources: {}
---
apiVersion: v1
kind: Service
metadata:
  name: echoserver
  labels:
    app: echoserver
spec:
  type: ClusterIP
  selector:
    app: echoserver
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: http
---
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: echoserver
  # annotations:
  #   kubernetes.io/tls-acme: "true"
  #   certmanager.k8s.io/acme-http01-edit-in-place: "true"
  #   nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  # tls:
  # - hosts:
  #   - echo.k8s-lab.teko.vn
  #   secretName: demo-tls
  rules:
  - host: echo.k8s-lab.teko.vn
    http:
      paths:
      - backend:
          serviceName: echoserver
          servicePort: http
```
## Tạo file config và cấp quyền cho user truy cập vào k8s
- Bài toán: Cung cấp file config kubectl cho Dev để truy cập vào cụm k8s nhưng với quyền chỉ thao tác với `configmaps`trên namespace `identity-service`
B1: Chạy script như hướng dẫn: https://github.com/dangvv-teko/flask_app/blob/master/K8s/README.md
B2: Tạo role và rolebinding

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: identity-decision-maker
  namespace: identity-service
rules:
- apiGroups: 
  - ""
  resources:  
  - configmaps
  resourceNames:
  - decisions
  - oathkeeper
  verbs: 
  - create
  - get
  - watch
  - update
  - patch
  - delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: identity-decision-maker
  namespace: identity-service
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: identity-decision-maker
subjects:
- kind: ServiceAccount
  name: identity-decision-maker
  namespace: identity-service
```
