# Delazi Algorithm
# Irreducible Polynomial x^8 + x^7 + x^5 + x^3 + 1

# constants
SBOX = [
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

INVERSE_SBOX = [
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

# key expander (64 bytes)
KEY_EXPANDER_STRING = "gyattrizzlersigmaohiofanumtaxjdonmysoulshuwalahumbatugaskriptoduar"
KEY_EXPANDER_HEX = KEY_EXPANDER_STRING.encode('latin-1').hex()
# init_vector (16 bytes)
INIT_VECTOR_STRING = "adalahinitvector"
INIT_VECTOR_HEX = INIT_VECTOR_STRING.encode('latin-1').hex()

# helpers
# pad Z to string to make it 16 byte
def string_padding(input_string):
  padding = len(input_string) % 16
  output_string = input_string
  if padding != 0:
    output_string += "Z" * (16-padding)
  return output_string

# convert string to hex
def string_to_hex(string):
  hex = string.encode('latin-1').hex()
  return hex

# convert hex to string
def hex_to_string(hex):
  string = bytes.fromhex(hex).decode('latin-1')

  return string

# get round from key length
def get_round(length):
  if (length == 16):
    return 10
  elif (length == 24):
    return 12
  elif (length == 32):
    return 14

# input: a-b-c-d (4 bytes)
# output: d-c-b-a (4 bytes)
def mix_key(input):
  output = ""
  for i in range(3,-1,-1):
    output += input[i]
  return output

# get value of sbox from row-col
def get_sbox_value(row, col):
  # compute in flat list
  index = 16 * row + col
  return SBOX[index]

# get value of inverse sbox from row-col
def get_inverse_sbox_value(row, col):
  # compute in flat list
  index = 16 * row + col
  return INVERSE_SBOX[index]

# generate round key (round + 1 times):
# key = 16 byte -> round = 10 -> expand key to 4*(10 + 1) + 12 = 56 byte
# key = 24 byte -> round = 12 -> expand key to 4*(12 + 1) + 12 = 64 byte
# key = 32 byte -> round = 14 -> expand key to 4*(14 + 1) + 12 = 72 byte
# key = 32 byte -> round = 16 -> expand key to 4*(16 + 1) + 12 = 80 byte
def key_expansion(external_key_hex, round):
  result_key = external_key_hex

  # if external key is 16 byte (16 + 16 + 16 + 8)
  if (len(external_key_hex) == 32):
    # xor 16 bytes of external key with first 16 bytes of key expander
    expander_chunk1 = bytes.fromhex(KEY_EXPANDER_HEX[0:32])
    external_key_chunk1 = bytes.fromhex(external_key_hex[0:32])
    result_chunk1 = bytes(x ^ y for x, y in zip(expander_chunk1, external_key_chunk1)).hex()

    # xor 16 bytes of external key with second 16 bytes of key expander
    expander_chunk2 = bytes.fromhex(KEY_EXPANDER_HEX[32:2*32])
    result_chunk2 = bytes(x ^ y for x, y in zip(expander_chunk2, external_key_chunk1)).hex()

    # xor first 8 bytes of external key with last 8 bytes of key expander
    expander_chunk3 = bytes.fromhex(KEY_EXPANDER_HEX[2*32:2*40])
    external_key_chunk2 = bytes.fromhex(external_key_hex[0:2*8])
    result_chunk3 = bytes(x ^ y for x, y in zip(expander_chunk3, external_key_chunk2)).hex()

    # combine results
    result_key += result_chunk1 + result_chunk2 + result_chunk3
    # mix results
    result_key_mix = ""
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])

  # if external key is 24 byte (24 + 24 + 16)
  elif (len(external_key_hex) == 48):
    # xor 24 bytes of external key with first 24 bytes of key expander
    expander_chunk1 = bytes.fromhex(KEY_EXPANDER_HEX[0:48])
    external_key_chunk1 = bytes.fromhex(external_key_hex[0:48])
    result_chunk1 = bytes(x ^ y for x, y in zip(expander_chunk1, external_key_chunk1)).hex()

    # xor first 16 bytes of external key with last 16 bytes of key expander
    expander_chunk2 = bytes.fromhex(KEY_EXPANDER_HEX[48:80])
    external_key_chunk2 = bytes.fromhex(external_key_hex[0:32])
    result_chunk2 = bytes(x ^ y for x, y in zip(expander_chunk2, external_key_chunk2)).hex()

    # combine results
    result_key += result_chunk1 + result_chunk2
    # mix results
    result_key_mix = ""
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])

  # if external key is 32 byte and round is 14 (32 + 32 + 8)
  elif (len(external_key_hex) == 64 and round == 14):
    # xor 32 bytes of external key with first 32 bytes of key expander
    expander_chunk1 = bytes.fromhex(KEY_EXPANDER_HEX[0:64])
    external_key_chunk1 = bytes.fromhex(external_key_hex[0:64])
    result_chunk1 = bytes(x ^ y for x, y in zip(expander_chunk1, external_key_chunk1)).hex()

    # xor first 8 bytes of external key with last 8 bytes of key expander
    expander_chunk2 = bytes.fromhex(KEY_EXPANDER_HEX[64:80])
    external_key_chunk2 = bytes.fromhex(external_key_hex[0:16])
    result_chunk2 = bytes(x ^ y for x, y in zip(expander_chunk2, external_key_chunk2)).hex()

    # combine results
    result_key += result_chunk1 + result_chunk2
    # mix results
    result_key_mix = ""
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])

  # if external key is 32 byte and round is 16 (32 + 32 + 16)
  elif (len(external_key_hex) == 64 and round == 16):
    # xor 32 bytes of external key with first 32 bytes of key expander
    expander_chunk1 = bytes.fromhex(KEY_EXPANDER_HEX[0:64])
    external_key_chunk1 = bytes.fromhex(external_key_hex[0:64])
    result_chunk1 = bytes(x ^ y for x, y in zip(expander_chunk1, external_key_chunk1)).hex()

    # xor first 16 bytes of external key with last 16 bytes of key expander
    expander_chunk2 = bytes.fromhex(KEY_EXPANDER_HEX[64:96])
    external_key_chunk2 = bytes.fromhex(external_key_hex[0:32])
    result_chunk2 = bytes(x ^ y for x, y in zip(expander_chunk2, external_key_chunk2)).hex()

    # combine results
    result_key += result_chunk1 + result_chunk2
    # mix results
    result_key_mix = ""
    for i in range (0, len(result_key), 4):
      result_key_mix += mix_key(result_key[i:i+4])
  
  return result_key_mix

