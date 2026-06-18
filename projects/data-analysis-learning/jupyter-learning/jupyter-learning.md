# AI/CV 学生需要学 Jupyter Notebook 吗？

## 一句话结论

**必须会用，但不必"精通"。Jupyter 是实验笔记本——写代码、看结果、记笔记三位一体。**

调试模型、可视化中间结果、写实验报告——Jupyter 把这三件事合在一页里。

---

## AI/CV 方向的 Jupyter 应用场景

| 频率 | 场景 | 为什么 Jupyter 最合适 |
|------|------|----------------------|
| 🔥 高 | **调试模型** | 改一个 cell → 跑一个 cell，不用重跑整个脚本 |
| 🔥 高 | **可视化数据** | `plt.imshow(img)` 结果直接嵌在代码下面 |
| 🔥 高 | **看中间特征图** | 把 feature map 每层画出来，肉眼确认 |
| ⚡ 中 | **写实验报告** | Markdown cell + Code cell 穿插，导出 PDF |
| ⚡ 中 | **做 PPT 配图** | 跑出图 → 右键保存 → 贴进 Keynote |
| 📉 低 | **交作业** | 老师直接跑你的 notebook 看结果 |

---

## Jupyter 学习内容全景图

### 🟢 生存级（~6 个）

| 操作 | 说明 |
|------|------|
| 启动 & 打开 | `jupyter notebook` / `jupyter lab` |
| 新建 notebook | New → Python 3 |
| 运行 cell | Shift + Enter |
| 切换 cell 类型 | Y (代码) / M (Markdown) |
| 保存 | Ctrl + S / Cmd + S |
| 关闭 & 退出 | 关浏览器 → 终端 Ctrl+C |

### 🟡 效率级（~8 个）— 全靠快捷键

| 操作 | 快捷键 | 说明 |
|------|--------|------|
| 上方插入 cell | **A** | Above，在 command mode 下 |
| 下方插入 cell | **B** | Below |
| 删除 cell | **D, D** | 连按两次 D |
| 剪切/复制/粘贴 | **X / C / V** | 跟系统快捷键习惯一致 |
| 运行并插入新 cell | **Alt + Enter** | 跑完下面自动开一个 |
| 只运行不跳转 | **Ctrl + Enter** | 跑完光标留在原地 |
| 代码补全 | **Tab** | Edit mode 下 |
| 查看函数文档 | **Shift + Tab** | 光标放在函数名上按 |

### 🔵 进阶级（用到再学）

| 操作 | 说明 |
|------|------|
| `%matplotlib inline` | 图片嵌在 notebook 里 |
| `%%time` / `%timeit` | 测代码运行时间 |
| `!pip install xxx` | 在 notebook 里执行 shell 命令 |
| Magic Commands (`%run`, `%load`) | 高级魔法 |
| Jupyter Lab 扩展 | 目录、代码折叠、变量查看器 |

```
生存级  6 个  ← 打开就能用，半天上手
效率级  8 个  ← 快捷键刻进肌肉记忆
进阶级  5 个  ← 效率进一步提升
────────────────
约 19 个核心操作
```

---

## 建议学习路线（约 2 天）

| 天数 | 内容 |
|------|------|
| 第 1 天 | 启动 → 新建 → 写 3 个 cell（代码 + Markdown 混排）→ 跑 → 保存 |
| 第 2 天 | 把快捷键打熟：A/B/DD/X/C/V/Y/M，直到不用鼠标 |
| 之后 | 把调试工作从 `.py` 脚本迁移到 notebook |

### 推荐资源

- **Jupyter 官方 Try Jupyter** — 浏览器直接体验，不用装
- **DataCamp Jupyter Tutorial** — 免费，交互式

---

## 核心心态

> Jupyter 是草稿纸，不是工程代码。想法来了快速试，跑通了再整理成 `.py` 脚本。

别在 notebook 里写大型项目——它会让你养成"从上跑到下"的坏习惯。正确用法：**探索 → 验证 → 搬进 .py**。

---

## ⌨️ Notebook 快捷键速查

> 🔥 **Command Mode**（按 Esc 进入，蓝色边框）vs **Edit Mode**（按 Enter 进入，绿色边框）

### 常用模式切换

| 快捷键 | 作用 |
|--------|------|
| **Enter** | 进入 Edit Mode（编辑当前 cell） |
| **Esc** | 回到 Command Mode |

