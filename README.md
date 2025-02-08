# DGT - My Python Code Collection

This repository contains Python code from my school projects and personal experiments. Some scripts are simple exercises, while others are small text-based games I created for fun.

---

## About This Repository
- School-related Python scripts
- Fun text-based games
- Random experiments and practice programs

This repository is mainly for personal storage and learning purposes.

---

## Code Examples
Here’s a simple example of message cipher and decipher:

```python
import random
text = input("Správa: ")
dot = text[0]
if dot == ":":
    text = text[1:]
    first = text[::2]
    second = text[1::2]
    for sym in first:
        numb = second[0]
        second = second[1:]
        sim = ord(sym) - int(numb)
        print(chr(sim), end="")
else:
    print(":", end="")
    for znak in text:
        num = random.randint(0, 9)
        ynak = ord(znak) + num
        print(chr(ynak), end="")
        print(num, end="")
