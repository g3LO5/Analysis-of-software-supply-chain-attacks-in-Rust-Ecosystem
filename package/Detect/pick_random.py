import os
import random

def select_random_messages(input_directory, output_directory, num_messages=42):
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as f:
                content = f.read()
            messages = content.split('\n\n--[ Match')
            if num_messages > len(messages):
                selected_messages = messages
            elif num_messages <= 0:
                continue
            else:
                selected_messages = random.sample(messages, num_messages)
            selected_messages = ['--[ Match' + msg for msg in selected_messages]
            with open(os.path.join(output_directory, 'selected_' + filename), 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(selected_messages))

input_directory = r'D:\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\Detect\result'  # Thay thế 'your_input_directory' bằng đường dẫn thư mục chứa file .txt của bạn
output_directory = r'D:\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\Detect\result_random'  # Thay thế 'your_output_directory' bằng đường dẫn thư mục bạn muốn lưu các file đã chọn
select_random_messages(input_directory, output_directory)
