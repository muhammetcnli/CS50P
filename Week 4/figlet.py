import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Invalid usage")
    sys.exit()
elif len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    print("Invalid usage")
    sys.exit()
else:
    if sys.argv[2] in fonts:
        pass
    else:
        print("Invalid usage")
        sys.exit()

    input_text = input("Input: ")
    if len(sys.argv) == 1:
        random_font = random.choice(fonts)

        figlet.setFont(font=random_font)

        print(figlet.renderText(input_text))

    elif len(sys.argv) == 3:
            figlet.setFont(font=sys.argv[2])

            print(figlet.renderText(input_text))
    else:
        sys.exit()

    