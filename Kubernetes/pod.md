# Chi tiết về Pod trong K8S
- Container thường hướng tới việc giải quyết một vấn đề đơn lẻ, được xác định trong phạm vị hẹp, như là một microservice. Nhưng trong thế giới thực , các vấn đề đỏi hỏi nhiều container cho một giải pháp hoàn chỉnh. Bài viết này sẽ nói tới việc kết hợp nhiều container và trong 1 pod duy nhất của **K8s**, việc này có ý nghĩa gì và các container đó giao tiếp với nhau như thế nào?
# Pod K8s là gì???
- **pod** là đơn vị nhỏ nhất có thể triển khai và quản lý bởi **K8s**. Nói cách khác, nếu bạn cần chạy 1 container duy nhất trong **K8s**thì bạn cũng phải tạo một Pod chứa container đó.
- Một **pod**có thể chứa nhiều hơn 1 container. Các container trong cùng 1 pod dược kết hợp chặt chẽ với nhau. Vậy chúng kết hợp chặt chẽ với nhau như thế nào??? => hãy nghĩ về nó theo cách này: *Các container trong 1 pod đại diện cho các tiến trình mà giống như các tiến trình chạy trên một máy chủ thật.*, hiểu nôm na thì **pod**giống như 1 máy chủ duy nhất.
# Tại sao K8s sử dụng pod là đơn vị triển khai nhỏ nhất mà không phải là container?
- Giả sử rằng triển khai 1 ứng dụng web cần 2 container là `web`và `database`. Để quản lý một container, **K8s** cần bổ sung thông tin, chẳng hạn như chính sách khởi động lại (restart policy), xác định vấn đề cần làm với một container khi nó kết thúc (terminate), ... => Thay vì quả tải việc bổ sung thuộc tính cho những điều đã tồn tại, các kỹ sư **K8s** đã quyết định sử dụng 1 thực thể mới (new entity), đó là **pod**, là một container logic (logically container - wraps (dịch là vỏ bọc)) chứa 1 hoặc nhiều container và được quản lý như 1 thực thể duy nhất.
# Tại sao K8s cho phép nhiều hơn 1 container trong 1 pod?
- Các container trong một pod chạy trên cùng 1 *"logical host"*, chúng sử dụng chung một namesapace (nói cách khác là chung địa chỉ IP và port space), và cùng IPC namespace. Chúng có thể sử dụng chung volume được chia sẻ (shared volume). Những đặc tính này làm cho các container giao tiếp hiệu quả, đảm bảo data locality. Ngoài ra, pod cho phép bạn quản lý nhiều application container được kết hợp chặt chẽ dưới dạng 1 đơn vị duy nhất.
- Vậy nếu một ứng dụng cần vài container chạy trên cùng một host, tại sao không tạo 1 container duy nhất với mọi thứ chúng cần??? Điều tiên chúng có thể vi pham nguyên tắc `mỗi process cho mỗi container`. Điều này quan trọng là bởi vì với nhiều process trong 1 container sẽ gây khó khăn trong việc sửa lỗi container (troubleshoot), vì log từ các process khác nhau sẽ trộn lẫn vào nhau, và nó gây khó khăn hơn cho việc quản lý process lifecycle, ví dụ như quản lý *"zombie processes"* khi tiên trình cha (parent process) bị chết. Thứ 2 là việc sử dụng một vài container cho 1 ứng dụng sẽ đơn giản hơn, minh bạch hơn.
# Kết nối giữa các container trong một pod
## Chia sẻ volume trong 1 pod-k8s
- Trong **K8s**, bạn có thể sử dụng một shared k8s volume một cách đơn giản và hiệu quả để chia sẻ dữ liệu giữa các container trong cùng một pod. Đối với hầu hết các trường hợp, nó đơn giản là sử dụng một thư mục tên máy chủ (host) để chia sẻ cho tất cả các conatainer trong 1 pod.
- **K8s volume** cho phép dữ liệu tồn tại khi khởi động lại một container, những volume này có cùng lifetime với Pod (câu này quan trọng này). Điều đó có nghĩa là volume (và cả dữ liệu trong đó) tồn tại tới chừng nào pod còn tồn tại. Nếu pod bị xóa vì bất kì lý do gì, ngay cả khi có 1 pod được tạo ra giống hệt được tạo ra, shared volume cũng bị hủy và được tạo lại.
- Một trường hợp chuẩn cho việc sử dụng pod nhiều container với một shared volume là khi một container chứa log hoặc các file khác cho thư mục chung, và các container khác đọc từ thư mục chia sẻ (share directory). Vi dụ ta có thể tạo 1 pod như sau:
```
apiVersion: v1
kind: Pod
metadata:
  name: mc1
spec:
  volumes:
  - name: html
    emptyDir: {}
  containers:
  - name: 1st
    image: nginx
    volumeMounts:
    - name: html
      mountPath: /usr/share/nginx/html
  - name: 2nd
    image: debian
    volumeMounts:
    - name: html
      mountPath: /html
    command: ["/bin/sh", "-c"]
    args:
      - while true; do
          date >> /html/index.html;
          sleep 1;
        done
```
<img src="https://i.imgur.com/lzRF62q.png">

