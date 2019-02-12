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
## 1. Cài đặt HA proxy - keepalived
- Chạy các lệnh trên cả 3 node master
`sudo apt-get install -y haproxy keepalived`
- Chạy lệnh sau với admin admin (`su -m`)
`echo "net.ipv4.ip_nonlocal_bind=1" >> /etc/sysctl.conf`
- Mở file config haproxy
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
- Thêm nội dung sau:
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
- Thêm nội dung sau:
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
- Thêm nội dung sau:
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
## 2. 
