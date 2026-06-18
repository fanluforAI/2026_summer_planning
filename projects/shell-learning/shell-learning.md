# AI 学生需要学 Shell 吗？

## 一句话结论

**不需要精通，但至少要会"生存级 Shell"。**

你不需要成为厨师，但你得会用微波炉和电饭煲。Shell 之于 AI 学生，就是那个"电饭煲"——不必做 Shell 高手，但基本操作绕不开。

---

## AI 学生的 Shell 应用场景（按频率排序）

### 🔥 高频场景（几乎每天都用）

| 场景 | 典型命令 | 为什么必须会 |
|------|---------|------------|
| **远程服务器跑实验** | `ssh`, `scp` | 模型训练不可能在你笔记本上跑，你一定得连 GPU 服务器 |
| **Python 环境管理** | `conda activate`, `pip install` | 每个项目环境不同，不会这个寸步难行 |
| **Git 版本控制** | `git add/commit/push/pull` | 代码协作、论文复现、交作业 |
| **文件浏览/操作** | `cd`, `ls`, `mv`, `rm`, `cat` | 服务器没有图形界面，只能靠命令行 |

### ⚡ 中频场景（每周几次）

| 场景 | 你会在干嘛 |
|------|-----------|
| **查看 GPU 状态** | `nvidia-smi` — 看显卡有没有被别人占满 |
| **后台跑训练** | `nohup python train.py &` 或 `tmux`/`screen` — 关掉终端训练不中断 |
| **监控资源** | `htop`, `df -h` — 看内存/硬盘有没有炸 |
| **批量处理数据** | `find`, `xargs`, 简单 `for` 循环 — 你有几万张图片要改名/分类的时候 |
| **看训练日志** | `tail -f`, `grep` — 实时看 loss 下降、找报错信息 |

### 📉 低频但救命

| 场景 | 例子 |
|------|------|
| **写个自动化脚本** | 每天自动备份实验 checkpoint 到云盘 |
| **Docker 部署** | 把模型打包成 Docker 镜像给导师/demo 用 |
| **调试环境** | `which python`、`echo $PATH` — 排查"明明装了为啥跑不了" |

---

## 针对 CV + 三维重建方向的典型一天

```bash
ssh student@lab-gpu-01          # 连上实验室服务器
conda activate nerf             # 切到 NeRF 环境
nvidia-smi                      # 看看 GPU 空不空
tmux new -s training            # 开个不会断的终端窗口
python train_nerf.py --epoch 100 | tee log.txt   # 跑训练 + 记日志
tail -f log.txt | grep "loss"   # 实时盯着 loss 下降
scp checkpoint.pth me@my-pc:~/  # 把模型下载回自己电脑
```

> 现在在 Grasshopper 里拖电池，以后在 Shell 里敲命令——本质都是"操控工具"，思维模式其实很像。

---

## Shell 学习内容全景图

> AI/CV 方向实际需要掌握的内容，分三个层级。

### 🟢 生存级（必学，~15 个）—— 不会就没法干活

| 类别 | 命令 | 数量 |
|------|------|------|
| 文件浏览 | `ls` `cd` `pwd` `cat` `less` | 5 |
| 文件操作 | `cp` `mv` `rm` `mkdir` `touch` | 5 |
| 权限相关 | `sudo` `chmod` `chown` | 3 |
| 查看内容 | `head` `tail` `wc` | 3 |

### 🟡 效率级（该学，~12 个）—— 会了效率翻倍

| 类别 | 命令 | 数量 |
|------|------|------|
| 搜索过滤 | `grep` `find` `which` | 3 |
| 管道重定向 | `\|` `>` `>>` `<` | 4 |
| 远程连接 | `ssh` `scp` | 2 |
| 进程管理 | `ps` `kill` `htop` | 3 |

### 🔵 进阶级（选学，~8 个）—— 锦上添花

| 类别 | 命令 | 数量 |
|------|------|------|
| 文本处理 | `awk` `sed` `sort` `uniq` | 4 |
| 终端复用 | `tmux` 或 `screen` | 1 |
| 环境变量 | `export` `echo $PATH` | 2 |
| 压缩打包 | `tar` `zip` | 2 |

```
生存级 15 个  ← 刚入门，必须拿下
效率级 12 个  ← 边用边学，自然就会
进阶级  8 个  ← 用到再查，不急
────────────────
总计约 35 个命令/概念
```

| 阶段 | 内容 | 时间 |
|------|------|------|
| 生存级 15 个 | 每天 2-3 个，边敲边记 | **1 周** |
| 效率级 12 个 | 做项目时自然用到 | **2-3 周** |
| 进阶级 8 个 | 需要时现查 | **终身** |

> **认真学的话，一个月足够从零到熟练。**

---

## 建议学习路线（约 2 周）

