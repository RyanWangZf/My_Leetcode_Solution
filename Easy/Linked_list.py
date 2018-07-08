# -*- coding: utf-8 -*-
# Python 3.6.2 AMD 64
'''
Leetcode Primary Algorithm Practices (Linked list)
@url: https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/41/
'''

# -----
# 链表(linked-list)及其附属功能的Python实现
# 注意各方法下的异常处理功能
# ----

class Node(object):
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象(Node)
    
    item = Node(data) 
    实例化了一个包含data和next两个部分的节点
    其中next指向None
    '''
    def __init__(self,data,pnext=None):
        self.data = data
        self._next = pnext
    
    def __repr__(self):
        '''
        Node的字符输出
        '''
        return str(self.data)
        
class Linkedlist(object):

    def __init__(self):
        self.head = None
        self.length = 0
        
    def isEmpty(self):
        return (self.length==0)
        
    def append(self,dataOrNode):
        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        
        if not self.head: # 如果head指针为空
            self.head = item
            self.length += 1
        else:
            node = self.head # head指针非空
            while node._next:# 遍历节点直到最后一个节点
                node = node._next
            node._next = item # 使最后一个节点的next指向新插入的item节点
            self.length += 1
            
    def delete(self,index):
        
        if self.isEmpty():
            print("The linked-list is empty!")
            return 
        
        if index<0 or index>=self.length:
            print("Error: out of index")
            return 
        
        if index == 0: # 删除第一个节点
            self.head = self.head._next
            self.length -= 1
            return
        
        # 遍历以找到需要删除的节点
        # prev: 保存前一个节点对象
        # node: 保存当前节点对象
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
            
        if j == index:
            prev._next = node._next
            self.length -= 1
    
    def update(self,index,data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("Error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
            
        if j == index:
            node.data = data
            
    def getItem(self,index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("Error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        
        return node.data
        
    def getIndex(self,data):
        j = 0
        if self.isEmpty():
            print("this linked-list is empty!")
            return 
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1
        
        if j == self.length:
            print("{} not found".format(str(data)))
            return 
            
    def insert(self,index,dataOrNode):
        if self.isEmpty():
            print("this linked-list is empty!")
            return
        
        if index < 0 or index >= self.length:
            print("Error: out of index")
            return
        
        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        
        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return 
            
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
            
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1
    
    def clear(self):
        self.head = None
        self.length = 0
        
    def __repr__(self):
        '''字符串输出(Built-in)'''
        if self.isEmpty():
            return "Empty linked-list"
        node = self.head
        nlist = ""
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist
    
    def __getitem__(self,ind):
        '''指数[ind]索引获取数据(Built-in)'''
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("Error: out of index")
            return
        return self.getItem(ind)
    
    def __setitem__(self,ind,val):
        '''指数[ind]索引修改数据(Built-in)'''
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("Error: out of index")
            return
        self.update(ind,val)
    
    def __len__(self):
        '''返回list长度的特殊方法(Built-in)'''
        return self.length


# -----
# 以下为链表相关的算法解法
# -----

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    "1"
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
         
    
    
    
    
    
    
    
    
    
    
    