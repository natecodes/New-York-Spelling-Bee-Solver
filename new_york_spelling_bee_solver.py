from english_words import english_words_lower_alpha_set

def solver(letters, special):
    answer = set()
    for word in english_words_lower_alpha_set:
        valid = False
        if special in word:
            valid = True

        for c in word:
            if c not in letters:
                valid = False
                break
            
        if valid: answer.add(word)

    print("\nPotential answers:")
    for word in sorted(sorted(answer), key=len):
        if len(word) >= 4: print(word)

def get_letters():
    letters = input("What are the letters today?\n")
    letters = [c for c in letters]
    special = input("What is the special letter?\n")

    if special not in letters:
        letters.append(special)

    return letters, special

solver(*get_letters())