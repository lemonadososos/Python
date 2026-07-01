message = input("Введите предложение (из-за /помех/ слова могут дублироваться в разных местах: ")

message = message.split()
message = set(message)

print("Количество слов: ", len(message))

print("Слова:", end=" ")
print(*message, sep=", ")
