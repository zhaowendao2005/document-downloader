# 网站内容抓取器 (Python版)

这是一个基于 Python 的命令行工具，用于从指定网站的 `sitemap.xml` 文件中提取所有链接，并抓取每个链接页面的主要内容，最后将每个页面的内容保存为带有元数据的独立 Markdown 文件。

## 功能特性

- **Sitemap 解析**: 自动读取并解析项目根目录下的 `sitemap.xml` 文件，获取所有待抓取的 URL。
- **并发抓取**: 使用多线程并发执行抓取任务，以提高效率。
- **User-Agent 轮换**: 内置 User-Agent 池，在每次请求时随机选择一个，模拟不同浏览器，降低被屏蔽风险。
- **代理禁用**: 自动禁用系统级的 HTTP/HTTPS 代理，确保网络请求的直接性。
- **结构化输出**:
    - 每次运行都会在 `output` 目录下创建一个以当前时间戳命名的独立文件夹（如 `output/output_20250622_020400`）。
    - 每个成功抓取的页面都会被保存为一个 `.md` 文件。
    - 输出文件会保持原始 URL 的路径结构。
- **元数据添加**: 在每个生成的 Markdown 文件头部，自动添加 YAML Front Matter 格式的元数据，包含原始 URL 和抓取时间。

---

## 安装与设置

### 1. 前置要求

- 确保您的系统已安装 **Python 3.6** 或更高版本。

### 2. 安装依赖

建议在 Python 虚拟环境中进行操作，以避免与系统库冲突。

a. **创建并激活虚拟环境** (可选，但推荐)

```bash
# 创建虚拟环境 (例如，命名为 venv)
python -m venv venv

# 激活虚拟环境
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

b. **安装所需库**

项目依赖已在 `requirements.txt` 中列出。运行以下命令进行安装：

```bash
pip install -r requirements.txt
```

### 3. 准备 `sitemap.xml`

将您要抓取的目标网站的 `sitemap.xml` 文件放置在项目的根目录下。

---

## 配置

您可以直接修改 `py_crawler.py` 脚本顶部的配置变量来调整爬虫的行为：

- `SITEMAP_PATH`: `sitemap.xml` 文件的路径，默认为根目录下的 `sitemap.xml`。
- `TARGET_SELECTOR`: 用于提取页面主要内容的 CSS 选择器。请根据目标网站的 HTML 结构进行修改。默认为 `.theme-doc-markdown`。
- `BASE_OUTPUT_DIR`: 保存所有输出结果的基础目录，默认为 `output`。
- `MAX_WORKERS`: 并发抓取的线程数，默认为 `10`。可根据您的网络情况和目标服务器的承受能力适当调整。

---

## 如何运行

完成安装和配置后，只需在项目根目录下运行以下命令：

```bash
python py_crawler.py
```

脚本会开始执行，并在终端显示实时进度和日志信息。

---

## 输出说明

运行成功后，您会在 `output` 目录下看到一个新创建的、以时间戳命名的文件夹。该文件夹内包含了所有成功抓取的页面的 `.md` 文件，并保留了网站的原始路径结构。

例如，URL `https://example.com/docs/guides/getting-started` 的内容将被保存为：`output/output_YYYYMMDD_HHMMSS/docs/guides/getting-started.md`。

每个 Markdown 文件的内容如下：

```markdown
---
url: https://example.com/docs/guides/getting-started
crawled_at: 2025-06-22T02:04:00.123456
---

这里是抓取到的页面正文内容...
```

---

## 局限性

当前版本的爬虫使用 `requests` 和 `BeautifulSoup` 库，这决定了它**只能抓取静态 HTML 页面的内容**。

对于大量使用 JavaScript 在客户端动态渲染内容的现代网站（例如基于 React, Vue, Docusaurus 的站点），此脚本可能无法提取到目标选择器 (`.theme-doc-markdown`) 中的内容，因为这些内容是在浏览器加载并执行 JS 后才生成的。

在我们的测试中，脚本成功抓取了 180 个链接中的 167 个，失败的 13 个链接正是需要 JS 渲染的页面。

**未来改进方向**: 如果需要完整抓取所有页面，可以将抓取引擎替换为 **Playwright** 或 **Selenium**，它们可以模拟真实浏览器环境来执行 JavaScript。