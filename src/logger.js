import winston from 'winston';
import config from './config.js';

const { createLogger, format, transports } = winston;
const { combine, timestamp, printf, colorize } = format;

// 自定义日志格式
const logFormat = printf(({ level, message, timestamp }) => {
  return `${timestamp} ${level}: ${message}`;
});

const logger = createLogger({
  level: config.logLevel || 'info',
  format: combine(
    timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    logFormat
  ),
  transports: [
    // 将日志输出到控制台
    new transports.Console({
      format: combine(
        colorize(),
        timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
        logFormat
      )
    }),
    // 将日志输出到文件
    new transports.File({ filename: config.logFile || 'crawler.log' })
  ]
});

export { logger };