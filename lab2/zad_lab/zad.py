from fileinput import filename
import re
import argparse


def replace_names(filename, old_func, new_func):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"No file {filename}")
        exit(2)
    non_comment_names = []
    all_file = f.read()
    comments_strings_re = rf"\".*?{old_func}.*?\"|'.*?{old_func}.*?'|#.*?{old_func}.*?\n"
    comments = list(re.finditer(comments_strings_re, all_file))
    all_names_re = rf"(?<![A-Za-z0-9_]){old_func}(?![A-Za-z0-9_])"
    all_names = list(re.finditer(all_names_re, all_file))

    for name in all_names:
        for c in comments:
            if c.start() <= name.span()[0] < c.end() or c.start() <= name.span()[1] < c.end():
                break
        else:
            non_comment_names.append(name)

    if len(non_comment_names) == 0:
        return

    subbed_file = all_file[:non_comment_names[0].span()[0]] + new_func
    for i in range(1, len(non_comment_names)):
        subbed_file += all_file[non_comment_names[i-1].span()[1]:non_comment_names[i].span()[0]] + new_func
    subbed_file += all_file[non_comment_names[-1].span()[1]:]

    f.close()
    try:
        with open(filename, "w") as f:
            f.write(subbed_file)
    except FileNotFoundError:
        print(f"No file {filename}")
        exit(2)

def merge_multiline_comments(filename):
    c1r = r"((#.*(\n|$))+)"
    try:
        content = open(filename, "r").read()
    except FileNotFoundError:
        print("No such file")
        exit(2)
    comments_strings_re = rf"\".*?\"|'.*?'"
    comments = list(re.finditer(comments_strings_re, content))
    
    comments_1 = list(re.finditer(c1r, content))

    non_string_comments = []
    for name in comments_1:
        for c in comments:
            if c.start() <= name.span()[0] < c.end() or c.start() <= name.span()[1] < c.end():
                break
        else:
            non_string_comments.append(name)
    
    # ^ make sure '#' is not inside ' ' or " "
    if len(non_string_comments) == 0:
        return

    new_content = content[:non_string_comments[0].span()[0]] + \
        re.sub("\n.*?#", "", content[non_string_comments[0].span()[0]:
                non_string_comments[0].span()[1]])
    for i, c in enumerate(non_string_comments):
        if i == 0:
            continue
        new_content += content[non_string_comments[i-1].span()[1]:c.span()[0]] + \
            re.sub("\n.*?#", "", content[c.span()[0]:c.span()[1]])

    else:
        new_content += content[non_string_comments[-1].span()[1]:]

    with open(filename, "w") as f:
        f.write(new_content)

def run(args):
    if args.file is None:
        while True:
            args.file = input('filename> ')
            for arg in args.names:
                packed = arg.split(sep=':')
                if len(packed) != 2:
                    raise Exception("Invalid names format")
                replace_names(args.file, packed[0], packed[1])
            if args.transform_comments:
                merge_multiline_comments(args.file)
    else:
        for arg in args.names:
            packed = arg.split(sep=':')
            if len(packed) != 2:
                raise Exception("Invalid names format")
            replace_names(args.file, packed[0], packed[1])
        if args.transform_comments:
            merge_multiline_comments(args.file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Renames selected functions")
    parser.add_argument('names', metavar='names', type=str, nargs=1,
                        help='list of function names')
    parser.add_argument('file', metavar='file', type=str, nargs='?',
                        help='python script name')
    parser.add_argument('--transform-comments',
                        help='remove multiline comments', action='store_true')
    args = parser.parse_args()
    run(args)
