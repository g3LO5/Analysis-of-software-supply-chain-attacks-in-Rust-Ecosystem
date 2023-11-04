import os
import json
import requests
import csv
from operator import itemgetter
from tqdm import tqdm

# Đường dẫn đến thư mục chứa các file .txt
dir_path = "C:\\Users\\Admin\\OneDrive\\Documents\\GitHub\\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\\package\\typo-squatting\\name-typop-squatting"
AverageTypos = 4;
# Lấy danh sách tên từ các file .txt
names = []
files = [f for f in os.listdir(dir_path) if f.endswith(".txt")]
for filename in files:
    with open(os.path.join(dir_path, filename), 'r') as f:
        lines = f.readlines()
        lines = [line for line in lines if line.startswith("Potential Squat candidate")]  # Chỉ lấy các dòng bắt đầu bằng "Potential Squat candidate"
        for line in lines[:min(AverageTypos, len(lines))]: 
            name = line.split("'")[1]  # Lấy tên từ dòng
            names.append(name)

# Tạo file CSV mới
with open('downloads.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Download Count"])  # Ghi tiêu đề cột

# Lấy số lượng tải về từ crates.io và ghi vào file CSV
total_names = len(names)
for i, name in enumerate(tqdm(names, desc="Pocessing names", unit="name")):
    response = requests.get(f"https://crates.io/api/v1/crates/{name}")
    data = json.loads(response.text)
    download_count = data['crate']['downloads']
    with open('downloads.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, download_count])  # Ghi dữ liệu vào file CSV

# Đọc file CSV, sắp xếp theo số lượng tải về từ thấp đến cao, và ghi lại vào file CSV
with open('downloads.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Bỏ qua tiêu đề cột
    downloads = list(reader)
downloads.sort(key=lambda x: int(x[1]))
with open('downloads.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Download Count"])  # Ghi lại tiêu đề cột
    for name, download_count in downloads:
        writer.writerow([name, download_count])  # Ghi lại dữ liệu đã sắp xếp
