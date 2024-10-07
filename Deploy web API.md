Deploy web API

Bước 1 :

Tạo 1 file  `app.py` sử dụng framework flask của python

`from flask import Flask`

`app = Flask(__name__)`

`@app.route('/')`

`def hello():`

​    `return "Hello World!"`

`if __name__ == '__main__':`

​    `app.run(debug= True, host='0.0.0.0', port=5000)`

Tạo 1 file `requirement.txt`

`flask`

Bước 2 :Viết Dockerfile cho dự án

`FROM python:3-alpine`

`WORKDIR /app`

`COPY requirement.txt .`

`RUN pip install --no-cache-dir -r requirement.txt`

`COPY . ./`

`EXPOSE 5000`

`ENTRYPOINT  ["python3", "app.py"]`

Bước 3 :Tạo image từ Dockerfile trên

`docker build -t flask-api:latest .`

Ktra k8s

`minikube status`

![image-20240925172351748](/home/ubuntu/.config/Typora/typora-user-images/image-20240925172351748.png)

`apply file deployment.yaml va service.yaml` va kiem tra ip cua minikube

![image-20240925172418780](/home/ubuntu/.config/Typora/typora-user-images/image-20240925172418780.png)

kubectl get services 

![image-20240925172644018](/home/ubuntu/.config/Typora/typora-user-images/image-20240925172644018.png)



- **Kiểm tra `kube-proxy`:**

`kube-proxy` thường chạy như một pod trong namespace `kube-system`.

kubectl get pods -n kube-system 

![image-20240925172806292](/home/ubuntu/.config/Typora/typora-user-images/image-20240925172806292.png)

