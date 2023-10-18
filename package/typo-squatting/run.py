import subprocess
import shutil

with open(r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\typo-squatting\name.txt', 'r') as f:
     for line in f:
         syn = line.strip()
         command = r'.\oss-find-squats.exe -o {0}.txt pkg:cargo/{1}'.format(syn, syn)
         result = subprocess.run(command, shell=True, capture_output=True, cwd=r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-find-squats\bin\Debug\net6.0')
         src = r"C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\OSSGadget\src\oss-find-squats\bin/Debug/net6.0/{0}.txt".format(syn)
         dst = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\typo-squatting'
         shutil.move(src,dst)