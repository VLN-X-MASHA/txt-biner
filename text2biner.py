#!/@Syntax Error/vanxzz
import os
from InquirerPy import inquirer

def text_to_binary(text):
    """Ubah teks (termasuk angka/simbol) menjadi biner"""
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Ubah biner menjadi teks biasa"""
    binary_values = binary.split()
    ascii_chars = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_chars)

def format_binary_columns(binary_str, per_line=4, space=1, indent=2):
    """Format biner agar kolom rata vertikal dengan indent"""
    bytes_list = binary_str.split()
    lines = []
    for i in range(0, len(bytes_list), per_line):
        line_bytes = bytes_list[i:i+per_line]
        line_str = (' ' * space).join(line_bytes)
        if i != 0:
            line_str = (' ' * indent) + line_str
        lines.append(line_str)
    return '\n'.join(lines)

def clear():
    os.system('clear')

while True:
    clear()
    print("\n══════════[ BINER CONVERTER ]══════════\n")
    
    pilihan = inquirer.select(
        message="PILIH MENU:",
        choices=[
            "UBAH TEKS KE CODE BINER",
            "UBAH CODE BINER KE TEKS",
            "KELUAR DARI BINER CONVERTER"
        ],
        default="UBAH TEKS KE CODE BINER"
    ).execute()

    if pilihan == "UBAH TEKS KE CODE BINER":
        teks = inquirer.text(message="masukkan teks :").execute()
        hasil = text_to_binary(teks)  # mentah
        # Salin ke clipboard Termux
        os.system(f'echo "{hasil}" | termux-clipboard-set')
        print(f"\nCODE BINER:\n❯ {format_binary_columns(hasil)}")
        print("\n(Hasil biner sudah disalin ke clipboard HP)")
        input("\nTekan Enter untuk lanjut...")

    elif pilihan == "UBAH CODE BINER KE TEKS":
        biner = inquirer.text(message="Masukkan code biner : ").execute()
        hasil = binary_to_text(biner)
        print(f"\nHASIL TEKS:\n❯ {hasil}")
        input("\nTekan Enter untuk lanjut...")

    elif pilihan == "KELUAR DARI BINER CONVERTER":
        print("\nSampai jumpa!")
        clear()
        break