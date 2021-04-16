"""
File: fizzbuzz.py
------------------
This program will play a classic kids game, where you take turns counting,
but if the number is divisible by 3 you say "fizz",
and if it's divisible by 5 you say "buzz",
and if it's divisible by both you say "fizzbuzz".
"""

def main():
    for i in range(1, 21):
        div3 = bool(i % 3)
        div5 = bool(i % 5)
        print(div3 * div5 * str(i) + (not div3) * "fizz" + (not div5) * "buzz")


if __name__ == '__main__':
    main()
