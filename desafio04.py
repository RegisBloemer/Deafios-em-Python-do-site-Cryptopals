import string

def xor_decrypt(ciphertext, key):
    plaintext = bytearray()
    for i in range(len(ciphertext)):
        plaintext.append(ciphertext[i] ^ key[i % len(key)]) 
    return plaintext

def calculate_key(ciphertext, max_key_length):
    likely_key_lengths = range(1, max_key_length + 1)
    likely_keys = []
    for key_length in likely_key_lengths:
        key = bytearray([0] * key_length)
        for i in range(key_length):
            blocks = [ciphertext[j] for j in range(i, len(ciphertext), key_length)]
            frequency = [0] * 256
            for b in blocks:
                frequency[b] += 1
            max_frequency = max(frequency)
            max_index = frequency.index(max_frequency)
            key[i] = max_index ^ ord(' ') 
        likely_keys.append(key)
    return likely_keys

def is_plaintext_readable(plaintext):
    return all(chr(char) in string.printable for char in plaintext)

def read_file_and_process_lines(filename, max_key_length):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            ciphertext = bytearray.fromhex(line)
            likely_keys = calculate_key(ciphertext, max_key_length)

            for key in likely_keys:
                plaintext = xor_decrypt(ciphertext, key)
                if is_plaintext_readable(plaintext):
                    print(plaintext.decode())
                    break

read_file_and_process_lines("doc.txt", 10)
