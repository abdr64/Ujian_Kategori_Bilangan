angka = int(input('Ketik angka : '))
katBil = []

def bulat(no):
    if no == no :
        return katBil.append('bulat')

def cacah(no):
    if no > 0:
        return katBil.append('cacah')

def nol(no):
    if no == 0:
        return katBil.append('nol')

def poNe(no):
    if no > 0:
        return katBil.append('asli')
    elif no < 0:
        return katBil.append('negatif')

def gG(no):
    if no % 2 != 0:
        return katBil.append('ganjil')
    else:
        return katBil.append('genap')


def prima(no):
    for urut in range(2,no):
        if no % urut == 0:
            return katBil.append('komposit')
            break
        else:
            return katBil.append('prima')

bulat(angka)
cacah(angka)
nol(angka)
poNe(angka)
gG(angka)
prima(angka)

print(katBil)