- Cài rook-ceph với flannel thì bình thường, với calico thì sẽ gặp lỗi như sau ở pod `rook-ceph-operator`

<img src="https://i.imgur.com/EpO3kPG.png">

- Các yêu cầu khi bạn cài `Calico`
  - Phải thiết lập `podSubnet` là dải IP mà sẽ gán cho các pod sử dụng calico trước khi cài Calico bằng cách create file calico.yaml
    - Ví dụ: 
    
    `kubeadm init --apiserver-advertise-address 192.168.40.180 --pod-network-cidr=192.168.0.0/16`
    
    - hoặc nếu dùng file config
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
    - Chi tiết xem ở đây nè: https://docs.projectcalico.org/v2.0/getting-started/kubernetes/installation/hosted/kubeadm/

- Khi bạn khởi tạo K8s với lệnh `kubeadm init --apiserver-advertise-address 192.168.40.180 --pod-network-cidr=192.168.0.0/16` như bên trên, thì `kubernetes service` - tức là `api-server` sẽ có thông tin như sau:

<img src="https://i.imgur.com/D9ib6jR.png">

- Vấn đề ở đây là: Khi tạo 1 pod chứa 1 container:
  - Nếu mô hình dùng `Flannel`: exec vào container đó có thể ping được tới `Endpoints` của `API-server (kubernetes service)`, có thể `curl -k https://10.96.0.1:443/`
  - Nếu dùng `Calico`thì không làm được những việc trên
- **Đó là lí do xảy ra lỗi như hình ở đầu bài viết. Do cơ chế hoạt động và mô hình mạng của calico và flannel khác nhau, cần tìm hiểu kĩ hơn**

## Khi muốn biết thư mục volume mount với container nằm ở đâu trên host thì dùng lệnh `docker inspect container-id` để xem. 
## khi cấu hình HA-proxy

<img src="https://i.imgur.com/I63etle.png">

- `check` nghĩa là kiểm tra server này, `fall 3` nghĩa là số lần kiểm tra **không có phản hồi** server này tối đa 3 lần trước khi đánh giá server đó bị DOWN, `rise 2` nghĩa là số lần kiểm tra **có phản hồi** server này trước khi đánh giá server đó đã UP 
- Link tham khảo nè: https://www.haproxy.com/documentation/aloha/10-0/traffic-management/lb-layer7/health-checks/

## Biến node master cũng là node worker

`kubectl taint nodes --all node-role.kubernetes.io/master-`

## Cách tạo pod theo node worker chỉ định
- https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/

## Để các pod trong Calico network có thể curl hay ping tới địa chỉ API-server
- Chạy lệnh lệnh sau trên **tất cả các node worker và các node master backup (nếu là mô hình nhiều node master)**

`iptables -t nat -A POSTROUTING -o ens3 -s 192.168.2.0/24 -j MASQUERADE`

- Trong đó:
  - `ens3` là interface của worker node nằm trong dải vật lý với master node
  - `192.168.2.0/24` là dải pod network mà node worker đó được Calico cấp

<img src="https://i.imgur.com/B2ovwAH.png">

- **Lưu ý: đây là mấu chốt để cài ceph là storage cho K8s với Calico network**

## Lưu ý khi cài Metricserver nè:
- Thay thế file `metrics-server/deploy/1.8+/metrics-server-deployment.yaml` bằng nội dung:

```
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: metrics-server
  namespace: kube-system
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: metrics-server
  namespace: kube-system
  labels:
    k8s-app: metrics-server
spec:
  selector:
    matchLabels:
      k8s-app: metrics-server
  template:
    metadata:
      name: metrics-server
      labels:
        k8s-app: metrics-server
    spec:
      serviceAccountName: metrics-server
      volumes:
      # mount in tmp so we can safely use from-scratch images and/or read-only containers
      - name: tmp-dir
        emptyDir: {}
      containers:
      - name: metrics-server
        image: k8s.gcr.io/metrics-server-amd64:v0.3.0
        imagePullPolicy: Always
        command:
        - /metrics-server
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP
        volumeMounts:
        - name: tmp-dir
          mountPath: /tmp
```

- rồi reboot lại cluster nhé. ahihi
