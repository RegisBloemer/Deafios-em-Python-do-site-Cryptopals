def xor_decrypt(ciphertext, key):
    # Inicializa um bytearray para armazenar o texto claro
    plaintext = bytearray()
    
    # Percorre cada byte do texto cifrado
    for i in range(len(ciphertext)):
        # Realiza o XOR entre o byte atual do texto cifrado e o byte correspondente da chave
        # (usando o operador "^") e adiciona o resultado ao bytearray do texto claro
        plaintext.append(ciphertext[i] ^ key[i % len(key)]) 
    
    # Retorna o texto claro como bytearray
    return plaintext

def calculate_key(ciphertext):
    # Lista de tamanhos de chave prováveis
    likely_key_lengths = [1, 2, 3, 4, 5]
    # Inicializa uma lista para armazenar as chaves prováveis
    likely_keys = []
    
    # Percorre cada tamanho de chave provável
    for key_length in likely_key_lengths:
        # Inicializa uma bytearray para armazenar a chave
        key = bytearray([0] * key_length)
        # Percorre cada byte da chave
        for i in range(key_length):
            # Divide o texto cifrado em blocos com o tamanho da chave atual
            blocks = [ciphertext[j] for j in range(i, len(ciphertext), key_length)]
            # Inicializa uma lista para armazenar a frequência de ocorrência de cada byte
            frequency = [0] * 256
            # Conta a frequência de ocorrência de cada byte no bloco atual
            for b in blocks:
                frequency[b] += 1
            # Encontra o byte mais frequente no bloco
            max_frequency = max(frequency)
            max_index = frequency.index(max_frequency)
            # Supõe que o byte mais frequente é o espaço " " e usa o XOR para descobrir o byte da chave
            key[i] = max_index ^ ord(' ') 
        # Adiciona a chave atual à lista de chaves prováveis
        likely_keys.append(key)
    
    # Retorna a lista de chaves prováveis
    return likely_keys

# Converte a string hexadecimal para um bytearray
ciphertext = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
# Calcula a lista de chaves prováveis
likely_keys = calculate_key(ciphertext)

# Percorre cada chave provável
for key in likely_keys:
    plaintext = xor_decrypt(ciphertext, key)
    # Verifica se o texto decifrado parece ser legível (não contém caracteres estranhos)
    if all(32 <= char <= 126 for char in plaintext):
        print(plaintext.decode())
        break