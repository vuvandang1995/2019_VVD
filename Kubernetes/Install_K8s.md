# Cài đặt Kubernetes
## 1. Môi trường
  - Ubuntu 16.04 - 3 node (k8s-master, k8s-node1, k8s-node2)
  - Docker version: 18.06.1-ce
  - Kubernetes version: 
## 2. Mô hình và IP

<img src="">

- Cấu hình tối thiểu:
  - K8s-master: 4 GB ram, 2 CPU, 40 GB disk
  - K8s-node1: 4 GB ram, 2 CPU, 40 GB disk
  - K8s-node2: 4 GB ram, 2 CPU, 40 GB disk
## 3. Chuẩn bị
- Đặt hostname, ip cho các node
- ssh với tài khoản **root** và thực hiện
### 3.1 k8s-master
  - Update:
  ```
  apt-get update -y && apt-get upgrade -y
  apt-get -y install -y vim curl wget 
  apt-get -y install byobu
  ```
