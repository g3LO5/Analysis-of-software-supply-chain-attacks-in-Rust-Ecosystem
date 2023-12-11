import os
import csv
import re

# Đường dẫn đến thư mục chứa các file .txt
folder_path = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\Detect\result'

# Mở file .csv để ghi kết quả
with open('results_analy_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['package_name', 'total_tags', 'unique_tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                # Loại bỏ các ký tự màu sắc
                content = re.sub(r'\x1b\[[0-9;]*m', '', content)
                package_name = filename.replace('.txt', '')
                match = re.search(r'Match #1 of (\d+)', content)
                if match is not None:
                    total_tags = int(match.group(1))
                    tags = re.findall(r'Tag: (.+)', content)
                    unique_tags = list(set(tags))  # Loại bỏ các tag trùng lặp

                    if total_tags == 0:
                        # Nếu total_tags bằng 0, bỏ qua việc ghi kết quả vào file .csv
                        continue

                    # Ghi kết quả vào file .csv ngay lập tức
                    writer.writerow({'package_name': package_name, 'total_tags': total_tags, 'unique_tags': ', '.join(unique_tags)})
