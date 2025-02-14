import time
import tensorflow as tf
from logger_config import setup_logger
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

logger = setup_logger(__name__)


# ImageDataGenerator 是一个用于生成批量图像数据的工具类。
# 对于训练数据，我们进行一些数据增强操作，以增加数据的多样性，提高模型的泛化能力。
# rescale=1./255 表示将图像的像素值归一化到 0 到 1 之间，这有助于模型的训练。
# shear_range=0.2 表示在图像上进行剪切变换的强度范围为 0.2。
# zoom_range=0.2 表示在图像上进行缩放变换的强度范围为 0.2。
# horizontal_flip=True 表示随机对图像进行水平翻转。
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
)

# 对于测试数据，我们只需要进行像素值归一化操作，不需要进行数据增强，因为我们要评估模型在真实数据上的性能。
test_datagen = ImageDataGenerator(rescale=1.0 / 255)

# flow_from_directory 方法用于从指定的目录中读取图像数据，并将其转换为适合模型输入的格式。
# 'data/train' 是训练数据所在的目录。
# target_size=(150, 150) 表示将所有图像的大小调整为 150x150 像素。
# batch_size=32 表示每次从数据集中取出 32 张图像作为一个批次进行训练。
# class_mode='categorical' 表示使用分类模式，即每个图像对应一个类别标签，标签采用 one - hot 编码。
train_generator = train_datagen.flow_from_directory(
    "images/train", target_size=(150, 150), batch_size=32, class_mode="categorical"
)

# 同样的方法用于生成验证数据生成器。
validation_generator = test_datagen.flow_from_directory(
    "images/validation", target_size=(150, 150), batch_size=32, class_mode="categorical"
)

# Sequential 是 Keras 中用于构建顺序模型的类，顺序模型是一种简单的线性堆叠模型，即一层接着一层地堆叠网络层。
model = Sequential(
    [
        # Conv2D 是二维卷积层，用于提取图像的特征。
        # 32 表示卷积核的数量，即该层会学习 32 种不同的特征。
        # (3, 3) 表示卷积核的大小为 3x3。
        # activation='relu' 表示使用 ReLU 激活函数，ReLU 函数可以引入非线性因素，增强模型的表达能力。
        # input_shape=(150, 150, 3) 表示输入图像的大小为 150x150 像素，且有 3 个颜色通道（RGB）。
        Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)),
        # MaxPooling2D 是二维最大池化层，用于对卷积层的输出进行下采样，减少数据的维度，同时保留重要的特征信息。(2, 2) 表示池化窗口的大小为 2x2。
        MaxPooling2D((2, 2)),
        # 再次添加一个卷积层，增加模型的复杂度，以学习更高级的特征。
        Conv2D(64, (3, 3), activation="relu"),
        # 再次进行最大池化操作。
        MaxPooling2D((2, 2)),
        # 又添加一个卷积层，进一步提取特征。
        Conv2D(128, (3, 3), activation="relu"),
        # 再次进行最大池化操作。
        MaxPooling2D((2, 2)),
        # Flatten 层用于将多维的特征图展平为一维向量，以便输入到全连接层中。
        Flatten(),
        # Dense 是全连接层，也称为密集层。
        # 128 表示该层有 128 个神经元。
        # activation='relu' 同样使用 ReLU 激活函数。
        Dense(128, activation="relu"),
        # 最后一层的神经元数量为 train_generator.num_classes，即类别数量。
        # activation='softmax' 表示使用 softmax 激活函数，用于输出每个类别的概率。
        Dense(train_generator.num_classes, activation="softmax"),
    ]
)

# optimizer='adam' 表示使用 Adam 优化器，Adam 是一种自适应学习率的优化算法，在许多情况下都能取得较好的效果。
# loss='categorical_crossentropy' 表示使用分类交叉熵损失函数，适用于多分类问题。
# metrics=['accuracy'] 表示使用准确率作为评估指标，用于衡量模型的性能。
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# fit 方法用于训练模型。
# train_generator 是训练数据生成器，用于提供训练数据。
# steps_per_epoch=train_generator.samples // train_generator.batch_size 表示每个 epoch 中要进行的步数，即训练数据的样本数除以批次大小。
# validation_data=validation_generator 表示使用验证数据生成器提供验证数据。
# validation_steps=validation_generator.samples // validation_generator.batch_size 表示在验证过程中要进行的步数。
# epochs=10 表示训练 10 个 epoch，即对整个训练数据集进行 10 次迭代训练。
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=10,
)

# 同样使用 flow_from_directory 方法生成测试数据生成器。
test_generator = test_datagen.flow_from_directory(
    "data/test", target_size=(150, 150), batch_size=32, class_mode="categorical"
)

# evaluate 方法用于评估模型在测试数据上的性能。
# test_loss 是测试集上的损失值，test_acc 是测试集上的准确率。
test_loss, test_acc = model.evaluate(test_generator)
logger.info(f"测试准确率: {test_acc}")

# save 方法用于将训练好的模型保存为 HDF5 格式的文件，方便后续使用。
model.save("dog_breed_classifier.h5")

time.sleep(0x3)

# 设置 Streamlit 应用的标题。
st.title("犬种分类器")

# 加载之前保存的模型。
model = tf.keras.models.load_model("dog_breed_classifier.h5")

# 获取所有类别的名称。
# train_generator.class_indices 是一个字典，键为类别名称，值为对应的索引。
# 通过 list() 函数将字典的键转换为列表，方便后续使用。
class_names = list(train_generator.class_indices.keys())

# 创建一个文件上传器，允许用户上传 JPG、JPEG 或 PNG 格式的图像文件。
uploaded_file = st.file_uploader("选择一张图片...", type=["jpg", "jpeg", "png"])

# 如果用户上传了文件，则进行以下操作。
if uploaded_file is not None:
    # 使用 load_img 函数加载上传的图像，并将其调整为 150x150 像素的大小。
    img = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(150, 150))
    # 将图像转换为 NumPy 数组。
    img = tf.keras.preprocessing.image.img_to_array(img)
    # 在数组的第一个维度上增加一个维度，以满足模型输入的要求（模型输入通常要求是一个批次的数据，即使只有一张图像）。
    img = np.expand_dims(img, axis=0)
    # 对图像的像素值进行归一化操作。
    img = img / 255.0

    # 使用模型对图像进行预测，得到每个类别的概率。
    predictions = model.predict(img)
    # 使用 argmax 函数找到概率最大的类别对应的索引。
    predicted_class = np.argmax(predictions)
    # 根据索引从 class_names 列表中获取对应的犬种名称。
    breed = class_names[predicted_class]

    # 在 Streamlit 应用中显示上传的图像。
    st.image(uploaded_file, caption="上传的图像.", use_column_width=True)
    # 在 Streamlit 应用中显示预测的犬种名称。
    st.write(f"预测的犬种: {breed}")
