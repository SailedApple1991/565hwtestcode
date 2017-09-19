def decode(key, plaintext):
    plaintext = plaintext.replace(" ","")
    plaintext = plaintext.translate(str.maketrans('','', '!@#$,.?;:"!-'))
    print(plaintext)
    if(any(c.isalpha() for c in key)):
        replacekey = []
        for character in key:
            number = ord(character) - 96
            replacekey.append(number)
        key = ''.join(replacekey)
    order = {
        int(val): num for num, val in enumerate(key)
    }
    inv_map = {v: k for k, v in order.items()}
    length = len(key)
    lenofS = len(plaintext)
    chunks = [plaintext[x:x + int(lenofS/length)] for x in range(0, len(plaintext), int(lenofS/length))]
    print(chunks)
    temp =[]
    print(inv_map)
    i = 0
    for i in range(0, int(lenofS/length)):
        for k, v in inv_map.items():
            print(chunks[v-1])
            print(chunks[v-1][i])
            temp.append(chunks[v-1][i])

    return(''.join(temp))

print(decode('4312567', 'ttnaaptmtsuoaodwcoixknlypetz'))