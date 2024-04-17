import matplotlib.pyplot as plt
import colorsys
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

bars_to_test = 30
def generate_colour_array(amt:int, saturation:float=0.75, lightness:float=0.75):
    color_arr = []
    step = 1/amt
    value = 0
    for i in reversed(range(amt)):
        if i != 0:
            value += step # colour value
        else:
            value = 1 # eventually the index will be 0, then we just set colour to 1!
        # first value controls colour, second value control saturation, third value controls lightness (0 - black, 1 - white)
        c = hsv2rgb(value,saturation,lightness) # generate rgb from hsv
        c = rgb_to_hex(c[0], c[1], c[2]) # generate hex from rgb
        color_arr.append(c)
    return color_arr

k = [i+1 for i in range(bars_to_test)]
v = [i+1 for i in range(bars_to_test)]

print(generate_colour_array(bars_to_test, saturation=.7, lightness=.8))

# plt.bar(k, v, color=generate_colour_array(bars_to_test, saturation=.7, lightness=.8))
# plt.show()