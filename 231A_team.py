n = int(input())
count = 0
if 1 <= n <= 1000:
    for i in range (n):
        num_task = str(input())
        if num_task.count("1") >= 2  : # num_task == "1 0 1" or num_task == "1 1 0" or num_task == "1 1 1" or num_task == "0 1 1"
            count += 1
    print(count)