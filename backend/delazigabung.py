# Irreducible Polynomial x^8 + x^7 + x^5 + x^3 + 1

sbox = [
  0x63, 0x7c, 0xa6, 0xe5, 0x81, 0x6d, 0x20, 0x83, 0x12, 0xb0, 0x2e, 0xe6, 0xc2, 0x79, 0x13, 0x15,
  0x91, 0x3d, 0xc0, 0x6a, 0x8f, 0xa9, 0xa1, 0x19, 0xb3, 0xdf, 0x6e, 0x5e, 0x11, 0x6c, 0x58, 0x27,
  0x1a, 0xa0, 0x06, 0xd0, 0xb2, 0xa3, 0xe7, 0x66, 0x5f, 0xff, 0x4c, 0x7b, 0x48, 0xfb, 0x14, 0xd4,
  0x41, 0x54, 0x77, 0xda, 0xaf, 0x9b, 0xfd, 0xc3, 0x10, 0x39, 0xae, 0xf7, 0xb4, 0x01, 0x0b, 0x25,
  0x95, 0xd2, 0xc8, 0xca, 0xd1, 0x34, 0xba, 0x31, 0xc1, 0xd3, 0x49, 0x55, 0x21, 0x9c, 0xab, 0xea,
  0x7d, 0x56, 0x2d, 0x02, 0xf4, 0x87, 0x6f, 0x07, 0xbc, 0xfc, 0x65, 0xfe, 0xd8, 0x2b, 0xf2, 0xb8,
  0x38, 0x28, 0xf8, 0xdd, 0x23, 0x7e, 0xbf, 0x80, 0x05, 0x9f, 0x1f, 0x72, 0x2c, 0xe2, 0x33, 0xdc,
  0x90, 0xf1, 0x4e, 0xaa, 0x85, 0xd7, 0x29, 0x98, 0x88, 0xb5, 0x18, 0x17, 0x1d, 0x6b, 0x0a, 0xd9,
  0x52, 0x86, 0xbb, 0x8a, 0xb6, 0xee, 0xb7, 0xe8, 0x3a, 0xcb, 0x82, 0xa2, 0xc5, 0x4f, 0x4a, 0x62,
  0x32, 0x74, 0x3b, 0x61, 0x3c, 0x24, 0x78, 0xe0, 0x42, 0xb9, 0xd6, 0x44, 0x4d, 0xf3, 0xed, 0xf0,
  0x26, 0x89, 0xf9, 0xa5, 0x0e, 0x09, 0x99, 0xec, 0xa8, 0xb1, 0x5b, 0xdb, 0x2f, 0x45, 0x51, 0x97,
  0x8c, 0x7a, 0xac, 0x75, 0x2a, 0xbd, 0xad, 0xe3, 0xbe, 0xcf, 0x47, 0x37, 0xe1, 0x93, 0xc4, 0xc9,
  0xce, 0xc7, 0xc6, 0x0c, 0xe4, 0x04, 0x76, 0x69, 0x43, 0xde, 0xa7, 0xef, 0x0d, 0x84, 0x92, 0x22,
  0x50, 0x68, 0x57, 0x1b, 0x5d, 0xfa, 0xeb, 0x36, 0x8e, 0x8d, 0xe9, 0x7f, 0x4b, 0x71, 0xf6, 0x03,
  0x9a, 0xd5, 0x60, 0x1c, 0xf5, 0x1e, 0xcd, 0xa4, 0x5a, 0x8b, 0x73, 0x16, 0x46, 0x64, 0x9e, 0x00,
  0x96, 0x0f, 0x08, 0x70, 0x94, 0x30, 0x59, 0x53, 0x5c, 0xcc, 0x67, 0x40, 0x9d, 0x35, 0x3e, 0x3f
]

