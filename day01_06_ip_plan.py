devices = [
    {"name": "CoreSwitch", "ip": "10.1.1.1", "role": "核心交换机"},
    {"name": "Firewall", "ip": "10.1.1.2", "role": "防火墙"},
    {"name": "WLC", "ip": "10.1.1.3", "role": "无线控制器"},
]

def display_width(text):
    width = 0
    for char in text:
        width += 2 if ord(char) > 127 else 1
    return width


def pad(text, width):
    return text + " " * (width - display_width(text))


print(pad("设备名称", 18) + pad("管理地址", 18) + "角色")
for device in devices:
    print("{:<18}{:<18}{}".format(device["name"], device["ip"], device["role"]))
