## 1. Triển khai docker cho web app với https
- Xem ví dụ ở thư mục hiện tại. 

<img src="https://i.imgur.com/COG4MqS.png">

- Trong hình ảnh trên, chỗ `volumes:` ở service `nginx`, dòng `- ./static:/static` là kiểu `bind mount`, dòng `- default:/etc/nginx/conf.d/default.conf` là kiểu `volume` => cần khai báo volume đó ở cuối file:
```
volumes:
  default:
```
## RUN và CMD khác nhau như nào?
- RUN là lệnh chạy chỉ 1 lần duy nhất khi build image bằng Dockerfile
- CMD là lệnh chạy khi đã build xong image, và nó sẽ được chạy mỗi khi start hoặc restart container đó
- lênh CMD chỉ có 1 duy nhất trong Dockerfile, nếu có 2 lệnh thì sẽ chỉ lệnh đầu tiên được sử dụng
## COPY và ADD khác nhau như nào?

## WORKDIR là tác dụng gì?
- Ví dụ dùng lệnh `WORKDIR /home/kvmvdi` trong Dockerfile thì khi ta dùng lệnh `docker exec -it container_name /bin/bash`thì nó sẽ mặc định nhảy vào thư mục `/home/kvmvdi` trong container đó.

### Docker-compose
- Docker-compose để định nghĩa và chạy nhiều container. Xem ví dụ ở repo `https://github.com/vuvandang1995/Portal_docker`
- Lệnh `docker-compose build nginx` để build image cho service `nginx`trong file `docker-compose.yml`, nếu không có chữ `nginx`thì lệnh này sẽ build image cho tất cả các service trong `docker-compose.yml`
- Lệnh `docker-compose up -d`. tùy chọn -d là để chạy container chế độ `daemon`, nghĩa là chạy ngầm. có thể chạy container chỉ định giống như bên trên
- Ngoài ra còn có `docker-compose stop, start, r`
### Dùng ADD trong Dockerfile
- khi `ADD` 1 file, thì dùng lệnh như bình thường. ví dụ:
`ADD requirements.txt /home/kvmvdi`
- Khi `ADD` 1 thư mục, thì cần tạo tên thư mục ở phía đích. Ví dụ:
`ADD kvmvdi /home/kvmvdi`
  - Câu lệnh trên là add toàn bộ nội dung của thư mục `kvmvdi` ở máy host vào thư mục `/home/kvmvdi/` trong container. Điều nhấn mạnh ở đây là cần thêm chữ `kvm` vào sau chữ `home` thì toàn bộ nôi dung từ thư mục `kvmvdi` ở máy host mới xuất hiện ở thư mục `/home/kvmvdi/` trong container.
