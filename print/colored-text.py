from Font import RESET, Color, Background

print(Background['Yellow'] + Color['Red'] + "this is a Red text" + RESET)


for color, code in Color.items():
    print(f"{code} this is {color} text  {RESET}")
