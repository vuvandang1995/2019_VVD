## Lí thuyết
- Helm có 2 phần, phần client là helm, còn server là 1 pod ở trong k8s cluster tên là tiller
## Cài đặt
- Cài server tiller
  - Tạo file `rbac-config.yaml` với nội dung sau:

  ```
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    name: tiller
    namespace: kube-system
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    name: tiller
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: cluster-admin
  subjects:
    - kind: ServiceAccount
      name: tiller
      namespace: kube-system
  ```

  `kubectl apply -f rbac-config.yaml`

  `helm init --service-account tiller --history-max 200`

- Cài Client (helm)

`curl https://raw.githubusercontent.com/helm/helm/master/scripts/get | sudo bash`

