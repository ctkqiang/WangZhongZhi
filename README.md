# 汪种知 🐕

> 您的智能犬种识别助手，让每一次相遇都成为了解的开始

## 项目简介

「汪种知」是一款革新性的犬种识别应用，融合了最新的人工智能技术与直观的用户界面设计。基于 Flutter 框架开发，集成深度学习模型，支持 60 种犬种的实时识别，为爱犬人士和专业人员提供便捷、准确的犬种鉴定服务。

### 🌟 核心特色

- **智能识别**：采用先进的深度学习算法，支持 60 种犬种的精确识别
- **实时分析**：秒级响应，快速输出识别结果
- **专业解析**：提供每个犬种的详细特征、习性和饲养建议
- **便捷操作**：支持实时拍照和相册导入，操作简单直观
- **优雅界面**：采用 Material Design 设计语言，提供流畅优雅的用户体验

### 🎯 应用场景

- **个人用户**：帮助识别陌生犬种，了解不同品种特点
- **宠物医院**：辅助医生快速识别犬种，提供针对性诊疗建议
- **培训机构**：用于犬种知识教学和实践培训
- **宠物商店**：协助客户了解不同犬种特点，做出更好的选择
- **动物救助**：帮助救助站快速识别流浪犬的品种，便于救助和安置

### 🛠 技术亮点

- **深度学习模型**：
  - 训练数据集超过 1000 张图片
  - 模型准确率为 42.71%
  - 支持实时图像处理和分析
- **Flutter 跨平台开发**：

  - 统一的用户体验
  - 高效的性能表现
  - 流畅的动画效果

- **本地化处理**：
  - 离线识别，保护隐私
  - 快速响应，无需网络
  - 实时分析，即时反馈

### 💡 创新价值

1. **科普教育**

   - 提供专业的犬种知识库
   - 帮助用户了解不同犬种特点
   - 促进科学养犬理念传播

2. **行业应用**

   - 为专业人士提供辅助工具
   - 提高工作效率和准确度
   - 促进行业数字化转型

3. **社会价值**
   - 推广科学养犬理念
   - 提高养犬认知水平
   - 促进人犬和谐相处

### 🔮 未来展望

1. **技术升级**

   - 持续优化识别算法
   - 扩充犬种数据库
   - 提升识别准确率

2. **功能拓展**

   - 添加犬种行为分析
   - 整合健康管理功能
   - 开发社区互动模块

3. **场景延伸**
   - 拓展专业版功能
   - 对接行业解决方案
   - 探索商业化可能

基于 Flutter 框架开发的犬种识别应用，集成深度学习模型，支持 60 种犬种的实时识别。本项目作为人工智能与移动应用开发的实践项目，旨在提供一个完整的端到端解决方案。

## 培训说明

### 培训目标

- 掌握 Flutter 框架的基本概念和开发流程
- 学习 Dart 编程语言的核心特性
- 理解 Flutter 界面构建和状态管理
- 熟悉常用 Widget 的使用方法

### 培训内容

1. Flutter 基础

   - Flutter 环境搭建
   - Dart 语言基础
   - Widget 介绍与使用
   - 布局与导航

2. UI 开发

   - Material Design 组件
   - Cupertino 组件
   - 自定义 Widget
   - 响应式布局

3. 状态管理

   - setState
   - GetX 使用

4. 网络与数据
   - HTTP 请求
   - JSON 解析
   - 本地存储
   - 数据库操作

### 学习资源

- Flutter 中文网：https://flutter.cn
- Dart 中文文档：https://dart.cn
- Flutter 实战：https://book.flutterchina.club

### 项目实践

学员将通过实际项目练习来巩固所学知识，包括：

- UI 界面构建
- 网络请求处理
- 数据存储管理
- 状态管理应用

### 📂 项目结构

