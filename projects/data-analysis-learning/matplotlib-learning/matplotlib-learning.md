# AI/CV 学生需要学 Matplotlib 吗？

## 一句话结论

**必须会基本操作——画 loss 曲线、可视化预测结果、展示论文配图。**

实验跑完了，你得让人看见效果。Matplotlib 就是那个"看见"的工具。

---

## AI/CV 方向的 Matplotlib 应用场景

| 频率 | 场景 | 典型操作 |
|------|------|---------|
| 🔥 高 | **画训练曲线** | loss/acc 随 epoch 变化 |
| 🔥 高 | **展示预测结果** | 原图 vs 预测 mask 并列对比 |
| ⚡ 中 | **数据分布检查** | 直方图看数据是否平衡 |
| ⚡ 中 | **论文配图** | 对比实验柱状图、消融实验 |
| 📉 低 | **交互式探索** | 结合 Jupyter Notebook 边看边调 |

---

## 跟其他库的关系

| 库 | Matplotlib → |
|------|------|
| NumPy | `plt.plot(x, y)` — x, y 都是 NumPy 数组 |
| Pandas | `df.plot()` — Pandas 内部还是调 Matplotlib |
| Seaborn | Matplotlib 的高级封装，更漂亮 |
| OpenCV | `cv2.imshow()` vs `plt.imshow(img)` |

> Matplotlib 是 Python 可视化的"底层语言"——其他库都是它外面穿的衣服。

---

## Matplotlib 学习内容全景图

### 🟢 生存级（~8 个）

| 操作 | 说明 |
|------|------|
| `plt.plot(x, y)` | 折线图（loss 曲线） |
| `plt.imshow(img)` | 显示图像 |
| `plt.subplot()` | 多图并列 |
| `plt.title()`, `plt.xlabel()` | 标题和轴标签 |
| `plt.legend()` | 图例 |
| `plt.savefig()` | 保存图片 |
| `plt.figure(figsize=...)` | 设置画布大小 |
| `plt.show()` | 显示出来 |

### 🟡 效率级（~6 个）

| 操作 | 说明 |
|------|------|
| `plt.bar()` | 柱状图（对比实验） |
| `plt.hist()` | 直方图（数据分布） |
| `plt.colorbar()` | 色条（看热力图/特征图） |
| `plt.tight_layout()` | 自动调间距——救命功能 |
| `plt.rcParams` | 全局字体/字号设置 |
| `plt.subplots(n, m)` | 批量创建子图 |

### 🔵 进阶级（用到再学）

| 操作 | 说明 |
|------|------|
| `matplotlib.animation` | 让训练过程动起来 |
| 3D 绘图 | `from mpl_toolkits.mplot3d import ...` — 显示三维点云 |
| 中文支持 | `plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']` |

```
生存级  8 个  ← 画出能看的图
效率级  6 个  ← 画出好看的图
进阶级  3 个  ← 画出让导师满意的图
────────────────
约 17 个核心操作
```

---

## 建议学习路线（约 3-4 天）

| 天数 | 内容 | 练手 |
|------|------|------|
| 第 1 天 | `plot` + `title` + `xlabel` + `legend` + `savefig` | 画一条 loss 曲线 |
| 第 2 天 | `subplot` + `imshow` + `colorbar` | 原图 / GT / 预测 三图并列 |
| 第 3 天 | `bar` + `hist` + `tight_layout` | 做一张实验对比图 |
| 之后 | 论文需要时再美化 |

### 推荐资源

- **Matplotlib 官方 Gallery** — 挑一个像你要的，复制代码改改
- **Seaborn 官方 Tutorial** — 如果觉得 Matplotlib 太底层，Seaborn 一行出图

---

## 核心心态

> Matplotlib 不需要背——先画出来，再慢慢美化。80% 的图只用 20% 的 API。

训练跑半天，看不到曲线等于白跑。第一件事永远是 `plt.plot(losses)`。

---

## 📖 API 速查

### `plt.plot()` — 折线图

```python
import matplotlib.pyplot as plt

epochs = range(1, 51)
loss = [0.8, 0.5, 0.3, ...]          # 50 个 epoch 的 loss
plt.plot(epochs, loss, label='train loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Curve')
plt.legend()
plt.savefig('loss.png', dpi=150)
plt.show()
```

### `plt.imshow()` — 显示图像

```python
plt.imshow(img)                 # RGB 图像
plt.imshow(img, cmap='gray')    # 灰度图
plt.axis('off')                 # 隐藏坐标轴
plt.colorbar()                  # 加色条
```

> CV 里最常用的组合：`subplot(1,3,1)` + `imshow` + `title` 做对比。

### `plt.subplot()` — 多图并列

```python
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)            # 1行3列，第1个
plt.imshow(original)
plt.title('Input')
plt.subplot(1, 3, 2)
plt.imshow(ground_truth)
plt.title('Ground Truth')
plt.subplot(1, 3, 3)
plt.imshow(prediction)
plt.title('Prediction')
plt.tight_layout()              # 魔法——自动调间距
plt.savefig('comparison.png')
```

> `tight_layout()` 是救命的——子图标签重叠时一行搞定。💡
