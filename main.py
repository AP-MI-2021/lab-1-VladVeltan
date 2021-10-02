def isprime(n):
    '''
    :param n: nr intreg pozitiv
    :return: daca n este prim sau nu
    '''
    d = 2
    i = 0
    if n == 1:
        return False
    for i in range (2,n//2+1):
        if n % i == 0:
            d = d+1
    if d == 2:
        return True
    return False
def get_product(lst):
    '''
    :param lst: lista de numere de tip intreg
    :return: returneaza produsul numerelor din lista data
    '''
    p = 1
    for i in range(len(lst)):
        p= p * lst[i]
    print(p)



def get_cmmdc_v1(x, y):
    '''
    :param x: nr intreg
    :param y: nr intreg
    :return: cmmdc a x si y
    '''
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x
def get_cmmdc_v2(x,y):
    '''
    :param x: nr intreg
    :param y: nr intreg
    :return: cmmmdc a x si y
    '''
    while y != 0:
        r = x % y
        x = y
        y = r
    return x
def main():
    '''
    interfata de tip consola
    '''
    shouldrun=True
    while shouldrun==True:
        print("1.Determinati daca un numar este prim:")
        print("2.Determinati produsul a n numere:")
        print("3.Determinati cmmdc a doua numere")
        print("x. Iesire")
        optiune=input("Alege optiune:")
        if optiune =="1":
            n=int(input("Alegeti numarul:"))
            print(isprime(n))
        elif optiune == "2":
            lst = []
            n = 0
            n = int(input("Introduceti numarul de numere ale listei:"))
            for i in range(n):
                x = int(input("Dati cele n numere: "))
                lst.append(x)
            print(get_product(lst))
        elif optiune == "3":
            print("1.Metoda -> scaderi repetate")
            print("2.Metoda -> impartiri repetate")
            optiune2=input("Alege optiune")
            if optiune2==1:
                x=int(input("Alege primul numar:"))
                y=int(input("Alege al doilea numar:"))
                print(get_cmmdc_v1(x, y))
            else:
                x = int(input("Alege primul numar:"))
                y = int(input("Alege al doilea numar:"))
                print(get_cmmdc_v2(x, y))
        elif optiune=="x":
                shouldrun=False
        else:
            print("Ati introdus o optiune gresita, mai incercati:")
main()
