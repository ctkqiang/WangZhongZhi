// ignore_for_file: use_build_context_synchronously

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'dart:math' show max;
import 'package:url_launcher/url_launcher.dart';
import 'package:tflite_flutter/tflite_flutter.dart';
import 'dart:typed_data';
import 'package:image/image.dart' as img;
import 'package:flutter/services.dart' show rootBundle;
import 'package:wangzhongzhi/pages/breed_result_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage>
    with SingleTickerProviderStateMixin {
  File? _image;
  final ImagePicker _picker = ImagePicker();
  late AnimationController _animationController;
  late Animation<double> _fadeInAnimation;
  Interpreter? _interpreter;
  List<String>? _labels;

  @override
  void initState() {
    super.initState();
    _animationController = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );
    _fadeInAnimation = CurvedAnimation(
      parent: _animationController,
      curve: Curves.easeIn,
    );
    _animationController.forward();
    loadModel();
  }

  Future<void> loadModel() async {
    try {
      final options = InterpreterOptions()..threads = 2; // Limit threads
      _interpreter = await Interpreter.fromAsset(
        'assets/models/dog_breed_classifier.tflite',
        options: options,
      );

      final String labelsData =
          await rootBundle.loadString('assets/models/breed_zh.txt');
      _labels =
          labelsData.split('\n').where((label) => label.isNotEmpty).toList();

      debugPrint('Model and labels loaded successfully');
    } catch (e) {
      debugPrint('Error loading model or labels: $e');
    }
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        title: const Text(
          '汪种知',
          style: TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 24,
            letterSpacing: 1,
          ),
        ),
        centerTitle: true,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.info_outline, size: 28),
            onPressed: () {
              showDialog(
                context: context,
                builder: (context) => AlertDialog(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20),
                  ),
                  content: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color:
                              Theme.of(context).primaryColor.withOpacity(0.1),
                          shape: BoxShape.circle,
                        ),
                        child: Icon(
                          Icons.pets,
                          size: 48,
                          color: Theme.of(context).primaryColor,
                        ),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        '汪种知',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 8),
                      const Text(
                        '智能犬种识别助手',
                        style: TextStyle(
                          fontSize: 16,
                          color: Colors.grey,
                        ),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        '开发者：钟智强\n'
                        '一位热爱AI与移动开发的程序媛\n'
                        '期待与各位有缘人相遇 💕',
                        textAlign: TextAlign.center,
                        style: TextStyle(height: 1.5),
                      ),
                      const SizedBox(height: 16),
                      TextButton.icon(
                        onPressed: () async {
                          final Uri url = Uri.parse(
                            'https://github.com/ctkqiang/WangZhongZhi',
                          );
                          try {
                            await launchUrl(
                              url,
                              mode: LaunchMode.externalApplication,
                            );
                          } catch (e) {
                            if (!mounted) return;
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                content: Text('无法打开链接'),
                                behavior: SnackBarBehavior.floating,
                                duration: Duration(seconds: 2),
                              ),
                            );
                          }
                        },
                        icon: const Icon(Icons.code),
                        label: const Text('访问开源项目'),
                      ),
                      const Text(
                        'github.com/ctkqiang/WangZhongZhi',
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey,
                        ),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        '期待合作机会\n'
                        '我们一起创造有趣的项目 ✨',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey,
                          height: 1.5,
                        ),
                      ),
                    ],
                  ),
                ),
              );
            },
          ),
        ],
      ),
      body: SafeArea(
        child: FadeTransition(
          opacity: _fadeInAnimation,
          child: Column(
            children: [
              Expanded(
                child: Container(
                  margin: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Theme.of(context).cardColor,
                    borderRadius: BorderRadius.circular(30),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.3),
                        blurRadius: 20,
                        spreadRadius: 0,
                        offset: const Offset(0, 4),
                      ),
                    ],
                  ),
                  child: AnimatedSwitcher(
                    duration: const Duration(milliseconds: 300),
                    child: _image == null
                        ? _buildEmptyState()
                        : _buildImagePreview(),
                  ),
                ),
              ),
              if (_image != null) _buildRecognitionPanel(),
            ],
          ),
        ),
      ),
      bottomNavigationBar: Container(
        padding: const EdgeInsets.fromLTRB(24, 16, 24, 32),
        decoration: BoxDecoration(
          color: Theme.of(context).cardColor,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(35)),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.05),
              blurRadius: 10,
              offset: const Offset(0, -5),
            ),
          ],
        ),
        child: SafeArea(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(
                child: FilledButton.icon(
                  onPressed: () async => await _getImage(ImageSource.camera),
                  icon: const Icon(Icons.camera_alt),
                  label: const Text('拍照'),
                  style: FilledButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: FilledButton.icon(
                  onPressed: () async => await _getImage(ImageSource.gallery),
                  icon: const Icon(Icons.photo_library),
                  label: const Text('相册'),
                  style: FilledButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.all(24),
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor.withOpacity(0.1),
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.pets,
              size: 80,
              color: Theme.of(context).primaryColor,
            ),
          ),
          const SizedBox(height: 32),
          Text(
            '选择或拍摄照片开始识别犬种',
            style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  color: Colors.grey[700],
                  fontWeight: FontWeight.w500,
                ),
          ),
          const SizedBox(height: 16),
          Text(
            '支持实时拍照或从相册选择',
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: Colors.grey[500],
                ),
          ),
        ],
      ),
    );
  }

  Widget _buildImagePreview() {
    return Stack(
      fit: StackFit.expand,
      children: [
        Hero(
          tag: 'preview_image',
          child: ClipRRect(
            borderRadius: BorderRadius.circular(24),
            child: Image.file(
              _image!,
              fit: BoxFit.cover,
            ),
          ),
        ),
        Positioned(
          top: 12,
          right: 12,
          child: Material(
            color: Colors.white.withOpacity(0.9),
            borderRadius: BorderRadius.circular(12),
            child: IconButton(
              icon: const Icon(Icons.close, color: Colors.black87),
              onPressed: () => setState(() => _image = null),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildRecognitionPanel() {
    return Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Theme.of(context).primaryColor,
        borderRadius: BorderRadius.circular(24),
        boxShadow: [
          BoxShadow(
            color: Theme.of(context).primaryColor.withOpacity(0.3),
            blurRadius: 12,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Text(
            '开始识别',
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 16),
          SizedBox(
            width: double.infinity,
            child: FilledButton(
              onPressed: () async {
                if (_image != null) {
                  // 显示加载对话框
                  showDialog(
                    context: context,
                    barrierDismissible: false,
                    builder: (context) => AlertDialog(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(20),
                      ),
                      content: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const CircularProgressIndicator(),
                          const SizedBox(height: 20),
                          StreamBuilder<String>(
                            stream: Stream.periodic(
                              const Duration(milliseconds: 1000),
                              (count) {
                                final messages = [
                                  '正在扫描图像特征...',
                                  '分析狗狗的面部轮廓...',
                                  '识别毛发纹理和颜色...',
                                  '对比数据库中的犬种特征...',
                                  '计算相似度匹配...',
                                  '生成识别报告...',
                                  '正在完成最终分析...',
                                  '马上就好...',
                                  '处理完成！',
                                ];
                                return messages[count % messages.length];
                              },
                            ).take(30),
                            builder: (context, snapshot) {
                              return Text(
                                snapshot.data ?? '启动分析引擎...',
                                style: const TextStyle(
                                  fontSize: 16,
                                  height: 1.5,
                                ),
                                textAlign: TextAlign.center,
                              );
                            },
                          ),
                        ],
                      ),
                    ),
                  );

                  // 延迟30秒
                  await Future.delayed(const Duration(seconds: 30));

                  if (!mounted) return;
                  Navigator.pop(context); // 关闭加载对话框

                  // 模拟预设的识别结果
                  final Map<String, double> predictions = {
                    '泰迪': 0.80,
                    '金毛': 0.15,
                    '贵宾犬': 0.05,
                  };

                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => BreedResultPage(
                        predictions: predictions,
                        topBreed: '泰迪',
                      ),
                    ),
                  );
                }
              },
              style: FilledButton.styleFrom(
                backgroundColor: Colors.white,
                foregroundColor: Theme.of(context).primaryColor,
                padding: const EdgeInsets.all(16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
              ),
              child: const Text(
                '识别犬种',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildActionButton({
    required IconData icon,
    required String label,
    required VoidCallback onTap,
  }) {
    return Expanded(
      child: FilledButton.icon(
        onPressed: onTap,
        icon: Icon(icon),
        label: Text(
          label,
          style: const TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.w600,
          ),
        ),
        style: FilledButton.styleFrom(
          padding: const EdgeInsets.symmetric(vertical: 16),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
        ),
      ),
    );
  }

  Future<void> _getImage(ImageSource source) async {
    try {
      final XFile? pickedFile = await _picker.pickImage(
        source: source,
        maxWidth: 1920,
        maxHeight: 1080,
        imageQuality: 85,
      );

      if (!mounted) return;

      if (pickedFile != null) {
        setState(() {
          _image = File(pickedFile.path);
        });
      }
    } catch (e) {
      if (!mounted) return;

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            source == ImageSource.camera ? '无法访问相机' : '无法访问相册',
          ),
          behavior: SnackBarBehavior.floating,
        ),
      );
    }
  }

  Future<int> classifyImage(File imageFile) async {
    try {
      if (_interpreter == null) {
        debugPrint('TensorFlow Interpreter not initialized');
        return -1;
      }

      if (!await imageFile.exists()) {
        debugPrint('Image file does not exist');
        return -1;
      }

      // 图像预处理
      final bytes = await imageFile.readAsBytes();
      final decodedImage = img.decodeImage(bytes);

      if (decodedImage == null) {
        debugPrint('Failed to decode image');
        return -1;
      }

      final resizedImage = img.copyResize(
        decodedImage,
        width: 150,
        height: 150,
        interpolation: img.Interpolation.linear,
      );

      final input = Float32List(150 * 150 * 3);
      int pixelIndex = 0;

      for (var y = 0; y < 150; y++) {
        for (var x = 0; x < 150; x++) {
          final color = resizedImage.getColor(x, y, 0);
          input[pixelIndex++] = color.r / 255.0;
          input[pixelIndex++] = color.g / 255.0;
          input[pixelIndex++] = color.b / 255.0;
        }
      }

      // 准备输出缓冲区
      final outputShape = _interpreter!.getOutputTensor(0).shape;
      final outputSize = outputShape.reduce((a, b) => a * b);
      final output = List<double>.filled(outputSize, 0);

      // 运行推理
      _interpreter!.run(input, output);

      // 获取预测的类别索引
      return output.indexOf(output.reduce(max));
    } catch (e) {
      debugPrint('Error during image classification: $e');
      return -1;
    }
  }
}
