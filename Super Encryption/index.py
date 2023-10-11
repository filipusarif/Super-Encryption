import string
import math

def substitusi_encript():
    plaintext = input("masukkan plain text: ")
    key = int(input("masukkan key(angka)"))
    
    # list yang berisikan semua 256 karakter
    all_letters= string.ascii_letters #256
        
    dict1 = {}

	# penjumlahan ascii karakter dengan key
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]

    # variable hasil cipher text
    cipher_txt=[]

    # pengulangan untuk pengecekan karakter
    for char in plaintext:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp =char
            cipher_txt.append(temp)
            
    cipher_txt= "".join(cipher_txt)
    
	# pengembalian hasil cipher text
    return cipher_txt


# Encryption
def orthogonal_encrypt(plain_text):  # Fungsi untuk enkripsi
    step_size = int(input("Masukkan kunci : "))
    matrix_representation = (
        []
    )  # Matriks kosong untuk menyimpan representasi matriks dari teks
    encrypted_text = ""  # Teks terenkripsi

    for i in range(step_size):  # Mengisi matriks dengan karakter dari teks
        matrix_row = []  # Baris matriks
        # Loop ini akan mengulangi sebanyak kolom yang diperlukan dalam matriks, dan jumlah kolom dihitung dengan
        # membagi panjang teks (len(plain_text)) dengan step_size, dan menggunakan math.ceil()
        # untuk memastikan hasil pembagian dibulatkan ke atas agar semua karakter teks dapat masuk.
        for j in range(math.ceil(len(plain_text) / step_size)):
            index = (
                j * step_size
                + i  # j = indeks kolom saat ini, step_size = jumlah baris, i = indeks baris saat ini
            )  # Indeks karakter yang akan dimasukkan ke dalam baris matriks
            if index < len(
                plain_text
            ):  # Jika masih ada karakter yang tersisa, masukkan karakter ke dalam baris matriks
                matrix_row.append(
                    plain_text[index]
                )  # Masukkan karakter ke dalam baris matriks
            else:  # Jika tidak ada karakter yang tersisa, masukkan karakter '@' ke dalam baris matriks
                matrix_row.append("@")  # Masukkan karakter '@' ke dalam baris matriks
        matrix_representation.append(
            matrix_row
        )  # Masukkan baris matriks ke dalam matriks representasi

    print("Matrix:\n")  # Tampilkan matriks representasi
    for row in matrix_representation:  # Untuk setiap baris dalam matriks representasi
        print(row)  # Tampilkan baris

    # proses enkripsi
    matrix_height = step_size  # Tinggi matriks
    matrix_width = math.ceil(len(plain_text) / matrix_height)  # Lebar matriks

    for i in range(matrix_height):  # Mulai dari baris terakhir
        if matrix_height % 2 == 0:  # Jika height matriks genap
            if i % 2 == 1:  # Pasti baris ganjil
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    if matrix_representation[i][j] != "@":  # Jika bukan karakter '@'
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    if matrix_representation[i][j] != "@":  # Jika bukan karakter '@'
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
        else:  # Jika height matriks ganjil
            if i % 2 == 1:  # Pasti baris genap
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    if matrix_representation[i][j] != "@":  # Jika bukan karakter '@'
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    if matrix_representation[i][j] != "@":  # Jika bukan karakter '@'
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
    return encrypted_text


# Decryption
def orthogonal_decrypt():  # Fungsi untuk dekripsi
    cipher_text = input("Masukkan Cipher text : ")
    step_size = int(input("Masukkan Key(angka) :"))
    matrix_height = step_size  # Tinggi matriks
    matrix_width = math.ceil(len(cipher_text) / matrix_height)  # Lebar matriks

    plain_text_matrix = (
        [  # Matriks kosong untuk menyimpan representasi matriks dari teks
            [" " for _ in range(matrix_width)] for _ in range(matrix_height)
        ]
    )

    idx = 0  # Indeks untuk mengakses karakter dalam teks terenkripsi

    for i in range(matrix_height):  # Mulai dari baris terakhir
        if matrix_height % 2 == 0:  # Jika tinggi matriks genap
            if i % 2 == 1:  # Jika baris genap
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks
        else:
            if i % 2 == 1:  # Jika baris genap
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks

    print("Matrix:\n")  # Tampilkan matriks representasi
    for row in plain_text_matrix:  # Untuk setiap baris dalam matriks representasi
        print(row)  # Tampilkan baris

    plain_text = ""  # Teks terdekripsi
    for j in range(matrix_width):  # Untuk setiap kolom dalam matriks representasi
        for i in range(matrix_height):  # Untuk setiap baris dalam matriks representasi
            if plain_text_matrix[i][j] != "@":  # Jika bukan karakter '@'
                plain_text += plain_text_matrix[i][
                    j
                ]  # Tambahkan karakter ke dalam teks terdekripsi

    return plain_text.replace("-", " ") # Kembalikan - menjadi spasi

def substitusi_decript(msg):
    key = int(input("masukkan kunci(angka) : "))
    
	# pengambilan 256 karakter ascii
    all_letters= string.ascii_letters
    
    dict2 = {}	
    
	# pengurangan ascii karakter dengan kunci
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
        
    # loop to recover plain text
    decrypt_txt = []

	# pengulangan untuk mengembalikan plain text
	# mengecek apakah char ada di msg
    for char in msg:
        # mengecek apakah char ada di all_letter ascii
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
            
    decrypt_txt = "".join(decrypt_txt)
    
	# mengembalikan Hasil decrypt 
    return decrypt_txt


def main():
    while (1):
        choice = int(
            input("\n----------------\nPlayfair Cipher\n----------------\n1. Enkripsi \n2. Dekripsi \n3. Keluar \nPilihan: "))
        if choice == 1:
            print("----------------")
            # memanggil function transposisi dengan parameter substitusi
			# function substitusi akan dieksekusi terlebih dahulu, untuk mendapatkan nilai yang akan digunakan sebagai parameter transposisi
            print("cipher text : ",orthogonal_encrypt(substitusi_encript()))
        elif choice == 2:
            print("----------------")
            # memanggil function substitusi dengan parameter transposisi
			# function transposisi akan dieksekusi terlebih dahulu, untuk mendapatkan nilai yang akan digunakan sebagai parameter substitusi
            print("plain text : ",substitusi_decript(orthogonal_decrypt()))
            
        elif choice == 3:
            exit()
        else:
            print("\nChoose correct choice: ")


if __name__ == "__main__":
    main()