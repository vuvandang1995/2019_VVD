# Vì sao kata containers ra đời?
- Như các bạn đã biết, container trong Docker sử dụng chung **kernel** với host, nghĩa là các container chỉ được sử dụng các hệ điều hành dùng kernel của host, ví dụ như docker host có hệ điều hành Ubuntu => dùng kernel Linux => các container trong nó sẽ có các hệ điều hành như Ubuntu, Centos, Debian, ... Docker trong Windows bản chất là Windows sẽ tạo 1 VM Linux để chạy docker trong đó.
- => Vấn để ở đây là khi các container sử dụng chung kernel với docker host thì chẳng may bị hack vào kernel docker host, hacker có thể tấn công vào các container bên trong, đây là một vấn đề bảo mật mà nhiều chuyên gia đang lo ngại. Và bây giờ, **Kata-containers** sinh ra để giải quyết vấn đề này. Theo thông tin ban đầu, Kata containers sẽ giúp tăng tốc độ và bảo mật cho các container. Và nó giải quyết các vấn đề đó như thế nào, hãy tìm hiểu lần lượt bên dưới nhé!
# Khái niệm
- **Kata Containers is a novel implementation of a lightweight virtual machine that seamlessly integrates within the container ecosystem. Kata Containers are as light and fast as containers and integrate with the container management layers—including popular orchestration tools such as Docker and Kubernetes (k8s)—while also delivering the security advantages of VMs.**
- Tôi dịch là: **Kata Containers** là một phương pháp triển khai mới cho các VM siêu nhẹ mà có thể tương thích hoàn hảo với hệ sinh thái Containers. Với **Kata Containers**, các containers sẽ rất nhẹ, nhanh và tương thích với các lớp quản lý containers, bao gồm các công cụ quản lý contarner rất phổ biến như Docker và Kubernet (K8S), hơn nữa các container này có lợi thế bảo mật như các VM.
- Hình sau mô tả về Container trong Cloud hiện nay và trong Kata Container

<img src="https://i.imgur.com/KMhDTJP.png">

