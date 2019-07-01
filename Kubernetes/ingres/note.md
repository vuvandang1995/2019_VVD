các bước cấu hình https trong ingress là:
- bạn dùng ingress controller là `nginx` hay `traefik` không quan trọng
  - nếu cấu hình `traefik` tự genarate ssl thì nó sẽ dùng `letsencrypt`
  - Nếu cấu hình không tự genarate ssl thì mình cần sử dụng certificate của mình.các bước như sau
    - deployment, server đã running rồi
    - tạo secret: `kubectl create secret tls nginx-certs-keys --cert=My_CA_Bundle.crt --key=telo.vn_key.key` 
      - **Lưu ý** chữ `tls` trong dòng bên trên là type bắt buộc khi tạo secret là cert có sẵn.
    - sau đó tạo ingress:
    
    ```
    apiVersion: networking.k8s.io/v1beta1
    kind: Ingress
    metadata:
      name: tls-example-ingress
    spec:
      tls:
      - hosts:
        - k8s-lab1.teko.vn
        secretName: nginx-certs-keys
      rules:
        - host: k8s-lab1.teko.vn
          http:
            paths:
            - path: /
              backend:
                serviceName: my-nginx
                servicePort: 80
    ```
## NOTE
- nói cho 1 cách dễ hiểu nhé: deployment và service chạy như thế nào không quan trọng, khi ra ngoài sẽ qua ingress có https.
- kiểu như là deployment chạy nginx port 80, service list port 80, quan ingress thì vẫn có thể truy cập vào nó qua https
