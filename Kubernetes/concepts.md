# K8s
- K8s hỗ trợ các công nghệ container là docker và rkt
- Các tiện ích của K8s:
  - Triển khai ứng dụng một cách nhanh chóng
  - Scale app dễ dàng
  - Liên tục đưa ra các tính năng mới
  - Tối ưu hóa việc sử dụng tài nguyên
1. Các khái niệm trong K8s
1.1 Pod
- Pod là 1 hoặc 1 nhóm các container phục vụ cho 1 ứng dụng, cùng chia sẻ tài nguyên lưu trữ, địa chỉ IP,...
- Pod cung cấp 2 loại tài nguyên chia sẻ cho các container: **networking** và **storage**
- **Networking:** Mỗi pod sẽ được cấp 1 địa chỉ IP. Các container trong cùng 1 pod sẽ chia sẻ networknamespace (nghĩa là dùng chung địa chỉ IP và port)
