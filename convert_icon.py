import os
# PIL : Python Imaging Library
from PIL import Image

# 获取目录下文件名
os.chdir('assets')
files = os.listdir()
# 图标大小
size = (256, 256)

# 给图标文件单独创建一个icon目录
if not os.path.exists('icon'):
    os.mkdir('icon')

for in_name in files:
    # 分离文件名与扩展名
    tmp = os.path.splitext(in_name)
    # 因为python文件跟图片在同目录，所以需要判断一下
    if tmp[1] == '.png':
        out_name = tmp[0] + '.ico'
        try:
            # 打开图片并设置大小
            im = Image.open(in_name).resize(size)
            # 图标文件保存至icon目录
            path = os.path.join('icon', out_name)
            im.save(path)

            print('{} --> {}'.format(in_name, out_name))
        except IOError:
            print('connot convert :', in_name)
