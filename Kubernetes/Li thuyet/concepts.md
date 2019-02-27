# K8s
- K8s hỗ trợ các công nghệ container là docker và rkt
- Các tiện ích của K8s:
  - Triển khai ứng dụng một cách nhanh chóng
  - Scale app dễ dàng
  - Liên tục đưa ra các tính năng mới
  - Tối ưu hóa việc sử dụng tài nguyên
## 1. Các khái niệm trong K8s
### 1.1 Pod
- Pod là 1 hoặc 1 nhóm các container phục vụ cho 1 ứng dụng, cùng chia sẻ tài nguyên lưu trữ, địa chỉ IP,...
- Pod cung cấp 2 loại tài nguyên chia sẻ cho các container: **networking** và **storage**
- **Networking:** Mỗi pod sẽ được cấp 1 địa chỉ IP. Các container trong cùng 1 pod sẽ chia sẻ networknamespace (nghĩa là dùng chung địa chỉ IP). Containers trong pod chạy như các tiến trình trong một máy tính độc lập, vì thế các container có thể giao tiếp với nhau thông qua **localhost**,tất nhiên phải dùng port khác nhau.
  - Ví dụ cho dễ hiểu nhé! Trong docker, để các container gọi đến nhau, bạn phải dùng tên và port. Còn trong K8s, bạn chỉ cần port là đủ, vì các contaiter để là locahost.
- **Storage:** Pod có thể chỉ định một **shared storage volume**. Các container trong cùng pod có thể truy cập trung vào volume này.
- Tất cả các pod mặc định mở tất cả các port với các pod khác. Để hạn chế việc này với mục đích tăng tính bảo mật của hệ thống, bạn cần tìm hiểu về **NetworkPolicy** trong K8s
- Ví dụ:
**Bước 1**: Tạo một ConfigMap với tập tin cấu hình nginx. Các yêu cầu HTTP đến cổng 80 sẽ được chuyển tiếp đến cổng 5000 trên localhost:

```sh
apiVersion: v1
ind: ConfigMap
metadata:
 name: mc3-nginx-conf
data:
 nginx.conf: |-
   user  nginx;
   worker_processes  1;

   error_log  /var/log/nginx/error.log warn;
   pid        /var/run/nginx.pid;

   events {
       worker_connections  1024;
   }

   http {
       include       /etc/nginx/mime.types;
       default_type  application/octet-stream;

       sendfile        on;
       keepalive_timeout  65;

       upstream webapp {
           server 127.0.0.1:5000;
       }

       server {
           listen 80;

           location / {
               proxy_pass         http://webapp;
               proxy_redirect     off;
           }
       }
   }
```

**Bước 2**:  Tạo một Pod chứa nhiều container với ứng dụng web đơn giản và nginx trong các container riêng biệt. Lưu ý rằng đồi với Pod, 
chúng ta chỉ định nghĩa Port 80, Port 5000 sẽ không thể truy cập được bên ngoài Pod.
 
 ```sh
 apiVersion: v1
kind: Pod
metadata:
  name: mc3
  labels:
    app: mc3
spec:
  containers:
  - name: webapp
    image: training/webapp
  - name: nginx
    image: nginx:alpine
    ports:
    - containerPort: 80
    volumeMounts:
    - name: nginx-proxy-config
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf
  volumes:
  - name: nginx-proxy-config
    configMap:
      name: mc3-nginx-conf
 ```
 
 **Bước 3**:  Expose cho Pod sử dụng dịch vụ NodePort
 
 ```sh
 $ kubectl expose pod mc3 --type=NodePort --port=80
service "mc3" exposed
 ```
 
 **Bước 4**: Xác định port trên node được sử dụng để chuyển tiếp cho Pod
 
 ```sh
 $ kubectl describe service mc3
...
NodePort:	<unset>	31418/TCP
...
 ```
 
 Bây giờ bạn có thể sử dụng trình duyệt (hoặc curl) để điều hướng đến port của node để truy cập ứng dụng web thông qua reverse proxy, như sau:
 
 ```sh
 http://myhost:31418
 ```
 
 Request này sau đó được chuyển tiếp (forward) tới port 5000 của webapp container.
 
<img src="https://i.imgur.com/6wIrthU.png">

