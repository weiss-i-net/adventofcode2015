import itertools as it
seq = "1113222113"

for i in range(50):
    if i == 40:
        print(len(seq))
    seq = "".join(
            str(sum(1 for _ in group)) + key
            for key, group in it.groupby(seq)
            )

print(len(seq))
