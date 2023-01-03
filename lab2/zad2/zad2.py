import re


def get_tokens(line: str) -> str:
    num_pattern = r"0|[1-9][0-9]*" # don't match 0123 as number, but rather 0 and 123
    it = re.finditer(num_pattern, line)
    prev = 0
    result = ""
    for i in it:
        if prev != i.start(0) and line[prev:i.start(0)] != ' ':
            result += (f"String: {line[prev:i.start(0)]}\n")
        result += (f"Number: {line[i.start(0):i.end(0)]}\n")
        prev = i.end(0)
    if prev != len(line):
        result += f"String: {line[prev:]}"

    return result if result[-1] != '\n' else result[:-1]


if __name__ == "__main__":
    while True:
        line = input('> ')
        if line == '\x04': # break on Ctrl-D @ windows
            break
        print(get_tokens(line))
        