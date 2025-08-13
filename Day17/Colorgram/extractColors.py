import colorgram

colors = colorgram.extract('hirst-image.jpg', 30)
rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r, g, b))

print(rgb)