# lazi process: encrypt
def lazi_encrypt(input_hex):
  output_hex = ""
  # process every 4 bytes
  for i in range (0, len(input_hex), 8):
    # input: (a, b, c, d)
    # output: (d, b + c + d, c + d, a + b + c + d)
    output_hex += input_hex[i+6:i+8]
    output_hex += format((int(input_hex[i+2:i+4], 16) + int(input_hex[i+4:i+6], 16) + int(input_hex[i+6:i+8], 16)) % 256, '02x')
    output_hex += format((int(input_hex[i+4:i+6], 16) + int(input_hex[i+6:i+8], 16)) % 256, '02x')
    output_hex += format((int(input_hex[i:i+2], 16) + int(input_hex[i+2:i+4], 16) + int(input_hex[i+4:i+6], 16) + int(input_hex[i+6:i+8], 16)) % 256, '02x')

  return output_hex

# lazi process: decrypt
def lazi_decrypt(input_hex):
  output_hex = ""
  # process every 4 bytes
  for i in range (0, len(input_hex), 8):
    # input: (d, b + c + d, c + d, a + b + c + d)
    # output: (a, b, c, d)
    d = input_hex[i:i+2]
    c = format((int(input_hex[i+4:i+6], 16) - int(d, 16)) % 256, '02x')
    b = format((int(input_hex[i+2:i+4], 16) - int(c, 16) - int(d, 16)) % 256, '02x')
    a = format((int(input_hex[i+6:i+8], 16) - int(b, 16) - int(c, 16) - int(d, 16)) % 256, '02x')
    output_hex += (a + b + c + d)

  return output_hex

