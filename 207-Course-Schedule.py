from typing import List
from collections import deque # 双端队列
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 核心:有向图判环
        indegree=[0]*numCourses
        adj=[[] for i in range(numCourses)]
        for e in prerequisites:
            a=e[1] #先修课程
            b=e[0] #目标课程
            #变为全局变量
            adj[a].append(b)
            indegree[b]+=1
        
        st=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                st.append(i)
        n=0
        while st: #如果中途为空就一定是True 如果开始为空就是False
            i=st.popleft()
            n+=1
            for j in adj[i]:
                indegree[j]-=1
                if indegree[j]==0:
                    st.append(j)
        return n==numCourses