| 天数 | 内容 |
|------|------|
| 第 1 天 | `cd`, `ls`, `pwd`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `less` |
| 第 2-3 天 | `ssh` 远程连接、`scp` 传文件、`conda` 环境管理 |
| 第 4-5 天 | `git` 基本工作流（clone → add → commit → push） |
| 第 6-7 天 | `tmux`、`nohup`（后台跑任务不中断） |
| 第 8-10 天 | `grep`、`tail`、`管道 \|`、简单 `for` 循环 |
| 之后 | 用到什么学什么，不要提前啃 |

### 推荐资源

- **MIT Missing Semester** — 免费的 Shell 生存技能课，6 节课覆盖上面全部
- 不需要买书，轻装上阵

---

## 核心心态

> Shell 就像数学——你不需要当数学家，但不能不会算数。

对跨考选手来说，早点熟悉服务器操作，绝对是竞争优势。💪

---

## 📖 命令速查

> 学一个记一个，慢慢攒。

### `ls` — list（列出目录内容）

全称：**l**i**s**t segments

```bash
ls                  # 列出当前目录有哪些文件和文件夹
ls /opt/anaconda3   # 列出指定路径的内容
ls -l               # 详细信息：权限、大小、修改日期
ls -a               # 包括隐藏文件（.开头的那种）
ls -la              # 上面两者的合体，最常用
```

| 常用选项 | 含义 |
|----------|------|
| `-l` | long format，显示权限/大小/时间 |
| `-a` | all，显示隐藏文件 |
| `-h` | human-readable，文件大小用 K/M/G 显示 |
| `-t` | 按修改时间排序，最新的在最上面 |
| `-r` | reverse，倒序排列 |

### `pwd` — print working directory（打印当前目录）

全称：**p**rint **w**orking **d**irectory

```bash
pwd                 # 显示你现在在哪个目录里
# 👆 例：/Users/fan/projects/shell-learning
```

> 最单纯的命令之一——迷路的时候敲一下，立刻知道自己在哪 📍。不需要任何参数。

### `cd` — change directory（切换目录）

全称：**c**hange **d**irectory

```bash
cd                      # 回到 home 目录
cd /opt/anaconda3       # 切到指定绝对路径
cd ..                   # 回到上一级目录
cd -                    # 回到上一次所在的目录（反复横跳神器🔥）
cd ~/projects           # ~ = home 目录的简写
```

> Shell 里使用频率最高的命令，没有之一。`cd -` 尤其实用——在两个目录之间来回切换。

### `bash` — Bourne Again SHell

- **Bourne**：致敬 Unix 原始 Shell 作者 Stephen Bourne（他的 Shell 叫 `sh`）
- **Again**："再来一次"，暗示它是 `sh` 的升级重生版
- **Shell**：操作系统外面的那层"壳"，接收你的命令传递给内核

| 名称 | 全称 | 关系 |
|------|------|------|
| `sh` | Bourne Shell | 祖师爷 |
| `bash` | Bourne Again SHell | sh 的增强版 |
| `zsh` | Z Shell | bash 的再增强版（macOS 默认） |

### `sudo` — SuperUser DO（以管理员身份执行）

```bash
sudo chmod +x /opt/anaconda3/bin/*   # 用管理员权限改权限
sudo apt install python               # 用管理员权限装软件
```

> 相当于 Windows 的"以管理员身份运行"。第一次输入 `sudo` 需要输密码。

### `join` — 合并文件（按共同字段）

```bash
# 文件 A：学号 + 姓名        文件 B：学号 + 成绩
join file_A.txt file_B.txt
# 👆 按第一列合并 → "学号 姓名 成绩"
```

> 类似数据库里的 JOIN，把两个文件按相同的 key 合并成一行。

### `head` — 查看文件开头（前几行）

```bash
head file.txt        # 默认显示前 10 行
head -n 5 file.txt   # -n 指定行数（-n = number of lines）
head -5 file.txt     # 简写，等同 -n 5
```

### `tail` — 查看文件末尾（最后几行）

```bash
tail file.txt              # 默认显示最后 10 行
tail -n 20 file.txt        # 最后 20 行
tail -f train.log          # -f = follow，实时追踪（看训练日志的神器🔥）
```

> `head` + `tail` 是一对，一个看头一个看尾。`tail -f` 对 AI 学生最实用——盯着 loss 下降就靠它。

### `cat` — concatenate（连接并显示文件内容）

全称：con**cat**enate

```bash
cat file.txt            # 把文件内容全部打印到终端
cat a.txt b.txt         # 连接多个文件并输出
cat -n file.txt         # 带行号显示（-n = number）
```

> 📏 适合看短文件。文件长了请用 `less`——`cat` 会刷屏。

### `less` — 分页查看文件

```bash
less train.log          # 打开文件，上下翻页
# less 内的快捷键：
#   Space / f → 下翻一页    b → 上翻一页
#   /keyword  → 向下搜索      ?keyword → 向上搜索
#   g → 跳到开头              G → 跳到末尾
#   q → 退出
```

