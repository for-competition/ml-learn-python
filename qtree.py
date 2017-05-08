# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:27:33 2017
@author: zackery
"""
#四叉树节点
class Node(object):
    def __init__(self):
        self.data = ()
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None

#建立地图四叉树        
class Qtree(Node):
    #获取给定区块的中心坐标
    def get_center(self,l,r,t,b):
        lat = round((t + b) /2,6)
        lng = round((l + r) /2,6)
        return (lat,lng)
    #获取四分以后每个区块的边
    def get_child_edge(self,l,r,t,b,n):
        if n == 1:
            return [self.get_center(l,r,t,b)[1],r,t,self.get_center(l,r,t,b)[0]]
        elif n == 2:
            return [l,self.get_center(l,r,t,b)[1],t,self.get_center(l,r,t,b)[0]]
        elif n == 3:
            return [l,self.get_center(l,r,t,b)[1],self.get_center(l,r,t,b)[0],b]
        elif n == 4:
            return [self.get_center(l,r,t,b)[1],r,self.get_center(l,r,t,b)[0],b]
        
    def create_tree(self, tree,l,r,t,b):
        if r-l<=0.02 or t-b<=0.02:
            tree.data = (l,r,t,b)
        else:
            data = self.get_center(l,r,t,b)
            tree.data = data
            tree.child1 = Node()
            edge1 = self.get_child_edge(l,r,t,b,1)
            self.create_tree(tree.child1,edge1[0],edge1[1],edge1[2],edge1[3])
            tree.child2 = Node()
            edge2 = self.get_child_edge(l,r,t,b,2)
            self.create_tree(tree.child2,edge2[0],edge2[1],edge2[2],edge2[3])
            tree.child3 = Node()
            edge3 = self.get_child_edge(l,r,t,b,3)
            self.create_tree(tree.child3,edge3[0],edge3[1],edge3[2],edge3[3])
            tree.child4 = Node()
            edge4 = self.get_child_edge(l,r,t,b,4)
            self.create_tree(tree.child4,edge4[0],edge4[1],edge4[2],edge4[3])
    #求四叉树高度        
    def tree_height(self,tree):
        if len(tree.data) == 4:
            return 1
        d1 = d2 = d3 = d4 = 1
        d1 += self.tree_height (tree.child1)
        d2 += self.tree_height (tree.child2)
        d3 += self.tree_height (tree.child3)
        d4 += self.tree_height (tree.child4)
        return max(d1,d2,d3,d4)
    
    def visit(self,tree):
        if len(tree.data) >= 2:
            print(str(tree.data) + '\t')
    #先序遍历
    def pre_order(self,tree):
        if tree is not None:
            self.visit (tree)
            self.pre_order (tree.child1)
            self.pre_order (tree.child2)
            self.pre_order (tree.child3)
            self.pre_order (tree.child4)
    #后序遍历
    def post_order(self,tree):
        if tree is not None:
            self.post_order (tree.child1)
            self.post_order (tree.child2)
            self.post_order (tree.child3)
            self.post_order (tree.child4)
            self.visit (tree)
            
t=Node()
tree=Qtree()
tree.create_tree(t,116.1,116.75,40.2,39.6)
tree.tree_height(t)
#找到订单所在的块

        
    
    
        
        
        
        
        