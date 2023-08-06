# !/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
from os.path import basename
from .pathfinder_network import *
from .read_file import *


def cmap2graph(
        file,
        data_type,
        keyterms=None,
        read_from_file=True,
        encoding='utf-8',
        read_from=0,
        pfnet=False,
        max=None,
        min=None,
        r=np.inf):

    try:
        assert data_type in ['pair', 'array']
    except:
        print('\033[0;31m\nERROR: the value of "data_type" is unrecognized, '
              'it must be either "pair" or "array"!\033[0m')
        exit(1)

    G = nx.Graph()

    if read_from_file:
        G.name = basename(file.split('.')[0])

        # Step 1: read file, each line in the file, add each line into the list
        content = read_file(file, encoding=encoding)
    else:
        content = list(file)

    # Step 2: find data by index (i.e., the parameter 'read_from'), skip the unwanted content
    if type(read_from) == int:
        content = content[read_from:]
    elif type(read_from) in [tuple, list]:
        content = content[read_from[0]:read_from[1]]
    if data_type == 'array':
        # Step 3-1: convert the triangle matrix to a n*n matrix (if necessary)
        # this means a triangle matrix
        # add first row, this is m[0, 0]
        # add elements in each row until the number of elements equal to n

        if len(content[0]) != len(content[-1]):
            print('convert it into n*n array')
            content.insert(0, ['0'])
            for i in range(0, len(content)):
                while len(content[i]) != len(content):
                    content[i].append('')

            # Step 3-2: add value
            # for each element m[i, j]
            # for each element in the diagonal line
            # for each element in the upper part of the triangle
            for i in range(0, len(content)):
                for j in range(0, len(content)):
                    if i == j:
                        content[i][j] = '0'
                    elif i < j:
                        content[i][j] = content[j][i]

        # Step 3-3: convert each value from string to int
        array = np.zeros([len(content), len(content)])

        for i in range(0, len(content)):
            for j in range(0, len(content)):

                array[i, j] = float(content[i][j])

        # Step 4: calculate PFNet (if necessary)
        if pfnet:
            if max is not None and min is not None:  # similarity --> distances (if necessary)
                array = max - array + min
                # the value that out of range would be set as inf
                array = np.where((array >= min) & (array <= max), array, np.inf)

            array = floyd(array, r=r)

        # diagonal
        if pfnet:
            np.fill_diagonal(array, False)
        else:
            np.fill_diagonal(array, 0)

        # Step 5: convert it to a graph
        pairs = []
        if pfnet:
            start, end = np.where(np.tril(array) == True)
            for i in range(0, len(start)):
                pairs.append([keyterms[start[i]], keyterms[end[i]]])
            G.add_edges_from(pairs)
        else:
            for i in range(0, len(keyterms)):
                for j in range(0, len(keyterms)):
                    if array[i, j] != 0 and i != j:
                        pairs.append([keyterms[i], keyterms[j], array[i, j]])
            G.add_weighted_edges_from(pairs)

    elif data_type == 'pair':
        for pair in content:
            G.add_edge(pair[0], pair[1])

    return G
