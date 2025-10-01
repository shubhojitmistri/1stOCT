from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random
from pathlib import Path

# Canvas settings
W, H = 1200, 1200
bg = (0, 0, 0, 0)  # transparent
img = Image.new("RGBA", (W, H), bg)
draw = ImageDraw.Draw(img)

# Load a monospaced font
def load_font(size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeMono.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except:
            continue
    return ImageFont.load_default()

base_font_size = 18
font = load_font(base_font_size)

# Create irregular "blob" mask
mask = Image.new("L", (W, H), 0)
m = ImageDraw.Draw(mask)
random.seed(7)
np.random.seed(7)
for _ in range(24):
    cx = int(np.random.normal(W/2, W*0.15))
    cy = int(np.random.normal(H/2, H*0.15))
    rx = random.randint(int(W*0.12), int(W*0.22))
    ry = random.randint(int(H*0.18), int(H*0.28))
    bbox = [cx-rx, cy-ry, cx+rx, cy+ry]
    intensity = random.randint(140, 255)
    m.ellipse(bbox, fill=intensity)

mask = mask.filter(ImageFilter.GaussianBlur(radius=36))

# Streak base
streaks = Image.new("RGBA", (W, H), (0,0,0,0))
sd = ImageDraw.Draw(streaks)
for x in range(80, W-80, 6):
    col_alpha = int(30 + 120*random.random())
    if col_alpha < 20:
        continue
    for y in range(60, H-60, 4):
        if mask.getpixel((x, y)) > 50 and random.random() < 0.22:
            length = random.randint(16, 90)
            sd.line([(x, y), (x, y+length)], fill=(0, 255, 70, col_alpha//2), width=1)

streaks = streaks.filter(ImageFilter.GaussianBlur(radius=1.4))
img = Image.alpha_composite(img, streaks)
draw = ImageDraw.Draw(img)

# Glyphs
glyphs = "01|¦-+/*=<>[]{}()#$%^&·'`~abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ"

# Render green code
column_step = 14
line_step = int(base_font_size * 1.1)
for xi, x in enumerate(range(60, W-60, column_step)):
    x_jitter = random.randint(-2, 2)
    lean = random.uniform(-0.25, 0.25)
    brightness = random.uniform(0.7, 1.0)
    for yi, y0 in enumerate(range(60, H-60, line_step)):
        y = y0 + int(lean * (x - W/2) * 0.02) + random.randint(-1, 1)
        if y < 0 or y >= H:
            continue
        mval = mask.getpixel((min(max(x,0),W-1), min(max(y,0),H-1)))
        if mval < 25:
            continue
        if random.random() > (mval/255.0):
            continue
        ch = random.choice(glyphs)
        fsz = base_font_size + random.randint(-3, 4)
        f = load_font(fsz)
        alpha = int(40 + 185 * (mval/255.0) * brightness)
        green = int(160 + 95 * (mval/255.0))
        if random.random() < 0.02:
            alpha = min(255, int(alpha*1.2))
            green = 255
        draw.text((x + x_jitter, y), ch, font=f, fill=(0, green, 80, alpha))

# Outer glow
glow = img.copy().filter(ImageFilter.GaussianBlur(radius=10))
gpix = glow.load()
for y in range(H):
    for x in range(W):
        r,g,b,a = gpix[x,y]
        if a > 0:
            gpix[x,y] = (0, min(255, int(g*1.05)), 40, int(a*0.9))

final = Image.alpha_composite(glow, img)

# Crop + resize
bbox = final.getbbox()
if bbox:
    final = final.crop(bbox).resize((900, 900), Image.Resampling.LANCZOS)

# Save
out_path = Path("green_binary_cascade.png")
final.save(out_path, format="PNG")
print("Image saved to", out_path)

# Show the image in default viewer
final.show()
