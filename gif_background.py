from PIL import Image
import ctypes
import time
import os

num_frames = 0

with Image.open('img.gif') as im:
    num_frames = im.n_frames
    for i in range(im.n_frames):
        im.seek(i)
        im.save('./frames/{}.png'.format(i))


while True:
    for i in range(num_frames):
        time.sleep(1/10)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\bogos\Desktop\michael\dev\coding\python\gif_background\frames\{num}.png".format(num = i), 0)