---

### 🟢 Command Mode 快捷键（按 Esc 先）

| 快捷键 | 作用 | 记忆技巧 |
|--------|------|---------|
| **Shift + Enter** | 运行当前 cell，选中下一个 | 最常用 🔥 |
| **Ctrl + Enter** | 运行当前 cell，光标留在原地 | 原地跑 |
| **Alt + Enter** | 运行当前 cell，并在下方插入新 cell | 跑 + 建 |
| **Y** | 切换为代码 cell | **Y** = p**y**thon |
| **M** | 切换为 Markdown cell | **M** = **M**arkdown |
| **R** | 切换为 Raw cell | **R** = **R**aw |
| **1 ~ 6** | 设为对应级别标题 | 1 = h1, 2 = h2 ... |
| **A** | 在上方插入 cell | **A** = **A**bove |
| **B** | 在下方插入 cell | **B** = **B**elow |
| **D, D** | 删除当前 cell | 连按两次 D（**D**elete） |
| **X** | 剪切当前 cell | 跟系统习惯一致 |
| **C** | 复制当前 cell | **C** = **C**opy |
| **V** | 粘贴到下方 | 跟系统习惯一致 |
| **Shift + V** | 粘贴到上方 | 反向粘贴 |
| **Z** | 撤销删除 cell | **Z** = undo（跟习惯相反但好记）|
| **Shift + M** | 合并选中的 cell | **M** = **M**erge |
| **S** | 保存 | **S** = **S**ave |
| **L** | 显示/隐藏行号 | **L** = **L**ine numbers |
| **O** | 折叠/展开输出 | **O** = **O**utput |
| **Shift + O** | 切换输出滚动模式 | 长输出不再撑爆屏幕 |

### 导航（Command Mode）

| 快捷键 | 作用 |
|--------|------|
| **↑** / **K** | 选中上一个 cell |
| **↓** / **J** | 选中下一个 cell |
| **Space** | 向下滚动 |
| **Shift + Space** | 向上滚动 |

### Kernel 操作（Command Mode）

| 快捷键 | 作用 | 说明 |
|--------|------|------|
| **I, I** | 中断 Kernel | 连按两次 I — "模型训飞了，快停下！" 🛑 |
| **0, 0** | 重启 Kernel | 连按两次数字0 — 清空所有变量，从头来过 🔄 |

### 其他（Command Mode）

| 快捷键 | 作用 |
|--------|------|
| **H** | 显示/隐藏快捷键面板 |
| **Esc** / **Q** | 关闭弹窗/pager |

---

### 🟢 Edit Mode 快捷键（按 Enter 先）

| 快捷键 | 作用 | 记忆技巧 |
|--------|------|---------|
| **Tab** | 代码补全 / 缩进 | 最常用 🔥 |
| **Shift + Tab** | 显示函数文档/提示 | 光标放函数名上按 |
| **Ctrl + ]** | 向右缩进 | 右括号方向 |
| **Ctrl + [** | 向左缩进 | 左括号方向 |
| **Ctrl + A** | 全选 | 系统通用 |
| **Ctrl + Z** | 撤销 | 系统通用 |
| **Ctrl + Shift + Z** / **Ctrl + Y** | 重做 | 反撤销 |
| **Ctrl + Home** | 跳到 cell 开头 | |
| **Ctrl + End** | 跳到 cell 末尾 | |
| **Ctrl + ←** | 向左跳一个词 | |
| **Ctrl + →** | 向右跳一个词 | |
| **Ctrl + Shift + P** | 打开命令面板 | 搜任何操作 |
| **Ctrl + Shift + -** | 在光标处拆分 cell | |
| **Ctrl + S** | 保存 | |

---

### 鼠标党速查（不用记键盘也能干活）

| 操作 | 怎么做 |
|------|--------|
| 新建 cell | 点击 cell 之间的 `+` 号 |
| 删除 cell | 点 cell 左侧 → 按 Delete |
| 移动 cell | 拖拽 cell 左侧区域上下移动 |
| 切换 cell 类型 | 顶部下拉菜单选择 Code / Markdown |
| 运行 cell | 点工具栏 ▶️ 按钮 |

---

> 💡 **核心原则**：左手键盘（A/B/DD/Y/M/Shift+Enter），右手偶尔鼠标——两手配合比纯键盘快。
