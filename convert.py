import tkinter as tk
import os
import easyocr
import cv2
from tkinter import filedialog as fd

ws = tk.Tk()
ws.title('Convert-TO-TXT')
ws.geometry('350x450+700+200')


def callback():
    name = fd.askdirectory()



    MyFile = open('logs.txt', 'w')

    for filename in os.listdir(name):
        f = os.path.join(name, filename)
        image = cv2.imread(f)
        resize = cv2.resize(image, (100, 40))
        cv2.imwrite('resize.png', resize)
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext('resize.png')
        MyFile.write(str(result))
        MyFile.write('\n')
        for detection in result:
            print(detection)
        if os.path.isfile(f):
            print(f)


errmsg = 'Error!'
tk.Button(text='Выберите директорию для загрузки папки с изображениями',
          command=callback).pack(fill=tk.X)
tk.mainloop()


