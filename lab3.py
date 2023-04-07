import numpy as np

num_nodes = 6

def create_connectivity_matrix(adj_matrix):
    con_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    print("\nConnectivity matrix:")
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i][j] > 0:
                con_matrix[i][j] = 1
            else:
                con_matrix[i][j] = adj_matrix[i][j]
            print(con_matrix[i][j], end="\t")
        print()
    return con_matrix

def read_adjacency_matrix():
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    print("Adjacency matrix:")
    try:
        with open("matrix.txt", "r") as f:
            for i in range(num_nodes):
                adj_matrix[i] = [int(x) for x in f.readline().split()]
                print(*adj_matrix[i], sep="\t")
    except FileNotFoundError:
        print("Invalid file format or file not found.")
    return adj_matrix

def find_hamiltonian_cycle(k, connectivity_matrix, visited, path, start):
    found_cycle = False
    for v in range(num_nodes):
        if connectivity_matrix[v][path[k-1]] or connectivity_matrix[path[k-1]][v]:
            if k == num_nodes and v == start:
                found_cycle = True
            elif visited[v] == -1:
                visited[v] = k
                path[k] = v
                k1 = k + 1
                found_cycle = find_hamiltonian_cycle(k1, connectivity_matrix, visited, path, start)
                if not found_cycle:
                    visited[v] = -1
            else:
                continue
    return found_cycle

def is_hamiltonian_cycle(connectivity_matrix, visited, path, start):
    print("\nHamiltonian cycle:")
    for j in range(num_nodes):
        visited[j] = -1
    path[0] = start
    visited[start] = start

    if find_hamiltonian_cycle(1, connectivity_matrix, visited, path, start):
        pass
    else:
        print("Solution not found")

    return path

def print_cycle(adj_matrix, path):
    weight = 0
    print(" Edge : Weight ")
    for i in range(num_nodes):
        if i == num_nodes-1:
            print(f" {path[i]+1} - {path[0]+1} : {adj_matrix[path[i]][path[0]]}")
            weight += adj_matrix[path[i]][path[0]]
        else:
            print(f" {path[i]+1} - {path[i+1]+1} : {adj_matrix[path[i]][path[i+1]]}")
            weight += adj_matrix[path[i]][path[i+1]]
    print("\n Total weight of the path:", weight, "\n")

def main():
    adj_matrix = read_adjacency_matrix()
    connectivity_matrix = create_connectivity_matrix(adj_matrix)

    visited = np.zeros(num_nodes, dtype=int) - 1
    path = np.zeros(num_nodes, dtype=int)
    start = 0

    hamiltonian_cycle = is_hamiltonian_cycle(connectivity_matrix, visited, path, start)
    print_cycle(adj_matrix, hamiltonian_cycle)

if __name__ == '__main__':
    main()
