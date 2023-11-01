import requests
from bs4 import BeautifulSoup

def get_package_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    packages = soup.find_all('div', class_='project')

    package_info = []
    for package in packages:
        name_tag = package.find('h5')
        if name_tag is not None:
            name_link = name_tag.find('a')
            if name_link is not None:
                name = name_link.text.strip()
                package_info.append(name)

    return package_info

def save_to_file(filename, data):
    with open(filename, 'a') as f:
        for line in data:
            f.write(f"{line}\n")

base_url = "https://libraries.io/search?order=desc&page={}&platforms=Cargo&sort=dependent_repos_count"
filename = "name.txt"

# Tạo ra tệp .txt trước
open(filename, 'w').close()

for i in range(1, 31):
    url = base_url.format(i)
    package_info = get_package_info(url)
    save_to_file(filename, package_info)

    # Dừng vòng lặp nếu đã có đủ 200 gói
    if sum(1 for line in open(filename)) >= 200:
        break
