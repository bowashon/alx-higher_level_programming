#!/usr/bin/python3
"""This module defining a class Node that defines a node of a singly linked list"""


class Node:
    """Define class Nose that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """instantiate the class
        Attribute:
        data: The data to store in the node.
        next_node: The next node in the linked list (default is None).
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ To retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Returns the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Defines the next_node """
        if not isinstance(value, Node) and value not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a class singlylinkedlist"""

    def __init__(self):
        """Initialize the head to None"""
        self.__head = None

    def __str__(self):
        """Return a string representation of the linked list."""
        current = self.__head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """insets new node to a singly linked list:
	Args:
	value: the node to insert
	"""
        new_node = Node(value)

        if not self.__head:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
