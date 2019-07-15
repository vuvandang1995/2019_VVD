## Muốn đổi gateway của server, cần thay đổi trong file:
  - Ubuntu 16: `/etc/network/interfaces`
  - Ubuntu 18: `/etc/netplan/xxx.yaml`
- dùng lệnh `ip route add ...`thì reboot lại server là mất
