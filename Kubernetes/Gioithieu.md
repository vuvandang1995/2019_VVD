# Giới thiệu về Kubernetes
- **Kubernetes** là một phần trong hệ sinh thái container ngày nay, vì thế, trước khi tìm hiểu về Kubernetes, chúng ta cần biết tổng quan về hệ sinh thái container. Hệ sinh thái container gồm 3 phần chính, đó là:
  - Phần 1: Đây là thành phần cơ bản và cốt lõi nhất trong hệ sinh thái container, nó bao gồm: kiến trúc lõi của Container (các khái niệm về runtime spec, image format spectk); khái niệm images, network và storage.
  - Phần 2: Các công nghệ về platform liên quan tới container, bao gồm: các sản phẩm để orchestration container (nghĩa là công cụ để khởi tạo các container theo cơ chế điều phối), nền tảng để quản lý các container và các nền tảng Paas dựa trên container.
  - Phần 3: Các công nghệ hỗ trợ container, bao gồm: công nghệ hỗ trợ khi triển khai container trên nhiều máy chủ vật lý, các giải pháp phụ trợ về thu thập log và giám sát.
  
<img src="">

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
    - Thích hợp với các ứng dụng có kiến trúc microservices hay cloud native app. 
