#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     12/02/2019
# Copyright:   (c) Lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print ('=======================================================')
print ('PROGRAM MENENTUKAN BILANGAN TERBESAR DARI TIGA BILANGAN')
print ('=======================================================')

def pengulangan():
    print ('Coba masukan bilangan yang anda inginkan ? ')
    a=int(input('Bilangan ke 1 = '))
    b=int(input('Bilangan ke 2 = '))
    c=int(input('Bilangan ke 3 = '))

    if a>b and a>c:
        if b>c:
            print (a, 'terbesar dan', c, 'terkecil')
        else:
            print (a, 'terbesar dan', b, 'terkecil')
    elif b>a and b>c:
        if a>c:
            print (b, 'terbesar dan', c, 'terkecil')
        else:
            print (b, 'terbesar dan', a, 'terkecil')
    else:
        if a>b:
            print (c, 'terbesar dan', b, 'terkecil')
        else:
            print (c, 'terbesar dan', a, 'terkecil')

    print ('')
    print ('ingin coba lagi? (ya/tidak)')
    x=input()
    if x=='ya':
        return pengulangan()
    if x=='tidak':
        print('=======================================================')
        print ('       TERIMAKASIH TELAH MENGGUNAKAN PROGRAM KAMI')
        print ('=======================================================')

pengulangan()