# xor block with round key
def xor_hex(input_hex, key_hex):
  input_chunk = bytes.fromhex(input_hex[0:32])
  key_chunk = bytes.fromhex(key_hex[0:32])
  result_hex = bytes(x ^ y for x, y in zip(input_chunk, key_chunk)).hex()
  return result_hex

# encrypt with sbox (row-col -> value)
def sbox_encrypt(input_hex):
  output_hex = ""
  for i in range(0, len(input_hex), 2):
    row = int(input_hex[i], 16)
    col = int(input_hex[i+1], 16)
    result_hex = format(get_sbox_value(row, col), '02x')
    output_hex += result_hex
  return output_hex

# decrypt with sbox (row-col -> value)
def sbox_decrypt(input_hex):
  output_hex = ""
  for i in range(0, len(input_hex), 2):
    row = int(input_hex[i], 16)
    col = int(input_hex[i+1], 16)
    result_hex = format(get_inverse_sbox_value(row, col), '02x')
    output_hex += result_hex
  return output_hex

# flip row
def flip_row_col(input_hex):
  output_hex = ""
  for i in [5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10]:
      output_hex += input_hex[i*2:(i+1)*2]
  return output_hex

# counter mode: increment each hex of input_hex by 1
def increment_counter(input_hex):
  output_hex = bytearray(len(input_hex) // 2)
  for i in range(0, len(input_hex), 2):
    output_hex[i // 2] = (int(input_hex[i:i+2], 16) + 1) % 256
  output_hex = bytes(output_hex).hex()

  return output_hex

# ecb mode: encrypt
def ecb_encrypt(input, external_key, round):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  encrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  # process every 16 bytes
  for i in range(0, len(input_hex), 32):
    chunk_hex = input_hex[i:i+32]

    # add round key
    result_hex = xor_hex(chunk_hex, expanded_key_hex[0:32])

    # round enciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    encrypted_hex += result_hex
  return encrypted_hex

# ecb mode: decrypt
def ecb_decrypt(input, external_key, round):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  decrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  # process every 16 bytes
  for i in range(0, len(input_hex), 32):
    result_hex = input_hex[i:i+32]

    # round deciphering
    j = round
    while (j > 0):
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      result_hex = lazi_decrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = sbox_decrypt(result_hex)
      j -= 1

    # inverse add round key
    result_hex = xor_hex(result_hex, expanded_key_hex[0:32])

    decrypted_hex += result_hex
  return decrypted_hex

# cbc mode: encrypt
def cbc_encrypt(input, external_key, round):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  encrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  # vector_hex = IV for first block
  #            = result of previous E function for next blocks
  vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), 32):
    # xor vector hex with plaintext
    chunk_hex = input_hex[i:i+32]
    result_hex = xor_hex(chunk_hex, vector_hex)

    # add round key
    result_hex = xor_hex(result_hex, expanded_key_hex[0:32])

    # round enciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    vector_hex = result_hex
    encrypted_hex += result_hex
  return encrypted_hex

# cbc mode: decrypt
def cbc_decrypt(input, external_key, round):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  decrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), 32):
    result_hex = input_hex[i:i+32]

    # round deciphering
    j = round
    while (j > 0):
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      result_hex = lazi_decrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = sbox_decrypt(result_hex)
      j -= 1

    # inverse add round key
    result_hex = xor_hex(result_hex, expanded_key_hex[0:32])
    
    # inverse xor vector hex
    result_hex = xor_hex(result_hex, vector_hex)

    vector_hex = input_hex[i:i+32]
    decrypted_hex += result_hex
  return decrypted_hex

# cfb mode: encrypt
def cfb_encrypt(input, external_key, round, cfb_size):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  encrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  vector_hex = INIT_VECTOR_HEX
  # process every cfb_size (2, 4, 8) bytes
  for i in range(0, len(input_hex), cfb_size*2):
    # add round key
    result_hex = xor_hex(vector_hex, expanded_key_hex[0:32])

    # round enciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    # xor cfb_size plaintext with first cfb_size of result of E function
    result_hex = xor_hex(input_hex[i:i+cfb_size*2], result_hex[0:cfb_size*2])
    vector_hex = vector_hex[cfb_size*2:32] + result_hex

    encrypted_hex += result_hex
  return encrypted_hex

