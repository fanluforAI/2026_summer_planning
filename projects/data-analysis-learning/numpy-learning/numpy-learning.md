# AI/CV 学生需要学 NumPy 吗？

## 一句话结论

**必须会。NumPy 是 Python 数据科学的"普通话"——图像就是数组，数组就是 NumPy。**

不会 NumPy，你连一张图都读不进来。

---

## AI/CV 方向的 NumPy 应用场景

### 🔥 高频场景（每天都在用）

| 场景 | 典型操作 | 为什么绕不开 |
|------|---------|------------|
| **图像即数组** | `img = np.array(pil_image)` | 所有图像库底层都是 NumPy |
| **矩阵运算** | `X @ W`, `np.dot()` | 手写网络层 / 验证 PyTorch 结果 |
| **数据预处理** | `mean = np.mean(X, axis=0)` | 归一化、标准化 |
| **维度变换** | `x.reshape(-1, 784)` | 把图像拉平成 MLP 输入 |
| **随机采样** | `np.random.randn(32, 100)` | 生成噪声、初始化权重 |

### ⚡ 中频场景

| 场景 | 典型操作 |
|------|---------|
| **SVD / 特征分解** | `np.linalg.svd(E)` — 三维重建每一步 |
| **掩码操作** | `img[mask > 0] = 255` — 分割标注 |
| **批量计算** | `np.sum((X - Y)**2, axis=1)` — 向量化加速 |
| **数据增强** | `np.fliplr(img)`, `np.rot90(img)` |

### 📉 低频但救命

| 场景 | 例子 |
|------|------|
| **性能优化** | 把 Python 循环改成 NumPy 向量化，快 100 倍 |
| **自定义 Metric** | 用 NumPy 写出论文里的评估公式 |
| **调试梯度** | 数值梯度检查：`(f(x+h)-f(x))/h` |

---

## NumPy 学习内容全景图

### 🟢 生存级（~10 个）

| 类别 | 操作 | 说明 |
|------|------|------|
| 创建 | `np.array()`, `np.zeros()`, `np.ones()` | 造数据 |
| 创建 | `np.arange()`, `np.linspace()` | 等差数列 |
| 创建 | `np.random.randn()`, `np.random.randint()` | 随机数据 |
| 属性 | `.shape`, `.dtype`, `.ndim` | 查数组信息 |
| 索引 | `x[0]`, `x[:, 1]`, `x[2:5]` | 取数据子集 |
| 变形 | `.reshape()`, `.flatten()` | 改变维度 |
| 统计 | `.mean()`, `.std()`, `.sum()`, `.max()` | 描述数据 |
| 运算 | `+`, `*`, `@`, `np.dot()` | 元素运算 / 矩阵乘 |

### 🟡 效率级（~8 个）

| 类别 | 操作 |
|------|------|
| 广播 | `broadcasting` — 不同形状数组自动对齐 |
| 轴操作 | `axis=0`, `axis=1` 的方向直觉 |
| 拼接 | `np.concatenate()`, `np.stack()` |
| 条件筛选 | `x[x > 0]`, `np.where()` |
| 排序 | `np.argsort()`, `np.argmax()` |
| 线性代数 | `np.linalg.inv()`, `np.linalg.svd()` |
| 保存加载 | `np.save()`, `np.load()`, `np.savetxt()` |
| 向量化思维 | 告别 `for` 循环 |

### 🔵 进阶级（用到再学）

| 操作 | 用在哪 |
|------|--------|
| `np.einsum()` | 爱因斯坦求和——高维张量运算的终极武器 |
| `np.stride_tricks` | 不复制内存的窗口滑动 |
| `np.ufunc` | 自定义向量化函数 |
| 内存布局 | C-order vs Fortran-order，`np.copy()` vs `view` |

```
生存级 10 个  ← 一周拿下，够做大部分数据操作
效率级  8 个  ← 边做项目边学
进阶级  4 个  ← 优化性能时再学
────────────────
约 22 个核心操作
```

---

