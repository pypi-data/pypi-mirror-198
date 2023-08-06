# !/usr/bin/env python
# -*- coding: utf-8 -*-

def read_file(filepath,
              encoding='utf-8'):

    content = []
    f = open(filepath, "r", encoding=encoding)
    for line in f.readlines():
        line = line.strip('\n')  # remove "\n" in "node1 \t node2 \n"
        if '\t' in line:
            # split to each element in a list by "\t"
            content.append(line.split('\t'))
        else:
            # split to each element in a list by " " (i.e., space)
            line = line.split(' ')
            if '' in line:
                line.remove('')  # delete the element that have "" value
            content.append(line)
    f.close()
    return content
