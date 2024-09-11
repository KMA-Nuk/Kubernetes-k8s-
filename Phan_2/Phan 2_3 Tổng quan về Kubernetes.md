Tổng quan về Kubernetes
- Khái niệm, lợi ích và vai trò của K8s trong quản lý container
- Các thành phần chính của K8s: Pod, Node, Cluster, etcd, Control Plane

**Khái niệm** : ( Container Orchestration tool , developed by Google ) là một nền tảng mã nguồn mở giúp tự động hoá việc triển khai, mở rộng và quản lý các ứng dụng container hoá. Kubernetes cho phép quản lý các container ứng dụng một cách dễ dàng và hiệu quả trên các môi trường đa đám mây. 

**Lợi ích của Kubernetes:** 

- **Tự động hoá**: Tự động quản lý các container     từ việc triển khai, giám sát đến bảo trì.
- **Khả năng mở rộng**: Hỗ trợ mở rộng ứng dụng dễ     dàng khi có sự gia tăng về tải.
- **Tính di động**: Kubernetes giúp ứng dụng của     bạn có thể chạy trên các môi trường khác nhau (on-premise, đám mây công cộng,     đám mây riêng) mà không cần thay đổi cấu trúc.
- **Tính sẵn sàng cao**: Kubernetes giúp phân tán ứng     dụng trên nhiều node để đảm bảo tính liên tục và sẵn sàng khi một phần của     hệ thống gặp sự cố.
- **Quản lý tài nguyên hiệu quả**: Điều chỉnh tự động mức tiêu     thụ tài nguyên của các container, tối ưu hóa việc sử dụng tài nguyên phần     cứng.

**Vai trò của Kubernetes trong quản lý container:**

Kubernetes đảm nhận vai trò là nền tảng điều phối container, giúp người dùng quản lý các container theo cách tự động và hiệu quả. Nó giúp kiểm soát quá trình triển khai ứng dụng, đảm bảo khả năng chịu lỗi, tự động phục hồi và tối ưu hóa tài nguyên hệ thống.

![img](file:///C:/Users/NghiaPC/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

Các thành phần chính của K8s

**Pod**:

- Là đơn vị nhỏ nhất trong     Kubernetes, bao gồm một hoặc nhiều container cùng chia sẻ một mạng và     không gian lưu trữ. Mỗi Pod đại diện cho một phiên bản chạy của một ứng dụng.
- Các Pod có thể giao tiếp với     nhau thông qua mạng của cluster và được quản lý bởi Kubernetes để đảm bảo     chúng hoạt động đúng cách.

**Node**:

- Là một máy chủ vật lý hoặc ảo     trong cluster, trên đó Kubernetes sẽ quản lý các Pod. Mỗi node chạy các     thành phần như kubelet, công cụ container (như Docker), và các dịch vụ mạng     khác.
- Có hai loại node: Worker Node     (chạy ứng dụng) và Master Node (điều khiển toàn bộ cluster).
- Đại diện cho 1 máy duy nhất     trong cluster

**Cluster**:

- Bao gồm nhiều node hoạt động đồng     thời để quản lý và chạy các ứng dụng container hoá. Kubernetes quản lý     toàn bộ các node trong một cluster để đảm bảo chúng hoạt động ổn định và     hiệu quả.

**etcd**:

- **Là một cơ sở dữ liệu** key-value phân tán, lưu trữ     toàn bộ thông tin trạng thái của cluster Kubernetes. Mọi thay đổi trong cấu     trúc cluster đều được lưu trữ và đồng bộ qua etcd.
- Nó đảm bảo tính nhất quán     trong quản lý thông tin trạng thái của các thành phần trong cluster.

**Control Plane:**

- Là tập hợp các thành phần điều     khiển chính của Kubernetes, bao gồm các dịch vụ như kube-apiserver,     kube-controller-manager, kube-scheduler, và etcd.
- Các thành phần này có nhiệm vụ     giám sát và điều khiển toàn bộ hoạt động của các Pod và Node trong     cluster, đảm bảo hệ thống hoạt động đúng như mong muốn.

 

**Thời đại triển khai ảo hóa:** Như một giải pháp, ảo hóa đã được giới thiệu. Nó cho phép bạn chạy nhiều Máy ảo (VM) trên CPU của một máy chủ vật lý. Ảo hóa cho phép các ứng dụng được cô lập giữa các VM và cung cấp mức độ bảo mật vì thông tin của một ứng dụng không thể được truy cập tự do bởi một ứng dụng khác.

![img](file:///C:/Users/NghiaPC/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

![img](file:///C:/Users/NghiaPC/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)