## 建议学习路线（约 1 周）

| 天数 | 内容 | 练手 |
|------|------|------|
| 第 1 天 | 创建数组 + 属性 (.shape/.dtype) | 造各种形状的数组 |
| 第 2 天 | 索引切片 + reshape | 把图片数组切成 patch |
| 第 3 天 | 统计函数 (mean/std/sum axis) | 算数据集的 mean/std |
| 第 4 天 | 广播 (broadcasting) | 减均值除以标准差 |
| 第 5 天 | 线性代数 (dot/inv/svd) | 手写 PCA |
| 第 6-7 天 | 向量化思维 | 把 for 循环改写成 NumPy |

### 推荐资源

- **NumPy 官方 Quickstart** — 半小时读完，覆盖生存级
- **100 NumPy Exercises** — 边敲边学
- **3Blue1Brown 线性代数** — 理解矩阵运算的几何直觉

---

## 核心心态

> 图像 = `(H, W, 3)` 数组。看 NumPy 就是在看图像，看图像就是在看 NumPy。

对 CV 学生来说，NumPy 不是"第三方库"——它就是数据本身。学 NumPy 的过程，就是学"怎么把图像/点云/特征矩阵用代码表示"的过程。

---

## 📖 API 速查

> 学一个记一个，慢慢攒。PyTorch 的 API 跟 NumPy 几乎一样，学会 NumPy = 学会半个 PyTorch。

### `np.array()` — 创建数组

```python
import numpy as np

a = np.array([1, 2, 3])              # 一维数组
b = np.array([[1, 2], [3, 4]])       # 二维数组（矩阵）
c = np.array(img)                     # 图像 → 数组
```

### `np.zeros()` / `np.ones()` — 全 0 / 全 1 数组

```python
np.zeros((3, 4))      # 3×4 的全 0 矩阵
np.ones((2, 3, 4))    # 2×3×4 的全 1 张量
np.zeros_like(img)    # 跟 img 一样形状的全 0 数组
```

### `.shape` — 数组形状

```python
img.shape             # (480, 640, 3) — 高 × 宽 × 通道
weights.shape         # (784, 256)   — 输入维度 × 输出维度
```

> CV 世界里看 `.shape` 跟呼吸一样频繁——确认维度是第一步。

### `.reshape()` — 改变形状

```python
x = np.arange(784).reshape(28, 28)        # 一维 → 二维（还原图像）
img_flat = img.reshape(-1, 3)             # (H×W, 3) 把像素拉平
x = x.reshape(32, 1, 28, 28)             # batch × channel × H × W
```

> `-1` = "你自己算"，最省心的参数 💡

### ndarray 属性 — 查数组"户口"

数组创建出来，第一件事就是查属性——确认数据结构对不对。

```python
img = np.array([[1, 2, 3], [4, 5, 6]])
```

| 属性 | 示例值 | 说明 |
|------|--------|------|
| `.shape` | `(2, 3)` | 形状：2 行 × 3 列 |
| `.ndim` | `2` | 维度数（几维数组） |
| `.size` | `6` | 总元素个数 = shape 各维乘积 |
| `.dtype` | `dtype('int64')` | 元素数据类型 |
| `.itemsize` | `8` | 每个元素占多少字节 |
| `.nbytes` | `48` | 数组总共占多少字节 = size × itemsize |
| `.T` | `shape (3, 2)` | 转置矩阵（行变列，列变行） |

```python
img.shape          # (2, 3)     ← 查形状
img.ndim           # 2           ← 几维？2维=矩阵，3维=图像(H,W,C)
img.size           # 6           ← 总共多少元素
img.dtype          # int64       ← 什么类型？（uint8 for 图像常见）
img.itemsize       # 8           ← 一个元素 8 字节
img.nbytes         # 48          ← 总共占多少内存
img.T              # [[1,4],[2,5],[3,6]]  ← 转置
```

**AI/CV 最常用的三个**：

