#!/usr/bin/env python

import re
import sys

def replace_file_placeholder(line, filename):
    with open(filename) as f:
        lines = ["\"" + l.strip("\n").replace("\"", "\\\"") + "\""
                 for l in f.readlines()]
        lines = "[" + ", ".join(lines) + "]"
        return line.replace("{% " + filename + " %}", lines)


def main():
    placeholder = re.compile(r".*{% (?P<filename>[\w\.]+) %}.*")
    with open(sys.argv[1]) as template:
        for line in template.read().split("\n"):
            match = placeholder.match(line)
            if match:
                line = replace_file_placeholder(line, match.group("filename"))
            print(line)


if __name__ == '__main__':
    main()
