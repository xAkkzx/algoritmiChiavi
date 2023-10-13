def operazioneStupida(a, e, m):
    return (a**e) % m

def operazionePocoIntelligente(a, e, m):
    num = bin(e)
    b = num.split('b')
    numb = b[1]
    numb = numb[::-1]
    tot = 1
    count = -1
    for i in numb:
        k = int(i)
        count+=1
        tot *= a**(k*(2**count))
    return tot % m

def operazioneIntelligente():
    return 0

print("Choice of function to perform: ")
print("1. Stupid operation")
print("2. LittleIntelligent operation")
print("3. Intelligent operation")
scelta = input("Type 1, 2, 3 or 4(EXIT) and press enter: ")

#switch case by choice
while(True):
    if scelta == "1":
        print(operazioneStupida(611, 9876, 10007))
    elif scelta == "2":
        print(operazionePocoIntelligente(611, 9876, 10007))
    elif scelta == "3":
        print(operazioneIntelligente())
    elif scelta == "4":
        break
    else:
        print("Invalid choice")

    scelta = input("Type 1, 2, 3 or 4(EXIT) and press enter: ")
    
