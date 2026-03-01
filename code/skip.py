import csv
import random
from math import gcd

INPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_input\sentences.tsv"
OUTPUT_PATH = r"C:\Users\nikhi\Downloads\QML\data_output\skip.csv"


def generate_coprime_key(length, min_skip=2, max_skip=10):
    """Generate a random skip (key) coprime with text length."""
    possible_keys = [k for k in range(min_skip, max_skip + 1) if gcd(k, length) == 1]
    if not possible_keys:
        return 1
    return random.choice(possible_keys)


def skip_cipher_coprime(text, key):
    """Skip cipher using coprime key — full-length permutation."""
    n = len(text)
    if n == 0:
        return ""
    
    result = []
    index = 0
    for _ in range(n):
        result.append(text[index])
        index = (index + key) % n
    
    return "".join(result)


def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as tsvfile, \
         open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as csvfile:

        reader = csv.reader(tsvfile, delimiter="\t")
        writer = csv.writer(csvfile)

        writer.writerow(["original_sentence", "encrypted_sentence", "key", "cipher"])

        for row in reader:
            if not row:
                continue

            original = row[0].strip().lower()
            if not original:
                continue

            key = generate_coprime_key(len(original), 2, 10)
            encrypted = skip_cipher_coprime(original, key)

            writer.writerow([original, encrypted, key, "skip"])


if __name__ == "__main__":
    main()