```plaintext
wangzhongzhi/
├── lib/                    # Flutter应用主目录
│   ├── pages/             # 页面文件
│   └── main.dart          # 应用入口文件
├── assets/                # 资源文件目录
│   └── models/            # 模型文件
│       ├── breed_zh.txt   # 中文犬种名称
│       ├── breed_en.txt   # 英文犬种名称
│       └── dog_breed_classifier.tflite  # 转换后的模型文件
├── training/              # 模型训练相关文件
│   ├── images/           # 训练图片目录
│   │   ├── train/       # 训练集
│   │   ├── validation/  # 验证集
│   │   └── test/        # 测试集
│   ├── train.py         # 训练脚本
│   └── logger_config.py # 日志配置
└── README.md             # 项目说明文档
```

### 🚀 模型训练指南

#### 环境配置

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 安装依赖
pip install tensorflow numpy pillow
```

#### 数据准备

1. 在 `training/images/` 目录下创建训练、验证和测试数据集文件夹
2. 每个犬种创建独立子文件夹，文件夹名为犬种英文名
3. 将对应图片放入相应文件夹

```plaintext
training/images/
├── train/
│   ├── labrador_retriever/
│   ├── german_shepherd/
│   └── ...
├── validation/
│   ├── labrador_retriever/
│   ├── german_shepherd/
│   └── ...
└── test/
    ├── labrador_retriever/
    ├── german_shepherd/
    └── ...
```

#### 执行训练

```bash
# 进入训练目录
cd training

