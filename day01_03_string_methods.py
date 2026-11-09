version_raw = "  Cisco IOS XE Software, Version 17.03.04  "
# 1. 去掉首尾空格
version_stripped = version_raw.strip()
print("去掉首尾空格：" + version_stripped)
# 2. 转成全大写
version_upper = version_stripped.upper()
print("转成全大写：" + version_upper)
# 3. 替换版本号
version_replaced = version_stripped.replace("17.03.04", "17.06.01")
print("替换版本号：" + version_replaced)