# Install K8s high-availability
## Mô hình
- 3 master node (install HA proxy - keepalived)
- 3 worker node
## IP address
- k8s-master: 192.168.40.180, 192.168.40.186 (Virtual IP)
- k8s-master2: 192.168.40.181
- k8s-master3: 192.168.40.182
- k8s-node1: 192.168.40.183
- k8s-node2: 192.168.40.184
- k8s-node3: 192.168.40.185
# Cài đặt
- ssh tất cả các node bằng tài khoản `root`
## 1. Đặt IP và name cho các server
### `k8s-master`:
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
        192.168.40.181       k8s-master2
        192.168.40.182       k8s-master3
        192.168.40.183       k8s-node1
        192.168.40.184       k8s-node2
        192.168.40.185       k8s-node3
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-master > /etc/hostname
        ```
      - Khởi động lại: `init 6`
### `k8s-master2`:
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
    - Đặt IP cho node **k8s-master2** bằng cách chạy lệnh bên dưới để sửa file `/etc/network/interfaces`
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
    - Đặt hostname cho máy `k8s-master2` bằng cách sửa nội dung các file `/etc/hosts/` và `/etc/hostname`
      - Chay lệnh dưới để khai báo hostname cho `k8s-master2`
        ```
        cat << EOF > /etc/hosts
        127.0.0.1       localhost k8s-master2
        192.168.40.180       k8s-master
        192.168.40.181       k8s-master2
        192.168.40.182       k8s-master3
        192.168.40.183       k8s-node1
        192.168.40.184       k8s-node2
        192.168.40.185       k8s-node3
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-master2 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
### `k8s-master3`:
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
    - Đặt IP cho node **k8s-master3** bằng cách chạy lệnh bên dưới để sửa file `/etc/network/interfaces`
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
    - Đặt hostname cho máy `k8s-master3` bằng cách sửa nội dung các file `/etc/hosts/` và `/etc/hostname`
      - Chay lệnh dưới để khai báo hostname cho `k8s-master3`
        ```
        cat << EOF > /etc/hosts
        127.0.0.1       localhost k8s-master3
        192.168.40.180       k8s-master
        192.168.40.181       k8s-master2
        192.168.40.182       k8s-master3
        192.168.40.183       k8s-node1
        192.168.40.184       k8s-node2
        192.168.40.185       k8s-node3
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-master3 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
### `k8s-node1`
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
      address 192.168.40.183
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
        192.168.40.181       k8s-master2
        192.168.40.182       k8s-master3
        192.168.40.183       k8s-node1
        192.168.40.184       k8s-node2
        192.168.40.185       k8s-node3
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-node1 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
### `k8s-node2`
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
      address 192.168.40.184
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
        192.168.40.181       k8s-master2
        192.168.40.182       k8s-master3
        192.168.40.183       k8s-node1
        192.168.40.184       k8s-node2
        192.168.40.185       k8s-node3
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-node2 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
### `k8s-node3`
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
    - Đặt IP cho node **k8s-node3** bằng cách chạy lệnh bên dưới để sửa file `/etc/network/interfaces`
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
      address 192.168.40.185
      netmask 255.255.255.0
      gateway 192.168.40.1
      dns-nameservers 8.8.8.8
      EOF
      ```
    - Đặt hostname cho máy `k8s-node3` bằng cách sửa nội dung các file `/etc/hosts/` và `/etc/hostname`
      - Chay lệnh dưới để khai báo hostname cho `k8s-node3`
        ```
        cat << EOF > /etc/hosts
        127.0.0.1       localhost k8s-node3
        192.168.40.180       k8s-master
        192.168.40.181       k8s-master2
        192.168.40.182       k8s-master3
        192.168.40.183       k8s-node1
        192.168.40.184       k8s-node2
        192.168.40.185       k8s-node3
        EOF
        ```
      - Sửa file `/etc/hostname`:
        ```
        echo k8s-node3 > /etc/hostname
        ```
      - Khởi động lại: `init 6`
## 2. Cài đặt HA proxy - keepalived
- Chạy các lệnh trên cả 3 node master:

`sudo apt-get install -y haproxy keepalived`

- Chạy lệnh sau với admin admin (`su -m`):

`echo "net.ipv4.ip_nonlocal_bind=1" >> /etc/sysctl.conf`

- Tạo file config keepalived trên `k8s-master`:

`sudo vim /etc/keepalived/keepalived.conf`

