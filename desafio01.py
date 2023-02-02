def hex_to_base64(hex_string):
    """
    Essa função recebe uma string hexadecimal como entrada e retorna sua
    representação em base64 como saída.
    """
    # Primeiro, precisamos converter a string hexadecimal em uma string de bytes
    byte_string = bytes.fromhex(hex_string)

    # Então, podemos codificar manualmente a string de bytes como base64
    # A codificação base64 usa 64 caracteres para codificar os dados
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # O processo de codificação base64 é o seguinte:
    # - Dividir a entrada em grupos de 3 bytes
    # - Cada grupo de 3 bytes é representado por 4 caracteres da string base64_chars
    # - Se o comprimento da entrada não for múltiplo de 3, caracteres de preenchimento '=' são adicionados
    #   ao final da string de saída

    # Calcular o número de caracteres de preenchimento
    padding = len(byte_string) % 3

    # Dividir a entrada em grupos de 3 bytes
    # A expressão zip(*[iter(byte_string)]*3) é usada para agrupar a entrada em blocos de 3
    base64_triplets = zip(*[iter(byte_string)]*3)

    # Codificar cada grupo de 3 bytes como 4 caracteres
    base64_encoded = ""
    for triplet in base64_triplets:
        # Preencher o último grupo com zeros se necessário
        if len(triplet) < 3:
            triplet += (0,) * (3 - len(triplet))
        # Converter cada byte em um inteiro
        a, b, c = map(int, triplet)
        # Obter os caracteres base64 para cada chunk de 6 bits
        chunk1 = base64_chars[a >> 2]
        chunk2 = base64_chars[((a & 3) << 4) | (b >> 4)]
        chunk3 = base64_chars[((b & 15) << 2) | (c >> 6)]
        chunk4 = base64_chars[c & 63]
        # Concatenar os chunks para formar a string base64
        base64_encoded += chunk1 + chunk2 + chunk3 + chunk4

    # Adicionar caracteres de preenchimento '=' ao final da string de saída
    base64_encoded += "=" * padding

    return base64_encoded

result = hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
pre_result = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

if result == pre_result:
    print(result)