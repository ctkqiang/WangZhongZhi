import 'package:flutter/material.dart';
import 'package:wangzhongzhi/pages/splash.dart';

const appName = '汪种知';

Future<void> main() async {
  runApp(const WangZhongZhi());
}

class WangZhongZhi extends StatefulWidget {
  const WangZhongZhi({super.key});

  @override
  State<WangZhongZhi> createState() => _WangZhongZhiState();
}

class _WangZhongZhiState extends State<WangZhongZhi> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: appName,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF89BCF5),
        ),
      ),
      home: const SplashScreen(),
    );
  }
}