| 属性 | 为什么常说 |
|------|-----------|
| `.shape` | "这个 tensor 维度对了吗？" — 排 bug 第一步 |
| `.dtype` | `float32` vs `float64` — 影响显存和精度 |
| `.ndim` | 确保 reshape 前后维度数正确 |

> 💡 PyTorch 的 `Tensor` 属性几乎一一对应：`.shape` → `.shape`，`.dtype` → `.dtype`，`.T` → `.T`。

---

## 📦 常用函数速查（按类别）

### 一、创建数组

| 函数 | 作用 | 示例 |
|------|------|------|
| `np.array(list)` | 从列表创建 | `np.array([1, 2, 3])` |
| `np.zeros(shape)` | 全 0 数组 | `np.zeros((2, 3))` |
| `np.ones(shape)` | 全 1 数组 | `np.ones((2, 3))` |
| `np.full(shape, val)` | 填充指定值 | `np.full((2, 3), 2026)` |
| `np.empty(shape)` | 未初始化（内容随机） | `np.empty((2, 3))` |
| `np.zeros_like(arr)` | 仿形状全 0 | `np.zeros_like(img)` |
| `np.ones_like(arr)` | 仿形状全 1 | `np.ones_like(label)` |
| `np.full_like(arr, val)` | 仿形状填充值 | `np.full_like(mask, 255)` |
| `np.arange(start, stop, step)` | 等差数列（整数步长） | `np.arange(0, 10, 2)` → `[0,2,4,6,8]` |
| `np.linspace(start, stop, n)` | 等差数列（指定个数） | `np.linspace(0, 1, 5)` → `[0, .25, .5, .75, 1]` |
| `np.eye(n)` | 单位矩阵 | `np.eye(3)` → 3×3 对角线全 1 |
| `np.copy(arr)` | 深拷贝（独立副本） | `b = np.copy(a)` |

```python
# arange vs linspace
np.arange(0, 1, 0.25)       # [0.   0.25 0.5  0.75] — 给步长
np.linspace(0, 1, 5)        # [0.   0.25 0.5  0.75 1.  ] — 给个数

# like 系列 — 保持原数组 shape 不变，换内容
np.zeros_like(img)           # 创建跟图像同形状的纯黑画布
np.ones_like(mask) * 255     # 创建跟 mask 同形状的纯白填充
```

### 二、随机数

| 函数 | 作用 | 示例 |
|------|------|------|
| `np.random.seed(n)` | 固定随机种子（可复现） | `np.random.seed(42)` |
| `np.random.randn(d0, d1, ...)` | 标准正态分布 | `np.random.randn(32, 100)` |
| `np.random.randint(low, high, size)` | 随机整数 | `np.random.randint(0, 256, (224, 224, 3))` |
| `np.random.rand(d0, d1, ...)` | [0,1) 均匀分布 | `np.random.rand(3, 3)` |
| `np.random.shuffle(arr)` | 就地打乱数组 | 洗数据用 |

```python
np.random.seed(42)                     # 🔥 第一行就写，保证每次结果一样
z = np.random.randn(32, 100)           # 生成潜变量噪声（GAN / VAE）
idx = np.random.permutation(1000)      # 随机打乱索引 → 用于 batch 采样
```

### 三、统计与聚合

| 函数 | 作用 | AI/CV 场景 |
|------|------|-----------|
| `np.sum(arr, axis=?)` | 求和 | 算 L1/L2 正则项 |
| `np.mean(arr, axis=?)` | 均值 | 数据集归一化：`(X - mean) / std` |
| `np.std(arr, axis=?)` | 标准差 | 同上 |
| `np.var(arr, axis=?)` | 方差 | 判断 feature map 是否崩了 |
| `np.max(arr)` / `np.min(arr)` | 最大/最小值 | 看像素值范围 |
| `np.argmax(arr, axis=?)` | 最大值的索引 | 分类器输出 → 预测类别 🔥 |
| `np.argmin(arr, axis=?)` | 最小值的索引 | — |
| `np.median(arr)` | 中位数 | 离群值分析 |

