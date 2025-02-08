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
```

---

## Notes on Learning

I created this repository to store code as I learn Python. Some of these scripts are part of my schoolwork, while others are personal experiments to practice coding and problem-solving.

One of the scripts in this repository is a message cipher and decipher, which I created to practice basic encryption and decryption techniques.

Feel free to explore as I continue learning and experimenting with new ideas!

---