# cfb mode: decrypt
def cfb_decrypt(input, external_key, round, cfb_size):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  decrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), cfb_size*2):
    # add round key
    result_hex = xor_hex(vector_hex, expanded_key_hex[0:32])

    # round deciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    # xor cfb_size ciphertext with first cfb_size of result of E function
    result_hex = xor_hex(input_hex[i:i+cfb_size*2], result_hex[0:cfb_size*2])
    vector_hex = vector_hex[cfb_size*2:32] + input_hex[i:i+cfb_size*2]

    decrypted_hex += result_hex
  return decrypted_hex

# ofb mode: encrypt
def ofb_encrypt(input, external_key, round, ofb_size):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  encrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), ofb_size*2):
    # add round key
    result_hex = xor_hex(vector_hex, expanded_key_hex[0:32])

    # round enciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    # xor ofb_size plaintext with first ofb_size of result of E function
    vector_hex = vector_hex[ofb_size*2:32] + result_hex[0:ofb_size*2]
    result_hex = xor_hex(input_hex[i:i+ofb_size*2], result_hex[0:ofb_size*2])

    encrypted_hex += result_hex
  return encrypted_hex

# ofb mode: decrypt
def ofb_decrypt(input, external_key, round, ofb_size):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  decrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), ofb_size*2):
    # add round key
    result_hex = xor_hex(vector_hex, expanded_key_hex[0:32])

    # round deciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    # xor ofb_size ciphertext with first ofb_size of result of E function
    vector_hex = vector_hex[ofb_size*2:32] + result_hex[0:ofb_size*2]
    result_hex = xor_hex(input_hex[i:i+ofb_size*2], result_hex[0:ofb_size*2])

    decrypted_hex += result_hex
  return decrypted_hex

# counter mode: encrypt
def counter_encrypt(input, external_key, round):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  encrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  init_vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), 32):
    result_hex = xor_hex(init_vector_hex, expanded_key_hex[0:32])

    # round enciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    # xor plaintext with result of E function (counter mode)
    result_hex = xor_hex(input_hex[i:i+32], result_hex)
    encrypted_hex += result_hex
    init_vector_hex = increment_counter(init_vector_hex)
  return encrypted_hex

# counter mode: decrypt
def counter_decrypt(input, external_key, round):
  input_hex, external_key_hex = string_to_hex(string_padding(input)), string_to_hex(external_key)

  decrypted_hex = ""
  expanded_key_hex = key_expansion(external_key_hex, round)
  init_vector_hex = INIT_VECTOR_HEX
  for i in range(0, len(input_hex), 32):
    result_hex = xor_hex(init_vector_hex, expanded_key_hex[0:32])

    # round deciphering
    j = 1
    while (j <= round):
      result_hex = sbox_encrypt(result_hex)
      result_hex = flip_row_col(result_hex)
      result_hex = lazi_encrypt(result_hex)
      result_hex = xor_hex(result_hex, expanded_key_hex[(j*8):(j*8)+32])
      j += 1

    # xor ciphertext with result of E function (counter mode)
    result_hex = xor_hex(input_hex[i:i+32], result_hex)
    decrypted_hex += result_hex
    init_vector_hex = increment_counter(init_vector_hex)
  return decrypted_hex

# main program
if __name__ == "__main__":
  input_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32."
  input_hex = string_to_hex(string_padding(input_string))

  # 16 byte = 128 bit
  # external_key_string = "eYsHnTjPfWqRdGmZ"

  # 32 byte = 256 bit
  external_key_string = "eYsHnTjPfWqRdGmZxLcVbQaUoIkEpXyn"

  external_key_hex = string_to_hex(external_key_string)

  print("Key length     : " + str(len(external_key_string)))
  print("Input length   : " + str(len(input_string)))

  print("Input          : " + input_string)

  # computation in hex
  round = get_round(len(external_key_string)) # temporary (user input)
  encrypt_result = ofb_encrypt(input_hex, external_key_hex, round, 2)
  print("Encrypt result : " + encrypt_result)

  decrypt_result = ofb_decrypt(encrypt_result, external_key_hex, round, 2)
  print("Decrypt result : " + hex_to_string(decrypt_result))

  # if(decrypt_result == input_string):
  #   print("Final check: complete")