import requests
from bs4 import BeautifulSoup
import json

# 目标URL
url = "https://geo.mirror.pkgbuild.com/wsl"

try:
    # 发送HTTP GET请求获取网页内容
    response = requests.get(url)
    if response.status_code != 200:
        error = f"Failed to retrieve the webpage. Status code: {response.status_code}"
        raise Exception(error)

    # 解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取所有<a>标签的href属性
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]
    if not hrefs:
        error = "No links found on the page."
        raise Exception(error)
    hrefs = [href for href in hrefs if href != '../']

    archlinux_wsl_list = list()

    # 打印提取到的链接
    for href in hrefs:
        website = url + '/' + href + 'archlinux.wsl'
        archlinux_wsl_list.append(
            {
                'name': href.replace('/', ''),
                'branch': 'wsl', 
                'docker_brew_archlinux': website
            })
    json.dump(archlinux_wsl_list, open(
        'archlinux_wsl_list.json', 'w'), indent=4)
except Exception as e:
    print(e)