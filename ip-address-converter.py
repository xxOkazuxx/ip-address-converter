def ip_to_binary(ip_address):
    octets = [int(octet) for octet in ip_address.split('.')]

    binary_octets = [format(octet, '08b') for octet in octets]

    binary_string = '.'.join(binary_octets)

    return binary_string


ip = input("IPv4アドレスを入力してください：")

# 変換
binary_result = ip_to_binary(ip)

# ワンライナーverは以下
# binary_result = '.'.join([format(octet, '08b') for octet in [int(octet) for octet in ip.split('.')]])

print(f"IPアドレス {ip}の2進数表現：")
print(binary_result)