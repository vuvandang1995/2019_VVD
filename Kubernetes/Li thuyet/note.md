## Khi muốn biết thư mục volume mount với container nằm ở đâu trên host thì dùng lệnh `docker inspect container-id` để xem. 
## khi cấu hình HA-proxy

<img src="https://i.imgur.com/I63etle.png">

- `check` nghĩa là kiểm tra server này, `fall 3` nghĩa là số lần kiểm tra **không có phản hồi** server này tối đa 3 lần trước khi đánh giá server đó bị DOWN, `rise 2` nghĩa là số lần kiểm tra **có phản hồi** server này trước khi đánh giá server đó đã UP 
- Link tham khảo nè: https://www.haproxy.com/documentation/aloha/10-0/traffic-management/lb-layer7/health-checks/

## Biến node master cũng là node worker

`kubectl taint nodes --all node-role.kubernetes.io/master-`

## Cách tạo pod theo node worker chỉ định
- https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/

## Link hay : https://github.com/feiskyer/kubernetes-handbook/blob/master/en/addons/monitor.md


## Các bước reset và re-install 1 cụm k8s
- b1:
  - `kubectl drain <node-name> --ignore-daemonsets --delete-local-data`
  - `kubectl delete node <node-name>`
- b2:
  - Khi `kubeadm reset`,cần xóa thư mục `~/.kube` và `/var/lib/etcd`
  
## Delete các thứ không dùng đến trong docker
`docker system prune -a --volumes`

