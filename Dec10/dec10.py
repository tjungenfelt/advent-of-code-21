import fileinput

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

f_signs = {'{', '(', '[', '<'}
reverse_couples = {']': '[',
           '}': '{',
           ')': '(',
           '>': '<'}
couples = {'[': ']',
           '{': '}',
           '(': ')',
           '<': '>'}
score = 0

# PART I

def get_points(corrupt_sign):
    if corrupt_sign == ')':
        points = 3
    if corrupt_sign == ']':
        points = 57
    if corrupt_sign == '}':
        points = 1197
    if corrupt_sign == '>':
        points = 25137
    return points


for line in lines:
    forward = []
    for i in range(0, len(line)):
        if line[i] in f_signs:
            forward.append(line[i])
        else:
            if forward[len(forward)-1] == reverse_couples[line[i]]:
                forward = forward[:-1]
            else:
                score += get_points(line[i])
                break

print('Score: ', score)

# PART II


def update_score(corrupt_sign, current_score):
    current_score *= 5
    if corrupt_sign == ')':
        current_score += 1
    if corrupt_sign == ']':
        current_score += 2
    if corrupt_sign == '}':
        current_score += 3
    if corrupt_sign == '>':
        current_score += 4
    return current_score


score = []
corrupt = [False for line in lines]
l = -1
idx = 0

for line in lines:
    l += 1
    forward = []
    for i in range(0, len(line)):
        if line[i] in f_signs:
            forward.append(line[i])
        else:
            if forward[len(forward)-1] == reverse_couples[line[i]]:
                forward = forward[:-1]
            else:
                corrupt[l] = True
    forward.reverse()
    if not corrupt[l]:
        score.append(0)
        for sign in forward:
            score[idx] = update_score(couples[sign], score[idx])
        idx += 1

score.sort()
print('Score: ', score[int(len(score)/2)])
