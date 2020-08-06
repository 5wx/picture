from PIL import Image

#定义代表灰度的字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ") #设置显示的字符集

#灰度值映射字符函数  将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):#alpha为透明度
    if alpha == 0:# 判断 alpha 值，为0表示全透明 
        return ' '
    length = len(ascii_char)# 获取字符集的长度，这里为 70
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)# 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    unit = (255.0 + 1)/length  #返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

#图片导入及尺寸设置
IMG = 'P.jpg' #设置图片文件
WIDTH = 600#设置字符画的宽
HEIGHT = 200#设置字符画的高
im = Image.open(IMG)
im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

#遍历图片获取字符
txt = ''
for i in range(HEIGHT):# 遍历该行中的每一列
    for j in range(WIDTH):# 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
        txt+= get_char(*im.getpixel((j,i)))
    txt += '\n'# 遍历完一行后需要增加换行符
    
#字符画输出和导入文件
OUTPUT = 'P.txt' #设置存放字符画的文本文件
with open(OUTPUT,'w') as f:#保存到文本文件
    f.write(txt)

