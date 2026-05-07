from collections import Counter
import string

FILE_NAME = "frequency.txt"

try:
    with open(FILE_NAME, "r") as f:
        text = f.read()

        text = text.lower()

        text = text.translate(str.maketrans('', '', string.punctuation))

        words = text.split()

        word_count = Counter(words)

        print("---- Word Frequency Analyzer ----")

        for word, count in word_count.items():
            print(f"{word} : {count}")

        print("\n---- Top 5 Most Common Words ----")
        for word, count in word_count.most_common(5):
            print(f"{word} : {count}")

except FileNotFoundError:
    print("File Not Found")