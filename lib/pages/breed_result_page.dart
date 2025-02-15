import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';

class BreedResultPage extends StatefulWidget {
  final Map<String, double> predictions;
  final String topBreed;

  const BreedResultPage({
    super.key,
    required this.predictions,
    required this.topBreed,
  });

  @override
  State<BreedResultPage> createState() => _BreedResultPageState();
}

class _BreedResultPageState extends State<BreedResultPage> {
  final Map<String, List<String>> breedFacts = {
    '拉布拉多寻回犬': [
      '原产于加拿大纽芬兰岛',
      '性格温顺友善，极具耐心',
      '优秀的导盲犬和搜救犬',
      '寿命约10-12年',
      '特别喜欢游泳和玩水',
    ],
    '德国牧羊犬': [
      '以忠诚和智慧著称',
      '最受欢迎的警犬品种',
      '工作能力极强，警觉性高',
      '寿命约9-13年',
      '需要大量运动和训练',
    ],
    '金毛寻回犬': [
      '原产于苏格兰，性格温和',
      '极其聪明，容易训练',
      '特别适合家庭和儿童',
      '寿命约10-12年',
      '优秀的导盲犬和治疗犬',
    ],
    '法国斗牛犬': [
      '体型小巧，性格活泼',
      '适合城市公寓生活',
      '不需要大量运动',
      '寿命约10-12年',
      '对主人非常忠诚',
    ],
    '英国斗牛犬': [
      '性格温和，极具耐心',
      '适合家庭饲养',
      '不需要太多运动',
      '寿命约8-10年',
      '对儿童特别友善',
    ],
    '贵宾犬': [
      '智商极高，容易训练',
      '不掉毛，适合过敏人士',
      '有多种体型可选',
      '寿命约12-15年',
      '需要定期专业美容',
    ],
    '比格犬': [
      '嗅觉灵敏，活力充沛',
      '性格友善开朗',
      '适合家庭饲养',
      '寿命约12-15年',
      '需要适量运动',
    ],
    '泰迪': [
      '原产于法国，是贵宾犬的一种',
      '以其聪明、活泼的性格闻名',
      '寿命一般在12-18年',
      '非常适合公寓生活',
      '对人类非常忠诚，特别适合陪伴',
    ],
    '金毛': [
      '原产于苏格兰，是优秀的导盲犬',
      '性格温和友善，特别喜欢水',
      '寿命约10-12年',
      '智商排名第4位',
      '非常适合有孩子的家庭',
    ],
    '贵宾犬': [
      '被认为是最聪明的犬种之一',
      '不掉毛，适合过敏体质的人',
      '寿命可达15-18年',
      '有多种体型大小',
      '需要定期专业美容',
    ],
    '西伯利亚哈士奇': [
      '原产于西伯利亚',
      '体力充沛，需要大量运动',
      '性格独立，不易训练',
      '寿命约12-14年',
      '适合寒冷气候',
    ],
    '柯基犬': [
      '英国女王最爱的犬种',
      '腿短但活力十足',
      '聪明机警，容易训练',
      '寿命约12-14年',
      '适合家庭饲养',
    ],
    '边境牧羊犬': [
      '被认为是最聪明的犬种',
      '工作能力极强',
      '需要大量运动和智力训练',
      '寿命约12-15年',
      '适合有经验的犬主',
    ],
    // Add more breeds as needed...
  };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('识别结果'),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              height: 300,
              padding: const EdgeInsets.all(16),
              child: PieChart(
                PieChartData(
                  sections: widget.predictions.entries.map((entry) {
                    final color = entry.key == '泰迪'
                        ? Colors.orange
                        : entry.key == '金毛'
                            ? Colors.amber
                            : Colors.brown;
                    return PieChartSectionData(
                      value: entry.value,
                      title:
                          '${entry.key}\n${(entry.value * 100).toStringAsFixed(1)}%',
                      color: color,
                      radius: 100,
                      titleStyle: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    );
                  }).toList(),
                  sectionsSpace: 2,
                ),
              ),
            ),
            const Padding(
              padding: EdgeInsets.all(16),
              child: Text(
                '趣味知识',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            if (breedFacts.containsKey(widget.topBreed))
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: breedFacts[widget.topBreed]!.length,
                itemBuilder: (context, index) {
                  return Card(
                    margin: const EdgeInsets.symmetric(
                      horizontal: 16,
                      vertical: 4,
                    ),
                    child: ListTile(
                      leading: const Icon(Icons.pets),
                      title: Text(breedFacts[widget.topBreed]![index]),
                    ),
                  );
                },
              ),
          ],
        ),
      ),
    );
  }
}
