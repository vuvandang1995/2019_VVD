## Install nginx ubuntu 18.04
## Config
- Thêm dòng sau vào file: `/etc/nginx/nginx.conf`
  ```
  stream {
          include /etc/nginx/conf.d/*.stream;
  }
  ```
- Tạo 1 file có đuôi `.stream`trong thư mục `/etc/nginx/conf.d/`. Ví dụ tạo file `k8s-lb.stream` nội dung như sau:
  ```
  upstream k8s-master {
    server 10.148.0.20:6443;	
    server 10.148.0.17:6443;	
    server 10.148.0.18:6443;	
  }

  server {
      listen 6443;
      proxy_pass k8s-master;
  }
  ```
- Đọc config chắc là hiểu được ngay nhỉ =))
