Tạo cụm k8s gồm 2 node (Ubuntu 22.04 - K8s version v1.31)

1 master node : IP : 10.0.2.17, resource 2 cpu,23gi disk, 2 gb ram

1 worker node : IP : 10.0.2.18, resource 2 cpu,20gi disk, 2 gb ram

![image-20241006222658591](/home/ubuntu/.config/Typora/typora-user-images/image-20241006222658591.png)

Ssh vào 2 máy ảo bằng terminal trên máy host

`ssh -p <host_port> user@localhost`

# Tiến hành trên 2 node

`sudo apt update`
`sudo apt upgrade -y`

`sudo reboot`

### Đặt hostname và cập nhật hosts file

#### Master node

```bash
sudo hostnamectl set-hostname "k8s-master1"
```

#### Worker 1

```bash
sudo hostnamectl set-hostname "k8s-worker1"
```

`sudo apt install -y nano` // Cài nano editor nếu server chưa có
`sudo nano /etc/hosts`

thêm vào bên dưới file nội dung dưới đây:

10.0.2.17  k8s-master1 k8s-master1
10.0.2.18  k8s-worker1 k8s-worker1

### Disable swap và cập nhật kernel

`sudo swapoff -a`

`free -h` 

`sudo nano /etc/fstab`

Tìm dòng: `/swap.img none swap sw 0 0` và cập nhật lại thành:

```bash
#/swap.img       none       swap       sw       0       0
```

`sudo mount -a`
`free -h`

```bash
sudo tee /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF
sudo modprobe overlay
sudo modprobe br_netfilter
sudo tee /etc/sysctl.d/kubernetes.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```

Sau đó reload lại `sysctl`

```bash
sudo sysctl --system

```

## Cài đặt containerd run time - containerd

`sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates`
`sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/docker.gpg`
`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
`sudo apt update`
`sudo apt install -y containerd.io`

Cấu hình containerd

`containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1`
`sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml`
`sudo systemctl restart containerd`
`sudo systemctl enable containerd`

## Cài đặt Kubernetes

```shell
sudo apt-get update
# apt-transport-https may be a dummy package; if so, you can skip that package
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
# If the directory `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
# sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet
```

## Khởi tạo cluster bằng kubeadm

### Chạy trên node master

`kubeadm init --apiserver-advertise-address=10.0.2.17 --pod-network-cidr=10.0.0.0/16`

<!--( chạy lênh trên xong thì 2 mục cần lưu lại mkdir ... & kubeadm join ....)-->

`mkdir -p $HOME/.kube`
`sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config`
`sudo chown $(id -u):$(id -g) $HOME/.kube/config`

`kubectl cluster-info`
`kubectl get nodes`

### Thêm worker node vào cluster

Chạy trên node worker node

`kubeadm` join k8s-master1:6443 --token daii9y.g4dq24u6irkz4pt0 \```
        --discovery-token-ca-cert-hash sha256:58b9cc96ed57a5797fddea653756dbda830efbff55b720a10cffb3948d489148```

( lệnh trên tùy vào chạy init cop ở đó)

### Chạy trên node master

`kubectl get nodes` 

kết quả trả về : Status : NotReady

### Cài đặt Calico Pod Network cho Kubernetes cluster (masternode)

`kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml`

`kubectl apply -f calico.yaml`

kiểm tra calico deploy thành công chưa ? 

```bash
kubectl get pods -n kube-system
```

`kubectl get nodes` 

kết quả trả về : Status : Ready