- Thêm nội dung sau: **Lưu ý: cần chỉnh sửa lại tên card mạng ens3 bên dưới cho đúng với server của bạn**
```
vrrp_script chk_haproxy {
  script "killall -0 haproxy"
  interval 2
  weight 3
}
vrrp_instance VI_1 {
  virtual_router_id 51
  advert_int 1
  priority 100
  state MASTER
  interface ens3
  virtual_ipaddress {
    192.168.40.186 dev ens3
  }
 authentication {
     auth_type PASS
     auth_pass 123456
     }
  track_script {
    chk_haproxy
  }
}
```
- Tạo file config keepalived trên `k8s-master2`:

`sudo vim /etc/keepalived/keepalived.conf`

- Thêm nội dung sau: **Lưu ý: cần chỉnh sửa lại tên card mạng ens3 bên dưới cho đúng với server của bạn**
```
vrrp_script chk_haproxy {
  script "killall -0 haproxy"
  interval 2
  weight 3
}
vrrp_instance VI_1 {
  virtual_router_id 51
  advert_int 1
  priority 99
  state BACKUP
  interface ens3
  virtual_ipaddress {
    192.168.40.186 dev ens3
  }
 authentication {
     auth_type PASS
     auth_pass 123456
     }
  track_script {
    chk_haproxy
  }
}
```
- Tạo file config keepalived trên `k8s-master3`:

`sudo vim /etc/keepalived/keepalived.conf`

- Thêm nội dung sau: **Lưu ý: cần chỉnh sửa lại tên card mạng ens3 bên dưới cho đúng với server của bạn**
```
vrrp_script chk_haproxy {
  script "killall -0 haproxy"
  interval 2
  weight 3
}
vrrp_instance VI_1 {
  virtual_router_id 51
  advert_int 1
  priority 98
  state BACKUP
  interface ens3
  virtual_ipaddress {
    192.168.40.186 dev ens3
  }
 authentication {
     auth_type PASS
     auth_pass 123456
     }
  track_script {
    chk_haproxy
  }
}
```
### Khởi động lại và bật dịch vụ keepalived trên cả 3 node master
```
sudo systemctl start keepalived
sudo systemctl enable keepalived
sudo systemctl restart keepalived
```
- Mở file config haproxy:

`sudo vim /etc/haproxy/haproxy.cfg`

- Thêm vào cuối file nội dung sau:
```
frontend kubernetes
        bind 192.168.40.186:6444
        option tcplog
        mode tcp
        default_backend kubernetes-master-nodes

backend kubernetes-master-nodes
        mode tcp
        balance roundrobin
        option tcp-check
        server k8s-master 192.168.40.180:6443 check fall 3 rise 2
        server k8s-master2 192.168.40.181:6443 check fall 3 rise 2
        server k8s-master3 192.168.40.182:6443 check fall 3 rise 2
```
### Khởi động lại và bật dịch vụ haproxy trên cả 3 node master
```
sudo systemctl start haproxy
sudo systemctl enable haproxy
sudo systemctl restart haproxy
```
## Cài các thành phần cho K8s
- **Trên tất cả các node:**

`apt-get -y update && apt-get -y install docker.io`

`apt-get update && apt-get install -y apt-transport-https`

