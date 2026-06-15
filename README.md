# 2026_summer_planning
hello guys, this is my first time to write ReadMe in github, nice to meet u guys. This is my Postgraduate Student 0 summer study for AI and CV 3D reconstruct, just record this good life time🤪

# 汤毕阳 · 暑假学习计划 · 思维导图

> 目标：城乡规划 → 深圳大学 王瑞胜教授 · AI（城市计算）方向  
> 时间：8周暑假（2026.07 – 2026.08）  
> 主题：从「会用工具」到「能写工具」，摄影测量 + 三维城市重建

---

## 一、数学加固（最高优先级）

### 线性代数 — Gilbert Strang MIT 18.06
- [ ] **Week 1-2**（前12讲）
  - 矩阵乘法、消元法、LU 分解、转置与置换
  - 向量空间与子空间（列空间、零空间）
  - 线性无关、基与维数
  - 四个基本子空间定理
- [ ] **Week 3-4**（后12讲）
  - 正交性、投影、Gram-Schmidt 正交化
  - 行列式、特征值与特征向量
  - **奇异值分解 SVD** ← 最重要！
  - 主成分分析 PCA ← CV/ML 中最常用
- [ ] **练习**
  - 课后奇数题（答案可查）
  - 用 NumPy 手写 SVD 分解 + PCA 降维
  - 理解协方差矩阵的几何意义
- **资源**
  - YouTube: MIT OpenCourseWare 18.06
  - 《线性代数及其应用》(David C. Lay) 中文版

### 概率与统计 —《概率导论》(Bertsekas)
- [ ] **Week 1-3**（配合线代进行）
  - 样本空间、概率公理、条件概率
  - 贝叶斯定理（重点！ML 的语言）
  - 离散/连续随机变量、常见分布
  - 期望、方差、协方差
  - 最大似然估计 MLE ← 必懂
  - 中心极限定理
- [ ] **练习**
  - 用 Python 模拟大数定律和 CLT
  - 手推高斯分布 MLE 的解析解

### 最优化 — Boyd《Convex Optimization》
- [ ] **Week 4-5**（前7章够用）
  - 凸集、凸函数、凸优化问题
  - 梯度下降（批量/随机/小批量）
  - 拉格朗日乘数法与对偶
  - KKT 条件（知道即可）
- [ ] **练习**
  - 手写梯度下降拟合线性回归
  - 对比 SGD vs Adam 的收敛曲线

---

## 二、Python 工程化

### 开发环境搭建
- [ ] **Week 1**
  - VS Code / PyCharm 配置
  - Git 基础：init, add, commit, branch, remote, push/pull
  - GitHub 账号使用：README, Issues, Actions
  - 虚拟环境：venv / conda env
  - pip / conda 包管理

### 科学计算核心库
- [ ] **Week 1-2** — NumPy
  - ndarray 创建与索引、广播机制
  - 矩阵运算、线性代数模块 `np.linalg`
  - 随机数生成、统计函数
- [ ] **Week 2** — Pandas
  - Series 与 DataFrame、数据读取(CSV/Excel)
  - 过滤、分组(groupby)、聚合、透视表
  - 时间序列处理、缺失值处理
- [ ] **Week 2-3** — Matplotlib / Seaborn
  - 折线图、散点图、柱状图、热力图
  - 子图布局、中文字体配置
  - 3D 可视化 `mpl_toolkits.mplot3d`

### 算法与数据结构实战
- [ ] **Week 3-6**（贯穿）— LeetCode 100题
  - **数组/字符串**：两数之和、滑动窗口、KMP（20题）
  - **链表**：反转、合并、环检测（10题）
  - **栈/队列/堆**：单调栈、优先队列、TopK（10题）
  - **树/图**：DFS/BFS、二叉树遍历、最短路径（20题）
  - **动态规划**：背包、LCS、编辑距离（20题）
  - **排序/搜索**：快排、归并、二分搜索变体（20题）
- **目标**：能独立写出常见算法，理解时间/空间复杂度

### 命令行能力
- [ ] **Week 1-2**
  - Shell 基础：ls, cd, grep, find, pipe, 重定向
  - 写简单 bash 脚本
  - SSH 远程连接

---

## 三、机器学习 & 深度学习

