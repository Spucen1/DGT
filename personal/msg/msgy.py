import random
import ast
text = input("Msg: ")
dot = text[0]
if dot == ":":
    key = input("Key: ")
    key = ast.literal_eval(key)
    text = text[1:]
    first = text[::2]
    second = text[1::2]
    reversed_second = [''] * len(second)
    for original_index, shuffled_index in enumerate(key):
        reversed_second[shuffled_index] = second[original_index]
    reversed_second = ''.join(reversed_second)
    for sym in first:
        numb = reversed_second[0]
        reversed_second = reversed_second[1:]
        sim = ord(sym) - int(numb)
        print(chr(sim), end="")
else:
    nums = ""
    char = ""
    for znak in text:
        num = random.randint(0, 9)
        ynak = ord(znak) + num
        nums = nums + str(num)
        char = char + chr(ynak)
    indicies = list(range(len(nums)))
    shuffled_i = indicies[:]
    random.shuffle(shuffled_i)
    shuffled_nums = ''.join(nums[i] for i in shuffled_i)
    encode = ''.join(a + b for a, b in zip(char, shuffled_nums))
    print("Code: :" + encode)
    print("Key: " + str(shuffled_i))


