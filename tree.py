#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:03:12 2021

@author: joan
"""
from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self):
        self.num_children = 0

    @abstractmethod
    def predict(self, x):
        pass


class Parent(Node):
    def __init__(self, feature_index, feature_value):
        super().__init__()
        self.feature_index = feature_index
        self.threshold = feature_value
        self.children = []
        self.left_child = None
        self.right_child = None

    def add_children(self, left, right):
        self.left_child = left
        self.right_child = right
        self.num_children = 2
        self.children = [left, right]

    def predict(self, x):
        if x[self.feature_index] < self.threshold:
            return self.left_child.predict(x)
        else:
            return self.right_child.predict(x)

    def __str__(self):
        return 'Parent k={}, v={}'.format(self.feature_index, self.threshold)


class Leaf(Node):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def predict(self, x):
        return self.label

    def __str__(self):
        return 'Leaf label={}'.format(self.label)



