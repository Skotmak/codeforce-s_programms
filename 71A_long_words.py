n = int(input())
if 1 <= n <= 100:
    for i in range (n):
        word = str(input())
        if len(word) > 10:
            count = str(len(word) - 2)
            print(word[0] + count + word[-1])
        else:
            print(word)
