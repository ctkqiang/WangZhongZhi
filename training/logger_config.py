import os
import logging
import sys
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:
    """
    配置日志记录器

    参数:
        name: 日志记录器名称
    返回:
        配置好的日志记录器实例
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 配置日志格式
    formatter = logging.Formatter(
        "[鹰眼AI]:  %(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 配置控制台输出处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 配置文件输出处理器
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = "log"

    os.makedirs(log_dir, exist_ok=True)

    file_handler = logging.FileHandler(f"{log_dir}/app_{timestamp}.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
