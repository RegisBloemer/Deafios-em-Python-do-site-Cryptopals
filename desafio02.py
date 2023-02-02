def fixed_xor(hex1, hex2):
    """
    Essa função recebe duas strings hexadecimais como entrada e retorna a string hexadecimal
    resultante da operação XOR entre as duas strings.
    """
    # Converter as strings hexadecimais em um formato binário equivalente
    bin1 = bin(int(hex1, 16))[2:].zfill(len(hex1) * 4)
    bin2 = bin(int(hex2, 16))[2:].zfill(len(hex2) * 4)

    # Realizar a operação XOR bit a bit entre as duas strings binárias
    xor_result = int(bin1, 2) ^ int(bin2, 2)

    # Converter o resultado da operação XOR de volta para um formato hexadecimal
    return hex(xor_result)[2:].zfill(len(hex1))

print(fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
