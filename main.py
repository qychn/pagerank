from digraph import Digraph
from pagerank import pagerank
import datetime
import operator

if __name__ == '__main__':
    # 创建一个网络拓朴图
    dg = Digraph()

    # dg.add_edge(("1", "2"))
    # dg.add_edge(("1", "3"))
    # #dg.add_edge(("2", "5"))
    # dg.add_edge(("3", "1"))
    # dg.add_edge(("3", "2"))
    # dg.add_edge(("3", "5"))
    # dg.add_edge(("4", "5"))
    # dg.add_edge(("4", "6"))
    # dg.add_edge(("5", "4"))
    # dg.add_edge(("5", "6"))
    # dg.add_edge(("6", "4"))

    # 读取数据集
    with open('input/Wiki-Vote.txt', 'r') as f:
        data = f.readlines()
        for line in data[4:500]:
            split = line.strip().split("\t")
            dg.add_edge(tuple(split))

    start = datetime.datetime.now()
    page_ranks = pagerank(dg)
    end = datetime.datetime.now()
    print(end - start)
    sorted_x = sorted(page_ranks.items(), key=lambda x: x[1], reverse=True)
    # print("The final page rank is\n", page_ranks)

f = open('output/rank.csv', 'w')
for name in sorted_x:
    f.write("%s,%s\n" % (name[0], name[1]))
f.close()
