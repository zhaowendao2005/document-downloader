import axios from 'axios';
import * as cheerio from 'cheerio';
import pLimit from 'p-limit';
import config from './config.js';
import { logger } from './logger.js';

const limit = pLimit(config.concurrency || 5);

/**
 * 爬取单个 URL 并提取内容。
 * @param {string} url 要爬取的 URL。
 * @returns {Promise<object|null>} 包含 URL 和提取内容的對象，如果失敗則返回 null。
 */
async function fetchAndParse(url) {
  try {
    logger.debug(`正在请求: ${url}`);
    const { data: html } = await axios.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
      }
    });
    logger.debug(`成功获取: ${url}`);
    
    const $ = cheerio.load(html);
    const extractedContent = {};

    config.selectors.forEach(selector => {
      const content = $(selector).text().trim();
      if (content) {
        extractedContent[selector] = content;
        logger.debug(`在 ${url} 的选择器 "${selector}" 中提取了内容。`);
      } else {
        logger.warn(`在 ${url} 中未找到选择器 "${selector}" 或其内容为空。`);
      }
    });

    return {
      url,
      content: extractedContent
    };
  } catch (error) {
    logger.error(`爬取或解析 ${url} 时出错: ${error.message}`);
    return null;
  }
}

/**
 * 并行爬取 URL 列表。
 * @param {string[]} urls 要爬取的 URL 列表。
 * @returns {Promise<object[]>} 包含爬取结果的数组。
 */
export async function crawl(urls) {
  logger.info(`开始并行爬取 ${urls.length} 个 URL，并发数为 ${config.concurrency}...`);
  const tasks = urls.map(url => limit(() => fetchAndParse(url)));
  const results = await Promise.all(tasks);
  
  // 过滤掉失败的任务
  return results.filter(result => result !== null);
}