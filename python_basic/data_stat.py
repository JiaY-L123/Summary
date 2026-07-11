import os
import matplotlib.pyplot as plt

# --------------------------
# 模块1：os遍历文件夹，字典存储分类标签
# 功能：读取images下子文件夹，文件夹名作为标签，保存所有图片路径
# --------------------------
# 解决matplotlib中文乱码
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 批量读取图片文件夹，用字典存储标签与图片路径
img_root = "./images"
label_dict = {}

# 遍历所有分类文件夹
for label in os.listdir(img_root):
    label_full_path = os.path.join(img_root, label)
    # 只处理文件夹，跳过文件
    if not os.path.isdir(label_full_path):
        continue
    
    img_path_list = []
    # 遍历当前分类下所有图片
    for file_name in os.listdir(label_full_path):
        # 只保留图片格式
        if file_name.endswith((".jpg", ".png", ".jpeg")):
            full_img_path = os.path.join(label_full_path, file_name)
            img_path_list.append(full_img_path)
    # 存入字典：key=分类标签，value=该分类所有图片路径
    label_dict[label] = img_path_list

# 提取绘图需要的x、y数据
x_labels = list(label_dict.keys())       # 横轴：分类名称 cat/dog
y_counts = [len(paths) for paths in label_dict.values()]  # 纵轴：每类图片数量

# 2. Matplotlib基础绘图模板（你要学习的核心代码）
# --------------------------
# 模块2：Matplotlib绘图模板
# 功能：绘制分类数量柱状图，保存高清分布图
# --------------------------
# 创建画布，设置尺寸宽10英寸，高6英寸
plt.figure(figsize=(10, 6))

# 绘制分类柱状图，统计图片数量
bars = plt.bar(x_labels, y_counts, color="#5470c6")

# 设置图表标题、坐标轴文字
plt.title("数据集各类图片数量分布", fontsize=14)
plt.xlabel("图片分类标签", fontsize=12)
plt.ylabel("图片数量", fontsize=12)

# 横轴文字旋转45度，防止文字重叠
plt.xticks(rotation=45)

# 在每个柱子顶部标注图片数量
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f"{height}", ha="center", va="bottom")

# 自动调整画布边距，避免文字被截断
plt.tight_layout()

# 保存高清图片（必须写在plt.show()前面）
plt.savefig("dataset_dist.png", dpi=300)

# 弹出窗口展示图表
plt.show()
# 全部分类遍历完成后添加
