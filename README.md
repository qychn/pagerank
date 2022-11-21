# PageRank模拟谷歌搜索引擎
## 介绍
数据使用的是:维基百科投票决定晋升为行政长官（至2008年1月）。


数据集介绍：

`Wiki-Vote.txt`: A->B意味着用户A投票支持B成为维基百科管理员。由该数据来构建图，计算pagerank值

实现功能包括：
1. 根据`Wiki-Vote.txt`构建图
2. 计算pagerank值

项目结构：
```
-- input
    Wiki-Vote.txt 
-- output
    rank.csv // rank值保结果
digraph.py // 有向图的实现类
pagerank.py // 计算pagerank值的类实现
main.py // 程序入口文件
```

## run 
```
python3 main.py
```