inverse_sbox = [
  0xef, 0x3d, 0x53, 0xdf, 0xc5, 0x68, 0x22, 0x57, 0xf2, 0xa5, 0x7e, 0x3e, 0xc3, 0xcc, 0xa4, 0xf1,
  0x38, 0x1c, 0x08, 0x0e, 0x2e, 0x0f, 0xeb, 0x7b, 0x7a, 0x17, 0x20, 0xd3, 0xe3, 0x7c, 0xe5, 0x6a,
  0x06, 0x4c, 0xcf, 0x64, 0x95, 0x3f, 0xa0, 0x1f, 0x61, 0x76, 0xb4, 0x5d, 0x6c, 0x52, 0x0a, 0xac,
  0xf5, 0x47, 0x90, 0x6e, 0x45, 0xfd, 0xd7, 0xbb, 0x60, 0x39, 0x88, 0x92, 0x94, 0x11, 0xfe, 0xff,
  0xfb, 0x30, 0x98, 0xc8, 0x9b, 0xad, 0xec, 0xba, 0x2c, 0x4a, 0x8e, 0xdc, 0x2a, 0x9c, 0x72, 0x8d,
  0xd0, 0xae, 0x80, 0xf7, 0x31, 0x4b, 0x51, 0xd2, 0x1e, 0xf6, 0xe8, 0xaa, 0xf8, 0xd4, 0x1b, 0x28,
  0xe2, 0x93, 0x8f, 0x00, 0xed, 0x5a, 0x27, 0xfa, 0xd1, 0xc7, 0x13, 0x7d, 0x1d, 0x05, 0x1a, 0x56,
  0xf3, 0xdd, 0x6b, 0xea, 0x91, 0xb3, 0xc6, 0x32, 0x96, 0x0d, 0xb1, 0x2b, 0x01, 0x50, 0x65, 0xdb,
  0x67, 0x04, 0x8a, 0x07, 0xcd, 0x74, 0x81, 0x55, 0x78, 0xa1, 0x83, 0xe9, 0xb0, 0xd9, 0xd8, 0x14,
  0x70, 0x10, 0xce, 0xbd, 0xf4, 0x40, 0xf0, 0xaf, 0x77, 0xa6, 0xe0, 0x35, 0x4d, 0xfc, 0xee, 0x69,
  0x21, 0x16, 0x8b, 0x25, 0xe7, 0xa3, 0x02, 0xca, 0xa8, 0x15, 0x73, 0x4e, 0xb2, 0xb6, 0x3a, 0x34,
  0x09, 0xa9, 0x24, 0x18, 0x3c, 0x79, 0x84, 0x86, 0x5f, 0x99, 0x46, 0x82, 0x58, 0xb5, 0xb8, 0x66,
  0x12, 0x48, 0x0c, 0x37, 0xbe, 0x8c, 0xc2, 0xc1, 0x42, 0xbf, 0x43, 0x89, 0xf9, 0xe6, 0xc0, 0xb9,
  0x23, 0x44, 0x41, 0x49, 0x2f, 0xe1, 0x9a, 0x75, 0x5c, 0x7f, 0x33, 0xab, 0x6f, 0x63, 0xc9, 0x19,
  0x97, 0xbc, 0x6d, 0xb7, 0xc4, 0x03, 0x0b, 0x26, 0x87, 0xda, 0x4f, 0xd6, 0xa7, 0x9e, 0x85, 0xcb,
  0x9f, 0x71, 0x5e, 0x9d, 0x54, 0xe4, 0xde, 0x3b, 0x62, 0xa2, 0xd5, 0x2d, 0x59, 0x36, 0x5b, 0x29
]

key_expander = "gyattrizzlersigmaohiofanumtaxjdonmysoulshuwalahumbatugaskriptoduar"
def mix_key(input):
  output = ""
  for i in range(3,-1,-1):
    output += input[i]
  return output

def key_expansion(key_string, round):
  result_key = ""
  result_key_mix = ""
  result_key += key_string
  if(len(key_string) == 16 and round == 10):
    chunk1 = key_expander[0:16].encode()
    result_bytes1 = bytes(x ^ y for x, y in zip(key_string[0:16].encode(), chunk1))
    key_chunk1 =  result_bytes1.decode()
    chunk2 = key_expander[16:32].encode()
    result_bytes2 = bytes(x ^ y for x, y in zip(key_string[0:16].encode(), chunk2))
    key_chunk2 =  result_bytes2.decode()
    chunk3 = key_expander[32:40].encode()
    result_bytes3 = bytes(x ^ y for x, y in zip(key_string[0:8].encode(), chunk3))
    key_chunk3 =  result_bytes3.decode()

    result_key += key_chunk1 + key_chunk2 + key_chunk3
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])

  elif(len(key_string) == 24 and round == 12):
    chunk1 = key_expander[0:24].encode()
    result_bytes1 = bytes(x ^ y for x, y in zip(key_string[0:24].encode(), chunk1))
    key_chunk1 =  result_bytes1.decode()
    chunk2 = key_expander[24:48].encode()
    result_bytes2 = bytes(x ^ y for x, y in zip(key_string[0:24].encode(), chunk2))
    key_chunk2 =  result_bytes2.decode()
    # chunk3 = key_expander[48:64].encode()
    # result_bytes3 = bytes(x ^ y for x, y in zip(key_string[0:16].encode(), chunk3))
    # key_chunk3 =  result_bytes3.decode()

    result_key += key_chunk1 + key_chunk2
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])

  elif(len(key_string) == 32 and round == 14):
    chunk1 = key_expander[0:32].encode()
    result_bytes1 = bytes(x ^ y for x, y in zip(key_string[0:32].encode(), chunk1))
    key_chunk1 =  result_bytes1.decode()
    chunk2 = key_expander[32:56].encode()
    result_bytes2 = bytes(x ^ y for x, y in zip(key_string[0:32].encode(), chunk2))
    key_chunk2 =  result_bytes2.decode()
    # chunk3 = key_expander[48:64].encode()
    # result_bytes3 = bytes(x ^ y for x, y in zip(key_string[0:16].encode(), chunk3))
    # key_chunk3 =  result_bytes3.decode()

    result_key += key_chunk1 + key_chunk2
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])

  elif(len(key_string) == 32 and round == 16):
    chunk1 = key_expander[0:32].encode()
    result_bytes1 = bytes(x ^ y for x, y in zip(key_string[0:32].encode(), chunk1))
    key_chunk1 =  result_bytes1.decode()
    chunk2 = key_expander[32:64].encode()
    result_bytes2 = bytes(x ^ y for x, y in zip(key_string[0:32].encode(), chunk2))
    key_chunk2 =  result_bytes2.decode()
    # chunk3 = key_expander[48:64].encode()
    # result_bytes3 = bytes(x ^ y for x, y in zip(key_string[0:16].encode(), chunk3))
    # key_chunk3 =  result_bytes3.decode()

    result_key += key_chunk1 + key_chunk2
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])
  
  return result_key_mix

