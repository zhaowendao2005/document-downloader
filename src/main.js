import { getUrls } from './sitemapParser.js';
import { crawl } from './crawler.js';
import { logger } from './logger.js';
import config from './config.js';

async function main() {
  logger.info('开始执行爬虫任务...');
  try {
    const urls = await getUrls();
    logger.info(`从 sitemap 中成功提取 ${urls.length} 个 URL。`);

    const results = await crawl(urls);
    logger.info(`成功爬取 ${results.length} 个页面。`);
    // 在这里可以添加处理结果的逻辑，例如保存到文件
    // console.log(results);

  } catch (error) {
    logger.error('任务执行过程中发生严重错误:', error);
  } finally {
    logger.info('爬虫任务执行完毕。');
  }
}

main();