apiVersion: v1
kind: Service
metadata:
  name: openid-mysql
  labels:
    app: openid
spec:
  ports:
  - port: 3306
  clusterIP: None
  selector:
    app: openid
    tier: mysql
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: openid-mysql
spec:
  selector:
    matchLabels:
      app: openid # has to match .spec.template.metadata.labels
  serviceName: "openid-mysql"
  replicas: 2 # by default is 1
  template:
    metadata:
      labels:
        app: openid # has to match .spec.selector.matchLabels
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: mysql
        image: mysql:5.7
        args:
          - "--ignore-db-dir=lost+found"
          - "--character-set-server=utf8mb4"
          - "--collation-server=utf8mb4_unicode_ci"
        env:
          - name: MYSQL_ROOT_PASSWORD
            value: "123456"
          - name: MYSQL_DATABASE
            value: "openid"
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: mysql-persistent-storage
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "rook-ceph-block"
      resources:
        requests:
          storage: 10Gi