- Trong ví dụ này, chúng ta xác định có một file tên là html. Nó có kiểu emptyDir, có nghĩa là volume lần đầu được tạo khi một pod được gán cho 1 node, và tồn tại tới khi nào pod vẫn đang chạy trên node đó.. Như tên gọi, ban đầu nó empty.  Container đầu tiên chạy nginx server và shared volume được gắn vào thư mục `/usr/share/nginx/html`. Container thứ 2 sử dụng Debian image và có shared volume được gắn vào thư mục `/html`. Mỗi giây, container thứ 2 chạy lệnh `args: ...` (như trong file định nghĩa bên trên) để thêm ngày giờ hiện tại vào file index.html nằm trong shared volume (tức là file `/html` của host ấy). Khi người dùng thực hiện yêu cầu HTTP tới pod, Nginx server đọc tệp này và chuyện nó trở lại cho người dùng trong một phản hồi cho request.

### Inter-process communications (IPC)

Các container trong Pod cùng chia sẻ IPC namespace, có nghĩa là chúng có thể giao tiếp với nhau bằng cách sử dụng chuẩn IPC như 
SystemV semaphores hoặc POSIX shared memory.

Trong ví dụ sau, chúng ta định nghĩa một Pod có 2 container. Chúng ta sử dụng cùng một Docker image cho cả hai. Container đầu tiên, producer, 
tạo một hàng đợi thông điệp Linux chuẩn (standard Linux message queue), viết một số thông báo ngẫu nhiên, và sau đó viết một thông báo thoát 
đặc biệt. Container thứ 2, consumer, mở cùng message queue đó để đọc và đọc tin nhắn cho tới khi nó nhận được thông báo thoát (exit message). 
Chúng ta cùng thiết lập một chính sách khởi động lại (restart policy) là "Never", Pod sẽ dừng sau khi kết thúc cả 02 container.

```sh
apiVersion: v1
kind: Pod
metadata:
  name: mc2
spec:
  containers:
  - name: producer
    image: allingeek/ch6_ipc
    command: ["./ipc", "-producer"]
  - name: consumer
    image: allingeek/ch6_ipc
    command: ["./ipc", "-consumer"]
  restartPolicy: Never
```
 
 Để kiểm tra điều này, tạo pod bằng cách sử dụng kubectl và xem trạng thái Pod
 
 ```sh
 $ kubectl get pods --show-all -w
NAME      READY     STATUS              RESTARTS  AGE
mc2       0/2       Pending             0         0s
mc2       0/2       ContainerCreating   0         0s
mc2       0/2       Completed           0         29
 ```
 
 Bây giờ, bạn có thể kiểm tra log cho mỗi container và xác minh (verify) rằng container thứ 2 nhận tất cả các message từ container thứ nhất, 
 bao gồm cả thông báo thoát (exit message):
 
 ```sh
 $ kubectl logs mc2 -c producer
...
Produced: f4
Produced: 1d
Produced: 9e
Produced: 27
$ kubectl logs mc2 -c consumer
...
Consumed: f4
Consumed: 1d
Consumed: 9e
Consumed: 27
Consumed: done
 ```
 
 ![multicontainerpodproducerconsumer](../../images/multicontainerpodproducerconsumer.png)
 
 Tuy nhiên, có một vấn đề lớn với Pod này và nó liên quan đến cách các container khởi động
 
### Container dependencies and startup order
 
Hiện tại, tất cả các container trong một Pod đang được khởi động song song và không có cách nào để xác định rằng một container phải 
khởi động sau một container khác. Ví dụ, trong ví dụ về IPC, có khả năng container thứ hai có thể hoàn thành việc khởi động trước khi container thứ 
nhất khởi động và tạo hàng đợi thông điệp xong. Trong trường hợp này, container thứ 2 sẽ bị lỗi, vì nó mong rằng hàng đợi (message queue) đã tồn tại.

Một số nỗ lực để cung cấp một vài biện pháp kiểm soát cách container khởi động, như **Kubernetes Init Containers**, bắt đầu đầu tiên (start first) 
(và tuần tự), đang được phát triển, nhưng trong môi trường cloud native, tốt hơn là lập kế hoạch cho các lỗi ngoài tầm kiểm soát của bạn. 
Ví dụ, một cách để khắc phục sự cố này là thay đổi ứng dụng để chờ hàng đợi tin nhắn được tạo.

### Inter-container network communication
 
Các container trong một Pod có thể được truy cập thông qua "localhost"; chúng sử dụng cùng một network namespace. Ngoài ra, đối với các container, 
hostname được nhìn thấy là tên của Pod. Bởi vì container chia sẻ cùng một địa chỉ IP và port space, bạn nên sử dụng các port khác nhau trong container 
cho các kết nối đến (incoming). Nói cách khác, các ứng dụng trong một Pod phải phối hợp việc sử dụng port của chúng.

Trong ví dụ sau, chúng ta sẽ tạo một Pod có nhiều container, trong đó nginx trong một container làm việc như một reverse proxy cho ứng dụng web 
đơn giản ở container thứ hai.

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
 
 ![multicontainerwebapp](../../images/multicontainerwebapp.png)
 
### Exposing multiple container in a Pod
 
 Trong ví dụ này cho thấy cách sử dụng một container duy nhất để truy cập các container khác trong Pod, nó khá phổ biến đối với một số container 
 trong một port để listen trên các port khác nhau - tất cả đều cần được exposed. Để thực hiện điều này, bạn có thể tạo một dịch vụ đơn lẻ (single service) 
 với nhiều port được exposed, hoặc bạn có thể tạo một dịch vụ duy nhất (single service) cho mọi port bạn đang cố gắng exposed.
 
## Where to go from here

Bằng cách tạo Pod, k8s cung cấp rất nhiều tính linh hoạt để phối hợp cách thức hoạt động của container và cách giao tiếp giữa container với nhau. 
Chúng có thể chia sẻ file volume, chúng có thể giao tiếp thông qua mạng, và chúng thậm chí có thể giao tiếp bằng cách sử dụng IPC.








