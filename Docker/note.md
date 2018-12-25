## 1. Triển khai docker cho web app với https
- Xem ví dụ ở thư mục hiện tại. 

<img src="">

- Trong hình ảnh trên, chỗ `volumes:` ở service `nginx`, dòng `- ./static:/static` là kiểu `bind mount`, dòng `- default:/etc/nginx/conf.d/default.conf` là kiểu `volume` => cần khai báo volume đó ở cuối file:
```
volumes:
  default:
```
