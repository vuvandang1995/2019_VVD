## Ceph for storage K8s
## Install

`git clone https://github.com/rook/rook.git`

`cd rook/cluster/examples/kubernetes/ceph`

`kubectl create -f operator.yaml`

- Wait until container all running
- Custom `cluster.yaml` file

`vim cluster.yaml`

- Comment the 240th and 243th line
- Remove comment the last line and edit it to suit your disk

<img src="https://i.imgur.com/VCaUlUo.png">

`kubectl create -f cluster.yaml`

