"""
Program to find community in a social network based on similarity score of the
friendship network and collocation data of the nodes.

Python version: 2.7
Dependencies: networkx, matplotlib

Similarity score for friendship network can de determined form the adjcency matrix.
We are considering similarity to be 1 if they are friends
(there is an edge between two nodes) or 0 is they aren't friends
(there is no edge bewteen the two nodes).
Current implementation has a new randomly generated graph each time the program is run.
May want to change that!

Run Instructions:
Command: python community.py 50 data.csv 5
Where 50 is the no of nodes,
data.csv is the csv file with the collocation data
and 5 is the threshold
"""

import sys
import csv
from random import randint
import networkx as nx
import matplotlib.pyplot as plt


def generate_friendship_network(N):
    adj = [[0 for _ in range(0, N)] for _ in range(0, N)]
    for i in range(0, N):
        for j in range(0, i):
            adj[i][j] = adj[j][i] = randint(0, 1)
    return adj


def read_colocation_data(fileName):
    F = open(fileName, 'rb')
    reader = csv.reader(F)
    data = []
    for row in reader:
        data.append(row)
    F.close()
    return data


def colocation_similarity(data, N):
    SIMILARITY_MATRIX = [[0 for _ in range(0, N)] for _ in range(0, N)]
    for X in range(0, N):
        for Y in range(X, N):
            SIMILARITY = 0
            for i in range(0, 12):
                if data[X][i] == data[Y][i]:
                    SIMILARITY += 1
            SIMILARITY_MATRIX[X][Y] = SIMILARITY_MATRIX[Y][X] = SIMILARITY
    for X in range(0, N):
        SIMILARITY_MATRIX[X][X] = -1
    return SIMILARITY_MATRIX


def create_network(F, S, N, THRESHOLD):
    G = nx.Graph()
    G.add_nodes_from([x for x in range(0, N)])
    # WEIGHT_MATRIX = [[0 for _ in range(0, N)] for _ in range(0, N)]
    for X in range(0, N):
        for Y in range(X, N):
            WEIGHT = F[X][Y] + S[X][Y]
            if(WEIGHT >= THRESHOLD):
                G.add_edge(X, Y)
                G[X][Y]['weight'] = WEIGHT
            # WEIGHT_MATRIX[X][Y] = WEIGHT_MATRIX[Y][X] = WEIGHT
    return G


def create_network_for_node(F, S, N, THRESHOLD, CHOICE):
    G = nx.Graph()
    G = nx.Graph()
    G.add_nodes_from([x for x in range(0, N)])
    X = CHOICE
    # WEIGHT_MATRIX = [[0 for _ in range(0, N)] for _ in range(0, N)]
    for Y in range(0, N):
        WEIGHT = F[X][Y] + S[X][Y]
        if(WEIGHT >= THRESHOLD):
            G.add_edge(X, Y)
            G[X][Y]['weight'] = WEIGHT
        # WEIGHT_MATRIX[X][Y] = WEIGHT_MATRIX[Y][X] = WEIGHT
    return G


def main(argv=None):
    if argv is None:
        argv = sys.argv
    DATA = read_colocation_data(argv[2])
    S = colocation_similarity(DATA, int(argv[1]))
    F = generate_friendship_network(int(argv[1]))

    CHOICE = raw_input(
        "Enter node number or enter All for the whole network: ")
    if CHOICE == "All":
        G = create_network(F, S, int(argv[1]), int(argv[3]))
    else:
        G = create_network_for_node(
            F, S, int(argv[1]), int(argv[3]), int(CHOICE))

    plt.subplot(111)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    sys.exit(main())
