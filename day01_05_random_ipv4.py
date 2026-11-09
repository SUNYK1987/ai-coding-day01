import random

segments = [
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
]
ipv4 = ".".join(str(segment) for segment in segments)
print("随机产生的IPv4地址为: " + ipv4)
