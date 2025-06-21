# Website Content Scraper (Python Version)

This is a Python-based command-line tool with a GUI, designed to extract all links from a website's `sitemap.xml`, scrape the main content from each page, and save the content of each page as a separate Markdown file with metadata.

## Features

- **Sitemap Parsing**: Automatically reads and parses the `sitemap.xml` file located in the project's root directory to get all URLs to be scraped.
- **Concurrent Scraping**: Uses multi-threading to perform scraping tasks concurrently, improving efficiency.
- **User-Agent Rotation**: Includes a built-in User-Agent pool and randomly selects one for each request to simulate different browsers and reduce the risk of being blocked.
- **Proxy Disabling**: Automatically disables system-level HTTP/HTTPS proxies to ensure direct network requests.
- **Structured Output**:
    - Each run creates a separate, timestamped folder within the `output` directory (e.g., `output/output_20250622_032700`).
    - Each successfully scraped page is saved as a `.md` file.
    - The output files maintain the original URL's path structure.
- **Metadata Addition**: Automatically adds YAML Front Matter metadata at the beginning of each generated Markdown file, including the original URL and the time of scraping.
- **Graphical User Interface (GUI)**: Built with Tkinter, providing a user-friendly way to manage the scraper.
- **Cross-Platform Packaging**: Prepared for packaging into a single executable file using PyInstaller.

---

## Installation and Setup

### 1. Prerequisites

- Ensure you have **Python 3.6** or higher installed on your system.

### 2. Installing Dependencies

It is recommended to operate within a Python virtual environment to avoid conflicts with system libraries.

a. **Create and Activate a Virtual Environment** (Optional, but recommended)

```bash
# Create a virtual environment (e.g., named venv)
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate
# On macOS / Linux
source venv/bin/activate
```

b. **Install Required Libraries**

The project dependencies are listed in `requirements.txt`. Run the following command to install them:

```bash
pip install -r requirements.txt
```

### 3. Prepare `sitemap.xml`

Place the `sitemap.xml` file of your target website in the root directory of the project.

---

## How to Use

### Running the Application

After completing the installation and setup, simply run the following command in the project's root directory to launch the GUI:

```bash
python main_gui.py
```

### GUI Guide

1.  **Select Sitemap**: Click the "Select Sitemap.xml File" button to locate and choose the target `sitemap.xml` file.
2.  **Select Output Directory**: Click the "Select Output Directory" button to choose a folder where the scraped results will be saved.
3.  **Configure Parameters**:
    - **Concurrency**: Adjust the number of concurrent threads based on your network conditions (5-20 is recommended).
    - **CSS Selectors**: Enter one or more CSS selectors in the text box, one per line. The program will attempt to extract content matching all these selectors from the page.
    - **Save Config**: After modifying the configuration, you can click "Save Config" to set it as the default for future runs.
4.  **Start Scraping**: Click the "Start Scraping" button to begin the task.
5.  **View Logs**: The log area at the bottom will display real-time progress and results.

---

## Packaging (Optional)

You can package the application into a single executable file (`.exe` on Windows) using PyInstaller.

A pre-configured `.spec` file is provided. To build the executable, run:
```bash
pyinstaller crawler.spec
```
The executable file, named `文档内容抓取器.exe` (or `ContentScraper.exe`), will be available in the `dist` directory. You can distribute this file along with the `config.json` to run on other machines without a Python environment.

---

## Limitations

The current version of the scraper uses the `requests` and `BeautifulSoup` libraries, which means it **can only scrape content from static HTML pages**.

For modern websites that heavily use JavaScript to render content dynamically on the client-side (e.g., sites built with React, Vue, or Docusaurus), this script may fail to extract content from the target selectors, as this content is generated after the browser loads and executes JS.

**Future Improvement**: To handle all pages, the scraping engine could be upgraded to use **Playwright** or **Selenium**, which can simulate a real browser environment to execute JavaScript.