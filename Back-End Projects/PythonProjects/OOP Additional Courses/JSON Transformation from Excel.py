import pandas as pd

datapath = "json_trial.xlsx"

data = pd.read_excel("json_trial.xlsx")

mcc_code = data.payu_mcc
x1 = data.x1001.fillna("null")
x2 = data.x1002.fillna("null")
x3 = data.x1003.fillna("null")
x4 = data.x1004.fillna("null")
x5 = data.x1005.fillna("null")
x6 = data.x1006.fillna("null")
x7 = data.x1007.fillna("null")
x8 = data.x1008.fillna("null")
x9 = data.x1009.fillna("null")
x10 = data.x1010.fillna("null")
x11 = data.x1011.fillna("null")
x12 = data.x1012.fillna("null")
x13 = data.x1013.fillna("null")
x14 = data.x1014.fillna("null")
x15 = data.x1015.fillna("null")
x16 = data.x1016.fillna("null")
x17 = data.x1017.fillna("null")
x18 = data.x1018.fillna("null")
x19 = data.x1019.fillna("null")
x20 = data.x1020.fillna("null")
x21 = data.x1021.fillna("null")
x22 = data.x1022.fillna("null")
x23 = data.x1023.fillna("null")
x24 = data.x1024.fillna("null")
x25 = data.x1025.fillna("null")
x26 = data.x1026.fillna("null")
x27 = data.x1027.fillna("null")
x28 = data.x1028.fillna("null")
x29 = data.x1029.fillna("null")
x30 = data.x1030.fillna("null")
x31 = data.x1031.fillna("null")
x32 = data.x1032.fillna("null")
x33 = data.x1033.fillna("null")
x34 = data.x1034.fillna("null")

print("[")
x = 0
while x < len(mcc_code):
    if x == len(mcc_code)-1:
        print("\t{")
        print(f'\t\t"partner_value": {mcc_code[x]},')
        print(f'\t\t"validator_value": [{x1[x]}, {x2[x]}, {x3[x]}, {x4[x]}, {x5[x]}]')
        print("\t}")
    else:
        print("\t{")
        print(f'\t\t"partner_value": {mcc_code[x]},')
        print(f'\t\t"validator_value": [{x1[x]}, {x2[x]}, {x3[x]}, {x4[x]}, {x5[x]}, {x6[x]}, {x7[x]}, {x8[x]}, {x9[x]},'
              f' {x10[x]}, {x11[x]}, {x12[x]}, {x13[x]}, {x14[x]}, {x15[x]}, {x16[x]}, {x17[x]}, {x18[x]}, {x19[x]},'
              f' {x20[x]}, {x21[x]}, {x22[x]}, {x23[x]}, {x24[x]}, {x25[x]}, {x26[x]}, {x27[x]}, {x28[x]}, {x29[x]},'
              f' {x30[x]}, {x31[x]}, {x32[x]}, {x33[x]}, {x34[x]}]')
        print("\t},")
    x += 1
print("]")
