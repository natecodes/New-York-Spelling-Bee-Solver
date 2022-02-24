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

    for word in sorted(answer, key=len):
        if len(word) >= 4: print(word)

solver(['n','l','b','u','e','i', 'f'], 'f')