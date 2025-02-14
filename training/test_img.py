import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import glob
import logging

# 配置日志
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# 设置TensorFlow日志级别
tf.get_logger().setLevel(logging.ERROR)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


def load_model(model_path):
    """加载模型并进行基本检查"""
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"""
            错误：模型文件不存在！
            
            未能在以下路径找到模型文件：{model_path}
            
            请先执行以下操作之一：
            1. 运行训练脚本生成模型
               python3 training/train.py
            
            2. 或从项目仓库下载预训练模型：
               https://github.com/ctkqiang/WangZhongZhi.git
        """
        )

    try:
        model = tf.keras.models.load_model(model_path)
        logger.info("模型加载成功")
        return model
    except Exception as e:
        raise Exception(f"模型加载失败：{str(e)}")


def process_image(img_path):
    """处理图片文件"""
    try:
        img = image.load_img(img_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array / 255.0
    except Exception as e:
        raise Exception(f"图片处理失败：{str(e)}")


def main():
    # 获取绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    # 设置模型和测试图片路径
    model_path = os.path.join(project_root, "assets", "dog_breed_classifier.h5")
    test_image_dir = os.path.join(project_root, "training", "images", "test")

    # 加载模型
    model = load_model(model_path)

    # 验证测试目录是否存在
    if not os.path.exists(test_image_dir):
        raise FileNotFoundError(f"测试图片目录不存在：{test_image_dir}")

    # 获取所有犬种目录
    breed_dirs = glob.glob(os.path.join(test_image_dir, "*"))
    if not breed_dirs:
        logger.warning(f"未在 {test_image_dir} 找到任何犬种目录")
        return

    # 处理每个犬种目录
    for breed_dir in breed_dirs:
        breed_name = os.path.basename(breed_dir)
        image_paths = glob.glob(os.path.join(breed_dir, "*"))

        if not image_paths:
            logger.warning(f"在 {breed_name} 目录中未找到图片")
            continue

        logger.info(f"正在处理 {breed_name} 的图片...")

        for img_path in image_paths:
            try:
                # 处理图片
                img_array = process_image(img_path)

                # 预测
                predictions = model.predict(img_array, verbose=0)
                predicted_class = np.argmax(predictions)

                # 输出结果
                logger.info(f"图片：{os.path.basename(img_path)}")
                logger.info(f"预测类别：{predicted_class}")
                logger.info("-" * 50)

            except Exception as e:
                logger.error(f"处理图片 {img_path} 时出错：{str(e)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"程序执行出错：{str(e)}")
