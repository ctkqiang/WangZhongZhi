from icrawler.builtin import GoogleImageCrawler
import os
import sys
from typing import Optional
from logger_config import setup_logger

logger = setup_logger(__name__)


def validate_input(text: str) -> bool:
    """验证输入是否有效"""
    return bool(text and not text.isspace())


def download_images(
    keywords: str,
    max_num: int = 5,
    save_dir: str = "images",
    is_train: bool = False,
    is_validation: bool = False,
    is_test: bool = False,
) -> Optional[str]:
    try:
        if is_train:
            save_dir = "images/train"
        elif is_validation:
            save_dir = "images/validation"
        elif is_test:
            save_dir = "images/test"
        else:
            save_dir = "images"

        os.makedirs(save_dir, exist_ok=True)
        keyword_dir = os.path.join(save_dir, keywords)
        os.makedirs(keyword_dir, exist_ok=True)

        class CustomNameParser:
            def __init__(self, name):
                self.count = 1
                self.name = name

            def __call__(self, task, response):
                ext = os.path.splitext(task.file_name)[1] or ".jpg"
                filename = f"{self.name}_{self.count}{ext}"
                logger.info(f"Downloading: {filename}")
                self.count += 1
                return filename

        crawler = GoogleImageCrawler(
            storage={"root_dir": keyword_dir},
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4,
        )

        crawler.parser.filename_parser = CustomNameParser(name=keywords)

        search_term = f"{keywords} 狗 dog breed"
        logger.info(f"Starting download of {max_num} images for '{search_term}'")
        crawler.crawl(keyword=search_term, max_num=max_num)

        return keyword_dir

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return None


def read_breeds(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            breeds = [line.strip() for line in file if line.strip()]
        return breeds
    except Exception as e:
        logger.error(f"Error reading breed file: {str(e)}")
        return []


def main(listpath):
    logger.info("开始下载狗狗图片...")
    logger.info(listpath)

    breed_file = os.path.join(os.path.dirname(__file__), "data", listpath)

    breeds = read_breeds(breed_file)

    if not breeds:
        logger.error("No breeds found in the file")
        sys.exit(1)

    try:
        max_num = int(input("每个品种需要下载多少张图片？(默认: 5): ") or "5")
        if max_num <= 0:
            raise ValueError
    except ValueError:
        logger.error("Invalid number of images specified")
        sys.exit(1)

    for breed in breeds:
        logger.info(f"Processing breed: {breed}")

        save_path_train = download_images(
            keywords=breed,
            max_num=max_num,
            is_train=True,
        )

        save_path_test = download_images(
            keywords=breed,
            max_num=max_num // 2,
            is_test=True,
        )

        save_path_validation = download_images(
            keywords=breed,
            max_num=max_num // 2,
            is_validation=True,
        )

        if save_path_train:
            logger.info(f"训练集下载完成，保存路径: {save_path_train}")
        if save_path_test:
            logger.info(f"测试集下载完成，保存路径: {save_path_test}")
        if save_path_validation:
            logger.info(f"验证集下载完成，保存路径: {save_path_validation}")


if __name__ == "__main__":
    # TODO: 可以将文件路径改为 "breed_en.txt" 以下载英文品种的狗狗图片
    main(listpath="breed_en.txt")
