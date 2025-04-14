from random import choice

def random_string() -> str:
    random_list: list[str] = [
        "Please try writing something more descriptive.",
        "Oh! It appears you writing something I don't understand.",
        "Do you mind trying to rephrase that?",
        "I'm terrible sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else"
    ]

    return choice(random_list)

if __name__ == '__main__':
    for i in range(5):
        print(random_string())