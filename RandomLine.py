def randomline(filename):
    import FileLen
    from random import randint
    Max = FileLen.filelen(filename)
    num = randint(0, Max)
    with open(filename) as f:
        for i, STR in enumerate(f, 1):
            if i == num:
                break
    print STR
    