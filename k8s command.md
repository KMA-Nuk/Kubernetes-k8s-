minikube stop

minikube start --force

![image-20240929212729143](/home/ubuntu/.config/Typora/typora-user-images/image-20240929212729143.png)

----------------

minikube delete :xóa toàn bộ cluster

xóa riêng từng thành phần

kubectl delete --all pods

kubectl delete --all services

kubectl delete --all deployments

kubectl delete service tên service

----------

rm -rf /tmp/juju-*  	:xóa 

chmod 1777 /tmp 	:cấp quyền
![image-20240929093627547](/home/ubuntu/.config/Typora/typora-user-images/image-20240929093627547.png)

----------------------

kubectl get  - liệt kê tài nguyên

kubectl get pods

kubectl get deployments

kubectl get services

kubectl get pod -n name_space -o wide || kubectl get pod -o wide  :liệt kê tất cả các pod,hiển thị tất cả thông tin

 kubectl get node -o wide

![image-20240929082114592](/home/ubuntu/.config/Typora/typora-user-images/image-20240929082114592.png)

cột RESTART :số lần Pod đó được khởi động lại

-----

kubectl get rs :xem số lượng replicaset

![image-20240929082531568](/home/ubuntu/.config/Typora/typora-user-images/image-20240929082531568.png)

DESIRED :Trạng thái mong muốn 

-------------------

kubectl describe - hiển thị thông tin chi tiết về 1 tài nguyên

kubectl describe  deployment flask-api-deployment

kubectl describe pod - Mô tả tất cả các pod trong namespace mặc định

![image-20240929080904828](/home/ubuntu/.config/Typora/typora-user-images/image-20240929080904828.png)

---------

kubectl logs - n các bản ghi (logs) từ một container trong một pod

kubectl logs flask-api-deployment-9dbd6d698-2kcr4

--------

kubectl exec - thực hiện 1 lệnh trên 1 container trong 1 pod

kubectl exec -it flask-api-deployment-9dbd6d698-2kcr4 -- /bin/sh

kubectl exec <tên-pod> -- printenv

**`-it`**: Tùy chọn này cho phép bạn tương tác với shell trong Pod. `-i` giữ cho phiên làm việc mở, và `-t` cấp terminal.

**`--`**: Dùng để chỉ định rằng những tham số sau dấu `--` là lệnh sẽ chạy trong Pod.

**`/bin/sh`**: Đây là shell bạn muốn truy cập. Nếu container của bạn sử dụng shell khác, chẳng hạn như bash, bạn có thể thay thế nó bằng `/bin/bash`.

kubectl exec -it flask-api-deployment-9dbd6d698-2kcr4 -c <container-name> -- /bin/sh

-----------

kubectl api-resources - kiểm tra ds tài nguyên khả dụng

--------

kubectl rollout undo deployment/nginx-deployment :quay lại phiên bản trước đó

-----

kubectl rollout pause deployment/nginx-deployment :tạm dừng để nâng cấp,thêm biến môi trường,... tránh việc khởi động lại nhiều lần

kubectl rollout resume deployment/nginx-deployment :tiếp tục

-----

kubectl scale deployment nginx-deployment --replicas=6 :scale quy mô

----

kubectl rollout status deployment/nginx-deployment :theo dõi quá trình triển khai

![image-20240929081755943](/home/ubuntu/.config/Typora/typora-user-images/image-20240929081755943.png)

-----

dọn dẹp Replicaset cũ

kubectl get replicasets

kubectl delete rs <replicaset_name>

---------

configmap

kubectl exec -it <pod-name> -- printenv GREETING_MESSAGE AUDIENCE 

kubectl edit configmap myconfigmap

kubectl delete cm <tên_configmap>

<value>

kubectl create configmap config-example-value --from-literal=car=Ferrari --from-literal=contry=Vietnam

kubectl describe cm config-example-value

<file>

vi test-configmap.properties

kubectl create configmap test-configmap --from-file=./test-configmap.properties

<yaml>

apply ->

pod.yaml -> ssh vao pod -> printenv

-------------

- làm việc với namespace trong k8s
- tìm hiểu dns trong k8s
- tìm hiểu configmap -volume; secrets
- static pod
- test lenh: minikube service <ten_service>

apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-api-deployment
  labels:
    environment: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-api
  template:
    metadata:
      labels:
        app: flask-api
    spec:
      containers:
      - name: flask-api
        image: nghia5/flask-api:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "256Mi"
            cpu: "500m"
          limits:
            memory: "512Mi"
            cpu: "1"
        env:
        - name: GREETING_MESSAGE
          valueFrom:
            configMapKeyRef:
              name: myconfigmap
              key: env_text1
        - name: AUDIENCE
          valueFrom:
            configMapKeyRef:
              name: myconfigmap
              key: env_text2

Compare staticpod & pod (normal)

- Staticpod :

  - được quản lý trực tiếp bởi kubelet trên các node (k thông qua Apiserver) -> k thể kubectl apply hay delete
  - được lưu trữ trong thư mục  `/etc/kubernetes/manifests` (hoặc thư mục khác). Tệp yaml nào chứa kind: Pod trong thư mục này tự động đc kubelet khởi chạy
  - được dùng cho các thành phần quan trọng của hệ thống như : apiserver, ectd
  - để xóa ,cập nhật phải vào trực tiếp thư mục  manifests để thao tác với tệp yaml
  - nếu pod bị lỗi ->kubelet sẽ tự động khởi chạy lại pod đó 

  

- Pod normal:

  - được quản lý bởi Api server(kubectl) : kubectl apply, delete,update
  - thông tin pod được lưu trữ trong ectd   -> pod sau đó đc tạo bởi thông tin này

Ngày 1/10/2024
Công việc ngày hôm qua:
tìm hiểu về configmap
Công việc ngày hôm nay:
tìm hiểu dns trong k8s ,configmap & secret

----

sudo rm /etc/kubernetes/manifests/static-pod.yaml

sudo nano /etc/kubernetes/manifests/static-pod.yaml

sudo nano /etc/kubernetes/manifests/kube-apiserver.yaml

sudo nano /etc/kubernetes/manifests/etcd.yaml

sudo cat /etc/kubernetes/manifests/kube-apiserver.yaml

sudo cat /etc/kubernetes/manifests/etcd.yaml

sudo rm /etc/kubernetes/manifests/etcd.yaml

sudo apt-get update

sudo apt-get install nano -y

---

rm -rf /tmp/juju-*  

/etc/kubernetes/manifests/static-pod-2.yaml

ls /etc/kubernetes/manifests/
