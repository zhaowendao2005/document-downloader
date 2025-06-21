import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
import logging
import random
import re
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- 配置 ---
SITEMAP_PATH = 'sitemap.xml'
TARGET_SELECTOR = '.theme-doc-markdown'
# 新增：基础输出目录
BASE_OUTPUT_DIR = 'output'
MAX_WORKERS = 10
USER_AGENT_POOL = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
]

# --- 日志配置 ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_sitemap(path):
    """解析 sitemap.xml 文件并提取所有 URL。"""
    try:
        logging.info(f"正在从 '{path}' 解析站点地图...")
        tree = ET.parse(path)
        root = tree.getroot()
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [elem.text for elem in root.findall('ns:url/ns:loc', namespace)]
        if not urls:
            logging.warning("在 sitemap 中没有找到 URL。")
            return []
        logging.info(f"成功解析到 {len(urls)} 个 URL。")
        return urls
    except Exception as e:
        logging.error(f"解析 Sitemap 文件失败: {e}")
        return []

def url_to_filename(url, output_dir):
    """将 URL 转换为安全的文件路径。"""
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    # 移除路径开头的斜杠
    if path.startswith('/'):
        path = path[1:]
    # 如果路径为空（首页），使用 index
    if not path:
        path = 'index'
    # 移除尾部的斜杠
    if path.endswith('/'):
        path = path[:-1]
        
    # 将路径中的斜杠替换为目录分隔符，并创建目录
    file_path_parts = path.split('/')
    dir_path = os.path.join(output_dir, *file_path_parts[:-1])
    
    # 创建目录结构
    os.makedirs(dir_path, exist_ok=True)
    
    # 使用最后一部分作为文件名
    filename = file_path_parts[-1]
    # 清理文件名
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    return os.path.join(dir_path, f"{filename}.md")

def fetch_and_save(url, output_dir):
    """抓取单个 URL，提取内容并直接保存为 MD 文件。"""
    try:
        headers = {'User-Agent': random.choice(USER_AGENT_POOL)}
        proxies = {'http': None, 'https': None}
        
        response = requests.get(url, headers=headers, timeout=15, proxies=proxies)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')
        content_element = soup.select_one(TARGET_SELECTOR)
        
        if content_element:
            content = content_element.get_text(separator='\n', strip=True)
            
            # 创建元数据
            metadata = f"---\nurl: {url}\ncrawled_at: {datetime.now().isoformat()}\n---\n\n"
            full_content = metadata + content
            
            # 生成文件名并保存
            filepath = url_to_filename(url, output_dir)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            logging.info(f"成功保存内容到: {filepath}")
            return {"url": url, "status": "success", "path": filepath}
        else:
            logging.warning(f"在 {url} 中未找到目标选择器 '{TARGET_SELECTOR}'。")
            return {"url": url, "status": "not_found"}
            
    except requests.RequestException as e:
        logging.error(f"抓取 {url} 时发生网络错误: {e}")
        return {"url": url, "status": "error", "reason": str(e)}
    except Exception as e:
        logging.error(f"处理 {url} 时发生未知错误: {e}")
        return {"url": url, "status": "error", "reason": str(e)}

def main():
    """主执行函数。"""
    # 1. 创建带时间戳的输出目录
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join(BASE_OUTPUT_DIR, f"output_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"所有文件将保存到: {output_dir}")

    urls = parse_sitemap(SITEMAP_PATH)
    if not urls:
        logging.warning("没有可抓取的 URL，程序退出。")
        return

    success_count = 0
    failure_count = 0
    
    logging.info(f"开始使用 {MAX_WORKERS} 个并发线程抓取 {len(urls)} 个 URL...")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(fetch_and_save, url, output_dir): url for url in urls}
        
        for i, future in enumerate(as_completed(future_to_url)):
            result = future.result()
            if result and result['status'] == 'success':
                success_count += 1
            else:
                failure_count += 1
            print(f"进度: {i + 1}/{len(urls)} (成功: {success_count}, 失败: {failure_count})", end='\r')

    print("\n")
    logging.info("所有抓取任务已完成。")
    logging.info(f"总计: {len(urls)} 个链接，成功抓取并保存: {success_count} 个，失败: {failure_count} 个。")

if __name__ == "__main__":
    main()