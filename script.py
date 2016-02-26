import os
import random
import json
import colorsys

colorHue = random.randint(0,360)
testAngleBarColor = 276
testAngleBarFontColor = 0

mainColor = (colorHue,50,18)
secondaryColorOne = ((colorHue + testAngleBarColor)%360,70,30)
secondaryColorTwo = ((colorHue + testAngleBarFontColor)%360,70,30)
complementaryColor = ((colorHue + 180)%360,70,30)

def rgb_to_hexadecimal(color):
    return '%02x%02x%02x' % tuple([z * 255 for z in color])

def hsv_to_rgb(color):
    return colorsys.hsv_to_rgb(color[0]/360.0,color[1]/100.0,color[2]/100.0)

def generate_wallpaper():
    colorSaturation = 50
    os.system("python ~/wallpaper_changer/script.py " + str(colorHue) + " " + str(colorSaturation) + " ~/wallpaper_changer/1941277.png wallpaper.png")
    os.system("feh --bg-scale wallpaper.png")
    #os.system("rm wallpaper.png")
    return

def generate_i3_theme():
    barBackgroundColor = secondaryColorOne
    barFontColor = (secondaryColorTwo[0],30,90)
    barSeparatorColor = (secondaryColorTwo[0],70,90)
    windowBorderColor = (mainColor[0],100,60)
    focusedWorkspaceBackgroundColor = barBackgroundColor#(mainColor[0],50,50) #80 50
    unfocusedWindowBorderColor = mainColor
    theme = "# vim: filetype=yaml\n---\nmeta:\n  description: AUTOMATICALLY GENERATED THEME\n"
    theme += "bar_colors:\n  background: '{0}'\n  separator: '{1}'\n  statusline: '{2}'\n  focused_workspace:\n    border: '{3}'\n    background: '{4}'\n    text: '{5}'\n\n".format('barbg','barseparator','barfont','barfont','focusedwsbg','barfont')
    theme += "window_colors:\n  focused:\n    border: windowbg\n    background: windowbg\n    text: barseparator\n  unfocused:\n    border: windowbg\n    background: unfocusedwindowbg\n    text: barbg\n\n"
    theme+= "colors:\n"
    theme+= "  barbg: '#{}'\n".format(rgb_to_hexadecimal(hsv_to_rgb(barBackgroundColor)))
    theme+= "  barfont: '#{}'\n".format(rgb_to_hexadecimal(hsv_to_rgb(barFontColor)))
    theme+= "  barseparator: '#{}'\n".format(rgb_to_hexadecimal(hsv_to_rgb(barSeparatorColor)))
    theme+= "  windowbg: '#{}'\n".format(rgb_to_hexadecimal(hsv_to_rgb(windowBorderColor)))
    theme+= "  focusedwsbg: '#{}'\n".format(rgb_to_hexadecimal(hsv_to_rgb(focusedWorkspaceBackgroundColor)))
    theme+= "  unfocusedwindowbg: '#{}'\n".format(rgb_to_hexadecimal(hsv_to_rgb(unfocusedWindowBorderColor)))
    
    theme_file = open("theme.yaml","w")
    theme_file.write(theme)
    theme_file.close()
    os.system("i3-style theme.yaml  -o ~/.config/i3/config --reload")
    return

def generate_rofi_theme():
    s100b20 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,20/100.0) ])
    windowBackgroundColor = rgb_to_hexadecimal(colorsys.hsv_to_rgb(complementaryColor[0]/360.0,complementaryColor[1]/100.0,20/100.0))
    highlightRowBackgroundColor = rgb_to_hexadecimal(colorsys.hsv_to_rgb(complementaryColor[0]/360.0,complementaryColor[1]/100.0,25/100.0))
    s100b80 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,80/100.0) ])
    s60b80 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,60/100.0,80/100.0) ])
    s0b20 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,0/100.0,10/100.0) ])
    s0b10 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,0/100.0,20/100.0) ])
    s100b70 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,70/100.0) ])
    s50b100 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,50/100.0,100/100.0) ])
    s20b100 = '#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,20/100.0,100/100.0) ])
    s0b25 = '%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,0/100.0,25/100.0) ])
    color_window = "rofi.color-window: argb:ed{}, argb:ed{}, {}".format(windowBackgroundColor,windowBackgroundColor,s100b80)
    color_normal = "rofi.color-normal: argb:ed{}, {}, argb:ed{}, #{}, {}".format(windowBackgroundColor,s100b80,windowBackgroundColor,highlightRowBackgroundColor,s100b80)
    color_active = "rofi.color-active: argb:ed{}, {}, {}, {}, {}".format(windowBackgroundColor,s50b100,s0b20,s0b20,s20b100)

    os.system("sed -i '/color-window/ c {}' ~/.Xresources".format(color_window))
    os.system("sed -i '/color-normal/ c {}' ~/.Xresources".format(color_normal))
    os.system("sed -i '/color-active/ c {}' ~/.Xresources".format(color_active))
    os.system("xrdb -load .Xresources")
    
generate_wallpaper()
generate_i3_theme()
generate_rofi_theme()
