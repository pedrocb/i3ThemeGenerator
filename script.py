import os
import random
import json
import colorsys

colorHue = random.randint(0,360)
testAngleBarColor = random.randint(50,310) #276
testAngleBarFontColor = random.randint(0,360)

mainColor = (colorHue,50,18)
secondaryColorOne = ((colorHue + testAngleBarColor)%360,50,30)
secondaryColorTwo = ((colorHue + testAngleBarFontColor)%360,70,30)
complementaryColor = ((colorHue + 180)%360,70,30)

def rgb_to_hexadecimal(color):
    return '%02x%02x%02x' % tuple([z * 255 for z in color])

def hsv_to_rgb(color):
    return colorsys.hsv_to_rgb(color[0]/360.0,color[1]/100.0,color[2]/100.0)

def get_color(color):
    return rgb_to_hexadecimal(hsv_to_rgb(color))


def generate_wallpaper():
    colorSaturation = 50
    os.system("python ~/wallpaper_changer/script.py " + str(colorHue) + " " + str(colorSaturation) + " ~/wallpaper_changer/1941277.png wallpaper.png")
    os.system("feh --bg-scale wallpaper.png")
    os.system("rm wallpaper.png")
    return

def generate_i3_theme():
    barBackgroundColor = secondaryColorOne
    barFontColor = (secondaryColorTwo[0],70,80)
    barSeparatorColor = (secondaryColorTwo[0],70,90)
    windowBorderColor = (mainColor[0],100,60)
    unfocusedWindowBorderColor = mainColor

    barBackgroundLine = "  backgroundBar: '\\'#{}\\'".format(get_color(barBackgroundColor))
    barFontLine = "  barFont: '\\'#{}\\'".format(get_color(barFontColor))
    barSeparatorLine = "  barSeparator: '\\'#{}\\'".format(get_color(barSeparatorColor))
    windowBorderLine = "  windowBackground: '\\'#{}\\'".format(get_color(windowBorderColor))
    unfocusedWindowBorderLine = "  unfocusedWindowBorder: '\\'#{}\\'".format(get_color(unfocusedWindowBorderColor))

    
    os.system("sed -i '/^[ \t]*backgroundBar/ c \{} ~/theme.yaml".format(barBackgroundLine))
    os.system("sed -i '/^[ \t]*barFont/ c \{} ~/theme.yaml".format(barFontLine))
    os.system("sed -i '/^[ \t]*barSeparator/ c \{} ~/theme.yaml".format(barSeparatorLine))
    os.system("sed -i '/^[ \t]*windowBackground/ c \{} ~/theme.yaml".format(windowBorderLine))
    os.system("sed -i '/^[ \t]*unfocusedWindowBorder/ c \{} ~/theme.yaml".format(unfocusedWindowBorderLine))
    
    os.system("i3-style theme.yaml  -o ~/.config/i3/config --reload")
    return

def generate_rofi_theme():
    windowBackgroundColor = secondaryColorOne
    highlightRowBackgroundColor = (secondaryColorOne[0],secondaryColorOne[1],40)
    fontColor = (secondaryColorTwo[0],50,90);
    s100b80 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,80/100.0) ])
    s0b20 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,0/100.0,10/100.0) ])
    s50b100 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,50/100.0,100/100.0) ])
    s20b100 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,20/100.0,100/100.0) ])
    color_window = "rofi.color-window: #{}, #{}, {}".format(get_color(windowBackgroundColor),get_color(windowBackgroundColor),s100b80)
    color_normal = "rofi.color-normal: #{}, #{}, #{}, #{}, #{}".format(get_color(windowBackgroundColor),get_color(fontColor),get_color(windowBackgroundColor),get_color(highlightRowBackgroundColor),get_color(fontColor))
    color_active = "rofi.color-active: #{}, {}, {}, {}, {}".format(get_color(windowBackgroundColor),s50b100,s0b20,s0b20,s20b100)

    os.system("sed -i '/color-window/ c {}' ~/.Xresources".format(color_window))
    os.system("sed -i '/color-normal/ c {}' ~/.Xresources".format(color_normal))
    os.system("sed -i '/color-active/ c {}' ~/.Xresources".format(color_active))
    os.system("xrdb -load .Xresources")
    
generate_wallpaper()
generate_i3_theme()
generate_rofi_theme()
