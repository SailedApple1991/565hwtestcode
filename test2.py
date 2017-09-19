test = 'UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZ' \
       'VUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSX' \
       'EPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ'
test2 = 'it was disclosed yesterday that several informal but' \
        'direct contacts have been made with political' \
        'representatives of the viet cong in moscow'

test2 = test2.replace(" ", "")
dic = {}

for index, item in enumerate(test2):
    dic[item] = test[index]
print(dic)