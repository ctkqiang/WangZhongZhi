import tensorflow as tf
import os
import logging

# 配置日志
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def convert_model():
    # 获取绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    model_path = os.path.join(project_root, "assets", "dog_breed_classifier.h5")
    tflite_path = os.path.join(project_root, "assets", "dog_breed_classifier.tflite")

    # 确保assets目录存在
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    try:
        # 加载模型
        logger.info("正在加载模型...")
        model = tf.keras.models.load_model(model_path)
        logger.info("模型加载成功")

        # 转换模型
        logger.info("正在转换模型为TFLite格式...")
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()
        logger.info("模型转换成功")

        # 保存模型
        logger.info(f"正在保存TFLite模型到 {tflite_path}")
        with open(tflite_path, "wb") as f:
            f.write(tflite_model)
        logger.info("TFLite模型保存成功")

    except FileNotFoundError:
        logger.error(
            f"""
        错误：未找到模型文件！
        
        请先执行以下操作之一：
        1. 运行训练脚本生成模型
           python3 training/train.py
        
        2. 或从项目仓库下载预训练模型：
           https://github.com/ctkqiang/WangZhongZhi.git
        """
        )
        raise
    except Exception as e:
        logger.error(f"转换过程中出错：{str(e)}")
        raise


if __name__ == "__main__":
    try:
        convert_model()
    except Exception as e:
        logger.error("模型转换失败")
        exit(1)
