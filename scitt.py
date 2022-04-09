"""
MIT License

Copyright (c) 2022 atlas_core

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

I am in no way affiliated with Scott Wozniak (aka Scott the Woz),
I simply made this for fun.
"""


from PIL import Image, ImageFont, ImageDraw
from tkinter import filedialog
import requests
from random import choice
from io import BytesIO
import os
import glob

from utils import multiple_options, Option

url = input("file path/URL (enter nothing to open file explorer selection)? ")
if not url:
    url = filedialog.askopenfilename()
    # print(url)
    if not url:
        print("still no file selected.")
        exit(1)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


f = resource_path('./scott the woz template.png')
# f2 = '/home/atlas/Pictures/EvpalhLWQAE_rOk.jpeg'
# f2 = '/home/atlas/.steam/steam/appcache/librarycache/814540_header.jpg'
# f2 = '/home/atlas/.steam/steam/appcache/librarycache/333600_library_600x900.jpg'
# f2 = '/home/atlas/.steam/steam/appcache/librarycache/333600_header.jpg'
# f2 = '/home/atlas/Pictures/unorganized mess/burger king.jpg'
f3 = resource_path("./timestamp scott.png")
# overlays = ["overlays/alcohol.png",
#             "overlays/lemonade.png",
#             "overlays/ohgodohfuck.png",
#             "overlays/chef.png"]

overlays = []
for fileext in ('png', 'jpg'):
    overlays += glob.glob(f'./overlays/*.{fileext}', recursive=True)

# font = ImageFont.truetype("./Roboto.ttf", 32)
# will not work for me. it will just crash using OSError.
font = [ImageFont.truetype(font=BytesIO(open(resource_path("./Roboto.ttf"), "rb").read()), size=32) for _ in range(1000)][1]


try:
    if url.startswith("http"):
        response = requests.get(url)
        img2 = Image.open(BytesIO(response.content))
    else:
        if os.path.exists(url):
            img2 = Image.open(url)
        else:
            print("that does not seem to be a file.")
            exit(1)
except Exception as e:
    print("something happened and I couldn't get your image. sorry.")
    exit(1)

img2 = img2.resize((484, 262))

index = 0
try:
    # index = int(input("which overlay? "))
    # if index == 0:
    #     index = False
    # else:
    #     index -= 1
    #     file_link = overlays[index]
    file_link = multiple_options("which overlay?", [Option(filepath, index) for index, filepath in enumerate(overlays)]).name
except (ValueError, IndexError):
    print("that wasn't a correct overlay.")
    file_link = choice(overlays)

img = Image.open(f)  # open template

img.paste(img2, (37, 41, 521, 303))  # paste background image

draw = ImageDraw.Draw(img)

the_man = Image.open(file_link)
the_man = the_man.resize((504, 282))
the_man = the_man.convert('RGBA')
img.paste(the_man, (27, 31, 531, 313), the_man)  # take care of scott's body on the thumbnail

timestamp_img = Image.open(f3)
timestamp_img = timestamp_img.convert('RGBA')
img.paste(timestamp_img, (407, 260, 522, 305), timestamp_img)  # draw timestamp

draw.text((27, 331), input("title? "), font=font)
# img.show()
img.save('output.png')
