import os
import requests

# Tạo thư mục 'Package' nếu nó chưa tồn tại
if not os.path.exists('Package'):
    os.makedirs('Package')

# Đọc tên và phiên bản của các gói từ file
with open('NameAndVersion.txt', 'r') as f:
    packages = [line.strip() for line in f]

# Tải về từng gói
for package in packages:
    name, version = package.split()
    url = f"https://static.crates.io/crates/{name}/{name}-{version}.crate"
    
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Tạo tên file để lưu gói
        filename = f"Package/{name}-{version}.crate"

        # Ghi nội dung phản hồi vào file
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Đã tải về {filename}")
    else:
        print(f"Không thể tải về {url}")