### 1.2 ReplicaSet
- Hiểu một cách đơn giản thì **replicaSet** giúp bạn tự động scale pod ra thành nhiều pod giống nhau, đảm bảo số lượng pod ở mọi thời điểm. Khi có pod xảy ra sự cố, bị xóa hay gặp lỗi, nó sẽ tự động sinh ra pod khác để thay thế và luôn đảm bảo đủ số lượng khi đã khai báo.
- Ví dụ:
```
apiVersion: extensions/v1beta1
 kind: ReplicaSet
 metadata:
   name: nginx-rs
 spec:
   replicas: 3
   selector:
     matchLabels:
       app: nginx
   template:
     metadata:
       labels:
         app: nginx
     spec:
       containers:
       - name: nginx
         image: nginx
         ports:
         - containerPort: 80
```
- Như đã khai báo:  relicas: 3 thì hệ thống sẽ sinh ra 3 pod nginx và đảm bảo đủ khi chạy ứng dụng
### 1.3 Deployment
- Deployment sinh ra với mục đích quản lý các pod và replicaSet. Ngoài ra, Deployment còn cung cấp thế cho bạn một tính năng rất tuyệt vời, đó là **rollout update**, nhờ đó bạn có thể **rollback** một revision của deployment bất cứ lúc nào
- Ví dụ về deployment:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```
### 1.4 [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- Giả sử chúng ta dùng deployment định nghĩa ra thành phần của 1 pod web server và thiết lập replicas là 3. Nghĩa là sẽ có 3 pod giống nhau được sinh ra, người dùng muốn truy cập vào web, cần phải biết 1 trong 3 địa chỉ IP của các pod. Nhưng pod có thể xảy ra sự cố nào đó và được khởi tạo lại, rất có thể pod mới sinh ra để thay thế đó sẽ có địa chi IP khác với IP của pod cũ, người dùng làm sao biết IP mới đó mà truy cập, **Service** sẽ giải quyết vấn đề này.
- Có thể hiểu 1 cách đơn giản như này: **Service** là đại diện cho 1 nhóm các pod có chung 1 mục đích. **Service** giống như 1 domain, domain được trỏ vào pod, giống như trỏ vào web server. Điều tuyệt vời ở đây là: 1 "domain"(service) có thể trỏ được vào nhiều "web server"(pod). Đôi khi người ta hay gọi là mô hình micro-services. **Services** ở đây giống như **gateway server**cho các pod. Khi đó, **service**sẽ đóng vai trò là một **Internal LoadBalancer**
- Ví dụ, có 3 pod relicas là web server nginx. Tạo ra một **Service** là "domain" cho 3 pod đó. Nghĩa là khi có 1 request HTTP vào service, nó sẽ forward request xuống cho 3 pod. Còn việc pod nào được chọn xử lý request thì mặc định sẽ tuân theo cơ chế roud-robin (có thể tùy chỉnh lại cơ chế này)
- Ví dụ định nghĩa một Service
```
apiVersion: apps/v1beta1
kind: Deployment
metadata:
 name: mticket
 labels:
   app: mticket
spec:
 replicas: 1
 template:
    metadata:
      labels:
        app: mticket
    spec:
      containers:
      - name: rd
        image: redis:2.8
        ports:
        - containerPort: 6379
      - name: db
        image: dangvv1995/docker_db
        ports:
        - containerPort: 3306
      - name: web
        image: dangvv1995/docker_web:2.0
        ports:
        - containerPort: 8000
        - containerPort: 8001
      - name: nginx
        image: dangvv1995/nginxmtk:2.0
        ports:
        - containerPort: 80

---
kind: Service
apiVersion: v1
metadata:
  # Unique key of the Service instance
  name: mticketsv
spec:
  ports:
    # Accept traffic sent to port 80
    - name: http
      port: 80
      # targetPort: 80
  selector:
    # Loadbalance traffic across Pods matching
    # this label selector
    app: mticket
  # Create an HA proxy in the cloud provider
  # with an External IP address - *Only supported
  # by some cloud providers*
  type: NodePort
```
- **Chú ý:** chỗ `selector:` của service thường được trỏ tới đúng lable của Deployment hay pod định nghĩa trước đó. Bạn cũng có thể k dùng `selector` trong trường hợp:
  - Bạn muốn có một cluster database trong môi trường product, nhưng trong môi trường test lại muốn sử dụng 1 database khác.
  - Bạn muốn trỏ service của bạn vào một namespace khác hoặc 1 cluster khác.
  - Bạn muốn chuyển đổi service của bạn từ lúc đầu sang Kubernet và hệ thống back-end vẫn chạy bên ngoài K8s
- Ví dụ nha:
```
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
```
- Bởi vì service trên không có `selector` nên đối tượng **Endpoint** tương ứng không được tạo, bạn phải tự tạo bằng tay:
```
kind: Endpoints
apiVersion: v1
metadata:
  name: my-service
