from PIL import Image

def binary_deci(binary):
    decimal = 0
    l = len(binary)
    for x in binary:
        l -= 1
        decimal += pow(2, l) * int(x)
    return int(decimal)

def span(integer, integer_colour):
    return f"<span style='color: rgb{integer_colour};'>{integer}</span>"

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
deci_prime = int('''7927979834214278885390771595046177498965881389646413003365455349458380\
0752875112330497577072590410056319302097362948979529181388687739576420\
3900737557944599151341325965832675493049172295004571063364098257833552\
3641549489616725410258218516263965893919248089404574565910158990277028\
4738028669398231350765640886940456061841577932743964967153002600290272\
3663747879007951593978441774135172187517383305445246696271605464921673\
6746327127515357818695268723654833080675474647371937991396254303618885\
1395072761737558594890700659004693440196575830938410693341173570796962\
0637263325749692094202896799293053056852944839262013753502721495850785\
6452625762428471755004064484499200954749084559689716764971446192495967\
0872869149202127110039698147832007140198959813203064870961484589373232\
9614713399184605308351943538173578140975399565744012414846001495191231\
6491452031424273123403910641344966606201589414780394558923921494649265\
8215615966487980853762012650851760725198017838143060468068595601205735\
8295589454492765073524198309900844536344404496430169128133287256906508\
2926304456388388022974494832235239810324385649924988905009755735898384\
1755745559424859334783724938166870774552916101767392264944178403987027\
8827876475335798054159879960832662287263854783214826092645577286928161\
7882268432245409608679174388252582726802314441065618199164243383807905\
1388965925174188772931920812952993399743864681952615588309445394278592\
2614336639950093734006911840282877118928791862862974012922265144237924\
1514393437204525428446796198214980013657964335750271574040406431489654\
6268887159077584045719472228244281205672466173756512553255683346018219\
6661925051224581491822421536765497566481690451422103994766176827806744\
1891188695782947429505550947848039105129909743097255453760052389095664\
3454459382866374750083035214987234975311029345630577909657661309605136\
7521980830230354066309831443028138666267771188399079655337448290347428\
0837126317821051604564789060233241107978102840193693281509284006193490\
0033721356506402400461869966908275990196335440015280005120234094398640\
3346160599736294801747290515383506342195417292388306808022154454276675\
6208638144997952727372777464548726580881724336923744188725312482426674\
0770621260881514127914717905061557596354220564867919131544193296148925\
8240170479014430656727462751648140746306688450635149113774439461377050\
9488638720024863494653424332392600155429474233673344572747740355976574\
5284570458464495911239177812024204503667253534224504682610133427819763\
7109060704109323753374045369508631227460204366744936219984791370399183\
1800408185120605561904524179933925874274079786112246494941057187971179\
50034708657''')
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

text_file = open("out.html", "wt")
n = text_file.write(file)
text_file.close()

text_file = open("prime.txt", "wt")
text_file.write("decimal prime:\n\n"+ str(deci_prime) + "\n\nbinary prime:\n\n" + str(bi_prime) + "\n\nbinary prime photo:\n\n"+ str(number))
text_file.close()