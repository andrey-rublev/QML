import csv
import random
import string
import os

INPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_input\sentences.tsv"
OUTPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_output\vigenere.csv"

def generate_random_key(min_len=3, max_len=10):
    key_length = random.randint(min_len, max_len)
    key = ""

    for _ in range(key_length):
        rand_num = random.randint(0, 25)
        key += chr(rand_num + ord('a'))

    return key


def vigenere_cipher(text, key):
    result = ""
    key_index = 0
    key_length = len(key)

    for char in text:
        if char in string.ascii_lowercase:
            shift = ord(key[key_index % key_length]) - ord('a')
            new_index = (ord(char) - ord('a') + shift) % 26
            result += chr(new_index + ord('a'))
            key_index += 1
        else:
            result += char  # leave non-letters unchanged

    return result


def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as tsvfile, \
         open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as csvfile:

        reader = csv.reader(tsvfile, delimiter="\t")
        writer = csv.writer(csvfile)

        writer.writerow([
            "original_sentence",
            "encrypted_sentence",
            "key",
            "cipher"
        ])

        for row in reader:
            if not row:
                continue

            original = row[0].strip().lower()

            if not original:
                continue

            key = generate_random_key()
            encrypted = vigenere_cipher(original, key)

            writer.writerow([
                original,
                encrypted,
                key,
                "vigenere"
            ])


if __name__ == "__main__":
    main()