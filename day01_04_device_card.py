hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"
label_hostname = "设备名称"
label_ip = "管理地址"
label_vendor = "厂商"
label_model = "型号"
label_os = "系统版本"

def display_width(text):
    width = 0
    for char in text:
        width += 2 if ord(char) > 127 else 1
    return width

labels = [label_hostname, label_ip, label_vendor, label_model, label_os]
max_len = max(display_width(label + ":") for label in labels)

def device_line(label, value):
    padding = " " * (max_len - display_width(label + ":") + 1)
    return label + ":" + padding + value

print("=" * 10 + " 设备信息 " + "=" * 10)
print(device_line(label_hostname, hostname))
print(device_line(label_ip, ip))
print(device_line(label_vendor, vendor))
print(device_line(label_model, model))
print(device_line(label_os, os_version))
print("=" * 30)
