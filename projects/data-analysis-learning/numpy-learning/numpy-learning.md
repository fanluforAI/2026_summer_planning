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
