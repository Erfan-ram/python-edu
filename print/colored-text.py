from Font import RESET, Color, Background, Style

print(Background['Yellow'] + Color['Red'] + "this is a Red text" + RESET)


for __color, code in Color.items():
    print(f"{code} this is {__color} text  {RESET}")

for __background, code in Background.items():
    print(f"{code} this is {__background} background  {RESET}")

for __style, code in Style.items():
    print(f"{code} this is {__style} text  {RESET}")
