import pyqrcode
import os, shutil
title=input("Give your QR code a title")
text=input("what would you like your qr code to say")
file_name_svg = title+ 'svg'
file_name_png= title+ 'png'
url=pyqrcode.create(text)
url.svg(file_name_svg,scale=8)
url.png(file_name_png,scale=10)

os.mkdir(fr"X:\Users\Yashika\Desktop\{title}")

shutil.move(f"{file_name_svg}",fr"X:\Users\Yashika\Desktop\{title}")
shutil.move(f"{file_name_png}",fr"X:\Users\Yashika\Desktop\{title}")