> 💡 "less is more" — 确实有个老命令叫 `more`，但 `less` 更强：能往回翻、能搜索高亮。

### `wc` — word count（统计行数/单词数/字节数）

全称：**w**ord **c**ount

```bash
wc file.txt             # 三列输出：行数  单词数  字节数
wc -l file.txt          # 只统计行数（🔥 最常用）
wc -w file.txt          # 只统计单词数
wc -c file.txt          # 只统计字节数
```

| 选项 | 含义 | AI 学生典型场景 |
|------|------|---------------|
| `-l` | lines | `wc -l train.json` — 训练集有多少条？ |
| `-w` | words | 平时少用 |
| `-c` | chars | 看文件大小（比 `ls -l` 更精确） |

```bash
wc -l data/*.txt        # 每个 txt 文件各有多少行
ls data/ | wc -l        # 数据集目录里有多少文件？（管道组合技）
```

### `chmod` — change mode（修改文件权限）

全称：**ch**ange **mod**e

```bash
chmod +x script.sh    # 给文件加上执行权限（最常用）
chmod u+x file.sh     # 所有者(u)加执行权限
chmod g-w file.sh     # 同组(g)去掉写权限
chmod 755 file.sh     # 数字方式：rwxr-xr-x
```

| 谁来操作 | 代号 | 权限类型 | 代号 |
|----------|------|----------|------|
| 文件所有者 | `u`（user） | 读 | `r`（read） |
| 同组用户 | `g`（group） | 写 | `w`（write） |
| 其他人 | `o`（other） | 执行 | `x`（execute） |
| 所有人 | `a`（all） | — | — |

> 之前 `permission denied` 的 `/opt/anaconda3/bin`，就是缺执行权限，`sudo chmod +x` 能修好。

### `chown` — change owner（修改文件所有者）

全称：**ch**ange **own**er

```bash
chown user file.txt             # 改所有者
chown user:group file.txt       # 同时改所有者和组
chown -R user:group folder/     # -R 递归修改整个目录
```

> 🔐 常配 `sudo` 服用：`sudo chown fan /opt/anaconda3/bin/*` — `chmod` 管权限，`chown` 管归属，两把钥匙。

### `cp` — copy（复制文件/目录）

```bash
cp file.txt backup.txt        # 复制单个文件
cp -r projects/ backup/       # -r 递归复制整个目录（必须加 -r）
cp -r folder_a/ folder_b/     # 目录复制
```

> ⚠️ 复制目录不加 `-r` 会报错：`cp: xxx is a directory`

### `mv` — move（移动/重命名）

```bash
mv file.txt ../               # 移动到上级目录
mv old_name.txt new_name.txt  # 重命名（移到同目录但不同名）
mv folder/ /tmp/              # 移动整个目录（不需要 -r）
```

### `rm` — remove（删除）

```bash
rm file.txt                   # 删除文件
rm -r folder/                 # 删除目录（-r 递归）
rm -rf folder/                # 强制删除，不确认（⚠️ 危险，不可恢复）
```

> ⚠️ macOS 没有"回收站"，`rm` 删除的东西找不回来，慎用。

### `mkdir` — make directory（创建目录）

```bash
mkdir my_project              # 创建单个目录
mkdir -p a/b/c/d              # -p 级联创建（父目录不存在时自动创建）
```

### `touch` — 创建空文件 / 更新时间戳

```bash
touch new_file.py       # 创建空文件（最常用）
touch .gitkeep          # 让空目录能被 git 跟踪
touch -a file.txt       # 只更新访问时间（-a = access time）
```

> `mkdir` 建目录，`touch` 建文件——一对搭档。`__init__.py`、`.gitkeep`、`.gitignore` 都是 `touch` 出来的。

### `tree` — 树形显示目录结构

不是缩写，名字就是"树"的意思——把目录结构像树枝一样画出来 🌳

```bash
# macOS 不自带，需要先装：brew install tree
tree                    # 显示当前目录的完整树形结构
tree -L 2               # 只显示 2 层深度（-L = Level）
tree -d                 # 只显示目录，不显示文件（-d = directories only）
tree -a                 # 显示隐藏文件（-a = all）
tree -I "node_modules"  # 忽略指定目录（-I = Ignore，支持通配符）
tree -h                 # 显示文件大小（-h = human-readable）
tree --du -h            # 显示每个目录的总占用空间
```

| 常用选项 | 含义 |
|----------|------|
| `-L <n>` | Level，限定深度为 n 层 |
| `-d` | directories only，只看目录结构 |
| `-a` | all，包括隐藏文件 |
| `-I <pattern>` | Ignore，排除匹配的文件/目录 |
| `-h` | human-readable，显示文件大小 |
| `--du` | disk usage，统计每个目录的磁盘占用 |

> 💡 **不用装的平替**：`find . -maxdepth 2 \| sort` 或 `ls -R`（格式不同但也能看结构）
