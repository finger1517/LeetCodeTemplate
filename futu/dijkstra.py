def dijkstra_find_min_path(start, matrix):
    passed = [start]
    nopass = [x for x in range((len(matrix))) if x!=start]
    dis = matrix[start]
    while len(nopass):
        # print(nopass)
        idx = nopass[0]
        for i in nopass:
            if dis[i]<dis[idx]:
                idx=i
        nopass.remove(idx)
        passed.append(idx)
        for i in nopass:
            if dis[idx]+matrix[idx][i]<dis[i]:
                dis[i] = dis[idx]+matrix[idx][i]
    return dis
if __name__=="__main__":
    inf = 9999
    matrix = [[0,6,3,inf,inf,inf,inf],
         [6,0,2,5,inf,inf],
         [3,2,0,3,4,inf],
         [inf,5,3,0,2,3],
         [inf,inf,4,2,0,5],
         [inf,inf,inf,3,5,0]]
    a_start_minpath = dijkstra_find_min_path(0,matrix)
    a2d_minpath = a_start_minpath[3]
    print(a2d_minpath)
    
    
# 使用dijkstra算法找到a到所有点的最小路径长，然后提取a到d的最短路径