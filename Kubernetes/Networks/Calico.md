- Tham khảo video: https://www.facebook.com/dangtrinhnt/videos/598772787209628/
- Sau khi xem video, bạn sẽ cơ bản hiểu Network bên trong K8s là như nào. Mở rộng hơn 1 chút, sẽ thấy **Calico** là plugin phổ biến hiện nay có performance tốt hơn **kubenet** mặc định trong K8s và hơn **flannel** nhưng cơ chế hoạt động của nó sẽ phức tạp hơn.
- Tham khảo link sau để hiểu hơn (nhớ xem hết các part nhé): https://rendoaw.github.io/2017/10/Calico-and-Kubernetes-part-1 

## Cài đặt Calico
- **Lưu ý:** 
  - Nếu bạn dùng `kubeadm init` để cài K8s, thì cần setup thông số `--pod-network-cidr=192.168.0.0/16`.
  - Hoặc nếu dùng file config:
  
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
  
  - vì sao lại là `192.168.0.0/16`? bởi vì đó là dải khai báo mặc định trong file `calico.yaml`, nếu bạn sửa thành dải khác thì bạn cũng phải sửa trong file `calico.yaml`. Nếu dải `192.168.0.0/16` đã được sử dụng trong k8s cluster của bạn rồi thì phải đổi sang dải khác. Dải địa chỉ cho các service (`--service-cidr` - là 1 option trong lệnh kubeadm init ... , default là `10.96.0.0/12`) cũng không được trùng với `pod-network-cidr`.
  - Chi tiết: [Calico](https://docs.projectcalico.org/v2.0/getting-started/kubernetes/installation/hosted/kubeadm/)

## Để các pod trong Calico network có thể curl hay ping tới địa chỉ API-server
- Chạy lệnh lệnh sau trên **tất cả các node worker và các node master backup (nếu là mô hình nhiều node master)**

`iptables -t nat -A POSTROUTING -o ens3 -s 192.168.2.0/24 -j MASQUERADE`

- Trong đó:
  - `ens3` là interface của worker node nằm trong dải vật lý với master node
  - `192.168.2.0/24` là dải pod network mà node worker đó được Calico cấp

<img src="https://i.imgur.com/B2ovwAH.png">

- **Lưu ý: đây là mấu chốt để cài ceph là storage cho K8s với Calico network**

