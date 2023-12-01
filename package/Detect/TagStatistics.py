import os
import re
import csv
from collections import Counter
from tqdm import tqdm

def remove_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def count_tags(directory):
    tag_counter = Counter()
    tag_files = {}
    tag_pattern = re.compile(r'Tag: (.*)')

    filenames = [f for f in os.listdir(directory) if f.endswith('.txt')]
    for filename in tqdm(filenames, desc="Processing files"):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = remove_ansi_codes(line)
                match = tag_pattern.search(clean_line)
                if match:
                    tag = match.group(1)
                    tag_counter[tag] += 1
                    if tag not in tag_files:
                        tag_files[tag] = set()
                    tag_files[tag].add(filename)

    return tag_counter, tag_files

def save_to_csv(counter, tag_files, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag', 'Count', 'Files'])
        for tag, count in counter.items():
            files = ', '.join(tag_files[tag])
            writer.writerow([tag, count, files])

directory = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\Detect\result'
output_file = r'C:\Users\Admin\OneDrive\Documents\GitHub\Analysis-of-software-supply-chain-attacks-in-Rust-Ecosystem\package\Detect\tag_counts.csv'

tag_counter, tag_files = count_tags(directory)
save_to_csv(tag_counter, tag_files, output_file)
