def tower_hanoi(n, a, b, c,):
    if n == 1:
        print(f"Move disk 1 from rod {a} to rod {c}")
        return
    tower_hanoi(n - 1, a, c, b)
    print(f"Move disk {n} from rod {a} to rod {c}")
    tower_hanoi(n - 1, b, a, c)

tower_hanoi(10, "a", "b", "c")