# Sử dụng Python 3.9 làm base image
FROM python:3-alpine

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Cài đặt curl
RUN apk add --no-cache curl

# Copy file requirements.txt vào container
COPY requirement.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirement.txt

# Copy toàn bộ mã nguồn vào container
#COPY . ./
COPY /tools/Code/Flaskapi/ ./

# Expose port 5000
EXPOSE 5000

# Lệnh chạy ứng dụng Flask
ENTRYPOINT ["python3", "app.py"]
