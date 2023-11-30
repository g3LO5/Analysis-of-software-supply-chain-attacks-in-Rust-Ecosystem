import os
import subprocess
import re
from tqdm import tqdm

# Hàm để loại bỏ các mã ANSI
def remove_ansi_codes(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Loại bỏ các mã ANSI
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    no_ansi_text = ansi_escape.sub('', text)

    # Ghi lại tệp tin không có mã ANSI
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(no_ansi_text)

# Đường dẫn đến thư mục chứa các tệp tin
input_dir = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\GetPackage\package'

# Đường dẫn đến thư mục lưu kết quả
output_dir = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\Detect\result'

# Đường dẫn đến oss-detect-backdoor.exe
oss_detect_backdoor_path = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-detect-backdoor\bin\Debug\net6.0\oss-detect-backdoor.exe'

# Lấy danh sách tất cả các tệp tin trong thư mục input
files = [f for f in os.listdir(input_dir) if f.startswith('cargo-pkg-cargo-')]

# Duyệt qua tất cả các tệp tin trong thư mục input
for filename in tqdm(files, desc="Processing files"):
    # Tạo câu lệnh
    name = filename.replace('cargo-pkg-cargo-', '')
    output_file = os.path.join(output_dir, f"{name}.txt")

    # Kiểm tra xem tệp tin kết quả đã tồn tại chưa
    if not os.path.exists(output_file):
        command = f'{oss_detect_backdoor_path} pkg:cargo/{name} > {output_file}'

        # Chạy câu lệnh
        subprocess.run(command, shell=True)

        # Loại bỏ các mã ANSI
        remove_ansi_codes(output_file)
