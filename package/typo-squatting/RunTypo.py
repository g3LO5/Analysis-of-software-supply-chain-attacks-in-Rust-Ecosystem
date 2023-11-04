import os
import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from threading import Lock

lock = Lock()
processing_names = set()

def run_command(name):
    dst = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\typo-squatting\name-typop-squatting/{0}.txt'.format(name)
    with lock:
        if name in processing_names or os.path.exists(dst):
            pbar.update()  # Cập nhật thanh tiến trình
            print(f"File {name} already exists. Skipping.")
            return
        processing_names.add(name)
    command = r'.\oss-find-squats.exe -o {0}.txt pkg:cargo/{1}'.format(name, name)
    result = subprocess.run(command, shell=True, capture_output=True, cwd=r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-find-squats\bin\Debug\net6.0')
    src = r"C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-find-squats\bin/Debug/net6.0/{0}.txt".format(name)
    with lock:  # Sử dụng khóa khi di chuyển file
        shutil.move(src,dst)
    pbar.update()  # Cập nhật thanh tiến trình

with open(r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\GetPackage\name.txt', 'r') as f:
    lines = [line.strip() for line in f]

pbar = tqdm(total=len(lines), desc="Processing ", unit="name")
with ThreadPoolExecutor() as executor:
    executor.map(run_command, lines)
pbar.close()
