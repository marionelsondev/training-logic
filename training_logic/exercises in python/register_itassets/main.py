itAssetId = []
itName = []
itAssetType = []
itAssetValue = []
itAssetDepartment = []
countItAssetId = 0
addItAsset = "S"

while addItAsset == "S":
    itAssetId.append(countItAssetId)
    itName.append(input("Enter the name of the equipment: \n"))
    itAssetType.append(input("Enter the type of equipment: \n"))
    itAssetValue.append(float(input("Enter the value of the equipment: \n")))
    itAssetDepartment.append(input("Enter the department where the equipment is located: \n"))
    countItAssetId += 1
    addItAsset = input("Type 'S' to register a new IT asset or press enter to exit the program: \n").upper()

for index in range(0, len(itAssetId)):
    print("-------------------------------\n","ID:", (index+1))
    print("Name:", itName[index])
    print("Type:", itAssetType[index])
    print("Value:", itAssetValue[index])
    print("Department:", itAssetDepartment[index])