import csv
import random
import math

INPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_input\sentences.tsv"
OUTPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_output\columnar.csv"

def generate_numeric_key():
    length = random.randint(3, 9)
    digits = list(range(1, length + 1))
    random.shuffle(digits)
    return digits  # return as list of ints

def columnar_transposition_encrypt(text, key_digits):
    text = text.lower()

    n_cols = len(key_digits)
    n_rows = math.ceil(len(text) / n_cols)

    # Pad with 'x'
    padded_length = n_rows * n_cols
    text += 'x' * (padded_length - len(text))

    # Build grid row-wise
    grid = [text[i:i+n_cols] for i in range(0, len(text), n_cols)]

    ciphertext = ""
    for digit in sorted(key_digits):
        col_index = key_digits.index(digit)
        for row in grid:
            ciphertext += row[col_index]

    return ciphertext


def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as tsvfile, \
         open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as csvfile:

        reader = csv.reader(tsvfile, delimiter="\t")
        writer = csv.writer(csvfile)

        writer.writerow(["original_sentence", "encrypted_sentence", "key", "cipher"])

        for row in reader:
            if not row:
                continue

            original = row[0].strip()
            if not original:
                continue

            key_digits = generate_numeric_key()
            encrypted = columnar_transposition_encrypt(original, key_digits)

            # Convert key list to string like "31452"
            key_string = ''.join(str(d) for d in key_digits)

            writer.writerow([original, encrypted, key_string, "columnar"])


if __name__ == "__main__":
    main()