def get_sbox_value(row, col):
  # Compute the index in the flat list
  index = 16 * row + col
  return sbox[index]

def get_inverse_sbox_value(row, col):
  # Compute the index in the flat list
  index = 16 * row + col
  return inverse_sbox[index]

def flip_row(input_string):
  result_string = ""
  for i in [5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10]:
      result_string += input_string[i*2:(i+1)*2]
  return result_string

def lazi_encrypt(input_hex):
  result_hex = ""
  for i in range (0,len(input_hex), 8):
    result_hex += input_hex[i+6:i+8]
    result_hex += format((int(input_hex[i+2:i+4],16) + int(input_hex[i+4:i+6],16) + int(input_hex[i+6:i+8],16)) % 256, '02x')
    result_hex += format((int(input_hex[i+4:i+6],16) + int(input_hex[i+6:i+8],16)) % 256, '02x')
    result_hex += format((int(input_hex[i:i+2],16) + int(input_hex[i+2:i+4],16) + int(input_hex[i+4:i+6],16) + int(input_hex[i+6:i+8],16)) % 256, '02x')

  return result_hex

def lazi_decrypt(input_hex):
  result_hex = ""
  for i in range (0,len(input_hex), 8):
    a4 = input_hex[i:i+2]
    a3 = format((int(input_hex[i+4:i+6],16) - int(a4,16)) % 256, '02x')
    a2 = format((int(input_hex[i+2:i+4],16) - int(a3,16) - int(a4,16)) % 256, '02x')
    a1 = format((int(input_hex[i+6:i+8],16) - int(a2,16) - int(a3,16) - int(a4,16)) % 256, '02x')
    result_hex += (a1+a2+a3+a4)

  return result_hex