```
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF

apt-get update  -y
apt-get install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl
```
```
systemctl enable docker.service
systemctl start docker.service
systemctl status docker.service
systemctl enable kubelet.service 
```
- **Trên node master đầu tiên (k8s-master)**
    - Tạo file `kubeadm-config.yaml`:
    
    `vim kubeadm-config.yaml`
    
    ```
    apiVersion: kubeadm.k8s.io/v1beta1
    kind: ClusterConfiguration
    kubernetesVersion: stable
    apiServer:
      certSANs:
      - "192.168.40.186"
    controlPlaneEndpoint: "192.168.40.186:6444"
    networking:
      podSubnet: 192.168.0.0/16
    ```
    - **Lưu ý: địa chỉ trong file config sẽ là địa chỉ của Virtal IP phần keepalived**
    - Tạo cluster:
    
    `kubeadm init --config=kubeadm-config.yaml`
    
    - Kết quả ra như bên dưới thì bạn đã làm đúng, không thì làm lại từ đầu nha :D
    ```
    ........
    kubeadm join 192.168.40.186:6444 --token t9zkev.ns6r6od1oovlio2i --discovery-token-ca-cert-hash sha256:904629ae281ef47a9c8ddda6507a4d5812bfdf586ad73f8a039230715b2db8fa
    ```
    - **Lưu ý: Nhớ lưu câu lệnh kết quả bên trên lại, nếu bạn lỡ chưa lưu thì dùng lệnh này để lấy lại:**
    
    `kubeadm token create --print-join-command`
    
    - Khai báo biến môi trường cấu hình user admin cho K8s:
    ```
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```
    - Cài đặt Pod network:
    - **Nếu bạn dùng Flannel**
    
        - Chạy trên tất cả các node lệnh sau:
        
        `sysctl net.bridge.bridge-nf-call-iptables=1`
        
    ```
    kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/a70459be0084506e4ec919aa1c114638878db11b/Documentation/kube-flannel.yml
    ```
    
    - **nếu bạn dùng Weave**
    
    `kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"`
    
    - **Nếu bạn dùng Calico**
    ```
    kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
    kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml
    ```
    - Link tham khảo cài Caloco nè: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
    - Hoặc cài Calico full từ trang chủ nè: https://docs.projectcalico.org/v3.5/getting-started/kubernetes/
    - Copy các chứng chỉ và key mà `kubeadmin` vừa generate lên 2 node master còn lại
    
    `vim copy.sh`
    
    ```
    USER=root
    MASTER_NODE_IPS="192.168.40.181 192.168.40.182"
    for host in ${MASTER_NODE_IPS}; do
       scp /etc/kubernetes/pki/ca.crt "${USER}"@$host:
       scp /etc/kubernetes/pki/ca.key "${USER}"@$host:
       scp /etc/kubernetes/pki/sa.key "${USER}"@$host:
       scp /etc/kubernetes/pki/sa.pub "${USER}"@$host:
       scp /etc/kubernetes/pki/front-proxy-ca.crt "${USER}"@$host:
       scp /etc/kubernetes/pki/front-proxy-ca.key "${USER}"@$host:
       scp /etc/kubernetes/pki/etcd/ca.crt "${USER}"@$host:etcd-ca.crt
       scp /etc/kubernetes/pki/etcd/ca.key "${USER}"@$host:etcd-ca.key
       scp /etc/kubernetes/admin.conf "${USER}"@$host:
    done
    ```
    
    `sh copy.sh`
    - Hãy đảm bảo tất cả các pod đều đã được running thì mới chuyển sang các node khác để làm nhé!
    
    `watch kubectl get pods --all-namespaces`

- **Trên 2 node master còn lại**
    - **k8s-master2**:
        - Di chuyển các chứng chỉ và key vào thư mục `/etc/kubernetes/pki/` bằng cách:
        
        `vim move.sh`
        
        ```
        USER=root
        mkdir -p /etc/kubernetes/pki/etcd
        mv /${USER}/ca.crt /etc/kubernetes/pki/
        mv /${USER}/ca.key /etc/kubernetes/pki/
        mv /${USER}/sa.pub /etc/kubernetes/pki/
        mv /${USER}/sa.key /etc/kubernetes/pki/
        mv /${USER}/front-proxy-ca.crt /etc/kubernetes/pki/
        mv /${USER}/front-proxy-ca.key /etc/kubernetes/pki/
        mv /${USER}/etcd-ca.crt /etc/kubernetes/pki/etcd/ca.crt
        mv /${USER}/etcd-ca.key /etc/kubernetes/pki/etcd/ca.key
        mv /${USER}/admin.conf /etc/kubernetes/admin.conf
        ```
        
        `sh move.sh`
        
        - Khai báo biến môi trường cấu hình user admin cho K8s:
        ```
        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config
        ```
        
        - Join các k8s-master2 vào cluster bằng cách sử dụng câu lệnh kết quả của `k8s-master`, thêm option này vào sau câu lênh đó: `--experimental-control-plane`
        
        `kubeadm join 192.168.40.186:6444 --token t9zkev.ns6r6od1oovlio2i --discovery-token-ca-cert-hash sha256:904629ae281ef47a9c8ddda6507a4d5812bfdf586ad73f8a039230715b2db8fa --experimental-control-plane`
        
        - Nếu kết quả câu lệnh trên có error thì cũng không sao, cứ chờ và kiểm tra các node cho tới khi ready nhé
        
        `watch kubectl get nodes`
        
        - Nếu kết quả câu lệnh bên trên thấy trường roles của các master node là `<none>` thì chạy lệnh sau
        
        `kubectl label nodes <node-name> node-role.kubernetes.io/master=''`
        
        `kubectl taint nodes <node-name> node-role.kubernetes.io/master='':NoSchedule`
        
    - **k8s-master3**:
        - Di chuyển các chứng chỉ và key vào thư mục `/etc/kubernetes/pki/` bằng cách:
        
        `vim move.sh`
        
        ```
        USER=root
        mkdir -p /etc/kubernetes/pki/etcd
        mv /${USER}/ca.crt /etc/kubernetes/pki/
        mv /${USER}/ca.key /etc/kubernetes/pki/
        mv /${USER}/sa.pub /etc/kubernetes/pki/
        mv /${USER}/sa.key /etc/kubernetes/pki/
        mv /${USER}/front-proxy-ca.crt /etc/kubernetes/pki/
        mv /${USER}/front-proxy-ca.key /etc/kubernetes/pki/
        mv /${USER}/etcd-ca.crt /etc/kubernetes/pki/etcd/ca.crt
        mv /${USER}/etcd-ca.key /etc/kubernetes/pki/etcd/ca.key
        mv /${USER}/admin.conf /etc/kubernetes/admin.conf
        ```
        
        `sh move.sh`
        
        - Khai báo biến môi trường cấu hình user admin cho K8s:
        ```
        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config
        ```
        
        - Join các k8s-master3 vào cluster bằng cách sử dụng câu lệnh kết quả của `k8s-master`, thêm option vào sau câu lênh đó: `--experimental-control-plane`
        
        `kubeadm join 192.168.40.186:6444 --token t9zkev.ns6r6od1oovlio2i --discovery-token-ca-cert-hash sha256:904629ae281ef47a9c8ddda6507a4d5812bfdf586ad73f8a039230715b2db8fa --experimental-control-plane`
        
        - Nếu kết quả câu lệnh trên có error thì cũng không sao, cứ chờ và kiểm tra các node cho tới khi ready nhé
        
        `watch kubectl get nodes`
        
        - Nếu kết quả câu lệnh bên trên thấy trường roles của các master node là `<none>` thì chạy lệnh sau
        
        `kubectl label nodes <node-name> node-role.kubernetes.io/master=`
        
        `kubectl taint nodes <node-name> node-role.kubernetes.io/master='':NoSchedule`
        
