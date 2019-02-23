- Cài rook-ceph với flannel thì bình thường, với calico thì sẽ gặp lỗi như sao ở pod `rook-ceph-operator`

<img src="https://i.imgur.com/PEx39Fl.png">

- Các yêu cầu khi bạn cài `Calico`
  - Phải thiết lập `podSubnet` là dải IP mà sẽ gán cho các pod sử dụng calico trước khi cài Calico bằng cách create file calico.yaml
    - Ví dụ: 
    
    `kubeadm init --apiserver-advertise-address 192.168.40.180 --pod-network-cidr=192.168.0.0/16`
    
    - vì sao lại là `192.168.0.0/16`? bởi vì đó là dải khai báo mặc định trong file `calico.yaml`, nếu bạn sửa thành dải khác thì bạn cũng phải sửa trong file `calico.yaml`. Nếu dải `192.168.0.0/16` đã được sử dụng trong k8s cluster của bạn rồi thì phải đổi sang dải khác. Dải địa chỉ cho các service (`--service-cidr` - là 1 option trong lệnh kubeadm init ... , default là `10.96.0.0/12`) cũng không được trùng với `pod-network-cidr`.
    - Chi tiết xem ở đây nè: https://docs.projectcalico.org/v2.0/getting-started/kubernetes/installation/hosted/kubeadm/

- Khi bạn khởi tạo K8s với lệnh `kubeadm init --apiserver-advertise-address 192.168.40.180 --pod-network-cidr=192.168.0.0/16` như bên trên, thì `kubernetes service` - tức là `api-server` sẽ có thông tin như sau:

<img src="https://i.imgur.com/D9ib6jR.png">

- Vấn đề ở đây là: Khi tạo 1 pod chưa 1 container:
  - Nếu mô hình dùng `Flannel`: exec vào container đó có thể ping được tới `Endpoints` của `API-server (kubernetes service)`, có thể `curl -k https://10.96.0.1:443/`
  - Nếu dùng `Calico`thì không làm được những việc trên, đó là lí do xảy ra lỗi như hình ở đầu bài viết. Do cơ chế hoạt động và mô hình mạng của calico và flannel khác nhau, cần tìm hiểu kĩ hơn
  