def add_round_key(input_hex, key):
  key_hex = key.encode().hex()

  result_hex = bytearray(len(key_hex) // 2)
  for i in range(0,len(key_hex), 2):
    result_hex[i // 2] = int(input_hex[i:i+2], 16) ^ int(key_hex[i:i+2], 16)

  result_hex = bytes(result_hex).hex()
  return result_hex

def xor_key(input_hex, key_hex):
  result_hex = bytearray(len(key_hex) // 2)
  for i in range(0,len(key_hex), 2):
    result_hex[i // 2] = int(input_hex[i:i+2], 16) ^ int(key_hex[i:i+2], 16)

  result_hex = bytes(result_hex).hex()
  return result_hex

def string_padding(input_string):
  padding = len(input_string) % 16
  if padding != 0:
    input_string += "Z" * (16-padding)
  return input_string

def string_to_hex(input_string):
  hex_result = input_string.encode('utf-8').hex()  # Convert the chunk to hexadecimal representation # Append the hexadecimal representation to the list
  return hex_result

def hex_to_string(hex_string):
    # Remove any spaces and convert the string to lowercase
    hex_string = hex_string.replace(" ", "").lower()

    # Convert pairs of hexadecimal characters to bytes and then decode to a string
    normal_string = bytearray.fromhex(hex_string).decode('utf-8')

    return normal_string

def sbox_encrypt(input_hex):
  output_hex = ""
  for i in range(0, len(input_hex), 2):
    row = int(input_hex[i],16)
    col = int(input_hex[i+1],16)
    result_hex = format(get_sbox_value(row,col), '02x')
    output_hex += result_hex
  return output_hex

def sbox_decrypt(input_hex):
  output_hex = ""
  for i in range(0, len(input_hex), 2):
    row = int(input_hex[i],16)
    col = int(input_hex[i+1],16)
    result_hex = format(get_inverse_sbox_value(row,col), '02x')
    output_hex += result_hex
  return output_hex

def add_count(input_hex):
  result_hex = bytearray(len(input_hex) // 2)
  for i in range(0,len(input_hex), 2):
    result_hex[i // 2] = (int(input_hex[i:i+2], 16) + 1) % 16

  result_hex = bytes(result_hex).hex()
  return result_hex


def ecb_encrypt(input_hex, key, round):
  encrypted_hex = ""
  expanded_key = key_expansion(key,round)
  for i in range(0, len(input_hex), 32):
    chunk = input_hex[i:i+32]
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    encrypted_hex += result_hex
  return encrypted_hex

def ecb_decrypt(input_hex, key, round):
  decrypted_hex = ""
  expanded_key = key_expansion(key,round)
  for i in range(0, len(input_hex), 32):
    result_hex = input_hex[i:i+32]

    j = round
    while(j>0):
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      result_hex = lazi_decrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = sbox_decrypt(result_hex)
      j-=1

    result_hex = add_round_key(result_hex,expanded_key[0:16])
    decrypted_hex += result_hex
  return decrypted_hex

def cbc_encrypt(input_hex, key, round):
  encrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = input_hex[i:i+32]
    result_hex = xor_key(chunk, init_vector)
    result_hex = add_round_key(result_hex,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    init_vector = result_hex
    encrypted_hex += result_hex
  return encrypted_hex

def cbc_decrypt(input_hex, key, round):
  decrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    result_hex = input_hex[i:i+32]

    j = round
    while(j>0):
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      result_hex = lazi_decrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = sbox_decrypt(result_hex)
      j-=1

    result_hex = add_round_key(result_hex,expanded_key[0:16])
    result_hex = xor_key(result_hex, init_vector)
    init_vector = input_hex[i:i+32]
    decrypted_hex += result_hex
  return decrypted_hex

def cfb_encrypt(input_hex, key, round):
  encrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = init_vector
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    result_hex = xor_key(input_hex[i:i+32], result_hex)
    init_vector = result_hex
    encrypted_hex += result_hex
  return encrypted_hex

def cfb_decrypt(input_hex, key, round):
  decrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = init_vector
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    result_hex = xor_key(input_hex[i:i+32], result_hex)
    init_vector = input_hex[i:i+32]
    decrypted_hex += result_hex
  return decrypted_hex

def ofb_encrypt(input_hex, key, round):
  encrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = init_vector
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    init_vector = result_hex
    result_hex = xor_key(input_hex[i:i+32], result_hex)
    encrypted_hex += result_hex
  return encrypted_hex

def ofb_decrypt(input_hex, key, round):
  decrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = init_vector
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    init_vector = result_hex
    result_hex = xor_key(input_hex[i:i+32], result_hex)
    decrypted_hex += result_hex
  return decrypted_hex

def counter_encrypt(input_hex, key, round):
  encrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = init_vector
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    init_vector = add_count(init_vector)
    result_hex = xor_key(input_hex[i:i+32], result_hex)
    encrypted_hex += result_hex
  return encrypted_hex

def counter_decrypt(input_hex, key, round):
  decrypted_hex = ""
  expanded_key = key_expansion(key,round)
  init_vector = "1234567890ABCDEFABCDEF1234567890"
  for i in range(0, len(input_hex), 32):
    chunk = init_vector
    result_hex = add_round_key(chunk,expanded_key[0:16])

    j = 1
    while(j<=round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = add_round_key(result_hex,expanded_key[(j*4):(j*4)+16])
      j+=1

    init_vector = add_count(init_vector)
    result_hex = xor_key(input_hex[i:i+32], result_hex)
    decrypted_hex += result_hex
  return decrypted_hex

# key = 16, round = 10
# key = 24, round = 12
# key = 32, round = 14
# key = 32, round = 16

# apa itu key expansion wkwk

input_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32."
# input_string = "abcde"
key_string = "jKPmNqXoRvSbTdUw"
# key_string = "ZxRyTbDmFpHqWsEuJiOkLxNa"
# key_string = "eYsHnTjPfWqRdGmZxLcVbQaUoIkEpXyn"
input_string = string_padding(input_string)
input = string_to_hex(input_string)
print("key length: " + str(len(key_string)))

print("string length: " + str(len(input_string)))
print("length: " + str(len(input)))

print("input: " + input_string)
print("hex input: " + input)

encrypt_result = counter_encrypt(input, key_string, 10)
print("encrypt result: " + encrypt_result)

decrypt_result = counter_decrypt(encrypt_result, key_string, 10)
print("decrypt result: " + decrypt_result)

result = hex_to_string(decrypt_result)
print("result: " + result)

if(result == input_string):
  print("final check: complete")