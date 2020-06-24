# -*- coding:utf-8 -*-
import random
import time

'''
öklid->ebob
'''
t0 = time.clock()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
genişletilmiş öklid algoritması
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y


    if temp_phi == 1:
        print "phi: ", phi
        return d  + phi



'''
Asal Testi
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

'''def asal(kaca_kadar):

    asallar = list()
    if kaca_kadar < 2:
        return None
    elif kaca_kadar == 2:
        return asallar
    else:
        for i in range(3,kaca_kadar):
            bolundu = False
            for j in range(2,i):
                if i % j == 0:
                    bolundu=True
                    break
            if bolundu == False:
                asallar.append(i)
    return asallar'''



def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('İki sayıda asal olmalı.')
    elif p == q:
        raise ValueError('p ve q değeri eşit olamaz')
    # n = pq
    n = p * q
    print "n : ", n

    # Phi
    phi = (p - 1) * (q - 1)


    # e ve phi'ye eygun bir asal sayı seç
    e = int(raw_input("e değerini girin (Örnek:523): "))

    '''def is_prime2(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
       # print(n)
        return True

    # Driver function
    t0 = time.time()
    c = 0  # for counting

    for n in range(p, p*q):
        x = is_prime2(n)
        c += x

    print "Araliktaki toplam asal sayi :", c

    t1 = time.time()
    print "Desifreleme anahtarinin bulunmasi icin gecen sure :", t1 - t0'''


    '''start3 = time.time()
    lower = int(p)
    upper = int(p * q)

    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num),
    end3 = time.time()
    time_taken3 = end3 - start3
    print "Desifrelenme anahtarinin bulunma suresi", time_taken3'''


    # öklid kullanarak phiyi doğrula
    g = gcd(e, phi)
    while g != 1:
        e =int
        g = gcd(e, phi)

    # öklid kulanarak özel anahtar oluştur

    d = multiplicative_inverse(e, phi)


    # Ortak anahtar  (e, n) özel anahtar(d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    # Anahtar Bileşenleri
    key, n = pk
    # Her girdiyi a^b mod m ile karaktere dayalı sayıya  dönüştürür.
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Listeye byte olarak döndürür

    return cipher



def decrypt(pk, ciphertext):

    key, n = pk
    # Ciphertext ten yararlanarak şifreli metni düz metine dönüştürür.
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Dizideki byteları string olarak döndürür.
    return ''.join(plain)







if __name__ == '__main__':
    '''
    
    '''

    p = int(raw_input("Asal bir sayı gir(örnek:503) : "))
    q = int(raw_input("Tekrar Asal sayı gir (İlk girdiğin ile aynı olamaz(Örnek:509)): "))

    #print "\n".join(map(str, asal(p * q)))



    public, private = generate_keypair(p, q)
    print "Ortak ve Özel  Anahtarlarınız üretiliyor..."

    print "Ortak anahtarınız ", public, " Özel anahtarınız ", private
    message = raw_input("Bir mesaj girin: ")
    print "Lütfen Bekleyin ..."

    start = time.time()
    encrypted_msg = encrypt(private, message)
    end = time.time()
    time_taken = end - start

    print "Şifrelenmiş mesajınız: "

    start3 = time.time()
    print ''.join(map(lambda x: str(x), encrypted_msg))
    end3= time.time()
    time_taken3 = end - start3

    print "Şifreniz anahtar ile çözülüyor ", public, " . . ."
    print "Mesajınız:"

    start2 = time.time()
    print decrypt(public, encrypted_msg)
    end2 = time.time()
    time_taken2 = end2 - start2
    print "Desifreleme anahtarinin bulunma suresi", time_taken
    print "Sifreleme suresi:", time_taken3
    print "Desifreleme suresi:", time_taken2
    print time.clock(), "Toplamda Geçen süre: "


