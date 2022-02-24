from english_words import english_words_lower_alpha_set


class Solution:
    def __init__(self):
        self.get_letters()
        self.solver()

    def solver(self):
        answer = set()
        for word in english_words_lower_alpha_set:
            valid = False
            if self.special in word:
                valid = True

            for c in word:
                if c not in self.letters:
                    valid = False
                    break

            if valid:
                answer.add(word)

        print("\nPotential answers:")
        for word in sorted(sorted(answer), key=len):
            if len(word) >= 4:
                print(word)

    def get_letters(self):
        self.letters = input("What are the letters today?: ")
        self.special = input("What is the special letter?: ")

        if self.special not in self.letters:
            self.letters.append(self.special)


test = Solution()
