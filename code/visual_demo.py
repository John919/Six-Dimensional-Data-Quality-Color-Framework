import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 定义六维数据质量指标
dimensions = ["Completeness", "Accuracy", "Consistency", 
              "Timeliness", "Uniqueness", "Validity"]

# 2. 模拟一份测试数据质量得分（0-100）
scores = [85, 92, 78, 88, 95, 80]

# 3. 颜色映射：绿(≥80)、黄(50-79)、红(<50)
colors = []
for s in scores:
    if s >= 80:
        colors.append("green")
    elif s >= 50:
        colors.append("orange")
    else:
        colors.append("red")

# 4. 生成可视化柱状图
plt.figure(figsize=(10, 6))
bars = plt.bar(dimensions, scores, color=colors)
plt.ylim(0, 100)
plt.title("Six-Dimensional Data Quality Assessment", fontsize=14)
plt.xlabel("Quality Dimensions", fontsize=12)
plt.ylabel("Score (0-100)", fontsize=12)

# 在柱子上显示分数
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height+1,
             f'{height}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig("docs/quality_visualization.png")  # 保存到文档文件夹
plt.show()

print("✅ Six-dimensional data quality visualization completed!")