# 运行训练脚本
python train.py
```

#### train.py 核心功能

- **数据增强**：通过 ImageDataGenerator 实现图像旋转、缩放等操作
- **模型构建**：使用 CNN 架构，包含多个卷积层和池化层
- **训练过程**：执行 10 轮训练，自动保存最佳模型
- **模型评估**：输出训练、验证和测试集的准确率
- **结果保存**：
  - 模型文件：`dog_breed_classifier.h5`
  - 类别映射：`breed_class_mapping.json`

#### 训练参数说明

- 图像尺寸：150×150 像素
- 批次大小：32
- 训练轮数：10
- 优化器：Adam
- 损失函数：Categorical Crossentropy

#### 注意事项

1. 确保训练数据集分布均衡
2. 图片格式支持：JPG、PNG
3. 建议每个类别至少准备 100 张图片
4. 训练过程中会自动记录日志
5. 可通过调整 `train.py` 中的参数优化训练效果

### 模型训练数据

```bash
Found 601 images belonging to 60 classes.
Found 300 images belonging to 60 classes.
Epoch 1/10
12/18 [===================>..........] - ETA: 22s - loss: 4.1473 - accuracy: 0.0080/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/PIL/Image.py:1054: UserWarning: Palette images with Transparency expressed in bytes should be converted to RGBA images
warnings.warn(
18/18 [==============================] - 62s 3s/step - loss: 4.1303 - accuracy: 0.0053 - val_loss: 4.0923 - val_accuracy: 0.0278
Epoch 2/10
18/18 [==============================] - 34s 2s/step - loss: 4.0942 - accuracy: 0.0264 - val_loss: 4.0807 - val_accuracy: 0.0521
Epoch 3/10
18/18 [==============================] - 29s 2s/step - loss: 4.0757 - accuracy: 0.0246 - val_loss: 4.0029 - val_accuracy: 0.0417
Epoch 4/10
18/18 [==============================] - 29s 2s/step - loss: 3.9938 - accuracy: 0.0387 - val_loss: 3.8604 - val_accuracy: 0.0660
Epoch 5/10
18/18 [==============================] - 31s 2s/step - loss: 3.8481 - accuracy: 0.0791 - val_loss: 3.6985 - val_accuracy: 0.1181
Epoch 6/10
18/18 [==============================] - 43s 2s/step - loss: 3.7142 - accuracy: 0.0949 - val_loss: 3.4112 - val_accuracy: 0.1840
Epoch 7/10
18/18 [==============================] - 35s 2s/step - loss: 3.5063 - accuracy: 0.1230 - val_loss: 3.1563 - val_accuracy: 0.1875
Epoch 8/10
18/18 [==============================] - 18s 1s/step - loss: 3.1739 - accuracy: 0.2021 - val_loss: 2.7770 - val_accuracy: 0.3472
Epoch 9/10
18/18 [==============================] - 19s 1s/step - loss: 3.0304 - accuracy: 0.2302 - val_loss: 2.5901 - val_accuracy: 0.3229
Epoch 10/10
18/18 [==============================] - 22s 1s/step - loss: 2.7395 - accuracy: 0.2917 - val_loss: 2.2847 - val_accuracy: 0.4271
Found 298 images belonging to 60 classes.
10/10 [==============================] - 4s 364ms/step - loss: 2.3151 - accuracy: 0.4262
[鹰眼 AI]: 2025-02-14 19:19:55,616 - **main** - INFO - 测试准确率: 0.42617449164390564
```

#### 数据集信息

| 数据集类型 | 图片数量 | 类别数量 |
| ---------- | -------- | -------- |
| 训练集     | 601      | 60       |
| 验证集     | 300      | 60       |
| 测试集     | 298      | 60       |

🌟 **数据分布数学描述**：

- 平均每类样本数：
  $$\mu = \frac{N_{total}}{C} = \frac{601+300+298}{60} \approx 19.98$$
- 标准差：
  $$\sigma = \sqrt{\frac{1}{C}\sum_{i=1}^{C}(n_i - \mu)^2}$$
  其中 $n_i$ 为第 i 类的样本数

#### 训练结果

##### 最终性能指标

| 数据集类型 | 准确率 |
| ---------- | ------ |
| 训练集     | 29.17% |
| 验证集     | 42.71% |
| 测试集     | 42.62% |

🌟 **性能分析**：

- 过拟合系数：
  $$\Delta = \text{训练准确率} - \text{验证准确率} = 29.17\% - 42.71\% = -13.54\%$$
  负值表明存在欠拟合现象

##### 训练进度表现

| 训练阶段 | 准确率 | 说明         |
| -------- | ------ | ------------ |
| 起始阶段 | 0.53%  | 模型开始学习 |
| 中期阶段 | 18.75% | 性能显著提升 |
| 最终阶段 | 42.71% | 达到最佳表现 |

> 注：通过 10 轮（epochs）训练，模型性能从初始的 0.53%提升至最终的 42.71%，显示出良好的学习能力。

🌟 **学习曲线分析**：
令 $a_t$ 表示第 $t$ 个 epoch 的准确率，可得学习速率：
$$\alpha_t = \frac{a_{t} - a_{t-1}}{\Delta t}$$
其中 $\Delta t$ 为时间间隔（单位：秒）

### 犬种分类对照表

本项目包含 30 种常见犬种的分类，以下是英文和中文对照：

| 英文名称             | 中文名称       |
| -------------------- | -------------- |
| Labrador Retriever   | 拉布拉多寻回犬 |
| German Shepherd      | 德国牧羊犬     |
| Golden Retriever     | 金毛寻回犬     |
| French Bulldog       | 法国斗牛犬     |
| Bulldog              | 英国斗牛犬     |
| Poodle               | 贵宾犬         |
| Beagle               | 比格犬         |
| Rottweiler           | 罗威纳犬       |
| Dachshund            | 腊肠犬         |
| Yorkshire Terrier    | 约克夏梗       |
| Boxer                | 拳师犬         |
| Pomeranian           | 博美犬         |
| Chihuahua            | 吉娃娃         |
| Siberian Husky       | 西伯利亚哈士奇 |
| Great Dane           | 大丹犬         |
| Doberman Pinscher    | 杜宾犬         |
| Shih Tzu             | 西施犬         |
| Border Collie        | 边境牧羊犬     |
| Cocker Spaniel       | 可卡犬         |
| Australian Shepherd  | 澳大利亚牧羊犬 |
| Bernese Mountain Dog | 伯恩山犬       |
| Pug                  | 巴哥犬         |
| Corgi                | 柯基犬         |
| Saint Bernard        | 圣伯纳犬       |
| Chow Chow            | 松狮犬         |
| Alaskan Malamute     | 阿拉斯加雪橇犬 |
| Bull Terrier         | 牛头梗         |
| Dalmatian            | 大麦町犬       |
| Shetland Sheepdog    | 设得兰牧羊犬   |
| Newfoundland         | 纽芬兰犬       |

### 📐 技术原理

#### 深度学习模型架构

1. **卷积神经网络结构**
   输入层 (150×150×3) → 卷积层 → 池化层 → 全连接层 → 输出层 (60 类别)

2. **数据预处理**

- 图像缩放: 150×150 像素
- 像素归一化: RGB 值/255
- 数据增强: 随机翻转、旋转、缩放

🌟 **卷积运算数学表示**：
$$(I * K)_{ij} = \sum_{m}\sum_{n} I(i+m,j+n)K(m,n)$$
其中：

- $I$ 为输入图像矩阵
- $K$ 为卷积核
- $(i,j)$ 为输出特征图位置

#### 模型评估指标

1. **准确率计算**
   $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN} \times 100\%$$
   其中：

- TP = 真阳性
- TN = 真阴性
- FP = 假阳性
- FN = 假阴性

2. **损失函数**
   交叉熵损失：
   $$L = -\frac{1}{N}\sum_{i=1}^{N}\sum_{c=1}^{C} y_{i,c} \log(p_{i,c})$$
   其中：

- $N$ = 样本数
- $C$ = 类别数
- $y_{i,c}$ = 样本 i 的真实类别 c 的指示器（0 或 1）
- $p_{i,c}$ = 样本 i 属于类别 c 的预测概率

🌟 **梯度下降更新公式**：
$$\theta_{t+1} = \theta_t - \eta \cdot \nabla_\theta L(\theta_t)$$
其中：

- $\theta$ = 模型参数
- $\eta$ = 学习率 (默认 0.001)
- $\nabla_\theta L$ = 损失函数梯度

🌟 **Adam 优化器参数更新**：
$$m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$$
$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}$$
$$\hat{v}_t = \frac{v_t}{1-\beta_2^t}$$
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon}\hat{m}_t$$
默认参数：$\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$

#### 模型优化策略

🌟 **学习率衰减**：
采用指数衰减策略：
$$\eta_t = \eta_0 \cdot e^{-kt}$$
其中：

- $\eta_0$ = 初始学习率 (0.001)
- $k$ = 衰减率
- $t$ = 训练步数

🌟 **正则化方法**：
L2 权重衰减：
$$L_{total} = L + \frac{\lambda}{2}\|\theta\|^2$$
其中 $\lambda$ 为正则化系数

### 📈 性能优化建议

1. **数据增强公式扩展**：

   - 随机旋转角度：$\theta \sim U(-15^\circ, 15^\circ)$
   - 亮度调整因子：$\alpha \sim U(0.8, 1.2)$
   - 对比度调整：$\beta \sim U(0.8, 1.2)$

2. **模型复杂度分析**：
   参数量计算公式：
   $$Params = \sum_{l=1}^{L}(k_l \times k_l \times c_{in}^{(l)} \times c_{out}^{(l)} + c_{out}^{(l)})$$
   其中：
   - $k_l$ = 第 l 层卷积核尺寸
   - $c_{in}^{(l)}$ = 输入通道数
   - $c_{out}^{(l)}$ = 输出

### 📱 应用演示

<div align="center">
<table>
   <tr>
      <td align="center" width="400">
         <img src="https://github.com/ctkqiang/WangZhongZhi/blob/main/assets/images/WechatIMG33.jpg?raw=true" width="350" />
         <br />
         <strong>实时识别界面</strong>
      </td>
      <td align="center" width="400">
         <img src="https://github.com/ctkqiang/WangZhongZhi/blob/main/assets/images/WechatIMG32.jpg?raw=true" width="350" />
         <br />
         <strong>识别结果展示</strong>
      </td>
   </tr>
</table>
</div>

主要功能展示：
- 左图：实时摄像头预览和拍照识别界面
- 右图：识别结果分析和详细信息展示
  - 犬种概率分布饼图
  - 详细品种特征说明
  - 饲养建议和注意事项


## 许可证

本项目采用 **木兰宽松许可证 (Mulan PSL)** 进行许可。  
有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

[![License: Mulan PSL v2](https://img.shields.io/badge/License-Mulan%20PSL%202-blue.svg)](http://license.coscl.org.cn/MulanPSL2)

## 🌟 开源项目赞助计划

### 用捐赠助力发展

感谢您使用本项目！您的支持是开源持续发展的核心动力。  
每一份捐赠都将直接用于：  
✅ 服务器与基础设施维护  
✅ 新功能开发与版本迭代  
✅ 文档优化与社区建设

点滴支持皆能汇聚成海，让我们共同打造更强大的开源工具！

---

### 🌐 全球捐赠通道

#### 国内用户

<div align="center" style="margin: 40px 0">

<div align="center">
<table>
<tr>
<td align="center" width="300">
<img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9863.jpg?raw=true" width="200" />
<br />
<strong>🔵 支付宝</strong>
</td>
<td align="center" width="300">
<img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9859.JPG?raw=true" width="200" />
<br />
<strong>🟢 微信支付</strong>
</td>
</tr>
</table>
</div>
</div>

#### 国际用户

<div align="center" style="margin: 40px 0">
  <a href="https://qr.alipay.com/fkx19369scgxdrkv8mxso92" target="_blank">
    <img src="https://img.shields.io/badge/Alipay-全球支付-00A1E9?style=flat-square&logo=alipay&logoColor=white&labelColor=008CD7">
  </a>
  
  <a href="https://ko-fi.com/F1F5VCZJU" target="_blank">
    <img src="https://img.shields.io/badge/Ko--fi-买杯咖啡-FF5E5B?style=flat-square&logo=ko-fi&logoColor=white">
  </a>
  
  <a href="https://www.paypal.com/paypalme/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/PayPal-安全支付-00457C?style=flat-square&logo=paypal&logoColor=white">
  </a>
  
  <a href="https://donate.stripe.com/00gg2nefu6TK1LqeUY" target="_blank">
    <img src="https://img.shields.io/badge/Stripe-企业级支付-626CD9?style=flat-square&logo=stripe&logoColor=white">
  </a>
</div>

---

### 📌 开发者社交图谱

#### 技术交流

<div align="center" style="margin: 20px 0">
  <a href="https://github.com/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-开源仓库-181717?style=for-the-badge&logo=github">
  </a>
  
  <a href="https://stackoverflow.com/users/10758321/%e9%92%9f%e6%99%ba%e5%bc%ba" target="_blank">
    <img src="https://img.shields.io/badge/Stack_Overflow-技术问答-F58025?style=for-the-badge&logo=stackoverflow">
  </a>
  
  <a href="https://www.linkedin.com/in/ctkqiang/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-职业网络-0A66C2?style=for-the-badge&logo=linkedin">
  </a>
</div>

#### 社交互动

<div align="center" style="margin: 20px 0">
  <a href="https://www.instagram.com/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-生活瞬间-E4405F?style=for-the-badge&logo=instagram">
  </a>
  
  <a href="https://twitch.tv/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/Twitch-技术直播-9146FF?style=for-the-badge&logo=twitch">
  </a>
  
  <a href="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9245.JPG?raw=true" target="_blank">
    <img src="https://img.shields.io/badge/微信公众号-钟智强-07C160?style=for-the-badge&logo=wechat">
  </a>
</div>

---

🙌 感谢您成为开源社区的重要一员！  
💬 捐赠后欢迎通过社交平台与我联系，您的名字将出现在项目致谢列表！
