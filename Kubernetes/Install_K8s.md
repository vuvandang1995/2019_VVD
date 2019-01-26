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
  - `apt-get -y update && apt-get -y install docker.io`
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
      
      - <img src="https://i.imgur.com/FFewZvm.png">
      
    - Sau khi chạy kết quả như sau là thành công: http://paste.openstack.org/raw/720277/ (Nếu chưa đúng thì kiểm tra lại từ đầu nhé
    - Luư ý: Nếu gặp thông báo lỗi [ERROR Swap]: running with swap on is not supported. Please disable swap khi thực hiện kubeadm init thì cần thực hiện lệnh swapoff -a. Sau đó thực hiện lại lệnh ở trên.
    - Tới đây, bạn có 2 sự lựa chọn, 1 là sử dụng user `root` hiện tại để tiếp tục cài đặt, cấu hình, 2 là sử dụng 1 tài khoản khác
  ### 4.3.1 Sử dụng tài khoản root để thao tác với K8s
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
  ### 4.4 Cài đặt Pod Network
   - Đứng trên node **k8s-master** cài đặt Pod network
   - **K8s** có nhiều sự lựa chọn giải pháp network để kết nối các container, trong hướng dẫn này, tôi sử dụng `flannel`
   `kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`
   - Kết quả lệnh như sau:
   ```
    root@k8s-master:~# kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
    clusterrole.rbac.authorization.k8s.io "flannel" created
    clusterrolebinding.rbac.authorization.k8s.io "flannel" created
    serviceaccount "flannel" created
    configmap "kube-flannel-cfg" created
    daemonset.extensions "kube-flannel-ds" created
   ```
   - Từ bản 1.9 trở lên, thực hiện lệnh dưới để tạo token trên **k8s-master**, kết quả trả về được sử dụng để thực hiện trên **k8s-node1** và **k8s-node2**
   `sudo kubeadm token create --print-join-command`
   - Sau câu lệnh trên, bạn sẽ nhận được 1 token, bạn sẽ sử dụng token đó trên **k8s-node1** và **k8s-node2** để join vào cụm cluster mà mình vừa tạo bên trên
 ### 4.5 Thực hiện join `k8s-node1` và `k8s-node2`và cụm cluster
  - Đứng trên cả 2 node **k8s-node1** và **k8s-node2** và thực hiện câu lệnh join, tốt hơn cả là bạn nên copy câu lệnh trong kết quả phần đầu của mục **4.3** ý. còn đây là câu lệnh của mình:
  `kubeadm join --token 150984.0da1fe160e5113f0 192.168.40.180:6443 --discovery-token-ca-cert-hash sha256:cb8e0cd1238dc8fe8b1b2f16fe02817425005f04a8ddd09a7c19db08b75f72eb`
  - Lưu ý: Nếu có thông báo [ERROR Swap]: running with swap on is not supported. Please disable swap khi thực hiện lệnh join thì sử dụng lệnh dưới và thực hiện lại lệnh join.
  `swapoff -a`
  - Kết quả trả về là:
  ```
  [preflight] Running pre-flight checks.
        [WARNING FileExisting-crictl]: crictl not found in system path
  [discovery] Trying to connect to API Server "192.168.40.180:6443"
  [discovery] Created cluster-info discovery client, requesting info from "https://172.16.68.130:6443"
  [discovery] Requesting info from "https://172.16.68.130:6443" again to validate TLS against the pinned public key
  [discovery] Cluster info signature and contents are valid and TLS certificate validates against pinned roots, will use API Server "172.16.68.130:6443"
  [discovery] Successfully established connection with API Server "172.16.68.130:6443"

  This node has joined the cluster:
  * Certificate signing request was sent to k8s-master and a response
    was received.
  * The Kubelet was informed of the new secure connection details.

  Run 'kubectl get nodes' on the k8s-master to see this node join the cluster.
  root@k8s-node1:~#
  ```
  - Sau khi đã join **k8s-node1** và **k8s-node2** bằng lệnh trên, kiểm tra lại đã ok chưa bằng lệnh:
  ```
  export KUBECONFIG=/etc/kubernetes/admin.conf
  kubectl get nodes
  ```
  - Kết quả trả về của lệnh trên như sau:
  ```
  NAME      STATUS    ROLES     AGE       VERSION
  k8s-master    Ready     k8s-master    9h        v1.9.2
  k8s-node1     Ready     <none>    8h        v1.9.2
  k8s-node2     Ready     <none>    6m        v1.9.2
  ```
  - Chúng ta có thể thấy ở cột STATUS đã có trạng thái Ready. Tiếp tục thực hiện hiện lệnh dưới để download hoặc kiểm tra trạng thái của các thành phần trong K8S trên các node đã hoạt động hay chưa. `kubectl get pod --all-namespaces`
  - Kết quả như bên dưới là ok (kiểm tra cột STATUS).

  ```
  NAMESPACE     NAME                             READY     STATUS    RESTARTS   AGE
  kube-system   etcd-k8s-master                      1/1       Running   0          9h
  kube-system   kube-apiserver-k8s-master            1/1       Running   0          9h
  kube-system   kube-controller-manager-k8s-master   1/1       Running   0          9h
  kube-system   kube-dns-6f4fd4bdf-ctxx7         3/3       Running   0          9h
  kube-system   kube-flannel-ds-kjnhs            1/1       Running   0          9h
  kube-system   kube-flannel-ds-wz648            1/1       Running   0          8h
  kube-system   kube-flannel-ds-xtcj9            1/1       Running   0          36m
  kube-system   kube-proxy-5slwp                 1/1       Running   0          36m
  kube-system   kube-proxy-5trrj                 1/1       Running   0          9h
  kube-system   kube-proxy-b54bs                 1/1       Running   0          8h
  kube-system   kube-scheduler-k8s-master            1/1       Running   0          9h
  ```
- Tới đây chúng ta đã có môi trường để bắt đầu thực hành với K8S rồi. Sau phần này chúng ta nên đọc sang phần các khái niệm trong K8S trước khi đi vào thực hành chi tiết hơn.
    
## Cài Dashboard cho K8s
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

- Sau đó dùng token bên trên và địa chỉ IP của các node trong cụm Cluster để đăng nhập và dashboard, nhớ là https nhé: https://192.168.40.182:30324


## Cài Google Cloud SDK
### 1. Centos, redhat
```
# Update YUM with Cloud SDK repo information
sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

# Install the Cloud SDK
yum install google-cloud-sdk
```
### 2. Ubuntu
```
# Create an environment variable for the correct distribution
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

# Add the Cloud SDK distribution URI as a package source
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk
```
- Link tham khảo gốc](https://medium.com/@nnilesh7756/how-to-install-and-configure-the-google-cloud-sdk-2fad4a7d3ed7)





