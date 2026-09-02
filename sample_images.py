"""
Generates synthetic leaf images with authentic visual disease patterns
(chlorosis, concentric rings, pustules, necrotic spots) for offline / 1-click testing.
"""
import io
import base64
from PIL import Image, ImageDraw, ImageFilter
import math
import random

def generate_sample_leaf_image(disease_type="tomato_early_blight"):
    """
    Renders an illustrated leaf with disease symptoms and returns as base64 PNG.
    """
    img = Image.new("RGBA", (500, 500), (245, 248, 245, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw background farm vignette
    draw.rectangle([0, 0, 500, 500], fill=(240, 245, 240, 255))
    
    # Draw leaf stalk / petiole
    draw.line([(250, 480), (250, 260)], fill=(70, 120, 50), width=10)
    
    # Base Leaf Color
    leaf_color = (68, 148, 62) if disease_type != "wheat_yellow_rust" else (90, 160, 60)
    if disease_type == "healthy_crop":
        leaf_color = (46, 160, 55)
        
    # Draw Leaf Contour (Elliptical / Ovate shape)
    if "wheat" in disease_type:
        # Long blade leaf
        draw.polygon([(250, 40), (290, 200), (280, 420), (250, 460), (220, 420), (210, 200)], fill=leaf_color)
        draw.line([(250, 460), (250, 60)], fill=(50, 120, 40), width=4)
        for y in range(80, 440, 18):
            draw.line([(250, y), (275, y - 10)], fill=(60, 130, 45), width=2)
            draw.line([(250, y), (225, y - 10)], fill=(60, 130, 45), width=2)
    elif "groundnut" in disease_type:
        # 4-leaflet clover-like groundnut leaves
        for offset_x, offset_y in [(-60, 160), (60, 160), (-70, 270), (70, 270)]:
            draw.ellipse([250 + offset_x - 45, offset_y - 65, 250 + offset_x + 45, offset_y + 65], fill=(55, 140, 50))
    else:
        # Standard Broad leaf
        leaf_pts = [
            (250, 50), (330, 130), (380, 220), (370, 320), (320, 400),
            (250, 440), (180, 400), (130, 320), (120, 220), (170, 130)
        ]
        draw.polygon(leaf_pts, fill=leaf_color)
        draw.line([(250, 440), (250, 70)], fill=(45, 110, 40), width=6)
        for y, offset in [(140, 65), (210, 95), (280, 90), (350, 60)]:
            draw.line([(250, y), (250 + offset, y - 30)], fill=(45, 110, 40), width=3)
            draw.line([(250, y), (250 - offset, y - 30)], fill=(45, 110, 40), width=3)

    # Add disease symptoms
    if disease_type == "tomato_early_blight":
        spots = [(210, 180, 38), (310, 260, 48), (220, 330, 42), (280, 140, 30)]
        for x, y, r in spots:
            draw.ellipse([x - r - 8, y - r - 8, x + r + 8, y + r + 8], fill=(215, 195, 45, 180))
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(95, 55, 25))
            draw.ellipse([x - r + 8, y - r + 8, x + r - 8, y + r - 8], outline=(140, 90, 45), width=3)
            draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(55, 30, 15))

    elif disease_type in ["potato_late_blight", "tomato_late_blight"]:
        blotches = [
            [(150, 200), (220, 180), (250, 240), (190, 280), (140, 240)],
            [(300, 270), (360, 290), (350, 360), (280, 340)]
        ]
        for poly in blotches:
            draw.polygon(poly, fill=(50, 42, 35))
            for px, py in poly:
                draw.ellipse([px-4, py-4, px+4, py+4], fill=(230, 235, 230, 200))

    elif disease_type == "wheat_yellow_rust":
        for x_line in [235, 242, 258, 265]:
            for y_dot in range(90, 400, 8):
                if random.random() > 0.15:
                    draw.rectangle([x_line - 2, y_dot - 3, x_line + 2, y_dot + 3], fill=(245, 195, 20))

    elif disease_type == "rice_blast":
        diamonds = [(250, 160, 15, 35), (230, 270, 12, 30), (270, 340, 14, 32)]
        for cx, cy, rx, ry in diamonds:
            draw.polygon([(cx, cy - ry), (cx + rx, cy), (cx, cy + ry), (cx - rx, cy)], fill=(130, 45, 35))
            draw.polygon([(cx, cy - ry + 6), (cx + rx - 4, cy), (cx, cy + ry - 6), (cx - rx + 4, cy)], fill=(180, 180, 175))

    elif disease_type == "cotton_bacterial_blight":
        spots = [(190, 200), (210, 230), (290, 210), (310, 270), (240, 310)]
        for sx, sy in spots:
            draw.polygon([(sx, sy), (sx+16, sy-8), (sx+24, sy+12), (sx+8, sy+20)], fill=(65, 35, 25))

    elif disease_type == "apple_scab":
        for ax, ay, ar in [(200, 170, 20), (290, 190, 24), (240, 280, 28), (320, 290, 18)]:
            draw.ellipse([ax-ar, ay-ar, ax+ar, ay+ar], fill=(55, 60, 35))
            draw.ellipse([ax-ar+4, ay-ar+4, ax+ar-4, ay+ar-4], fill=(35, 38, 22))

    elif disease_type == "groundnut_tikka":
        for gx, gy, gr in [(190, 160, 12), (210, 250, 16), (310, 180, 14), (320, 280, 18), (280, 220, 10)]:
            draw.ellipse([gx-gr-4, gy-gr-4, gx+gr+4, gy+gr+4], fill=(210, 190, 30))
            draw.ellipse([gx-gr, gy-gr, gx+gr, gy+gr], fill=(50, 30, 15))

    elif disease_type == "mustard_white_rust":
        for mx, my, mr in [(220, 160, 14), (280, 200, 18), (230, 270, 22), (290, 310, 16), (200, 340, 12)]:
            draw.ellipse([mx-mr, my-mr, mx+mr, my+mr], fill=(245, 248, 240))
            draw.ellipse([mx-mr+3, my-mr+3, mx+mr-3, my+mr-3], outline=(200, 210, 190), width=2)

    elif disease_type == "chilli_leaf_curl":
        for cx, cy in [(140, 200), (360, 230), (200, 370)]:
            draw.arc([cx-25, cy-25, cx+25, cy+25], start=0, end=180, fill=(185, 175, 40), width=4)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("utf-8")
