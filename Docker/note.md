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
