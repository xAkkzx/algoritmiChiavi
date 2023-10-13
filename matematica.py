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

def operazioneIntelligente(a, e, m):
    num = bin(e)
    b = num.split('b')
    numb = b[1]
    numb = numb[::-1]
    tot = 1
    count = -1
    for i in numb:
        k = int(i)
        count+=1
        tot *= (a**(k*(2**count)))%m
    return tot % m

print("Choice of function to perform: ")
print("1. Stupid operation")
print("2. LittleIntelligent operation")
print("3. Intelligent operation")
choice = input("Type 1, 2, 3 or 4(EXIT) and press enter: ")

#switch case by choice
while(True):
    if choice == "1":
        a = int(input("Type a: "))
        e = int(input("Type e: "))
        m = int(input("Type m: "))
        print(operazioneStupida(a, e, m))
    elif choice == "2":
        a = int(input("Type a: "))
        e = int(input("Type e: "))
        m = int(input("Type m: "))
        print(operazionePocoIntelligente(a, e, m))
    elif choice == "3":
        a = int(input("Type a: "))
        e = int(input("Type e: "))
        m = int(input("Type m: "))
        print(operazioneIntelligente(a, e, m))
    elif choice == "4":
        break
    else:
        print("Invalid choice")

    choice = input("Type 1, 2, 3 or 4(EXIT) and press enter: ")
    
