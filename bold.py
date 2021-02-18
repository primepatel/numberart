from PIL import Image
from ascii import deci_prime
def binary_deci(binary):
    decimal = 0
    l = len(binary)
    for x in binary:
        l -= 1
        decimal += pow(2, l) * int(x)
    return int(decimal)

def span(integer, integer_colour):
    return f"<span style='color: rgb{integer_colour};'><b>{integer}</b></span>"

list1 = ['0', '1']
# list1 = ['8', '4', '0', '5', '9', '6', '3', '2', '1', '7']

im = Image.open("a.png")
im1 = im.resize((120, 72))
im2 = im1.convert("L")
w, h = im1.size
size = w*h
colour = im1.getdata()
raw_data2 = im2.getdata()

new_file = '''<h1></h1>
<p>'''
number = ''

for line_no in range(h):
    line = ''
    for pixel in range(line_no*w, line_no*w + w):
        num = list1[raw_data2[pixel]//128]
        number += num
        line += span(num, colour[pixel])
    line += '\n'
    # number += '\n'
    new_file += line
new_file += '</p>'
# print(number)
print(binary_deci(number))

# prime number

bi_prime = bin(deci_prime)

file = '''<h1></h1>
<p>'''
number = ''
for line_no in range(h):
    line = ''
    for pixel in range(line_no*w, line_no*w + w):
        num = bi_prime[2+pixel]
        number += num
        line += span(num, colour[pixel])
    line += '\n'
    number += '\n'
    file += line

file += "</p>"

text_file = open("outb.html", "wt")
n = text_file.write(file)
text_file.close()

text_file = open("prime.txt", "wt")
text_file.write("decimal prime:\n\n"+ str(deci_prime) + "\n\nbinary prime:\n\n" + str(bi_prime))
text_file.close()