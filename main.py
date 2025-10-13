import re
from collections import Counter

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

def frequently_repeated_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    freq = Counter(words)
    word, count = freq.most_common(1)[0]
    print(f"Most common word: '{word}' (occurs {count} times)")
    return word, count



def hash_text(text):
    hash_val = 5381
    for c in text:
        hash_val = ((hash_val << 5) + hash_val) + ord(c)
    return hash_val & 0xFFFFFFFF 



def encoding_text(text, sdvig=3):
    return ''.join(chr((ord(c) + sdvig) % 65536) for c in text)



def decoding_text(text, sdvig=3):
    return ''.join(chr((ord(c) - sdvig) % 65536) for c in text)



def analize_text(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]
    if not sentences:
        print("No offers found.")
        return
    avg = sum(lengths) / len(lengths)
    longest = sentences[lengths.index(max(lengths))]
    print(f"Average sentence length: {RESET}{GREEN}{avg:.2f} words{RESET}")
    print(f"The longest sentence: '{longest}'")
    return avg, longest



def statistics_of_text(text):
    lines = text.splitlines()
    words = re.findall(r'\b\w+\b', text)
    chars = len(text)
    unique_words = len(set(words))
    print(f"Number of words: {RESET}{YELLOW}{len(words)}{RESET}")
    print(f"Number of characters: {RESET}{YELLOW}{chars}{RESET}")
    print(f"Number of lines: {RESET}{YELLOW}{len(lines)}{RESET}")
    print(f"Unique words: {RESET}{YELLOW}{unique_words}{RESET}")
    return len(words), chars, len(lines), unique_words



def sort_by_lines_length(text):
    lines = text.splitlines()
    sorted_lines = sorted(lines, key=len)
    print("\nStrings sorted by length:")
    for line in sorted_lines:
        print(line)
    return '\n'.join(sorted_lines)



if __name__ == "__main__":
    text_example = """Это пример текста.
Текст используется для тестирования функций.
Это простой текст для анализа возможностей редактора!
петя петя петя это не петя а это э"""

    frequently_repeated_word(text_example)
    print("Text hash:", f"{RESET}{BLUE}{hash_text(text_example)}{RESET}")

    coded = encoding_text(text_example)
    decoded = decoding_text(coded)
    print("Decoding is correct:", f"{RESET}{GREEN}{decoded == text_example}{RESET}")

    analize_text(text_example)
    statistics_of_text(text_example)
    sort_by_lines_length(text_example)