import os
import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor

def run_command(syn):
    dst = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\typo-squatting\name-typop-squatting/{0}.txt'.format(syn)
    if os.path.exists(dst):
        print(f"File {syn} already exists. Skipping.")
        return
    command = r'.\oss-find-squats.exe -o {0}.txt pkg:cargo/{1}'.format(syn, syn)
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, cwd=r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-find-squats\bin\Debug\net6.0')
    src = r"C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-find-squats\bin/Debug/net6.0/{0}.txt".format(syn)
    shutil.move(src,dst)

with open(r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\GetPackage\name.txt', 'r') as f:
    lines = [line.strip() for line in f]

with ThreadPoolExecutor(max_workers=7) as executor:
    executor.map(run_command, lines)
