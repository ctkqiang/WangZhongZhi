from icrawler.builtin import GoogleImageCrawler
import os
import sys
from typing import Optional
from logger_config import setup_logger

logger = setup_logger(__name__)


def validate_input(text: str) -> bool:
    """
    验证用户输入是否有效
    参数:
        text: 用户输入的文本
    返回:
        布尔值，表示输入是否有效
    """
    return bool(text and not text.isspace())


def download_images(
    keywords: str,
    max_num: int = 5,
    save_dir: str = "images",
    is_train: bool = False,
    is_validation: bool = False,
    is_test: bool = False,
) -> Optional[str]:
    """
    下载指定关键词的图片
    参数:
        keywords: 搜索关键词（狗狗品种名称）
        max_num: 要下载的图片数量
        save_dir: 保存目录的基础路径
        is_train: 是否为训练集
        is_validation: 是否为验证集
        is_test: 是否为测试集
    返回:
        保存图片的目录路径，如果发生错误则返回None
    """
    try:
        # 根据数据集类型设置保存路径
        if is_train:
            save_dir = "training/images/train"
        elif is_validation:
            save_dir = "training/images/validation"
        elif is_test:
            save_dir = "training/images/test"
        else:
            save_dir = "training/images"

        # 创建保存目录
        os.makedirs(save_dir, exist_ok=True)
        keyword_dir = os.path.join(save_dir, keywords)
        os.makedirs(keyword_dir, exist_ok=True)

        class CustomNameParser:
            """
            自定义文件名解析器
            用于生成格式化的图片文件名
            """

            def __init__(self, name):
                self.count = 1
                self.name = name

            def __call__(self, task, response):
                ext = os.path.splitext(task.file_name)[1] or ".jpg"
                filename = f"{self.name}_{self.count}{ext}"
                logger.info(f"正在下载: {filename}")
                self.count += 1
                return filename

        # 配置图片爬虫
        crawler = GoogleImageCrawler(
            storage={"root_dir": keyword_dir},
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4,  # 使用4个线程同时下载，提高效率
        )

        crawler.parser.filename_parser = CustomNameParser(name=keywords)

        # 构建搜索词，添加"狗"和"dog breed"以提高搜索准确性
        search_term = f"{keywords} 狗 dog breed"
        logger.info(f"开始下载 {max_num} 张 '{search_term}' 的图片")
        crawler.crawl(keyword=search_term, max_num=max_num)

        return keyword_dir

    except Exception as e:
        logger.error(f"下载过程中发生错误: {str(e)}")
        return None


def read_breeds(file_path: str) -> list:
    """
    从文件中读取狗狗品种列表
    参数:
        file_path: 品种列表文件的路径
    返回:
        品种名称列表，如果发生错误则返回空列表
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            breeds = [line.strip() for line in file if line.strip()]
        return breeds
    except Exception as e:
        logger.error(f"读取品种文件时发生错误: {str(e)}")
        return []


def main(listpath):
    """
    主函数，协调整个下载过程
    参数:
        listpath: 品种列表文件的名称
    """
    logger.info("开始下载狗狗图片...")
    logger.info(f"使用品种列表文件: {listpath}")

    # 构建品种文件的完整路径
    breed_file = os.path.join(os.path.dirname(__file__), "data", listpath)

    # 读取品种列表
    breeds = read_breeds(breed_file)

    if not breeds:
        logger.error("品种文件为空或无法读取")
        sys.exit(1)

    try:
        # 获取用户输入的下载数量
        max_num = int(input("每个品种需要下载多少张图片？(默认: 5): ") or "5")
        if max_num <= 0:
            raise ValueError
    except ValueError:
        logger.error("输入的图片数量无效")
        sys.exit(1)

    # 为每个品种下载图片
    for breed in breeds:
        logger.info(f"正在处理品种: {breed}")

        # 下载训练集图片
        save_path_train = download_images(
            keywords=breed,
            max_num=max_num,
            is_train=True,
        )

        # 下载测试集图片
        save_path_test = download_images(
            keywords=breed,
            max_num=max_num // 2,  # 测试集使用一半数量的图片
            is_test=True,
        )

        # 下载验证集图片
        save_path_validation = download_images(
            keywords=breed,
            max_num=max_num // 2,  # 验证集使用一半数量的图片
            is_validation=True,
        )

        # 输出下载完成信息
        if save_path_train:
            logger.info(f"训练集下载完成，保存路径: {save_path_train}")
        if save_path_test:
            logger.info(f"测试集下载完成，保存路径: {save_path_test}")
        if save_path_validation:
            logger.info(f"验证集下载完成，保存路径: {save_path_validation}")


if __name__ == "__main__":
    # 默认使用英文品种文件，也可以改为使用中文品种文件
    main(listpath="breed_zh.txt")
