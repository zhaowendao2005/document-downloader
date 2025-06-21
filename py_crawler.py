import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
import logging
import random
import re
import json
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- 获取一个模块级的 logger ---
# 日志的配置（如 level 和 handler）将由主应用来决定
log = logging.getLogger(__name__)

# --- 默认 User-Agent 池 ---
USER_AGENT_POOL = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
]

def parse_sitemap(path):
    """解析 sitemap.xml 文件并提取所有 URL。"""
    try:
        log.info(f"正在从 '{path}' 解析站点地图...")
        tree = ET.parse(path)
        root = tree.getroot()
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [elem.text for elem in root.findall('ns:url/ns:loc', namespace)]
        if not urls:
            log.warning("在 sitemap 中没有找到 URL。")
            return []
        log.info(f"成功解析到 {len(urls)} 个 URL。")
        return urls
    except Exception as e:
        log.error(f"解析 Sitemap 文件失败: {e}")
        return []

def url_to_filename(url, output_dir):
    """将 URL 转换为安全的文件路径。"""
    parsed_url = urlparse(url)
    path = parsed_url.path
    if path.startswith('/'):
        path = path[1:]
    if not path:
        path = 'index'
    if path.endswith('/'):
        path = path[:-1]
    
    file_path_parts = path.split('/')
    dir_path = os.path.join(output_dir, *file_path_parts[:-1])
    os.makedirs(dir_path, exist_ok=True)
    
    filename = file_path_parts[-1]
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return os.path.join(dir_path, f"{filename}.md")

def fetch_and_process(url, output_dir, selectors):
    """
    抓取单个 URL，使用多个选择器提取内容，并保存为 MD 文件。
    """
    try:
        headers = {'User-Agent': random.choice(USER_AGENT_POOL)}
        proxies = {'http': None, 'https': None}
        
        response = requests.get(url, headers=headers, timeout=15, proxies=proxies)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')
        
        all_content_parts = []
        for selector in selectors:
            content_element = soup.select_one(selector)
            if content_element:
                content = content_element.get_text(separator='\n', strip=True)
                all_content_parts.append(f"## 内容来源 (Selector: `{selector}`)\n\n{content}")
        
        if all_content_parts:
            final_content = "\n\n---\n\n".join(all_content_parts)
            metadata = f"---\nurl: {url}\ncrawled_at: {datetime.now().isoformat()}\n---\n\n"
            full_content_to_save = metadata + final_content
            
            filepath = url_to_filename(url, output_dir)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content_to_save)
            
            log.info(f"成功保存内容到: {filepath}")
            return {"url": url, "status": "success", "path": filepath}
        else:
            log.warning(f"在 {url} 中，所有指定选择器均未找到内容。")
            return {"url": url, "status": "not_found"}
            
    except requests.RequestException as e:
        log.error(f"抓取 {url} 时发生网络错误: {e}")
        return {"url": url, "status": "error", "reason": str(e)}
    except Exception as e:
        log.error(f"处理 {url} 时发生未知错误: {e}")
        return {"url": url, "status": "error", "reason": str(e)}

def run_crawling(sitemap_path, output_dir, config, progress_callback=None):
    """
    可被外部调用的爬虫主函数。
    :param progress_callback: 用于报告进度的回调函数。
    """
    log.info(f"所有文件将保存到: {output_dir}")
    
    urls = parse_sitemap(sitemap_path)
    if not urls:
        log.warning("没有可抓取的 URL，程序退出。")
        return

    selectors = config.get('targetSelectors', [])
    if not selectors:
        log.error("配置中未提供 targetSelectors，无法提取内容。")
        return
        
    max_workers = config.get('maxWorkers', 5)
    success_count = 0
    failure_count = 0
    total_urls = len(urls)
    
    log.info(f"开始使用 {max_workers} 个并发线程抓取 {total_urls} 个 URL...")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fetch_and_process, url, output_dir, selectors): url for url in urls}
        
        for i, future in enumerate(as_completed(future_to_url)):
            result = future.result()
            if result and result['status'] == 'success':
                success_count += 1
            else:
                failure_count += 1
            
            if progress_callback:
                progress_callback(i + 1, total_urls, success_count, failure_count)

    log.info("所有抓取任务已完成。")
    log.info(f"总计: {total_urls} 个链接，成功抓取并保存: {success_count} 个，失败: {failure_count} 个。")

# 这个 main guard 块现在仅用于独立测试，GUI不应依赖它。
if __name__ == '__main__':
    # 为了测试，我们需要手动配置日志记录器
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log.info("正在以独立模式运行爬虫核心模块...")
    
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        log.error("未找到 config.json 文件。请确保配置文件存在。")
        config = {}
        
    sitemap_file = config.get("sitemapPath", "sitemap.xml")
    output_directory = os.path.join(
        config.get("baseOutputDir", "output"),
        f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    os.makedirs(output_directory, exist_ok=True)
    
    # 简单的进度打印回调
    def test_progress(current, total, success, fails):
        print(f"进度: {current}/{total} (成功: {success}, 失败: {fails})", end='\r')

    run_crawling(sitemap_file, output_directory, config, test_progress)
    print("\n测试运行完成。")