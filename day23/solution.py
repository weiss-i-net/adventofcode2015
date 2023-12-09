with open("input") as f:
    program = f.read().splitlines()

for is_part_2 in (0, 1):
    reg = { "a": is_part_2, "b": 0 }
    pc = 0
    while pc in range(len(program)):
        inst, *args = program[pc].split()
        if inst == "hlf":
            reg[args[0]] //= 2
        elif inst == "tpl":
            reg[args[0]] *= 3
        elif inst == "inc":
            reg[args[0]] += 1
        elif inst == "jmp":
            exec("pc = pc"+args[0])
            continue
        elif inst == "jie":
            if reg[args[0][0]] % 2 == 0:
                exec("pc = pc"+args[1])
                continue
        elif inst == "jio":
            if reg[args[0][0]] == 1:
                exec("pc = pc"+args[1])
                continue
        pc += 1
    print(reg["b"])



