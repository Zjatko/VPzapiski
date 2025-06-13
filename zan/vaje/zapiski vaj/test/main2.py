
import secrets
import socket
import threading
from Crypto.Util.Padding import pad, unpad

FLAG = "fake_flag"

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

S_BOXES = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [3, 4, 5, 6, 7, 8, 9, 10],
    [4, 5, 6, 7, 8, 9, 10, 11],
    [5, 6, 7, 8, 9, 10, 11, 12],
    [6, 7, 8, 9, 10, 11, 12, 13],
    [7, 8, 9, 10, 11, 12, 13, 14]
]

def int_to_64b_bitstring(n): return bin(n)[2:].zfill(64)
def permute(b, t): return ''.join(b[i - 1] for i in t)
def rotate_left(k, n): return k[n:] + k[:n]
def xor_strings(a, b): return ''.join(str(int(x)^int(y)) for x, y in zip(a, b))
def substitute(eh): return ''.join(format(S_BOXES[int(c[:3],2)%8][int(c[3:],2)%8], '04b') for c in [eh[i:i+6] for i in range(0, len(eh), 6)])
def feistel_network(r, k): return [permute(r, E), permute(substitute(xor_strings(permute(r, E), k)), P)]

def generate_round_keys_enc(k):
    k = permute(k, PC1)
    l, r = k[:28], k[28:]
    keys = []
    for s in shift_table:
        l, r = rotate_left(l, s), rotate_left(r, s)
        keys.append(permute(l + r, PC2))
    return keys

def des_encrypt(pt, key):
    keys = generate_round_keys_enc(key)
    pt = permute(pt, IP)
    l, r = pt[:32], pt[32:]
    for k in keys[:-1]: l, r = r, xor_strings(l, feistel_network(r, k)[-1])
    l, r = r, xor_strings(l, feistel_network(r, keys[-1])[-1])
    return permute(r + l, FP), feistel_network(r, keys[-1])[-1]

def des_ecb_encrypt(pt, key):
    pt = pad(pt.encode(), 8)
    res, outs = '', []
    for i in range(0, len(pt), 8):
        block = int_to_64b_bitstring(int.from_bytes(pt[i:i+8], 'big'))
        c, o = des_encrypt(block, key)
        res += c
        outs.append(o)
    return res, outs

def handle_client(conn, addr, key, flag_ct, flag_fo):
    counter = 32
    conn.sendall(b"Welcome to your homemade supersafe encryption service made by Jack the Intern")
    conn.sendall(f"Your credit for encrypted messages is at: {counter}".encode())
    try:
        while True:
            conn.sendall(b"Would you like to get the flag [1], encrypt a message yourself [2] or exit [3] >")
            command = conn.recv(1024).decode(errors='ignore').strip()
            if not command: break
            if command == "1":
                conn.sendall(f"Flag = {flag_ct} Feistel output = {flag_fo}".encode())
            elif command == "2":
                if counter > 0:
                    counter -= 1
                    conn.sendall(b"Enter the plaintext you want to encrypt >")
                    data = conn.recv(1024).decode(errors='ignore').strip()
                    ct, fo = des_ecb_encrypt(data, key)
                    conn.sendall(f"Ciphertext = {ct} Feistel output = {fo} Your credit for encrypted messages is at: {counter} ".encode())
                else:
                    conn.sendall(b"You have no credits for encrypted messages left.")
            elif command == "3":
                conn.sendall(b"Exiting...")
                break
            else:
                conn.sendall(b"Please enter a valid input")
    except:
        conn.sendall(b"Something went wrong.")
    finally:
        conn.close()

def main():
    key = int_to_64b_bitstring(secrets.randbits(64))
    flag_ct, flag_fo = des_ecb_encrypt(FLAG, key)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5010))
        s.listen()
        print("[+] Listening on port 5100...")
        while True:
            conn, addr = s.accept()
            print(f"[+] Connection from {addr}")
            threading.Thread(target=handle_client, args=(conn, addr, key, flag_ct, flag_fo)).start()

if __name__ == "__main__":
    main()





Flag = 1001110001100000100101101110111001010100001100100101000101010010011100001111011110010001100101011110100110110010000101101101100010101100101100000101010001011110010011010011110001110010101100010110110101011001100000110101010100100010010000101001011101101111 
Feistel_output = ['10010000010101111001111000110010', '10100100001110101010011101100011', '10010111110101110111010000000010', '11101110011111001101000110101100']


def reverse_substitute(eh):
    # Reverse the S-box substitution. We need to go through the S-boxes in reverse.
    reversed_sboxes = [
        [7, 6, 5, 4, 3, 2, 1, 0],
        [0, 1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1, 0],
        [4, 5, 6, 7, 0, 1, 2, 3],
        [6, 5, 4, 3, 2, 1, 0, 7],
        [2, 3, 4, 5, 6, 7, 0, 1],
        [1, 0, 3, 2, 7, 6, 5, 4],
        [3, 2, 5, 4, 1, 0, 7, 6]
    ]
    
    return ''.join(format(reversed_sboxes[int(c[:3], 2) % 8][int(c[3:], 2) % 8], '04b') for c in [eh[i:i + 6] for i in range(0, len(eh), 6)])

def reverse_feistel_network(r, k):
    # Reverse the Feistel network steps
    return xor_strings(rotate_left(xor_strings(permute(r, E), k), -1), permute(r, P))

def reverse_des(pt, key):
    # Reverse the entire DES process step by step
    keys = generate_round_keys_enc(key)
    pt = permute(pt, IP)
    l, r = pt[:32], pt[32:]
    
    # We need to reverse the Feistel rounds in reverse order
    for k in reversed(keys):
        r, l = l, reverse_feistel_network(r, k)
    
    return permute(r + l, FP)

def reverse_des_ecb_encrypt(ct, key):
    # Reverse DES in ECB mode
    ct = [ct[i:i + 64] for i in range(0, len(ct), 64)]
    pt = ''
    for c in ct:
        pt += reverse_des(c, key)
    return pt

# Assuming you have the Feistel outputs and key from the original process, we'll continue from there
def reverse_process(feistel_outputs, key):
    reversed_blocks = []
    
    for fo in feistel_outputs:
        reversed_output = reverse_substitute(fo)
        reversed_blocks.append(reversed_output)
    
    return reversed_blocks

# Example of running reverse steps
reversed_outputs = reverse_process(feistel_outputs, key)  # Feistel outputs from server's response
print("Reversed Feistel outputs:", reversed_outputs)

