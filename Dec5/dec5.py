import fileinput

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

df_list = []