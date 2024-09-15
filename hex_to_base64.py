import base64
import os

while True:
    # 提示用户输入十六进制字符串
    hex_strings = input("请输入十六进制字符串（多个项目请使用逗号或空格分隔）：")

    # 如果用户没有输入内容，直接跳过本次操作
    if not hex_strings:
        print("未提供输入。跳过此操作。")
        continue

    # 处理输入的字符串，支持逗号和空格分隔
    hex_strings = hex_strings.replace(',', ' ').split()

    base64_results = []

    for hex_string in hex_strings:
        try:
            # 检查十六进制字符串是否以'0x'开头（不区分大小写），如果是则移除
            if hex_string[:2].lower() == "0x":
                hex_string = hex_string[2:]

            # 检查十六进制字符串的长度是否有效
            if len(hex_string) % 2 != 0:
                raise ValueError("十六进制字符串长度无效。长度必须是偶数才能转换为字节。")

            # 将十六进制字符串转换为字节
            hex_bytes = bytes.fromhex(hex_string)

            # 将字节编码为BASE64字符串
            base64_string = base64.b64encode(hex_bytes).decode('utf-8')

            # 将结果添加到列表中
            base64_results.append(f"{base64_string}")
            
        except ValueError as e:
            base64_results.append(f"十六进制字符串错误 {hex_string}: {e}")

    # 打印所有结果，每行一个
    for result in base64_results:
        print(result)
    
    # 提示用户
    user_input = input("按 Enter 继续，输入 exit 退出，输入 clear 清除：").lower()
    if user_input == 'exit':
        break
    elif user_input == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')