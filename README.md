# Leetcode

*Author : wangwenju；QQ: 2413887576； 邮箱：wangwenju_wangs@163.com*

***

**specific task: 多标签文本分类任务**

***

+ <u>**文件说明**</u>

  + **排序** ：重重之重(Quick_sort), 核心思想：分治_递归算法，复杂度O（2^n）。

  + **动态规划** ： 思想~将大问题拆解子问题求解, 用空间换时间。

    + 问题理解：一定要理解dp[i],以i结尾所表示的含义

    + 初始状态：注意边界初始条件
    + 状态转移方程：样例dp[i] = max or min (dp[i-1],nums[i] )
    + 返回输出：return dp[-1] 或者max(dp), or sum(dp) 

  + **二叉树** :  所有二叉树可以理解为对树结构的遍历（前、中、后），遍历时需要注意结点的返 回值。

      			 样例 left = self.dfs(root.left,val1,val2), 参数val怎么传进去，返回left 是什么。

  + **单调栈**： 固定框架如下：

    ```python
    nums：输入数组
    #定义单调栈： monostack
    monostack= []
    #第一层遍历：
    for i in range(len(nums)):
        #第二层采用while循环,去除不满足条件的元素：
        while not monostack and mums[i] < mums[monostack[-1]]:
              monostack.pop()
        monostack.append(i)
        
    ```

    

