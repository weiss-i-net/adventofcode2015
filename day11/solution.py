import itertools as it
import more_itertools as mit

def increment(pw):
    pw = list(pw)
    for i, char in reversed(list(enumerate(pw))):
        if char == 'z':
            pw[i] = 'a'
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break
    return ''.join(pw)


def find_next_pw(pw):
    while True:
        pw = increment(pw)
        if set("iol") & set(pw):
            continue
        if not any(ord(a)+2 == ord(b)+1 == ord(c) for a, b, c in mit.windowed(pw, 3)):
            continue
        if len(set(a for a, b in it.pairwise(pw) if a == b)) < 2:
            continue
        break
    return pw


pw = "hepxcrrq"
part_1 = find_next_pw(pw)
print(part_1)
print(find_next_pw(part_1))
