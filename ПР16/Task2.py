allowed_id = {10, 20, 30}
input_id = [20, 40, 10, 50]

for i in range(len(input_id)):
    if input_id[i] not in allowed_id:
        allowed_id.add(input_id[i])
        print("ADDED")
    else:
        print("OK")
