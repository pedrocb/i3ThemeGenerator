import os
import random
import json
import colorsys

colorSaturation = 50
colorHue = random.randint(0,360)
os.system("python ~/wallpaper_changer/script.py " + str(colorHue) + " " + str(colorSaturation) + " ~/wallpaper_changer/1941277.png wallpaper.png")
os.system("feh --bg-scale wallpaper.png")

theme = "# vim: filetype=yaml\n---\nmeta:\n  description: AUTOMATICALLY GENERATED THEME\n"
theme += "bar_colors:\n  background: '{0}'\n  separator: '{1}'\n  statusline: '{2}'\n  focused_workspace:\n    border: '{3}'\n    background: '{4}'\n    text: '{5}'\n\n".format('barbg','barseparator','barfont','barfont','focusedwsbg','barfont')
theme += "window_colors:\n  focused:\n    border: windowbg\n    background: windowbg\n    text: barseparator\n  unfocused:\n    border: windowbg\n    background: unfocusedwindowbg\n    text: barbg\n\n"
theme+= "colors:\n"
theme+= "  barbg: '{}'\n".format("#000000")
theme+= "  barfont: '{}'\n".format('#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,40/100.0,100/100.0) ]))
theme+= "  barseparator: '{}'\n".format('#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,100/100.0) ]))
theme+= "  windowbg: '{}'\n".format('#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,60/100.0) ]))
theme+= "  focusedwsbg: '{}'\n".format('#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,80/100.0,50/100.0) ]))
theme+= "  unfocusedwindowbg: '{}'\n".format('#%02x%02x%02x'% tuple([z * 255 for z in colorsys.hsv_to_rgb(colorHue/360.0,100/100.0,0/100.0) ]))

theme_file = open("theme.yaml","w")
theme_file.write(theme)
theme_file.close()

os.system("i3-style theme.yaml  -o ~/.config/i3/config --reload")

print(theme)
