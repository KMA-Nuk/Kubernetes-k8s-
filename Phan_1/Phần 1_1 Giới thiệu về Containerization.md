**Khái niệm Container** : là một hình thức ảo hóa hệ điều hành cho phép nhiều ứng dụng hoặc dịch vụ chạy trên cùng một hệ điều hành mà vẫn được cách ly với nhau.Đóng gói toàn bộ ứng dụng: thư viện ,code, phụ thuộc cần thiết. Cho phép phần mềm chạy trong tầm kiểm soát và hoạt động tốt khi được chuyển từ môi trường máy chủ này sang môi trường máy chủ khác. 

**Khái niệm VM (virtual machine)** : VM tạo ra một máy tính ảo hoàn chỉnh, với hệ điều hành riêng biệt và tài nguyên phần cứng được cấp phát từ máy chủ vật lý.

| Virtual machine                                              | Container                                                    |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| -      Trong  mỗi máy ảo chạy một hệ điều hành khách (Guest OS) duy nhất. <br /> -      Mất  1 khoảng thời gian khá lâu để triển khai   -      Với  máy ảo, phần cứng đang được ảo hóa để chạy nhiều phiên bản HĐH.  <br />-      Không  thể chạy nhiều vm trên máy tính trung bình  <br /> -      Disadvantages:  <br />+ Consume a lot of disk space,Ram,Cpu from the  server  <br />+slow to startup | -      Các  container cung cấp mức độ ảo hóa HĐH để nhiều ứng dụng có thể chạy trên chỉ một  thực thể HĐH (OS instance)  <br />-      Container  kích thước nhẹ .ứng dụng này có kích thước chỉ vài megabyte và chỉ mất vài  giây để khởi động( so với gigabyte và mất vài phút để VM khởi động).  <br />-      Có  thể chạy nhiệu docker container trên 1 máy tính . |

 ![image-20240909120148937](C:\Users\NghiaPC\AppData\Roaming\Typora\typora-user-images\image-20240909120148937.png)

![image-20240909120029375](C:\Users\NghiaPC\AppData\Roaming\Typora\typora-user-images\image-20240909120029375.png)

**Lợi ích của container** trong phát triển và triển khai ứng dụng

1. Tính nhất quán giữa các môi trường : vấn đề : môi trường phát triển thường không giống với môi trường sản xuất. -> giải pháp : Containers giúp đóng gói toàn bộ ứng dụng cùng với các thư viện và phụ thuộc cần thiết. Điều này đảm bảo rằng ứng dụng sẽ chạy nhất quán trên mọi môi trường (phát triển, thử nghiệm, và sản xuất)

2. Tính di động cao : Một ứng dụng chạy trong container có thể chuyển từ máy tính cá nhân / của nhà phát triển -> máy chủ trên đám mây ( không gặp sự cố : khác biệt về môi trường). Các nền tảng như Docker và Kubernetes hỗ trợ chạy container trên bất kỳ hệ điều hành hay dịch vụ đám mây nào.

3. Tiết kiệm tài nguyên : Containers chia sẻ kernel hệ điều hành và không yêu cầu hệ điều hành riêng cho mỗi ứng dụng. Cho phép chạy nhiều container trên cùng một máy chủ mà không tốn nhiều tài nguyên như với VM.

   