### 经典机器学习 — 吴恩达 Coursera ML
- [ ] **Week 3-4**
  - 线性回归、逻辑回归
  - 正则化（L1/L2）、偏差-方差权衡
  - 决策树、随机森林、XGBoost
  - SVM、核方法
  - K-Means、DBSCAN 聚类
  - 交叉验证、混淆矩阵、ROC/AUC
- [ ] **练习**
  - 用 sklearn 完成 Titanic 预测（Kaggle）
  - 用 sklearn 做手写数字识别

### 深度学习入门 — 李宏毅 或 fast.ai
- [ ] **Week 4-5**
  - 神经元、激活函数、损失函数
  - 反向传播（BP）— 必须手推一遍！
  - MLP 多层感知机
  - **CNN 卷积神经网络** ← 重点
    - 卷积、池化、感受野
    - ResNet、UNet（王老师组常用UNet做分割）
  - 归一化：BatchNorm / LayerNorm
  - Dropout、数据增强
- [ ] **练习**
  - 手写 MLP 从零实现 MNIST 分类
  - 用 PyTorch 复现 ResNet-18

### Transformer 与 ViT
- [ ] **Week 6** — 王老师团队也在用
  - Self-Attention 机制（必手推 Q/K/V）
  - Multi-Head Attention
  - Positional Encoding
  - Vision Transformer (ViT)
  - 3D ViT / Point Transformer ← 了解一下
- [ ] **练习**
  - 读 ViT 论文，用 PyTorch 复现核心模块
  - 对比 CNN vs ViT 在分类任务上的差异

### PyTorch 实战
- [ ] **贯穿 Week 3-8**
  - Tensor 操作、自动微分 (autograd)
  - Dataset / DataLoader
  - nn.Module、常用层
  - 训练循环（train/eval）、保存/加载模型
  - GPU 训练 (`model.cuda()`, `tensor.to(device)`)
  - TensorBoard 可视化
  - 混合精度训练 (AMP)

---

## 四、三维视觉与点云处理 ← 核心交叉方向

### 摄影测量基础
- [ ] **Week 5**
  - 坐标系：像平面 → 像空间 → 物方
  - 内外方位元素（你已经接触过 Rhino 相机）
  - 共线条件方程 ← 摄影测量核心公式
  - 立体像对、核线几何
  - 空中三角测量（概念）
  - 倾斜摄影测量 — 无人机三维建模流程
- **资源**
  - 张祖勋《数字摄影测量学》
  - 你本科规划课本里的测量学部分

### 点云处理基础 — Open3D
- [ ] **Week 5-6**
  - [ ] 点云数据结构、可视化
  - [ ] 点云滤波：体素下采样、统计滤波、半径滤波
  - [ ] 法向量估计
  - [ ] 点云配准：ICP、特征匹配 + RANSAC
  - [ ] 点云分割：RANSAC 平面分割、区域生长
  - [ ] KD-Tree、八叉树空间索引
  - [ ] 点云 → 网格：Poisson 重构
- **资源**
  - Open3D 官方文档 Tutorial
  - 《点云库 PCL 从入门到精通》

### 点云深度学习
- [ ] **Week 6-7**
  - [ ] PointNet（CVPR'17）— 精读 + 复现
    - 为什么点云处理难？（无序性、旋转不变性）
    - 对称函数 (Max Pooling)
    - T-Net 空间变换网络
  - [ ] PointNet++（NeurIPS'17）— 精读 + 复现
    - 分层特征学习 (Set Abstraction)
    - 多尺度分组 (MSG/MRG)
    - 语义分割 head
  - [ ] 了解：Point Transformer、KPConv
- **练习**
  - 跑通 PointNet++ 在 S3DIS 上的训练
  - 用自己采集或下载的点云做推理测试

### 三维重建
- [ ] **Week 7-8**
  - [ ] SFM (Structure from Motion)：COLMAP 实操
  - [ ] MVS (Multi-View Stereo)
  - [ ] 点云到网格：理解 Delaunay 三角剖分
  - [ ] 建筑线框重建（认知PBWR方法）
  - [ ] 了解 NeRF / 3D Gaussian Splatting
- **资源**
  - 《Multiple View Geometry in Computer Vision》前6章
  - COLMAP 官方 Tutorial

---

## 五、王瑞胜老师论文精读

