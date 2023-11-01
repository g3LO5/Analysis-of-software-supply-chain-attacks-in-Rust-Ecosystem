import os

def count(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    total_lines = 0

    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            lines = f.readlines()
            total_lines += len([line for line in lines if line.strip()])

    average = round(total_lines / len(files)) if files else 0

    return average

directory = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\typo-squatting\name-typop-squatting'  # Thay thế 'your_directory' bằng đường dẫn thư mục của bạn
print(f"Average: {count(directory)}")
