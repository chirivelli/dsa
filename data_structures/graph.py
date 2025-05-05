from collections import defaultdict

class DAG:
    def __init__(self):
        self.adj = defaultdict(list)

def main():
    dag = DAG()
    edges = [[1,2], [2,3], [2,4], [3,4]]
    for u, v in edges:
        dag.adj[u].append(v)
        dag.adj[v].append(u)

    print(dag.adj)


if __name__ == '__main__':
    main()