subsets:
  - addresses:
      - ip: 1.2.3.4
    ports:
      - port: 9376
```
- Nhiều service đòi hỏi được expose nhiều hơn 1 port, K8s cũng hỗ trợ điều này. Vi dụ:
```
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 9376
  - name: https
    protocol: TCP
    port: 443
    targetPort: 9377
```
- **Lưu ý: khi đặt name cho ports, chỉ được đặt kí tự thường và số, giữa số và kí tự được nối nhau bởi dấu "-", ví dụ: 123-abc, web thì hợp lệ, 123_xyz hay _web thì không hợp lệ**

- Có 3 Service type:
  - ClusterIP (mặc định)
  - NodePort
  - LoadBalancer
#### 1.4.1 - **ClusterIP**

<img src="https://i.imgur.com/Mcvqjss.png">

- Với type là ClusterIP thì service chỉ có thể gọi trong cluster thông qua service name. Bên ngoài cluster sẽ không gọi được đến service này. Service nằm bên trong cluster và cần thông qua proxy bạn mới truy cập được đến service
- **Tác dụng của service với type là ClusterIP:**
  - Sử dụng để định danh giữa các dịch vụ trong cluster
  - Internal LoadBalancer
#### 1.4.2 - **NodePort**

<img src="https://i.imgur.com/IlrET6I.png">

- Với service types là NodePort, bạn đang ra lệnh cho cluster mở một cổng ở tất cả các Node trong cluster và từ đó người dùng cuối có thể truy cập ứng dụng của bạn thông qua **<Node_IP>:<Node_Port>**
- **Tác dụng:** Tác dụng lớn nhất là debug, bạn có thể expose ứng dụng của bạn ra ngoài internet để người dùng có thể truy cập được một cách rất đơn giản mà không tốn tiền như khi sử dụng LoadBalancer(sau này còn một cách khác là Ingress và cũng tốn tiền)
#### 1.4.3 - **LoadBalancer**

<img src="https://i.imgur.com/9JKSQY0.png">

- với kiểu service này, là bạn sử dụng 1 dịch vụ LoadBalacer bên ngoài
### 1.5 Volumes
- Volume thể hiện vị trí nơi mà các container có thể truy cập và lưu trữ thông tin
- Volumes có thể là local filesystem, local storage, Cehp, GlusterFS, ...
- Persistent volume (PV) là khái niệm để đưa ra một dung lượng lưu trữ THỰC TẾ 1GB, 10GB ...
- Persistent volume claim (PVC) là khái niệm ảo, đưa ra một dung lượng CẦN THIẾT, mà ứng dụng yêu cầu.
- Khi 1 PV thoả mãn yêu cầu của 1 PVC thì chúng "match" nhau, rồi "bound" (buộc / kết nối) lại với nhạu.
### 1.6 Namespaces
- Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces.
- Namespace là một cách để chia và cô lập tài nguyên của cụm cluster giữa nhiều người dùng, các object trong cùng một namespace sẽ có cùng một cơ chế điều khiển truy cập là `default`
- Ban đầu, Kubernetes có 3 namespace được tạo:
  - **default** là namespace mặc định cho các object mà nó không được khai báo namespace trong file .yaml của object đó.
  - **kube-system**: là namespace cho các đối tượng được tạo bởi hệ thống Kubernetes
  - **kube-public**: là namespace được tạo tự động và và thể truy cập bởi tất cả user
### 1.7 ConfigMap
- ConfigMap là giải pháp để nhét 1 file config / đặt các ENVironment var hay set các argument khi gọi câu lệnh. ConfigMap là một cục config, mà pod nào cần, thì chỉ định là nó cần - giúp dễ dàng chia sẻ file cấu hình.
### 1.8 Secret
- secret dùng để lưu trữ các mật khẩu, token, ... hay những gì cần giữ bí mật. Nó nằm bên trong container.
### Lables
- Labels: Là các cặp key-value được Kubernetes đính kèm vào pods, replication controllers,...
- Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects.




