```python
# axis 方向直觉（CV 里最常用）
X = np.random.randn(100, 784)           # 100 个样本，每样本 784 维

X.mean(axis=0)      # shape (784,) — 每个特征的均值（对样本求平均）
X.mean(axis=1)      # shape (100,) — 每个样本的均值

# 图像归一化
mean = X_train.mean(axis=0)             # 训练集每通道的均值
std  = X_train.std(axis=0)
X_norm = (X - mean) / std               # 标准化到 ~N(0,1)
```

### 四、数学运算

| 函数 | 作用 | 说明 |
|------|------|------|
| `np.add(a, b)` / `a + b` | 逐元素加 | |
| `np.subtract(a, b)` / `a - b` | 逐元素减 | |
| `np.multiply(a, b)` / `a * b` | 逐元素乘 | |
| `np.divide(a, b)` / `a / b` | 逐元素除 | |
| `np.dot(a, b)` / `a @ b` | 矩阵乘法 | 全连接层的本质 🔥 |
| `np.sqrt(arr)` | 开方 | |
| `np.exp(arr)` | e^x | Softmax 里用到 |
| `np.log(arr)` | ln(x) | Cross-Entropy Loss |
| `np.abs(arr)` | 绝对值 | L1 Loss |
| `np.clip(arr, min, max)` | 截断到区间 | 梯度裁剪，防止数值爆炸 |
| `np.power(arr, n)` / `arr ** n` | 幂次 | L2 Loss: `(pred - gt) ** 2` |

```python
# 向量化 vs 循环
for i in range(10000):                  # Python 循环 — 慢
    c[i] = a[i] + b[i]

c = a + b                               # NumPy 向量化 — 快 100 倍 🚀
```

### 五、数组操作

| 函数 | 作用 | 典型场景 |
|------|------|---------|
| `np.concatenate([a, b], axis=0)` | 沿轴拼接 | 纵向堆样本 |
| `np.stack([a, b], axis=0)` | 新轴堆叠 | 把多个图叠成 batch |
| `np.vstack([a, b])` | 垂直堆叠 | = `concatenate(axis=0)` |
| `np.hstack([a, b])` | 水平堆叠 | = `concatenate(axis=1)` |
| `np.expand_dims(arr, axis=0)` | 增加一个维度 | `(H,W)` → `(1,H,W)` 加 batch 维 |
| `np.squeeze(arr)` | 删除大小为 1 的维度 | `(1,28,28)` → `(28,28)` |
| `np.transpose(arr, axes)` | 换轴 | `(H,W,C)` → `(C,H,W)` PyTorch 格式 |
| `np.flip(arr, axis=?)` | 沿轴翻转 | `np.flip(img, 1)` = 水平翻转（数据增强） |
| `np.unique(arr)` | 去重 + 排序 | 看 label 有哪些值 |
| `np.where(cond, x, y)` | 条件筛选替换 | 语义分割上色 |

```python
# CV 三件套
img_cwh = np.transpose(img_hwc, (2, 0, 1))   # HWC → CHW（PyTorch 要的格式）
img_batch = np.expand_dims(img, axis=0)       # (H,W,3) → (1,H,W,3) 加 batch 维
img_flip = np.flip(img, axis=1)               # 水平翻转做数据增强
```

> `expand_dims` + `squeeze` 是一对：一个加维度一个减维度，处理模型输入输出时天天用。

### 六、线性代数

| 函数 | 作用 | 场景 |
|------|------|------|
| `np.linalg.norm(arr, ord=2)` | 范数（L2 默认） | 正则化、特征距离 |
| `np.linalg.inv(A)` | 矩阵求逆 | 最小二乘 |
| `np.linalg.svd(A)` | SVD 分解 | 本质矩阵/基础矩阵 |
| `np.linalg.eig(A)` | 特征值/特征向量 | PCA |

```python
U, S, Vt = np.linalg.svd(E)            # SVD → 三维重建核心操作
w, v = np.linalg.eig(C)                # 特征分解 → PCA 降维
```
