import os
from PIL import Image, ImageFilter

gen_path = r'C:\Users\prans\.gemini\antigravity-ide\brain\4f75fcaa-a6aa-4b88-ac9e-c54d40470ab6\hands_no_moon_1793304590844.jpg'
out_path = r'assets\shiva_parvati_vivah_hands.png'

img = Image.open(gen_path).convert('RGB')
w, h = img.size

# We can find the background by checking pixels that are connected to the boundary and near white
# Let's do a flood fill mask from all 4 corners / borders
from collections import deque

visited = bytearray(w * h)
queue = deque()

# Seed borders
for x in range(w):
    queue.append((x, 0))
    queue.append((x, h - 1))
for y in range(h):
    queue.append((0, y))
    queue.append((w - 1, y))

# Background threshold: high brightness and low color saturation
pixels = img.load()

def is_bg(r, g, b):
    # Pure white or off-white background
    # Background in this image is > 240 in all channels and max diff < 15
    return r > 240 and g > 240 and b > 240 and abs(r - g) < 18 and abs(r - b) < 18 and abs(g - b) < 18

for x, y in list(queue):
    idx = y * w + x
    r, g, b = pixels[x, y]
    if is_bg(r, g, b):
        visited[idx] = 1
    else:
        visited[idx] = 0

# BFS
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    cx, cy = queue.popleft()
    c_idx = cy * w + cx
    if visited[c_idx] != 1:
        continue
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < w and 0 <= ny < h:
            n_idx = ny * w + nx
            if visited[n_idx] == 0:
                r, g, b = pixels[nx, ny]
                if is_bg(r, g, b):
                    visited[n_idx] = 1
                    queue.append((nx, ny))

# Now create an alpha mask
# 0 for background, 255 for foreground
alpha_data = bytearray(w * h)
for i in range(w * h):
    alpha_data[i] = 0 if visited[i] == 1 else 255

mask = Image.frombytes('L', (w, h), bytes(alpha_data))

# Smooth the mask edge slightly to avoid harsh pixelation
mask_blurred = mask.filter(ImageFilter.GaussianBlur(radius=0.8))

# Assemble RGBA
rgba = img.convert('RGBA')
rgba.putalpha(mask_blurred)

# Let's crop to content bounding box with a small margin, similar to orig
bbox = rgba.getbbox()
print('Bounding box:', bbox)

rgba.save(out_path, 'PNG')
print('Saved to', out_path)
