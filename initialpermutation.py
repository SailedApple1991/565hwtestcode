data = [0,1,1,0,0,1,1,1,
        0,1,0,1,1,0,1,0,
        0,1,1,0,1,0,0,1,
        0,1,1,0,0,1,1,1,
        0,1,0,1,1,1,1,0,
        0,1,0,1,1,0,1,0,
        0,1,1,0,1,0,1,1,
        0,1,0,1,1,0,1,0]

boa1 = [data[57],data[49],data[41],data[33],data[25],data[17],data[9],data[1],
       data[59],data[51],data[43],data[35],data[27],data[19],data[11],data[3],
       data[61],data[53],data[45],data[37],data[29],data[21],data[13],data[5],
       data[63],data[55],data[47],data[39],data[31],data[23],data[15],data[7],
       data[56],data[48],data[40],data[32],data[24],data[16],data[8],data[0],
       data[58],data[50],data[42],data[34],data[26],data[18],data[10],data[2],
       data[60],data[52],data[44],data[36],data[28],data[20],data[12],data[4],
       data[62],data[54],data[46],data[38],data[30],data[22],data[14],data[6]]

boa = [[data[57],data[49],data[41],data[33],data[25],data[17],data[9],data[1]],
       [data[59],data[51],data[43],data[35],data[27],data[19],data[11],data[3]],
       [data[61],data[53],data[45],data[37],data[29],data[21],data[13],data[5]],
       [data[63],data[55],data[47],data[39],data[31],data[23],data[15],data[7]],
       [data[56],data[48],data[40],data[32],data[24],data[16],data[8],data[0]],
       [data[58],data[50],data[42],data[34],data[26],data[18],data[10],data[2]],
       [data[60],data[52],data[44],data[36],data[28],data[20],data[12],data[4]],
       [data[62],data[54],data[46],data[38],data[30],data[22],data[14],data[6]]]

inverse =[[boa1[39],boa1[7],boa1[47],boa1[15],boa1[55],boa1[23],boa1[63],boa1[31]],
          [boa1[38], boa1[6], boa1[46], boa1[14], boa1[54], boa1[22], boa1[62], boa1[30]],
          [boa1[37], boa1[5], boa1[45], boa1[13], boa1[53], boa1[21], boa1[61], boa1[29]],
          [boa1[36], boa1[4], boa1[44], boa1[12], boa1[52], boa1[20], boa1[60], boa1[28]],
          [boa1[35], boa1[3], boa1[43], boa1[11], boa1[51], boa1[19], boa1[59], boa1[27]],
          [boa1[34], boa1[2], boa1[42], boa1[10], boa1[50], boa1[18], boa1[58], boa1[26]],
          [boa1[33], boa1[1], boa1[41], boa1[9], boa1[49], boa1[17], boa1[57], boa1[25]],
          [boa1[32], boa1[0], boa1[40], boa1[8], boa1[48], boa1[16], boa1[56], boa1[24]]]


for i in range(0,len(boa)):
    print(boa[i])

print("\n")
for i in range(0, len(inverse)):
    print(inverse[i])



