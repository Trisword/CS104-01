names = []
for x in range(10):
    acceptedname = input("Enter Name:")
    names.append(acceptedname)

print(names)

for x in range(len(names)):
    print(names.pop(0))