### Building3D 数据集 & 建模管线
- [ ] **Week 5 — Building3D (ICCV'23)**
  - Large-scale Building Modeling from Point Clouds
  - 数据集规模：998km²，16个城市，LoD2级别
  - 理解标注格式：点云 + 网格 + 线框
  - 下载数据、跑通 baseline
  - 思考：城市规划知识如何辅助建筑类型识别？

- [ ] **Week 6 — PBWR (CVPR'24)**
  - Parametric Building Wireframe Reconstruction
  - 判别式 → 生成式 的转变思路
  - 理解参数化线框的表示方法
  - 和你 Grasshopper 参数化设计的共通之处

- [ ] **Week 7 — EdgeDiff (CVPR'25)**
  - Edge-Aware Diffusion Model for Building Reconstruction
  - 扩散模型在 3D 建筑重建中的应用
  - 为什么用边缘感知？解决了什么问题？

- [ ] **Week 7-8 — 其他相关论文**
  - Plane Segmentation 点云平面分割 (TPAMI)
  - 自监督点云学习论文
  - 点云语义分割最新方法
- **资源**
  - dblp.org/pid/42/5211-1
  - Papers with Code 查对应开源实现

### 团队技术栈（暑期提前熟悉）
- [ ] **Python**: PyTorch, Open3D, NumPy, Scikit-learn
- [ ] **点云处理**: Open3D, PDAL, CloudCompare
- [ ] **三维可视化**: Potree, Cesium.js, Three.js
- [ ] **几何库**: libigl, CGAL
- [ ] **CV**: OpenCV, Kornia
- [ ] **深度学习**: PyTorch Lightning, Hugging Face
- [ ] **版本控制**: Git + GitHub

---

## 八、周计划时间线

### Week 1（7月第1周）— 环境 + 线代
> 目标：搭好所有开发环境，线代启动
- [ ] 装 Python 3.10+/VS Code/Git
- [ ] 配好虚拟环境和 Jupyter
- [ ] Git 基础操作，建 GitHub 仓库
- [ ] NumPy 核心操作（数组、广播、线性代数）
- [ ] MIT 18.06 第1-6讲（向量空间前半）
- [ ] 《概率导论》第1-2章（概率基础）
- [ ] LeetCode 5题（数组/哈希表）

### Week 2（7月第2周）— 线代 + Pandas
> 目标：线代过完一半，数据处理能力建立
- [ ] Pandas 全面掌握
- [ ] Matplotlib 可视化
- [ ] MIT 18.06 第7-12讲（四个基本子空间）
- [ ] 《概率导论》第3-4章（随机变量与期望）
- [ ] LeetCode 10题（数组/字符串/栈）
- [ ] 开始用 Jupyter 写学习笔记

### Week 3（7月第3周）— 概率 + 经典ML
> 目标：概率论完结，ML 入门
- [ ] 《概率导论》第5-7章（极限定理、贝叶斯）
- [ ] 吴恩达 ML 课：线性回归→逻辑回归→正则化
- [ ] 线代：MIT 18.06 第13-18讲（特征值、SVD）
- [ ] PyTorch 入门：Tensor, autograd, nn.Module
- [ ] LeetCode 10题（队列/堆/排序）
- [ ] 手写梯度下降拟合线性回归

### Week 4（7月第4周）— 经典ML + DL 入门
> 目标：能用 sklearn 做分类回归，理解 BP
- [ ] 吴恩达 ML 课：SVM、决策树、聚类、评估
- [ ] Kaggle Titanic 完整走一遍
- [ ] 手推反向传播（纸笔 + 代码验证）
- [ ] PyTorch DataLoader / 训练循环
- [ ] 线代：SVD + PCA 代码实现
- [ ] LeetCode 10题（树/图）

### Week 5（8月第1周）— 摄影测量 + Open3D
> 目标：理解摄影测量基础，会操作点云
- [ ] 张祖勋《数字摄影测量学》重点章节
- [ ] Open3D 官方 Tutorial 全部过一遍
- [ ] 点云滤波、法向、配准、分割 动手操作
- [ ] 精读 Building3D 论文
- [ ] CNN 精读 + ResNet 复现
- [ ] 下载 Building3D 数据，尝试加载可视化

### Week 6（8月第2周）— PointNet + UNet
> 目标：点云深度学习入门
- [ ] 精读 + 复现 PointNet
- [ ] 精读 + 复现 PointNet++
- [ ] UNet 复现（语义分割）
- [ ] Transformer / ViT 理解
- [ ] 精读 PBWR (CVPR'24)
- [ ] LeetCode 15题（DP/图）

### Week 7（8月第3周）— 3D 重建 + 论文
> 目标：了解 3D 重建全流程
- [ ] COLMAP 实操：照片→稀疏点云→稠密点云
- [ ] 精读 EdgeDiff (CVPR'25)
- [ ] 了解 NeRF / 3DGS
- [ ] 跑通 Building3D baseline
- [ ] 复盘王老师 3 篇核心论文 ← 形成自己的理解
- [ ] LeetCode 15题（DP）

### Week 8（8月第4周）— Capstone + 联系导师
> 目标：做出一个可展示的小项目
- [ ] **Capstone 项目**（见下方）
- [ ] 写联系导师的邮件 ← 附上你的 GitHub + demo
- [ ] 整理暑期学习笔记（可以放个人网页上）
- [ ] 查漏补缺，回顾薄弱环节
- [ ] LeetCode 总结复习 20题

---

## 九、Capstone 项目 ← 简历加分

### 建议项目：建筑物屋顶平面分割与类型识别

**背景**
利用 Building3D 数据集或无人机倾斜摄影点云，实现建筑物屋顶平面的自动分割与类型分类（平顶/坡顶/穹顶等），输出矢量轮廓线。

**与王老师方向的关联**
- 点云平面分割 ← TPAMI 论文
- 建筑类型识别 ← Building3D
- 线框输出 ← PBWR

**技术路径**
1. 点云预处理（下采样、去噪、法向估计）
2. RANSAC 平面分割 → 提取屋顶面片
3. 基于法向和邻接关系聚类屋顶面片
4. 用 PointNet++ 或简单 ML 做类型分类
5. 提取屋顶轮廓线 → 输出矢量结果
6. 可视化展示

**产出**
- GitHub 仓库（README + 效果图 + 代码）
- 一段 3 分钟演示视频
- 一篇技术博客（可以发在博客园/知乎/个人网站）

### 备选项目：城市场景语义分割 Demo
- 用预训练 PointNet++ 在 S3DIS 上做推理
- 可视化语义结果，分析不同类型建筑的分类效果
- 思考规划知识如何改进分割结果

---

## 十、联系导师准备

### 邮件草稿要点
- 自我介绍：城乡规划本科 + 408统考排名第二
- 为什么选王老师：摄影测量 + 三维重建 + 城市规划背景的契合
- 已经准备的内容：
  - 读过 Building3D / PBWR / EdgeDiff 论文
  - 暑假做的 Capstone 项目
  - 正在打的基础（线代/概率/点云/PyTorch）
- 附件：简历 PDF + 项目 GitHub 链接
- 备注：表达「空间理解 + 计算能力」的独特定位

### 面试准备
- [ ] 能解释 PointNet 为什么用 Max Pooling
- [ ] 能说清楚线代中 SVD 的含义和应用
- [ ] 能讲出摄影测量和计算机视觉的关系
- [ ] 能阐述自己对「城市 AI」的理解和兴趣来源

---

## 十一、推荐资源清单

### 书
| 书 | 用途 |
|----|------|
| Gilbert Strang《Introduction to Linear Algebra》 | 线代 |
| Bertsekas《Introduction to Probability》 | 概率 |
| Boyd《Convex Optimization》 | 优化（前7章） |
| 张祖勋《数字摄影测量学》 | 摄影测量 |
| Hartley《Multiple View Geometry》 | 多视图几何（前6章） |
| 《动手学深度学习》(d2l.ai) | PyTorch + DL |

### 网课
| 课 | 链接 |
|----|------|
| MIT 18.06 线代 | YouTube MIT OpenCourseWare |
| 吴恩达 Machine Learning | Coursera |
| 李宏毅 ML/DL | YouTube / B站 |
| fast.ai | course.fast.ai |

### 论文（王老师）
| 论文 | 会议/期刊 |
|------|----------|
| Building3D | ICCV 2023 |
| PBWR | CVPR 2024 |
| EdgeDiff | CVPR 2025 |
| Plane Segmentation | TPAMI |

---

> 📌 本文档格式：Markdown，可导入 XMind / MindNode / Markmap 等思维导图工具  
> 📅 创建日期：2026.06.12  
> 🎯 制定者：汤毕阳 / Claude

