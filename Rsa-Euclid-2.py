import random
import math, time

from hashlib import sha256

from pip._vendor.distlib.compat import raw_input


def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


#öklid algoritması
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular Inverse mevcut değil.')
    return x % m


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('İki numarada asal olmalı.')
    elif p == q:
        raise ValueError('Sayılar eşit olamaz')

    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = int(raw_input("e değerini girin (Örnek:523): "))

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = coprime(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)
    print("n değeri:",n)
    print("phi değeri:",phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(privatek, plaintext):
    # Unpack the key into it's components
    key, n = privatek

    # Convert each letter in the plaintext to numbers based on the character using a^b mod m

    numberRepr = [ord(char) for char in plaintext]
    print("Şifrelemeden önce numaralar gösteriliyor: ", numberRepr)
    cipher = [pow(ord(char), key, n) for char in plaintext]

    # Return the array of bytes
    return cipher


def decrypt(publick, ciphertext):
    # Unpack the key into its components
    key, n = publick

    # Generate the plaintext based on the ciphertext and key using a^b mod m
    numberRepr = [pow(char, key, n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    print("Çözülen numaralar gösteriliyor: ", numberRepr)

    # Return the array of bytes as a string
    return ''.join(plain)


def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed



def verify(receivedHashed, message):

    ourHashed = hashFunction(message)
    if receivedHashed == ourHashed:
        print("Doğrulama Başarılı: ",)
        print(receivedHashed, " = ", ourHashed)
    else:

        print("Doğrulama Başarısız")
        print(receivedHashed, " != ", ourHashed)


def main():
    p = int(input("Asal bir sayı gir(örnek:503) : "))
    q = int(input("Tekrar Asal sayı gir (İlk girdiğin ile aynı olamaz(Örnek:509)): "))



    public, private = generate_keypair(p, q)
    print("Ortak ve Özel  Anahtarlarınız üretiliyor...")
    print("Ortak anahtarınız ", public, " Özel anahtarınız ", private)
    message = input("Bir mesaj girin: ")
    print("")

    hashed = hashFunction(message)

    print("Mesajınız şifreleniyor ", private, " . . .")
    encrypted_msg = encrypt(private, hashed)
    print("Şifrelenmiş mesajınız: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print(encrypted_msg)

    print("")
    print("Mesajınız ortak anahtar ile çözülüyor ", public, " . . .")

    decrypted_msg = decrypt(public, encrypted_msg)
    print("Çözülen mesajınız: ")
    print(decrypted_msg)

    print("")
    print("Doğrulanıyor. . .")
    verify(decrypted_msg, message)
    print("Mesajınız: ", message)


main()