- Chờ khoảng 30 giây, kiểm tra lại cluster các node master bằng lệnh:
```
kubectl get nodes -n kube-system
```
- Kết quả đúng như sau:
```
NAME          STATUS   ROLES    AGE     VERSION
k8s-master    Ready    master   24m     v1.13.3
k8s-master2   Ready    master   4m10s   v1.13.3
k8s-master3   Ready    master   9m40s   v1.13.3
```
- Kiểm tra cách thành phần K8s đã lên hay chưa?

`kubectl get pod -n kube-system -w`

- Kết quả:
```
NAME                                  READY   STATUS    RESTARTS   AGE
coredns-86c58d9df4-9745h              1/1     Running   0          22m
coredns-86c58d9df4-f9cn6              1/1     Running   0          22m
etcd-k8s-master                       1/1     Running   2          18m
etcd-k8s-master2                      1/1     Running   0          2m11s
etcd-k8s-master3                      1/1     Running   0          7m41s
kube-apiserver-k8s-master             1/1     Running   1          18m
kube-apiserver-k8s-master2            1/1     Running   0          2m12s
kube-apiserver-k8s-master3            1/1     Running   2          7m42s
kube-controller-manager-k8s-master    1/1     Running   2          17m
kube-controller-manager-k8s-master2   1/1     Running   0          2m12s
kube-controller-manager-k8s-master3   1/1     Running   0          7m42s
kube-proxy-2lt2c                      1/1     Running   0          7m42s
kube-proxy-d9j8p                      1/1     Running   1          22m
kube-proxy-kltbv                      1/1     Running   0          2m12s
kube-scheduler-k8s-master             1/1     Running   2          18m
kube-scheduler-k8s-master2            1/1     Running   0          2m12s
kube-scheduler-k8s-master3            1/1     Running   0          7m42s
weave-net-4p2zl                       2/2     Running   1          7m42s
weave-net-6gmgx                       2/2     Running   0          12m
weave-net-b86dt                       2/2     Running   1          2m12s
```
- **Join các node worker vào cluster:**

`kubeadm join 192.168.40.186:6444 --token t9zkev.ns6r6od1oovlio2i --discovery-token-ca-cert-hash sha256:904629ae281ef47a9c8ddda6507a4d5812bfdf586ad73f8a039230715b2db8fa`

- Kiểm tra lại trên các node master:

`kubectl get nodes -n kube-system`

- Kết quả đúng:
```
NAME          STATUS   ROLES    AGE   VERSION
k8s-master    Ready    master   65m   v1.13.3
k8s-master2   Ready    master   44m   v1.13.3
k8s-master3   Ready    <none>   50m   v1.13.3
k8s-node1     Ready    <none>   38m   v1.13.3
k8s-node2     Ready    <none>   38m   v1.13.3
k8s-node3     Ready    <none>   38m   v1.13.3
```
