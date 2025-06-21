import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
import sys # 新增
import threading
import queue
import logging
from datetime import datetime

# 导入我们重构后的爬虫核心模块
import py_crawler

# --- 新增：打包路径辅助函数 ---
def resource_path(relative_path):
    """ 获取资源的绝对路径，无论是作为脚本运行还是作为打包程序运行 """
    try:
        # PyInstaller 创建一个临时文件夹并将路径存储在 _MEIPASS 中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# --- GUI 应用类 ---
class CrawlerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("网站内容抓取器")
        self.master.geometry("800x650")

        self.sitemap_path = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.log_queue = queue.Queue()
        self.is_crawling = False
        self.config_path = resource_path('config.json') # 使用辅助函数

        self.create_widgets()
        self.load_initial_config()
        self.master.after(100, self.process_log_queue)

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        file_frame = ttk.LabelFrame(main_frame, text="输入与输出", padding="10")
        file_frame.pack(fill=tk.X, expand=True)
        
        ttk.Button(file_frame, text="选择 Sitemap.xml 文件", command=self.select_sitemap_file).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(file_frame, textvariable=self.sitemap_path, wraplength=600).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Button(file_frame, text="选择输出目录", command=self.select_output_dir).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(file_frame, textvariable=self.output_dir, wraplength=600).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        config_frame = ttk.LabelFrame(main_frame, text="抓取配置", padding="10")
        config_frame.pack(fill=tk.X, expand=True, pady=10)

        ttk.Label(config_frame, text="并发数:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.max_workers_entry = ttk.Entry(config_frame, width=10)
        self.max_workers_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(config_frame, text="CSS 选择器 (每行一个):").grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.selectors_text = tk.Text(config_frame, height=5, width=80)
        self.selectors_text.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # 新增：保存配置按钮
        ttk.Button(config_frame, text="保存配置", command=self.save_config).grid(row=2, column=1, padx=5, pady=5, sticky="e")


        control_frame = ttk.Frame(main_frame, padding="5")
        control_frame.pack(fill=tk.X, expand=True)

        button_inner_frame = ttk.Frame(control_frame)
        button_inner_frame.pack()
        
        self.start_button = ttk.Button(button_inner_frame, text="开始抓取", command=self.start_crawling)
        self.start_button.pack(side=tk.LEFT, pady=10, padx=10)
        
        self.help_button = ttk.Button(button_inner_frame, text="帮助", command=self.show_help)
        self.help_button.pack(side=tk.LEFT, pady=10, padx=10)

        log_frame = ttk.LabelFrame(main_frame, text="日志", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        self.log_text = scrolledtext.ScrolledText(log_frame, state='disabled', height=15, width=100)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_text.tag_config("INFO", foreground="black")
        self.log_text.tag_config("WARNING", foreground="orange")
        self.log_text.tag_config("ERROR", foreground="red")
        self.log_text.tag_config("PROGRESS", foreground="blue")


    def select_sitemap_file(self):
        path = filedialog.askopenfilename(title="选择 Sitemap.xml", filetypes=[("XML files", "*.xml"), ("All files", "*.*")])
        if path:
            self.sitemap_path.set(path)

    def select_output_dir(self):
        path = filedialog.askdirectory(title="选择保存结果的目录")
        if path:
            self.output_dir.set(path)

    def load_initial_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            self.max_workers_entry.delete(0, tk.END)
            self.max_workers_entry.insert(0, str(config.get('maxWorkers', 10)))
            self.selectors_text.delete('1.0', tk.END)
            self.selectors_text.insert(tk.END, "\n".join(config.get('targetSelectors', [])))
        except FileNotFoundError:
            self.log_queue.put(('WARNING', f"未找到配置文件: {self.config_path}。将使用默认配置。"))
            self.max_workers_entry.insert(0, "10")
        except Exception as e:
            messagebox.showerror("错误", f"加载 {self.config_path} 失败: {e}")

    def get_config_from_gui(self):
        try:
            max_workers = int(self.max_workers_entry.get())
        except ValueError:
            messagebox.showerror("错误", "并发数必须是一个整数。")
            return None
        
        selectors_str = self.selectors_text.get("1.0", tk.END).strip()
        if not selectors_str:
            messagebox.showerror("错误", "请至少提供一个 CSS 选择器。")
            return None
        
        selectors = [line for line in selectors_str.split('\n') if line.strip()]
        return {"maxWorkers": max_workers, "targetSelectors": selectors}
        
    def save_config(self):
        """保存当前GUI中的配置到 config.json"""
        config_data = self.get_config_from_gui()
        if not config_data:
            return
            
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2)
            messagebox.showinfo("成功", f"配置已成功保存到\n{self.config_path}")
        except Exception as e:
            messagebox.showerror("错误", f"保存配置失败: {e}")


    def start_crawling(self):
        if self.is_crawling:
            messagebox.showinfo("提示", "抓取任务正在进行中...")
            return
            
        sitemap = self.sitemap_path.get()
        output = self.output_dir.get()

        if not sitemap or not output:
            messagebox.showerror("错误", "请先选择 Sitemap 文件和输出目录。")
            return

        config = self.get_config_from_gui()
        if not config:
            return
            
        self.is_crawling = True
        self.start_button.config(state='disabled', text="抓取中...")
        self.log_text.config(state='normal')
        self.log_text.delete('1.0', tk.END)
        self.log_text.config(state='disabled')
        
        crawl_thread = threading.Thread(target=self.run_crawler_thread, args=(sitemap, output, config), daemon=True)
        crawl_thread.start()

    def run_crawler_thread(self, sitemap_path, output_dir_base, config):
        root_logger = logging.getLogger()
        original_level = root_logger.level
        root_logger.setLevel(logging.INFO)
        queue_handler = QueueHandler(self.log_queue)
        root_logger.addHandler(queue_handler)

        def progress_callback(current, total, success, fails):
            msg = f"进度: {current}/{total} (成功: {success}, 失败: {fails})"
            self.log_queue.put(('PROGRESS', msg))

        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            final_output_dir = os.path.join(output_dir_base, f"output_{timestamp}")
            os.makedirs(final_output_dir, exist_ok=True)
            logging.info(f"输出目录已创建: {final_output_dir}")
            py_crawler.run_crawling(sitemap_path, final_output_dir, config, progress_callback)
        except Exception as e:
            logging.error(f"发生严重错误: {e}", exc_info=True)
        finally:
            self.log_queue.put(None)
            root_logger.removeHandler(queue_handler)
            root_logger.setLevel(original_level)

    def process_log_queue(self):
        try:
            while True:
                record = self.log_queue.get_nowait()
                if record is None:
                    self.is_crawling = False
                    self.start_button.config(state='normal', text="开始抓取")
                    messagebox.showinfo("完成", "抓取任务已完成！")
                    return
                
                level, msg = record
                self.log_text.config(state='normal')
                if level == 'PROGRESS':
                    # 查找并删除上一条进度信息
                    last_line_pos = self.log_text.search("进度:", "end-2l", backwards=True, regexp=False)
                    if last_line_pos:
                        self.log_text.delete(last_line_pos, f"{last_line_pos} lineend")
                    self.log_text.insert(tk.END, f"{msg}\n", (level,))
                else:
                    self.log_text.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n", (level,))
                
                self.log_text.see(tk.END)
                self.log_text.config(state='disabled')
        except queue.Empty:
            pass
        finally:
            self.master.after(100, self.process_log_queue)

    def show_help(self):
        help_win = tk.Toplevel(self.master)
        help_win.title("帮助文档")
        help_win.geometry("600x450")
        help_win.transient(self.master)

        help_text_widget = scrolledtext.ScrolledText(help_win, wrap=tk.WORD, padx=10, pady=10)
        help_text_widget.pack(expand=True, fill=tk.BOTH)

        help_content = """
        欢迎使用网站内容抓取器！

        --- 操作教程 ---
        1. 选择 Sitemap: 点击“选择 Sitemap.xml 文件”按钮。
        2. 选择输出目录: 点击“选择输出目录”按钮。
        3. 配置参数:
           - 在“抓取配置”区域修改并发数和CSS选择器。
           - 修改配置后，可点击“保存配置”将其存为默认值。
        4. 开始抓取: 点击“开始抓取”按钮启动任务。
        5. 查看日志: 下方的日志区域会实时显示进度和结果。

        --- Sitemap.xml 格式规范 ---
        程序需要一个标准的 sitemap.xml 文件来获取网址列表。
        核心要求如下：
        - 必须是有效的 XML 文件。
        - 根节点为 <urlset>。
        - 每个网址信息包裹在 <url> 标签内。
        - 网址本身必须位于 <loc> 标签内。

        一个最简单的示例如下:
        ```xml
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url>
            <loc>https://example.com/page1</loc>
          </url>
          <url>
            <loc>https://example.com/page2</loc>
          </url>
        </urlset>
        ```
        """
        
        help_text_widget.insert(tk.INSERT, help_content)
        help_text_widget.config(state='disabled')


class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put((record.levelname, self.format(record)))

if __name__ == '__main__':
    root = tk.Tk()
    app = CrawlerApp(root)
    root.mainloop()