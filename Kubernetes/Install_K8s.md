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
  - Tắt tính năng **swap** của OS
    - Do **K8s** không hỗ trợ swap nên cần phải tắt swap. Thực hiện:
      - `swapoff -a`
      - Mở file `/etc/fstab` và comment dòng `/dev/mapper/master--vg-swap_1 none            swap    sw              0       0`
      
      <img src="">
      
      - Kiểm tra lại bằng lệnh: `free -m`
    - Đặt IP cho node **k8s-master** bằng cách chạy lệnh bên dưới để sửa file `/etc/network/interfaces`
      ```
      cat << EOF > /etc/network/interfaces
      # This file describes the network interfaces available on your system
      # and how to activate them. For more information, see interfaces(5).
      source /etc/network/interfaces.d/*
      # The loopback network interface
      auto lo
      iface lo inet loopback
      # The primary network interface
      auto ens3
      iface ens3 inet static
      address 192.168.40.180
      netmask 255.255.255.0
      gateway 192.168.40.1
      dns-nameservers 8.8.8.8
      EOF
      ```
    - Đặt hostname cho máy `k8s-master` bằng cách sửa nội dung các file `/etc/hosts/` và `/etc/hostname`
      - Chay lệnh dưới để khai báo hostname cho `k8s-master`
        ```
        cat << EOF > /etc/hosts
        127.0.0.1       localhost k8s-master
        192.168.40.180       k8s-master
        192.168.40.181       k8s-node1
        192.168.40.182       k8s-node2
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-master > /etc/hostname
        ```
      - Khởi động lại: `init 6`
      
### 3.2 k8s-node1
  - Update:
    ```
    apt-get update -y && apt-get upgrade -y
    apt-get -y install -y vim curl wget 
    apt-get -y install byobu
    ```
  - Tắt tính năng **swap** của OS
    - Do **K8s** không hỗ trợ swap nên cần phải tắt swap. Thực hiện:
      - `swapoff -a`
      - Mở file `/etc/fstab` và comment dòng `/dev/mapper/master--vg-swap_1 none            swap    sw              0       0`
      
      <img src="">
      
      - Kiểm tra lại bằng lệnh: `free -m`
    - Đặt IP cho node **k8s-node1** bằng cách chạy lệnh bên dưới để sửa file `/etc/network/interfaces`
      ```
      cat << EOF > /etc/network/interfaces
      # This file describes the network interfaces available on your system
      # and how to activate them. For more information, see interfaces(5).
      source /etc/network/interfaces.d/*
      # The loopback network interface
      auto lo
      iface lo inet loopback
      # The primary network interface
      auto ens3
      iface ens3 inet static
      address 192.168.40.181
      netmask 255.255.255.0
      gateway 192.168.40.1
      dns-nameservers 8.8.8.8
      EOF
      ```
    - Đặt hostname cho máy `k8s-node1` bằng cách sửa nội dung các file `/etc/hosts/` và `/etc/hostname`
      - Chay lệnh dưới để khai báo hostname cho `k8s-node1`
        ```
        cat << EOF > /etc/hosts
        127.0.0.1       localhost k8s-node1
        192.168.40.180       k8s-master
        192.168.40.181       k8s-node1
        192.168.40.182       k8s-node2
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-node1 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
      
### 3.3 k8s-node2
  - Update:
    ```
    apt-get update -y && apt-get upgrade -y
    apt-get -y install -y vim curl wget 
    apt-get -y install byobu
    ```
  - Tắt tính năng **swap** của OS
    - Do **K8s** không hỗ trợ swap nên cần phải tắt swap. Thực hiện:
      - `swapoff -a`
      - Mở file `/etc/fstab` và comment dòng `/dev/mapper/master--vg-swap_1 none            swap    sw              0       0`
      
      <img src="">
      
      - Kiểm tra lại bằng lệnh: `free -m`
    - Đặt IP cho node **k8s-node2** bằng cách chạy lệnh bên dưới để sửa file `/etc/network/interfaces`
      ```
      cat << EOF > /etc/network/interfaces
      # This file describes the network interfaces available on your system
      # and how to activate them. For more information, see interfaces(5).
      source /etc/network/interfaces.d/*
      # The loopback network interface
      auto lo
      iface lo inet loopback
      # The primary network interface
      auto ens3
      iface ens3 inet static
      address 192.168.40.182
      netmask 255.255.255.0
      gateway 192.168.40.1
      dns-nameservers 8.8.8.8
      EOF
      ```
    - Đặt hostname cho máy `k8s-node2` bằng cách sửa nội dung các file `/etc/hosts/` và `/etc/hostname`
      - Chay lệnh dưới để khai báo hostname cho `k8s-node2`
        ```
        cat << EOF > /etc/hosts
        127.0.0.1       localhost k8s-node2
        192.168.40.180       k8s-master
        192.168.40.181       k8s-node1
        192.168.40.182       k8s-node2
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-node2 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
      
