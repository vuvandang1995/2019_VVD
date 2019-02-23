- Cài rook-ceph với flannel thì bình thường, với calico thì sẽ gặp lỗi như sao ở pod `rook-ceph-operator`

<img src="">

- Vấn đề là các yêu cầu khi bạn cài `Calico`
  - Phải thiết lập `podSubnet` là dải IP mà sẽ gán cho các pod sử dụng calico.
    
