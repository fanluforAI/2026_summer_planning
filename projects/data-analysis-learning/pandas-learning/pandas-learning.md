# AI/CV 学生需要学 Pandas 吗？

## 一句话结论

**比 NumPy 重要性低，但处理表格数据时省一半代码。**

图像训练很少直接用 Pandas，但**分析实验结果、整理数据集标注、统计指标**时它是神器。

---

## AI/CV 方向的 Pandas 应用场景

| 频率 | 场景 | 典型操作 |
|------|------|---------|
| 🔥 高 | **看训练日志** | `pd.read_csv("train_log.csv")` → 画 loss 曲线 |
| 🔥 高 | **统计分类指标** | `.groupby("label").count()` — 每类多少张？ |
| ⚡ 中 | **整理标注数据** | 合并 `images.csv` + `labels.csv` |
| ⚡ 中 | **实验对比** | 多个模型的 acc/loss 放入 DataFrame 对比 |
| 📉 低 | **导出提交结果** | `df.to_csv("submission.csv")` — Kaggle 交作业 |

---

## 跟 NumPy 的边界

| | NumPy | Pandas |
|------|-------|--------|
| 核心对象 | `ndarray` | `DataFrame` / `Series` |
| 数据形态 | 纯数值矩阵 | 表格（有列名 + 多种类型） |
| AI 使用频率 | 每天 | 每周几次 |
| 什么时候用 | 读图、矩阵运算 | 分析结果、处理 CSV |

> 一句话：NumPy 管"图像变成的数字"，Pandas 管"实验记录变成的表"。

---

## Pandas 学习内容全景图

### 🟢 生存级（~6 个）

| 操作 | 说明 |
|------|------|
| `pd.read_csv()` | 读 CSV 文件 |
| `df.head()` | 看前几行 |
| `df.info()` | 看列名、类型、缺失值 |
| `df.describe()` | 统计摘要（均值、方差、四分位） |
| `df["col"]` | 取一列 |
| `df.to_csv()` | 保存 |

### 🟡 效率级（~6 个）

| 操作 | 说明 |
|------|------|
| `df.groupby()` | 分组统计 |
| `df.merge()` | 合并两个表（≈ SQL JOIN） |
| `df.query()` / `df[df['acc'] > 0.9]` | 条件筛选 |
| `df.sort_values()` | 按某列排序 |
| `df.isnull().sum()` | 查缺失值 |
| `df.apply()` | 对每行/列用自定义函数 |

### 🔵 进阶级（用到再学）

| 操作 | 说明 |
|------|------|
| `pd.pivot_table()` | 透视表 |
| `df.plot()` | 内置绑 Matplotlib |
| `pd.concat()` | 纵向/横向拼接 DataFrame |
| `df.to_excel()` / `df.to_json()` | 多格式导出 |

```
生存级  6 个  ← 读数据、看一眼、存结果，够用了
效率级  6 个  ← 分析实验结果
进阶级  4 个  ← 报表级输出
────────────────
约 16 个核心操作
```

---

## 建议学习路线（约 3-4 天）

| 天数 | 内容 |
|------|------|
| 第 1 天 | `read_csv` + `head` + `info` + `describe` — 先会"看" |
| 第 2 天 | 索引 `df["col"]` + `iloc`/`loc` + 条件筛选 |
| 第 3 天 | `groupby` + `merge` — 这两个搞定就覆盖 80% 分析需求 |
| 之后 | 用到再查 |

### 推荐资源

- **Pandas 官方 Getting Started** — 10 分钟教程
- **Kaggle Pandas 微课程** — 免费，交互式，6 小时

---

## 核心心态

> Pandas 是你做实验的"账本"——训练跑完，把结果丢进去算，一目了然。

不用像 NumPy 那样精炼到毫秒级——Pandas 追求的是**代码可读**，不是性能。

---

## 📖 API 速查

### `pd.read_csv()` — 读 CSV

```python
import pandas as pd

df = pd.read_csv("train_log.csv")    # 读进来就是 DataFrame
df.head()                            # 看前 5 行
df.info()                            # 看列名、类型、有无缺失
```

### `df.describe()` — 统计摘要

```python
df.describe()
# count | mean | std | min | 25% | 50% | 75% | max
# 一眼看出 acc 的均值、波动范围
```

### `df["col"]` — 取列

```python
df["loss"]                # 取 loss 列 → Series
df["acc"].mean()          # 平均准确率
df[["loss", "acc"]]       # 取多列 → DataFrame
```

### `df.groupby()` — 分组统计

```python
df.groupby("label").count()           # 每个类别的样本数
df.groupby("epoch")["loss"].mean()    # 每个 epoch 的平均 loss
```

> AI 学生最常用的俩 groupby：按类统计样本量、按 epoch 统计指标。
