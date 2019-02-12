# Triển khai K8s High-availability
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

- Mở file config haproxy:

`sudo vim /etc/haproxy/haproxy.cfg`

- Thêm vào cuối file nội dung sau:
```
frontend firstbalance
        bind *:6444 ssl crt /etc/ssl/k8s.pem
        option forwardfor
        default_backend api
backend api
        balance roundrobin
        server master 192.168.40.180:6443 check ssl verify none
        server master2 192.168.40.181:6443 check ssl verify none
        server master3 192.168.40.182:6443 check ssl verify none
        option httpchk
```
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
- Khởi động lại và bật dịch vụ haproxy-keepalived
```
sudo systemctl start haproxy
sudo systemctl enable haproxy
sudo systemctl restart haproxy
sudo systemctl start keepalived
sudo systemctl enable keepalived
sudo systemctl restart keepalived
```
## 3. Cài đặt Client tool
- Trong bài viết này, tôi sử dụng `cfssl` để tạo các chửng chỉ ssl và key xác thực. Tiếp đến là cài `cfssljson`, `kubectl`.
- Install `cfssl`
```
wget -q --show-progress --https-only --timestamping \
  https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 \
  https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64
```

`chmod +x cfssl_linux-amd64 cfssljson_linux-amd64`

`sudo mv cfssl_linux-amd64 /usr/local/bin/cfssl`

`sudo mv cfssljson_linux-amd64 /usr/local/bin/cfssljson`

- Install kubectl

`wget https://storage.googleapis.com/kubernetes-release/release/v1.12.0/bin/linux/amd64/kubectl`

`chmod +x kubectl`

`sudo mv kubectl /usr/local/bin/`
