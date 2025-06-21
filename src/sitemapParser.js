import fs from 'fs/promises';
import xml2js from 'xml2js';
import config from './config.js';
import { logger } from './logger.js';

const parser = new xml2js.Parser();

/**
 * 从 sitemap.xml 文件中解析并提取所有 URL。
 * @returns {Promise<string[]>} 包含所有 URL 的字符串数组。
 */
export async function getUrls() {
  try {
    logger.info(`正在从路径 ${config.sitemapPath} 读取 sitemap 文件...`);
    const xmlContent = await fs.readFile(config.sitemapPath, 'utf-8');
    const result = await parser.parseStringPromise(xmlContent);

    if (!result.urlset || !result.urlset.url) {
      logger.warn('sitemap.xml 文件格式不正确或为空，未找到 <urlset> 或 <url> 标签。');
      return [];
    }

    const urls = result.urlset.url.map(urlEntry => {
      if (urlEntry.loc && urlEntry.loc[0]) {
        return urlEntry.loc[0];
      }
      logger.warn('在 sitemap 中发现一个缺少 <loc> 标签的 <url> 条目。');
      return null;
    }).filter(url => url !== null); // 过滤掉无效的条目

    logger.debug(`成功解析了 ${urls.length} 个 URL。`);
    return urls;
  } catch (error) {
    logger.error(`解析 sitemap.xml 文件时出错: ${error.message}`);
    throw new Error('解析 sitemap.xml 失败。');
  }
}