print("Hello Welcome to my the Command Line Password Helper!")
print()
x = input("Please Enter the Password to be Evaluated: ")
symbols=['!','?','.','@','#','$','%','^','&','*','(',')','+','=']
print("Beggining Analysis Now...\n")
print("Starting Length Check...")
errorCount =0
passC=0
if(len(x)>=8):
    print("Passed Length Check...\n")
else:
    print("Failed Length Check...\nConsider making your password 8 characters or more!\n")
    errorCount = errorCount+1
print("Starting Symbols Check...")
for i in symbols:    
    if i in x:
        print("Passed Symbols Check...\n")
        break
    else:
        passC=0
if(passC==0):
    print("Failed Symbols Check...\n")
    errorCount = errorCount+1
print("Starting Lowercase Check...")
for i in x:
    if i>='a' and i<='z':
        print("Passed Lowercase Check...\n")
        break
    else:
        passC=0
if(passC==0):
    print("Failed Lowercase Check...\n")
    errorCount = errorCount+1
print("Starting Uppercase Check...")
for i in x:
    if i>='A' and i<='Z':
        print("Passed Uppercase Check...\n")
        passC=1
        break
    else:
        passC=0
if(passC==0):   
    print("Failed Uppercase Check...\n")
    errorCount = errorCount+1
print("Starting Numbers Check...")
for i in x:
    if i.isnumeric():
        print("Passed Numbers Check...\n")
        passC=1
        break
    else:
        passC=0
if (passC==0):
    print("Failed Numbers Check...\n")
    errorCount=errorCount+1

