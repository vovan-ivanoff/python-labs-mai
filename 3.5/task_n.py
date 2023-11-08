import json

file_1, file_2 = input(), input()
with open(file_1, 'r') as f:
    data_1 = json.load(f)
with open(file_2, 'r') as f:
    data_2 = json.load(f)
data_1 = {i["name"]: {k: v for k, v in i.items() if k != "name"} for i in data_1}
for d in data_2:
    if d["name"] in data_1:
        for key in d:
            if (key not in data_1[d["name"]] or d[key] > data_1[d["name"]][key]) and key != "name":
                data_1[d["name"]][key] = d[key]
    else:
        data_1[d["name"]] = {k: v for k, v in d.items() if k != "name"}
with open(file_1, 'w') as g:
    json.dump(data_1, g, ensure_ascii=False, indent=4)