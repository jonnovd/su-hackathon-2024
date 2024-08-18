file1 = "train_labels1.csv"
file2 = "train_labels2.csv"

potholes = []

with open(file1) as f:
    lines = f.readlines()
    for line in lines:
        potholes.append(line.strip())

with open(file2) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line not in potholes:
            potholes.append(line)

print(potholes)

with open('train_labels.csv', 'w', newline='\n') as file:
    for i in range(len(potholes)):
        file.write(f"{potholes[i]}\n")