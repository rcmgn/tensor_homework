from collections import deque

with open("out.txt") as file:
    print("adfsfdsa")
    [last_line] = deque(file, maxlen=1) or ['']
    print(last_line)
