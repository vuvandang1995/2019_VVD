# Cài đặt Kubernetes
## 1. Môi trường
  - Ubuntu 16.04 - 3 node (k8s-master, k8s-node1, k8s-node2)
  - Docker version: 18.06.1-ce
  - Kubernetes version: 
## 2. Mô hình và IP

<img src="https://i.imgur.com/tUdGSMF.png">

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
      
      <img src="https://i.imgur.com/uzDnYol.png">
      
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
      
      <img src="https://i.imgur.com/uzDnYol.png">
      
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
      
      <img src="https://i.imgur.com/uzDnYol.png">
      
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
      
## 4. Cài Docker và các thành phần của K8s
- Trên tất cả các node, sẽ cài đặt các thành phần: **docker**, **kubelet**, **kubeadm**, **kubectl**. Trong đó:
  - **docker**: là môi trường để chạy các container
  - **kubeadm**: Được sử dụng để thiết lập cụm cluster cho **K8s** (**Cluster** là 1 cụm máy thực hiện chung 1 mục đích). Tài liệu chuyên môn gọi **kubeadm** là **bootstrap** (tạm hiểu là một công cụ đóng gói )
  - **kubelet**: là thành phần chạy trên các host, có nhiệm vụ kích hoạt các **pod** và container trong cụm cluster của **K8s**
  - **kubectl**: là công cụ cung cấp CLI (giao diện dòng lệnh) để tương tác với **K8s** qua API
### 4.1 Cài đặt docker trên tất cả các node
    ```
    apt-get -y update && apt-get -y install docker.io
    ```
### 4.2 Cài đặt các thành phần của K8s trên tất cả các node
  - Tất cả các node:
    ```
    apt-get update && apt-get install -y apt-transport-https
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add
    cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
    deb http://apt.kubernetes.io/ kubernetes-xenial main
    EOF

    apt-get update  -y
    apt-get install -y kubelet kubeadm kubectl
    ```
### 4.3 Thiết lập cụm cluster
  - Chạy lệnh sau trên node **k8s-master** để thiết lập cluster:
    `kubeadm init --apiserver-advertise-address 192.168.40.180 --pod-network-cidr=10.244.0.0/16`
  - Trong đó:
    - `--apiserver-advertise-address` là tùy chọn để khai báo địa chỉ node **k8s-master**, ở đây chính là `192.168.40.180`, là địa chỉ chúng ta đã đặt ở bước 3 dùng để truyền thông giữa các node trong cụm cluster (node1: 192.168.40.181, node2: 192.168.40.182)
    - `--pod-network-cidr` là tùy chọn khai báo dải địa chỉ cho `flannet`. `flannet` là công nghệ network cho phép các container ở các host khác nhau giao tiếp với nhau, ở đây là các **pod** ở **k8s-node1** và **k8s-node2**. Nhìn hình sau để hiểu rõ vai trò của `flannet` hơn và đến bước thiết lập Pod network sẽ hiểu hơn:
      
      - <img src="">
      
    - Sau khi chạy kết quả như sau là thành công: http://paste.openstack.org/raw/720277/ (Nếu chưa đúng thì kiểm tra lại từ đầu nhé
    - Luư ý: Nếu gặp thông báo lỗi [ERROR Swap]: running with swap on is not supported. Please disable swap khi thực hiện kubeadm init thì cần thực hiện lệnh swapoff -a. Sau đó thực hiện lại lệnh ở trên.
    - Tới đây, bạn có 2 sự lựa chọn, 1 là sử dụng user `root` hiện tại để tiếp tục cài đặt, cấu hình, 2 là sử dụng 1 tài khoản khác
  ### 4.3.1: Sử dụng tài khoản root để thao tác với K8s
    - **Cách 1**: Trong mỗi phiên ssh bằng tài khoản `root`, để sử dụng được lệnh của **K8s** thì cần thực hiện lệnh dưới để khai báo biến môi trường.
      `export KUBECONFIG=/etc/kubernetes/admin.conf`
    - **cách 2**: Khai báo cố định biến môi trường, sẽ không phải export như bên trên mỗi lần ssh nữa:
      ```
      mkdir -p $HOME/.kube
      sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
      sudo chown $(id -u):$(id -g) $HOME/.kube/config
      ```
  ### 4.3.2 Sử dụng tài khoản khác root
    - Tạo user `ubuntu` để thực hiện cấu hình cho K8S. Nếu có user trước đó rồi thì không cần thực hiện bước này.

      ```sh
      adduser ubuntu
      ```

    - Nhập thông tin và mật khẩu cho user `ubuntu`, sau đó phân quyền sudoer bằng lệnh dưới.

      ```sh
      echo "ubuntu ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
      ```

    - Chuyển sang user ubuntu để thực hiện.

      ```sh
      su - ubuntu
      mkdir -p $HOME/.kube
      sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
      sudo chown $(id -u):$(id -g) $HOME/.kube/config
      ```

    - Sử dụng thủ thuật dưới để thao tác lệnh trong k8s được thuận lợi hơn nhờ việc tư động hoàn thiện lệnh mỗi khi thao tác.

      ```sh
      echo "source <(kubectl completion bash)" >> ~/.bashrc
      ```
  ### Cài đặt Pod Network
    - Đứng trên node **K8s** cài đặt Pod network
    - **K8s** có nhiều sự lựa chọn giải pháp network để kết nối các container, trong hướng dẫn này, tôi sử dụng `fl`
   
    
    
    
    
    







