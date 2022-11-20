while True:
    s = input()
    if s == "0":
        break
     
    even = 0
    odd = 0
    for i in range(0, len(s), 2):
        even += ord(s[i]) - 48
    for i in range(1, len(s), 2):
        odd += ord(s[i]) - 48
 
    if abs(odd - even) % 11 == 0:
        print(f"{s} is a multiple of 11.")
    else:
        print(f"{s} is not a multiple of 11.")