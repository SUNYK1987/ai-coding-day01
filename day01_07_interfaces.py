interfaces = [
    {"name": "Gi0/0", "status": "up", "speed": "1G"},
    {"name": "Gi0/1", "status": "down", "speed": "1G"},
    {"name": "Gi0/2", "status": "up", "speed": "10G"},
]


def display_width(text):
    width = 0
    for char in text:
        width += 2 if ord(char) > 127 else 1
    return width


def pad(text, width):
    return text + " " * (width - display_width(text))


print(pad("接口", 10) + pad("状态", 8) + "速率")
print("-" * 20)
for interface in interfaces:
    print("{:<10}{:<8}{}".format(interface["name"], interface["status"], interface["speed"]))
