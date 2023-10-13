def operazioneStupida(a, e, m):
    return (a**e) % m

def operazionePocoIntelligente(a, e, m):
    num = bin(e)
    a = num.split('b')
    numb = a[1]
    
    return numb

def operazioneIntelligente():
    return 0

print(operazioneStupida(611, 9876, 10007))

print("Choice of function to perform:")
print("1. Stupid operation")
print("2. LittleIntelligent operation")
print("3. Intelligent operation")
scelta = input("Type 1, 2, 3 or 4(EXIT) and press enter:")

#switch case by choice
while(True):
    if scelta == "1":
        a = input("Type a: ")
        e = input("Type e: ")
        m = input("Type m: ")
        print(operazioneStupida(a, e, m))
    elif scelta == "2":
        a = input("Type a: ")
        e = input("Type e: ")
        m = input("Type m: ")
        print(operazionePocoIntelligente(a, e, m))
    elif scelta == "3":
        a = input("Type a: ")
        e = input("Type e: ")
        m = input("Type m: ")
        print(operazioneIntelligente())
    elif scelta == "4":
        break
    else:
        print("Invalid choice")

    scelta = input("Type 1, 2, 3 or 4(EXIT) and press enter:")
    
print(operazionePocoIntelligente(1, 20,1))