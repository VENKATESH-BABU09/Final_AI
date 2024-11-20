from itertools import permutations


def solve_crypt(words,result):
    unique_chars=set("".join(words)+result)
    if len(unique_chars)>10:
        return False
    
    for perm in permutations(range(10),len(unique_chars)):
        char_to_dig=dict(zip(unique_chars,perm))

        if char_to_dig[words[0][0]]==0 or char_to_dig[words[1][0]]==0 or char_to_dig[result[0]]==0:
            continue
        def word_to_num(word):
            return int("".join(str(char_to_dig[char]) for char in word))
        

        if word_to_num(words[0])+word_to_num(words[1])==word_to_num(result):
            print("we got mapping:")
            for char,dig in char_to_dig.items():
                print(f"{char}->{dig}")

            return True
        
    return False


words=["SEND","MORE"]
result="MONEY"

if solve_crypt(words,result):
    print("yes")
else:
    print("no")