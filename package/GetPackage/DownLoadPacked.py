import csv
import subprocess
import os
from tqdm import tqdm

# Đường dẫn đến thư mục chứa lệnh oss-download
oss_download_path = "C:\\Users\\Admin\\OneDrive\\Documents\\GitHub\\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\\OSSGadget\\src\\oss-download\\bin\\Debug\\net6.0"

# Đường dẫn đến thư mục muốn lưu các gói đã tải về
download_directory = "C:\\Users\\Admin\\OneDrive\\Documents\\GitHub\\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\\package\\GetPackage\\package"

# Đọc file CSV và lấy tất cả các dòng
with open('downloads.csv', newline='') as csvfile:
    reader = list(csv.DictReader(csvfile))

# Tạo thanh tiến trình với tổng số dòng là độ dài của reader
with tqdm(total=len(reader), ncols=70) as pbar:
    for row in reader:
        # Lấy tên gói và đường dẫn tải về
        package_name = row['Name']

        # Tạo lệnh oss-download
        command = f"oss-download --download-directory {download_directory} -c pkg:cargo/{package_name}"

        # Chạy lệnh oss-download
        subprocess.run(command, cwd=oss_download_path, shell=True)

        # Cập nhật thanh tiến trình
        pbar.update(1)
