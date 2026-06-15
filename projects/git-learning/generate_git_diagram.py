from PIL import Image, ImageDraw, ImageFont
import os

# Canvas: 1200 x 500
W, H = 1200, 500
img = Image.new("RGB", (W, H), "#1e1e2e")
draw = ImageDraw.Draw(img)

# Try to get a CJK font, fall back to default
font_paths = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
]
font_title = None
font_body = None
font_small = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 28)
            font_body = ImageFont.truetype(fp, 20)
            font_small = ImageFont.truetype(fp, 15)
            break
        except:
            continue

if font_title is None:
    font_title = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Colors
BG_BOX = "#313244"
BORDER_ACTIVE = "#89b4fa"
BORDER_DIM = "#45475a"
TEXT_WHITE = "#cdd6f4"
TEXT_YELLOW = "#f9e2af"
TEXT_GREEN = "#a6e3a1"
TEXT_RED = "#f38ba8"
TEXT_BLUE = "#89b4fa"
TEXT_SUB = "#6c7086"
ARROW_COLOR = "#89b4fa"
LINE_COLOR = "#585b70"

# Box positions: 4 boxes horizontally
box_y = 140
box_h = 140
box_w = 200
gap = 60
start_x = 80

boxes = [
    {"label": "工作区", "en": "Working Directory", "sub": "写代码的地方", "x": start_x},
    {"label": "暂存区", "en": "Staging Area", "sub": "git add → 装车", "x": start_x + box_w + gap},
    {"label": "本地仓库", "en": "Local Repo", "sub": "git commit → 存档", "x": start_x + (box_w + gap) * 2},
    {"label": "远程仓库", "en": "Remote (GitHub)", "sub": "git push → 上传", "x": start_x + (box_w + gap) * 3},
]

# Draw boxes
for i, box in enumerate(boxes):
    x, y = box["x"], box_y
    # Box shadow
    draw.rounded_rectangle([x + 4, y + 4, x + box_w + 4, y + box_h + 4],
                           radius=16, fill="#181825")
    # Box body
    draw.rounded_rectangle([x, y, x + box_w, y + box_h],
                           radius=16, fill=BG_BOX, outline=BORDER_ACTIVE if i < 3 else "#f9e2af", width=3)

    # Emoji icon
    icons = ["✏️", "🛒", "📸", "☁️"]
    draw.text((x + 10, y + 14), icons[i], font=font_title, fill=TEXT_WHITE)

    # Label (Chinese)
    bbox = draw.textbbox((0, 0), box["label"], font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text((x + (box_w - tw) // 2, y + 30), box["label"], font=font_title, fill=TEXT_WHITE)

    # EN subtitle
    bbox = draw.textbbox((0, 0), box["en"], font=font_body)
    tw = bbox[2] - bbox[0]
    draw.text((x + (box_w - tw) // 2, y + 68), box["en"], font=font_body, fill=TEXT_SUB)

    # Sub description
    bbox = draw.textbbox((0, 0), box["sub"], font=font_small)
    tw = bbox[2] - bbox[0]
    draw.text((x + (box_w - tw) // 2, y + 105), box["sub"], font=font_small, fill=TEXT_GREEN)

# Arrows between boxes
arrow_y = box_y + box_h // 2
for i in range(3):
    x1 = boxes[i]["x"] + box_w + 6
    x2 = boxes[i + 1]["x"] - 6
    # Arrow line
    draw.line([(x1, arrow_y), (x2, arrow_y)], fill=ARROW_COLOR, width=3)
    # Arrow head
    head = [(x2 - 12, arrow_y - 8), (x2, arrow_y), (x2 - 12, arrow_y + 8)]
    draw.polygon(head, fill=ARROW_COLOR)

    # Command label above arrow
    cmds = ["git add", "git commit", "git push"]
    bbox = draw.textbbox((0, 0), cmds[i], font=font_small)
    tw = bbox[2] - bbox[0]
    cmd_x = (x1 + x2) // 2 - tw // 2
    draw.rectangle([cmd_x - 8, arrow_y - 34, cmd_x + tw + 8, arrow_y - 8], fill="#1e1e2e")
    draw.text((cmd_x, arrow_y - 30), cmds[i], font=font_small, fill=TEXT_GREEN)

# Reverse arrows (bottom side)
rev_y = box_y + box_h + 50
rev_cmds = ["git restore", "git reset", "git pull"]
rev_colors = [TEXT_RED, TEXT_RED, TEXT_BLUE]
for i in range(3):
    x1 = boxes[i + 1]["x"] + box_w // 2
    x2 = boxes[i]["x"] + box_w // 2

    # Dashed reverse arrow
    draw.line([(x1, rev_y), (x2, rev_y)], fill=rev_colors[i], width=2)

    # Arrow head pointing left
    head = [(x2 + 10, rev_y - 7), (x2, rev_y), (x2 + 10, rev_y + 7)]
    draw.polygon(head, fill=rev_colors[i])

    # Label
    bbox = draw.textbbox((0, 0), rev_cmds[i], font=font_small)
    tw = bbox[2] - bbox[0]
    cmd_x = (x1 + x2) // 2 - tw // 2
    draw.text((cmd_x, rev_y - 24), rev_cmds[i], font=font_small, fill=rev_colors[i])

# Divider line
div_x = boxes[2]["x"] + box_w + gap // 2
draw.line([(div_x, 20), (div_x, box_y + box_h + 80)], fill=LINE_COLOR, width=2, )
draw.line([(div_x, 20), (div_x, box_y + box_h + 80)], fill="#45475a", width=1)

# Labels: Local vs Remote
draw.text((div_x - 165, 25), "💻 你的电脑", font=font_body, fill=TEXT_BLUE)
draw.text((div_x + 20, 25), "☁️ 互联网", font=font_body, fill=TEXT_YELLOW)

# Bottom note
note = "🧠 记忆口诀：写代码 → add 装车 → commit 存档 → push 上传"
bbox = draw.textbbox((0, 0), note, font=font_body)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, H - 55), note, font=font_body, fill=TEXT_YELLOW)

# Save
output_path = os.path.join(os.path.dirname(__file__), "git-workflow-diagram.png")
img.save(output_path, "PNG")
print(f"✅ Saved to {output_path}")
