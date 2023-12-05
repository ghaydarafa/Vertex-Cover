import tracemalloc
import time
import sys

def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)

    for child in adj[src]:
        if child != par:
            # not including source in the vertex cover
            dp[src][0] = dp[child][1] + dp[src][0]

            # including source in the vertex cover
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])

def minSizeVertexCover(adj, N):
    dp = [[0 for j in range(2)] for i in range(N+1)]
    for i in range(1, N+1):
        # 0 denotes not included in vertex cover
        dp[i][0] = 0

        # 1 denotes included in vertex cover
        dp[i][1] = 1

    dfs(adj, dp, 1, -1)

    # printing minimum size vertex cover
    print(min(dp[1][0], dp[1][1]))

def read_adjacency_list(file_path):
    with open(file_path, "r") as file:
        # Read the number of nodes from the first line
        num_nodes = int(file.readline().strip())
        # Initialize an empty list to store the adjacency list
        adjacency_list = []

        # Read the adjacency list for each node
        for line in file:
            neighbors = list(map(int, line.strip().split()))
            adjacency_list.append(neighbors)

    adjacency_list.insert(0, [])
    return adjacency_list, num_nodes

def run_and_measure(filename):
    adj_list, num_nodes = read_adjacency_list(filename)

    # Mengatur batas rekursi agar sesuai dengan jumlah node
    sys.setrecursionlimit(num_nodes + 1)

    # Menjalankan fungsi minSizeVertexCover
    print(f"=== {filename.upper()} ===")
    print("Minimum size vertex cover:")
    
    tracemalloc.start()
    start_time = time.time()
    minSizeVertexCover(adj_list, num_nodes)
    end_time = time.time()
    memory_stats = tracemalloc.get_traced_memory()[1] / 1000000
    tracemalloc.stop()
    
    runtime_in_seconds = end_time - start_time
    runtime_in_milliseconds = runtime_in_seconds * 1000

    print(f"Runtime: {runtime_in_milliseconds:.6f} ms")
    print(f"Memory: {memory_stats:.6f} MB")
    print()
