from digraph import Digraph
from pagerank import pagerank

if __name__ == '__main__':
    # 创建一个网络拓朴图
    dg = Digraph()

    dg.add_nodes(["A", "B", "C", "D"])
    dg.add_edge(("A", "B"))
    dg.add_edge(("A", "C"))
    dg.add_edge(("A", "D"))
    dg.add_edge(("B", "A"))
    dg.add_edge(("B", "C"))
    dg.add_edge(("C", "D"))
    dg.add_edge(("D", "A"))
    dg.add_edge(("D", "B"))

    page_ranks = pagerank(dg)

    print("The final page rank is\n", page_ranks)