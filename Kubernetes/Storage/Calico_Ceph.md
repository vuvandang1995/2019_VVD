## K8s storage with Ceph
- Để cài được Ceph làm storage trên K8s, cần sử dụng Rook làm **orchestrator**
- Tham khảo rook ở đây: https://github.com/rook/rook/blob/master/Documentation/README.md
## Cài đặt
- Tôi giả sử các bạn đã có 1 hệ thống K8s với 1 master, 2 worker và sử dụng Calico network
  - **B1:** Chạy lệnh lệnh sau trên **tất cả các node worker và các node master backup (nếu là mô hình nhiều node master)**

  `iptables -t nat -A POSTROUTING -o ens3 -s 192.168.2.0/24 -j MASQUERADE`

  - Trong đó:
    - `ens3` là interface của worker node nằm trong dải vật lý với master node
    - `192.168.2.0/24` là dải pod network mà node worker đó được Calico cấp

<img src="https://i.imgur.com/B2ovwAH.png">

  - **B2:** pull git repo Rook về và làm theo hướng dẫn này nha. https://github.com/rook/rook/blob/master/Documentation/ceph-quickstart.md
  - Đến khi nào kết quà được như này thì ok.
  
<img src="https://i.imgur.com/J77j6ZM.png">

