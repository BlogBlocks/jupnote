def random_line(filename):
    line_num = 0
    selected_line = ''
    with open(filename) as f:
        while 1:
            line = f.readline()
            if not line: break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line
    return selected_line.strip()