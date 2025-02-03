import sys
from kanji_list import kanji_n1, kanji_n5

def add_kanji():
    kanji = input("Enter kanji: ")
    onyomi = input("Enter onyomi: ")
    kunyomi = input("Enter kunyomi: ")
    examples_onyomi = input("Enter examples for onyomi (comma separated): ").split('、')
    examples_kunyomi = input("Enter examples for kunyomi (comma separated): ").split('、')
    
    return {
        "kanji": kanji,
        "onyomi": onyomi,
        "kunyomi": kunyomi,
        "examples_onyomi": examples_onyomi,
        "examples_kunyomi": examples_kunyomi
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: py populate.py <kanji_list>")
        sys.exit(1)

    kanji_list_name = sys.argv[1]
    kanji_list = globals().get(kanji_list_name)

    if kanji_list is None:
        print(f"Kanji list '{kanji_list_name}' not found.")
        sys.exit(1)

    while True:
        new_kanji = add_kanji()
        kanji_list.append(new_kanji)
        print(f"Added {new_kanji} to {kanji_list_name}.")
        cont = input("Do you want to add another kanji? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()