import os
import time
import shutil

def monitor_log_file(log_file, template_file, destination_directory):
    processed_ids = set() # 做一个表

    while True:
        with open(log_file, 'r', encoding='utf-8') as file:  # 指定编码为utf-8
            lines = file.readlines() #读取日志
            for line in lines:
                if "LogOnline: STEAM: Adding P2P connection information with user " in line: #需要读取的日志内容
                    steam_id = line.split()[8] #第8段字符是Steam64ID
                    if line.split()[0] not in processed_ids and len(steam_id) == 17:
                        processed_ids.add(line.split()[0]) #第0段字符是时间
                        new_file_name = steam_id  # 保留文件名的第一个字符

                        # 复制并重命名文件
                        src_file = template_file
                        dst_file = os.path.join(destination_directory, f"{new_file_name}.sav")
                        shutil.copy(src_file, dst_file)

                        # 修改.sav文件
                        with open(dst_file, 'r+b') as sav_file:
                            content = sav_file.read()
                            player_steam_id_index = content.find(b"PlayerSteamID") + 43 #Steam64ID在存档中的位置，需要提前移除母档的Steam64ID
                            new_id = new_file_name.encode('utf-8')
                            content = content[:player_steam_id_index] + new_id + content[player_steam_id_index:]
                            sav_file.seek(0)
                            sav_file.write(content)
                            sav_file.truncate()

                        print(f"Processed and modified file: {new_file_name}.sav")

        time.sleep(1)  # 每秒检查一次日志文件

# 使用示例
log_file_path = r"C:\server_8\Dragons\Saved\Logs\Dragons.log"
template_file_path = r"C:\server_8\Dragons\Saved\SaveGames\0000.sav"
destination_directory_path = r"C:\server_8\Dragons\Saved\SaveGames\Players"

monitor_log_file(log_file_path, template_file_path, destination_directory_path)