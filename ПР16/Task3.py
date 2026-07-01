server_A ={ "data.db", "image.png", "log.txt"}
server_B = { "image.png", "script.py", "data.db"}

print(f"Общие файлы: {server_A & server_B}")
print(f"Потерянные файлы: {server_A - server_B}")
