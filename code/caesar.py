import csv
import random
import string

INPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_input\sentences.tsv"
OUTPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_output\ceasar.csv"

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char in string.ascii_lowercase:  # only shift a-z
            new_index = (ord(char) - ord('a') + shift) % 26
            result += chr(new_index + ord('a'))
        else:
            result += char  # leave everything else unchanged

    return result


def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as tsvfile, \
         open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as csvfile:

        reader = csv.reader(tsvfile, delimiter="\t")
        writer = csv.writer(csvfile)

        writer.writerow([
            "original_sentence",
            "encrypted_sentence",
            "shift",
            "cipher"
        ])

        for row in reader:
            if not row:
                continue

            original = row[0].strip().lower()

            if not original:
                continue

            shift = random.randint(1, 25)
            encrypted = caesar_cipher(original, shift)

            writer.writerow([
                original,
                encrypted,
                shift,
                "caesar"
            ])


if __name__ == "__main__":
    main()