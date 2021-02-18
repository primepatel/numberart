from PIL import Image

list1 = ['9', '2', '1', '7']
list1 = ['0', '1']

def binary_deci(binary):
    decimal = 0
    l = len(binary)
    for x in binary:
        l -= 1
        decimal += pow(2, l) * int(x)
    return int(decimal)


im = Image.open("r.jpg")
im1 = im.resize((140, 80))
im2 = im1.convert("L")
w, h = im1.size
size = w*h
colour = im1.getdata()
raw_data2 = im2.getdata()

number = ''
photo = ''
for line_no in range(h):
    line = ''
    for pixel in range(line_no*w, line_no*w + w):
        num = list1[raw_data2[pixel]//128]
        number += num
        line += num
    line += '\n'
    photo += line
# print('0b' + number)
# print(binary_deci(number))
print('\n\n\n' + photo)
print(photo.count('1'))

