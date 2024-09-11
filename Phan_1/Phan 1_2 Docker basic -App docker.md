*- Docker Basics
 \- Các khái niệm về Image, Container, Dockerfile
 \- Các lệnh cơ bản: build, run, pull, push
 \- Thực hành tạo và chạy một ứng dụng cơ bản trong Docker*

**Docker** : là 1 nền tảng đóng gói, triển khai và chạy ứng dụng trong các **container**. Các container này giống như những "hộp" chứa toàn bộ môi trường cần thiết để ứng dụng có thể chạy được, bao gồm mã nguồn, thư viện, và các phụ thuộc khác.. ( đóng gói sản phẩm )

**Docker file**: Là tệp văn bản chứa các hướng dẫn để xây dựng một Docker image. Dockerfile mô tả cách để thiết lập môi trường và chạy ứng dụng trong container.(công thức)(Dockerfile không có phần mở rộng phía sau)

**Image**: Là một tập hợp các lớp (layers) bao gồm tất cả các thông tin cần thiết để khởi chạy container, như mã nguồn, thư viện, và thiết lập. Một image có thể được tạo ra từ một Dockerfile hoặc tải về từ Docker Hub ( bao gồm : OS , lib ,code )

**Container:** Khi một container được tạo, nó sẽ chứa một ứng dụng và các tài nguyên cần thiết để ứng dụng có thể hoạt động. ( Container tương tự như một máy ảo nhẹ nhưng dùng chung kernel của hệ điều hành host. )

**Docker Hub**: Là một kho lưu trữ các image, nơi bạn có thể tải về các image có sẵn hoặc đẩy image của mình lên.

 

**Các lệnh cơ bản: build, run, pull, push**

 **docker build**: Dùng để tạo Docker image từ Dockerfile.

`docker build -t <image_name> .`		(-t : tag -> cho phép đặt tên image)

 **docker run**: Dùng để tạo và khởi chạy container từ image.

`docker run -d --name <container_name> <image_name>` 		(`-d` là viết tắt của **detached mode**. Container chạy ở chế độ nền (background), tiếp tục sử dụng terminal sau khi container được khởi chạy.)

 **docker pull**: Tải một Docker image từ registry (thường là từ Docker Hub).

`docker pull <image_name>`

 **docker push**: Đẩy Docker image từ local lên registry.

`docker push <image_name>`



**Tạo và chạy 1 application trong Docker**

**Bước 1** :Code web application python hiển thị "Hello World"

https://github.com/KMA-Nuk/codeappdocker.git

**Bước 2** :Đẩy image lên Docker Hub

*Command docker terminal* trên PowerShell

`docker build -t name_image .` :Tạo mới 1 image từ Dockerfile  (Trong đó name_image = Repositorise name (tạo trên DockerHub))

[Nếu có image sẵn thì dùng lệnh sau để gán: `docker tag id_image||name_image Repositorise_name`  (example: `docker tag ab3367dd1910 nghia5/helloworld` )]

`docker images` : show các image có sẵn

`docker push name_image:tagname` :Đẩy image lên Docker Hub

![image-20240911093113457](C:\Users\NghiaPC\AppData\Roaming\Typora\typora-user-images\image-20240911093113457.png)

**Bước 3** :Run application (Run image -> Tạo ra container -> Run container)

`docker run name_image` : Chạy application bằng docker

[example:`docker run -p 8080:8080 nghia5/helloworld` :Tạo ra 1 container với tên random , -p 8080:8080: Ánh xạ cổng 8080 trên máy chủ cục bộ (host) với cổng 8080 trong container. ]

`docker run --name [container_name] -dp [host_port]:[container_port] name_image` :đặt tên cho container.

*[Có thể run image bằng Docker Desktop]*

**Bước 4** :Truy cập Webapp 

`localhost:8080`

`docker stop name_container` :Dừng container đang chạy (với mode chạy ngầm -d)