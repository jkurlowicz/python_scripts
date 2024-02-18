import sys
number = sys.argv[1]

BITS_LENGTH = 32

results = []

def convertDecimalToBinary(number):
    return bin(number)[2:]

def convertDecimalToHex(number):
    return hex(number)

def convertToInt(number):
    dec_num: int

    if (number[:2] == '0x'):
        dec_num = int(number, 16)
    else:
        dec_num = int(number)

    return dec_num

def fillWithZeros(binary_value):
    return binary_value.zfill(BITS_LENGTH)

def shiftLeft(number, places):
    return convertToInt(number) << places

def formatBinaryString(binary_string):
    string_32 = binary_string

    if (len(binary_string) > 32 ):
        string_32 = binary_string[-32:]

    spaced_text = [string_32[i:i+8] + " " for i in range(0, len(string_32), 8)]
    return "".join(spaced_text)


for x in range(1, BITS_LENGTH+1):
    shifted_num = shiftLeft(number, x)
    binary = formatBinaryString(fillWithZeros(convertDecimalToBinary(shifted_num)))
    if (binary.find('1') == -1):
        break

    converted = {'bin': binary, 'hex': convertDecimalToHex(shifted_num)}
    results.append(converted)

print('Passed number: ' + number + '\n')
for idx, res in enumerate(results):
    print(f'Shifted by {idx + 1}')
    print('binary: ' + res['bin'] + '\n')
    print('hex: ' + res['hex'] + '\n')
    print('-'*40)
