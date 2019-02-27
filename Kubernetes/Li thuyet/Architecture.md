# Giới thiệu kiến trúc tổng quan về K8s
_ Như ở phần trước, chúng ta đã cài đặt [K8s](https://github.com/vuvandang1995/2019_VVD/blob/master/Kubernetes/Install_K8s.md) xong với các thành phần: **kubeadm**, **kubectl**, **kube-proxy**, **etcd**, **flannel** nằm trên các node, bài viết này sẽ làm rõ hơn về chúng.
- **Kubernetes** có thể được triển khai trên nhiều máy chủ vật lý, hoặc máy chủ ảo tạo thành cụm cluster. Cụm cluster này chịu sự quản lý của **K8s** và sinh ra các container khi người dùng có yêu cầu. Kiên trúc logic của **K8s** bao gồm 2 thành phần chính dựa theo vai trò của các node, đó là **Master node** và **worker node**
  - ***Master node***: Đóng vai trò là thành phần Control plane, điều khiển toàn bộ hoạt động chung và kiểm soát các container trên ***worker node***. Các thành phần chính trên ***Master node*** bao gồm: **API-server**, **Controller-manager**, **schedule**, **etcd** và **Docker Engine**.
    - ***Lưu ý:*** Có thể trong hình bên dưới bạn không nhìn thấy thành phần Docker engine trên **Master node** cần phải có docker, lí do là để chạy các thành phần của **K8s** trên container mà.
  - ***worker node***: Vai trò chính của **worker node** là môi trường để chạy các container mà người dùng yêu cầu, do vậy, thành phần chính của **worker node** là: **kubelet**, **kube-proxy** và **docker**
- Thông thường, 1 hệ thống sẽ có nhiều **worker node** hơn **master node**, vì thế, **master node** hay chính xác hơn là **K8s** cần hoàn thành tốt nhiệm vụ liên quan tới việc quản lý, xử lý các container sao cho linh hoạt và trơn tru nhất. Ngoài ra, với các hệ thống thực tế cần có khả năng `High Availability` thì sẽ cần triển khai nhiều **master node**.

<img src="https://i.imgur.com/n65bymi.jpg">

<img src="https://i.imgur.com/0Uw3Dbl.png">

<img src="https://i.imgur.com/e8omaMm.jpg">

- Minh hoạ vai trò của **K8s**

<img src="https://i.imgur.com/GE6qM6k.jpg">

# Các thành phần trong cụm cluster K8s
  - **etcd**
  - **API-server**
  - **Controller-manager**
  - **Agent (kubelet)**
  - **Schedule**
  - **Proxy (kube-proxy)**
  - **CLI (kubectl)**
## Etcd
- **Etcd** là một thành phần database phân tán, sử dụng ghi dữ liệu theo cơ chế `key/value` trong **K8s** cluster. **Etcd** được cài trên **master node** và nó lưu tất cả thông tin trong Cluster. **Etcd** sử dụng port 2380 để listening từng request và port 2379 để client gửi request tới.
- **Etcd** nằm trên **master node**
## API-server
- API-server là thành phần tiếp nhận yêu cầu của hệ thống **K8s** thông qua REST, tức là nó tiếp nhận các chỉ thị từ người dùng cho đến các services trong hệ thống cluster thông qua API - có nghĩa là người dùng hoặc các services khác trong cụm cluster có thể tương tác với **K8s** qua **http/https**
- API-server hoạt động trên port 6443 (https) và 8080 (http)
- API-server trên **master node**
## Controller-manager
- Thành phần controller-manager là thành phần quản lí trong **K8s**, nó có nhiệm vụ xử lý các tác vụ trong cụm cluster để đảm bảo hoạt động của các tài nguyên trong cluster. Controller-manager có các thành phần bên trong như sau:
  - **Node controller**: Tiếp nhận và trả lời các thông báo khi có một node bị down
  - **Replication Controller**: Đảm bảo các công việc duy trì chính xác số lượng bản replicate và phân phối các container trong pod (Pod tạm hình dung là một tâp hợp các container khi người dùng có nhu cầu tạo ra và cùng thực hiện chạy một ứng dụng)
  - **Endpoints Controller**: Populates the Endpoints object
  - **services account và token controllers**: Tạo ra các account và token để có thể sử dụng API cho các namespaces
- **Controller-manager** họat động trên **master node** và sử dụng port 10252
## Scheduler
- **kube-scheduler** có nhiệm vụ quan sát để lựa chọn ra các **worker node** mỗi khi có yêu cầu tạo **pod**. Nó sẽ lựa chọn sao cho phù hợp nhất dựa vào các cơ chế lập lịch mà nó có. 
- **kube-scheduler** nằm trên **master node** và sử dụng port 10251
## Agent - kubelet
- **Agent** hay chính là **kubelet**, là một thành phần chạy chính trên các **worker node**. Khi **kube-scheduler** đã xác định được pod chạy trên **worker node** nào thì nó sẽ gửi các thông tin cấu hình (bao gồm images, volume,...) tới **kubelet** trên node được chọn đó. Dựa và các thông tin nhận được, **kubelet** sẽ tiến hành tạo Pod theo yêu cầu.
- Vai trò chính của **kubelet** là:
  - Dõi theo các pod trên **workder node** nó thuộc
  - Mount các volume cho pod
  - Đảm bảo hoạt động của các container của pod
  - report về trạng thái của các pod để cụm cluster biết được xem các container còn hoạt động tốt hay không
- **kubelet** chạy trên **worker node** và sử dụng port 10250 và 10255
## Proxy
- Các services chỉ hoạt động ở chế độ logic, do vậy muốn bên ngoài có thể truy cập vào các service này thì cần có thành phần chuyển tiếp các request từ bên ngoài vào trong. (Kiểu như nat port 80 từ docker host vào port 80 của container trong Docker ý)
- **kube-proxy** được cài đặt trên **worker node** và sử dụng port 31080
## CLI
- **kubectl** là thành phần cung cấp giao diện dòng lệnh cho người dùng để tương tác với **K8s**.
- **kubectl** có thể được cài trên bất cứ máy nào miễn là có kết nối tới được với **API-server**
# Pod Network
- Phần này giải thích về cơ chế xử lý network cho các pod. Pod network đảm bảo cho các container có thế truyền thông được với nhau. Có nhiều sự lựa chọn về pod network nhưng tài liệu này lựa chọn **flannet**

<img src="https://i.imgur.com/FFewZvm.png">

  ### Tại sao trên master node cũng có các thành phần là `kubelet` và `kube-proxy`
  
  <img src="https://i.imgur.com/tUdGSMF.png">
  
  - Trả lời:  Doc các **master node** cũng có các services (ứng dụng) được sử dụng để đảm bảo hoạt động của **k8s**, do vậy chúng được chạy trong các container và thuộc một **pod** nằm trong namespace là **kube-system**
  
- Sử dụng lệnh sau để kiểm tra các pod của namespace **kube-system** : `kubectl get pod --all-namespaces -o wide`
- Kết quả là:
```
NAMESPACE     NAME                             READY     STATUS    RESTARTS   AGE       IP              NODE
kube-system   etcd-master                      1/1       Running   0          1d        172.16.68.130   master
kube-system   kube-apiserver-master            1/1       Running   0          1d        172.16.68.130   master
kube-system   kube-controller-manager-master   1/1       Running   0          1d        172.16.68.130   master
kube-system   kube-dns-6f4fd4bdf-ctxx7         3/3       Running   0          1d        10.244.0.2      master
kube-system   kube-flannel-ds-kjnhs            1/1       Running   0          1d        172.16.68.130   master
kube-system   kube-flannel-ds-wz648            1/1       Running   0          1d        172.16.68.131   node1
kube-system   kube-flannel-ds-xtcj9            1/1       Running   0          1d        172.16.68.132   node2
kube-system   kube-proxy-5slwp                 1/1       Running   0          1d        172.16.68.132   node2
kube-system   kube-proxy-5trrj                 1/1       Running   0          1d        172.16.68.130   master
kube-system   kube-proxy-b54bs                 1/1       Running   0          1d        172.16.68.131   node1
kube-system   kube-scheduler-master            1/1       Running   0          1d        172.16.68.130   master
```
- Ngoài ra, riêng thành phần **kubelet** trên **master node** thì không chạy trên container, nó chạy như 1 service trong hệ điều hành. Kiểm tra bằng lệnh `systemctl status kubelet`
- Kết quả:
```
kubelet.service - kubelet: The Kubernetes Node Agent
   Loaded: loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
  Drop-In: /etc/systemd/system/kubelet.service.d
           └─10-kubeadm.conf
   Active: active (running) since Thu 2018-01-25 23:50:36 +07; 1 day 21h ago
     Docs: http://kubernetes.io/docs/
 Main PID: 11378 (kubelet)
    Tasks: 16
   Memory: 46.7M
      CPU: 1h 45min 52.258s
   CGroup: /system.slice/kubelet.service
           └─11378 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --pod-manifest-path=/etc/kubernetes/manife

Jan 26 00:14:03 master kubelet[11378]: W0126 00:14:03.070593   11378 kubelet.go:1592] Deleting mirror pod "etcd-master_kube-system(2141fb05-01f3-11e8-a135-525400811cc0)" because it i
Jan 26 00:14:03 master kubelet[11378]: W0126 00:14:03.162630   11378 kubelet.go:1592] Deleting mirror pod "kube-apiserver-master_kube-system(217a6f08-01f3-11e8-a135-525400811cc0)" be
Jan 26 00:14:03 master kubelet[11378]: W0126 00:14:03.216007   11378 kubelet.go:1592] Deleting mirror pod "kube-controller-manager-master_kube-system(21b796d0-01f3-11e8-a135-52540081
Jan 26 00:14:03 master kubelet[11378]: W0126 00:14:03.317123   11378 kubelet.go:1592] Deleting mirror pod "kube-scheduler-master_kube-system(21d62e54-01f3-11e8-a135-525400811cc0)" be
Jan 26 00:14:12 master kubelet[11378]: W0126 00:14:12.846969   11378 conversion.go:110] Could not get instant cpu stats: different number of cpus
Jan 26 00:14:29 master kubelet[11378]: I0126 00:14:29.425093   11378 reconciler.go:217] operationExecutor.VerifyControllerAttachedVolume started for volume "kube-dns-config" (UniqueN
Jan 26 00:14:29 master kubelet[11378]: I0126 00:14:29.427162   11378 reconciler.go:217] operationExecutor.VerifyControllerAttachedVolume started for volume "kube-dns-token-tpdkw" (Un
Jan 26 00:14:30 master kubelet[11378]: W0126 00:14:30.147023   11378 pod_container_deletor.go:77] Container "7cb2acf1d1e6fa6183dcde381bbf120ff60308ac77a55921f23de2618130df52" not fou
Jan 26 00:14:53 master kubelet[11378]: W0126 00:14:53.026037   11378 conversion.go:110] Could not get instant cpu stats: different number of cpus
Jan 26 00:15:03 master kubelet[11378]: W0126 00:15:03.045872   11378 conversion.go:110] Could not get instant cpu stats: different number of cpus
lines 1-23/23 (END)
```
































