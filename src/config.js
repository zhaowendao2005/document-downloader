import fs from 'fs';
import path from 'path';

const configPath = path.join(process.cwd(), 'config.json');

let config;

try {
  const configFile = fs.readFileSync(configPath, 'utf-8');
  config = JSON.parse(configFile);
} catch (error) {
  console.error('无法读取或解析 config.json 文件:', error);
  // 如果配置文件关键，则退出进程
  process.exit(1);
}

export default config;