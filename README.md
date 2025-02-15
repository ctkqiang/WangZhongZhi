
# 汪种知

基于Flutter框架开发的犬种识别应用，集成深度学习模型，支持60种犬种的实时识别。本项目作为人工智能与移动应用开发的实践项目，旨在提供一个完整的端到端解决方案。

## 培训说明
 

### 培训目标
- 掌握Flutter框架的基本概念和开发流程
- 学习Dart编程语言的核心特性
- 理解Flutter界面构建和状态管理
- 熟悉常用Widget的使用方法

### 培训内容
1. Flutter基础
   - Flutter环境搭建
   - Dart语言基础
   - Widget介绍与使用
   - 布局与导航

2. UI开发
   - Material Design组件
   - Cupertino组件
   - 自定义Widget
   - 响应式布局

3. 状态管理
   - setState
   - GetX使用

4. 网络与数据
   - HTTP请求
   - JSON解析
   - 本地存储
   - 数据库操作

### 学习资源
- Flutter中文网：https://flutter.cn
- Dart中文文档：https://dart.cn
- Flutter实战：https://book.flutterchina.club

### 项目实践
学员将通过实际项目练习来巩固所学知识，包括：
- UI界面构建
- 网络请求处理
- 数据存储管理
- 状态管理应用

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
|-----------|----------|----------|
| 训练集 | 601 | 60 |
| 验证集 | 300 | 60 |
| 测试集 | 298 | 60 |

#### 训练结果
##### 最终性能指标
| 数据集类型 | 准确率 |
|-----------|--------|
| 训练集 | 29.17% |
| 验证集 | 42.71% |
| 测试集 | 42.62% |

##### 训练进度表现
| 训练阶段 | 准确率 | 说明 |
|---------|--------|------|
| 起始阶段 | 0.53% | 模型开始学习 |
| 中期阶段 | 18.75% | 性能显著提升 |
| 最终阶段 | 42.71% | 达到最佳表现 |

> 注：通过10轮（epochs）训练，模型性能从初始的0.53%提升至最终的42.71%，显示出良好的学习能力。

### 犬种分类对照表
本项目包含30种常见犬种的分类，以下是英文和中文对照：

| 英文名称 | 中文名称 |
|---------|---------|
| Labrador Retriever | 拉布拉多寻回犬 |
| German Shepherd | 德国牧羊犬 |
| Golden Retriever | 金毛寻回犬 |
| French Bulldog | 法国斗牛犬 |
| Bulldog | 英国斗牛犬 |
| Poodle | 贵宾犬 |
| Beagle | 比格犬 |
| Rottweiler | 罗威纳犬 |
| Dachshund | 腊肠犬 |
| Yorkshire Terrier | 约克夏梗 |
| Boxer | 拳师犬 |
| Pomeranian | 博美犬 |
| Chihuahua | 吉娃娃 |
| Siberian Husky | 西伯利亚哈士奇 |
| Great Dane | 大丹犬 |
| Doberman Pinscher | 杜宾犬 |
| Shih Tzu | 西施犬 |
| Border Collie | 边境牧羊犬 |
| Cocker Spaniel | 可卡犬 |
| Australian Shepherd | 澳大利亚牧羊犬 |
| Bernese Mountain Dog | 伯恩山犬 |
| Pug | 巴哥犬 |
| Corgi | 柯基犬 |
| Saint Bernard | 圣伯纳犬 |
| Chow Chow | 松狮犬 |
| Alaskan Malamute | 阿拉斯加雪橇犬 |
| Bull Terrier | 牛头梗 |
| Dalmatian | 大麦町犬 |
| Shetland Sheepdog | 设得兰牧羊犬 |
| Newfoundland | 纽芬兰犬 |
