# Giới thiệu về Kubernetes
- **Kubernetes** là một phần trong hệ sinh thái container ngày nay, vì thế, trước khi tìm hiểu về Kubernetes, chúng ta cần biết tổng quan về hệ sinh thái container. Hệ sinh thái container gồm 3 phần chính, đó là:
  - Phần 1: Đây là thành phần cơ bản và cốt lõi nhất trong hệ sinh thái container, nó bao gồm: kiến trúc lõi của Container (các khái niệm về runtime spec, image format spectk); khái niệm images, network và storage.
  - Phần 2: Các công nghệ về platform liên quan tới container, bao gồm: các sản phẩm để orchestration container (nghĩa là công cụ để khởi tạo các container theo cơ chế điều phối), nền tảng để quản lý các container và các nền tảng Paas dựa trên container.
  - Phần 3: Các công nghệ hỗ trợ container, bao gồm: công nghệ hỗ trợ khi triển khai container trên nhiều máy chủ vật lý, các giải pháp phụ trợ về thu thập log và giám sát.
  
<img src="https://i.imgur.com/y5C4fEp.png">

- **Kubernetes** là một sản phẩm nằm trong phần 2 của hệ sinh thái container. Nó đóng vai trò là 1 công cụ **orchestration** (tạo, điều phối và chỉ huy các container)- hiểu nôm na thì **Kubernetes** là thằng túm đầu các máy vật lý hoặc các máy ảo được cài đặt môi trường để triển khai container. Đi sâu vào phần cài đặt sẽ hiểu hơn
# Các thông tin khởi đầu với Kubernetes
## Những kiến thức cần chuẩn bị trước khi tìm hiểu Kubernetes
  - Cần đọc khái niệm lý thuyết và thực hành
  - Để tìm hiểu tốt về **Kubernetes** thì cần tìm hiểu hệ sinh thái container ở mức độ cơ bản trước (nghĩa là có thể cài, thực hành được với docker cơ bản).
  - Sử dụng tương đối thành thạo Linux
  - Kỹ năng bổ trợ khác như: Network(TCP/IP), một vài kĩ năm cài đặt các ứng dụng cơ bản như web server, database
  - Đối tượng người dùng thích hợp để tìm hiểu **Kubernetes**: Sinh viên IT, các sysadmin, dev,...
  - Tài liệu chuẩn nhất ở trang chủ của Kubernetes
 
 # Các thông tin tóm tắt về Kubernetes
  - Cha đẻ của **Kubernetes** là "người tí hon" Google. Và tất nhiên trong hệ thống của Google có ứng dụng container (nghe đâu đó thì có khoảng 2 tỷ container trong datacenter của google)
  - **Kubernetes** được viết tắt là **K8s**. Chữ **K**, chữ **s** là phần cuối, phần cuối của từ **Kubernetes**, còn số **8** đơn là thay thể cho cụm cái ở giữa **ubernete** gồm 8 chữ =))
  - **Kubernetes** là một ***Orchestration tool*** trong hệ sinh thái container (nghĩa là có 1 số công cụ tương đương với nó như docker swarm, mesos). Tóm lại nó là thằng để tạo, sửa, xóa, thêm bớt các container.
  - **K8s có thể thay thế OpenStack hay VMware không?** Câu trả lời là **không**, mà **K8s** còn có thể kết hợp được với OpenStack.
  - **K8s** phụ hợp trong ngữ cảnh nào?
    - Với hệ thống có nhiều máy chủ (từ 3 trở lên) sử dụng container, hoặc các hệ thống có số lượng container lớn (vài trăm đến tỷ container =)) )
    - Thích hợp với các ứng dụng có kiến trúc **microservices** hay **cloud native app**.
    - Thích hợp với các ứng dụng có nhu cầu scale khi có tải lớn (scale tự động, nghĩa là khi tăng số lượng request tăng lên thì container được quản lý bởi **K8s**  sẽ tự động sinh ra hoặc khi có 1 container nào đó bị down thì **K8s**sẽ tự động biết và bổ sung thay thế) => hay chưa? =))
    - Các sysadmin, developer, ... các công ty muốn tự động hóa các nhu cầu cài đặt, triển khai hoặc tích hợp các giải pháp về **CI/CD**
    - **K8s**  có thể cài đặt trên 1 node hoặc nhiều node (bao gồm cả server vật lý hoặc cloud server) 
    - **K8s** có thể được cài đặt tự động hoặc bằng tay, tùy vào cách cài đặt mà triên khi cho môi trường nào (môi trường thử nghiệm, môi trường demo đánh giá hay môi trường product)
    - **K8s** có rất nhiều khái niệm móc xích với nhau nên cần tìm hiểu cẩn thận và từ từ
    - Một số sản phẩm tương đương với **K8s** là: Docker swarm, Mesos
    - Khi **K8s** được cài đặt trên nhiều node thì được gọi là cụm Cluster
- Mô hình Cloud Native app

<img src="https://i.imgur.com/Hnj0l6g.jpg">

# Các cách cài đặt K8s
- Có 2 phương pháp để cài đặt **K8s** là cài bằng tay và cài tự động (dùng tools, script).
  - Cài tay:
    - Tốn thời gian, nhưng dễ hiểu sâu **K8s** hơn
    - Cài bằng các lệnh hoặc biên dịch từ mã nguồn mà  **K8s** cung cấp
  - Cài tự động
    - Sử dụng **Minikube** tool: là công cụ để cài đặt **K8s**, là mì ăn liền,có các đặc điểm sau:
      - Thích hợp với trải nghiệm ban đầu, cài trên 1 node
      - Chạy tốt nhất trên CentOS 7, Ubuntu 16.04


















