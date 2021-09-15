import time
import numpy as np
from PIL import Image, ImageFont, ImageDraw


def text2int(text):
    image = Image.new('RGB', (fontSize, fontSize))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'simsun.ttc', fontSize, encoding="utf-8")
    color = (255, 255, 255)  # 字体颜色
    draw.text((0, 0), text, font=font, fill=color)
    a_image = np.asarray(image)
    sum = 0
    for i in a_image:
        for j in i:
            for k in j:
                sum += k
    return sum


def processImage(path: str):
    image = Image.open(path).convert('L')

    image2 = Image.new('L', image.size)
    font = ImageFont.truetype(r'simsun.ttc', fontSize, encoding="utf-8")
    color = (255)  # 字体颜色
    a_image = np.asarray(image)
    print(image.size)
    for x in range(0, image.size[1], fontSize):
        for y in range(0, image.size[0], fontSize):
            sum = 0
            count = 0
            for x1 in range(x, min(x + fontSize, image.size[1])):
                for y1 in range(y, min(y + fontSize, image.size[0])):
                    sum += a_image[x1, y1]
                    count += 1
            sum = int(sum / count)
            sum = int(sum / (256 / len(dictionary))) * (256 / len(dictionary))
            draw = ImageDraw.Draw(image2)
            word = sum2word(sum)
            draw.text((y, x), word, font=font, fill=color)
    timestr = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    image2.save(r'output' + timestr + '.jpg')
    image2.show()
    return image2


def words2Dictionary(words: str):
    for i in words:
        sum = text2int(i)
        dictionary[i] = sum
    return dictionary


def sum2word(sum):
    dict = sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0]))
    return dict[int(sum / (256 / len(dict)))][0]


words = '李曦高铭瑶婚礼'
dictionary = {}
fontSize = 20

if __name__ == '__main__':
    words2Dictionary(words)
    print(dictionary)
    image = processImage(r'8.jpg')
