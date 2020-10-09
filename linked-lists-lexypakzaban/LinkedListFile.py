import sys
from typing import Generic, TypeVar, List
T = TypeVar("T")

class LL_Node(Generic[T]):
    def __init__(self, value:T = None, next: "LL_Node[T]" = None):
        self.set_value(value)
        self.set_next(next)

    def has_next(self):
        return self.next is not None

    def get_next(self)->"LL_Node[T]":
        return self.next

    def get_value(self) -> T:
        return self.value

    def set_value(self,in_val:T):
        self.value = in_val

    def set_next(self,nxt: "LL_Node[T]"):
        self.next = nxt

class LinkedList(Generic[T]):
    def __init__(self):
        self.start:LL_Node[T] = None
        #self.length = 0

    def is_empty(self):
        return self.start is None

    def add_to_end(self, item:T):
        """
        appends a node with the given value at the end of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :return: None
        """
        # OK, I've written this one for you, to get you started.
        if self.start is None:
            self.start = LL_Node[T](value=item)
        else:
            p:LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            p.set_next(LL_Node[T](value=item))
        #self.length += 1

    def add_to_start(self, item:T):
        """
        inserts a node with the given value at the start of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :return: None
        """
        new_node = LL_Node[T](value=item)
        if self.is_empty():
            self.start = new_node

        else:
            new_node.set_next(self.start)
            self.start = new_node
        #self.length += 1

    def add_all_to_end(self, items:List[T]):
        """
        appends each of the items in items as separate nodes at the end of this list, preserving order.
        Note: while you can call other methods, it might not be the most efficient!
        :param items: a list or tuple of items to add
        :return: None
        """

        for item in items:
            if self.is_empty():
                new_node = LL_Node(value=items[0])
                self.start = new_node
            else:
                p: LL_Node[T] = self.start
                while p.has_next():
                    p = p.get_next()
                p.set_next(LL_Node[T](value=item))
            #self.length += 1

    def __len__(self):
        """
        overrides the "len" operator - gives the number of items in this list.
        :return: the number of items
        """
        length = 0
        p: LL_Node[T] = self.start
        while p is not None:
            p=p.get_next()
            length += 1
        return length
        #return self.length

    def __contains__(self, item):
        """
        returns whether this linked list contains the item, at least once.
        :param item: the item to match
        :return: whether this item is in the linked list.
        """

        p: LL_Node[T] = self.start
        while p is not None:
            if p.get_value() == item:
                return True
            else:
                p = p.get_next()
        return False

    def index(self, item):
        """
        gives the index of the first instance in this list with matching item, or throws an error if not found.
        :param item: item to match
        :return: the positive index of the first occurance of the item.
        """

        p: LL_Node[T] = self.start
        index = 0

        while p is not None:
            if p.get_value() == item:
                return index
            else:
                p = p.get_next()
            index += 1

        raise RuntimeError(f"Item {item} not found in list.")

    def pointers_for_index(self, index:int)->{LL_Node[T], LL_Node[T]}:
        """
        Internal method - not really intended for an outside class to use this, but other methods in this class may
        find it handy!

        Gets the pointer to the ith item in the list and the pointer to the (i-1)th item in the list. If i is zero,
        then the latter will be None. If i extends 1 past the end of the list, p will be None and back will be the last
        element. If i extends further than that past the end of the list, then both will be None.
        :param index: a non-negative integer
        :return: p, back - the pointers for the ith and (i-1)th items in the list.
        """
        # OK. I've written this one for you.
        p:LL_Node[T] = self.start
        back:LL_Node[T] = None
        count = 0
        while count < index:
            back = p
            if p is not None:
                p = p.get_next()
            count += 1
            if p is None and back is None:
                break
        return p, back

    def item_at_index(self, index:int)->T:
        """
        gets the item stored in the list at position "index." Does not alter the list. Crashes if index is out of range.
        :param index: an index in range 0 ... len(list)-1, inclusive
        :return: the value stored in the list at this location.
        """
        p = self.pointers_for_index(index)[0]
        if p is not None:
            return p.value  # replace this to return an actual value.
        else:
            raise IndexError("Index out of range")

    def item_at_start(self)->T:
        """
        gets the value stored in the first node
        :return: value
        """

        p: LL_Node[T] = self.start
        return p.get_value()

    def item_at_end(self)->T:
        """
        gets the value stored in the last node.
        (Tip: remember, counting up the nodes is O(N)... try to avoid making two passes through this list.)
        :return:
        """

        if self.start is None:
            return None
        else:
            p:LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            return p.get_value()

    def insert_value_at_start(self, value:T):
        """
        creates a new node with value and inserts it at the start of the list.
        :param value: item to add.
        :return: None
        """
        new_node = LL_Node[T](value= value)
        if self.is_empty():
            self.start = new_node

        else:
            new_node.set_next(self.start)
            self.start = new_node
        #self.length += 1

    def insert_value_at_index(self, value:T, index:int):
        """
        puts the given value into a new node and inserts it into the list so that it is now at position "index." If
        index > length of the list, this will put it at the end of the list.
        :param value:
        :param index:
        :return:
        """
        # I've written this one for you.
        p, back = self.pointers_for_index(index)
        if p == self.start:
            self.insert_value_at_start(value)
        else:
            back.next = LL_Node[T](value=value, next = p)
        #self.length += 1

    def insert_all_at_index(self, in_list:List[T], index:int):
        """
        Goes through all the items in list, and adds them (in order) into this list, starting at the intial location.
        :param in_list:
        :param index:
        :return: None
        """
        if index < 0 or index > self.__len__():
            raise IndexError("Index out of range")
        else:
            for item in in_list:
                p, back = self.pointers_for_index(index)
                if back is not None:
                    back.next = LL_Node[T](value=item, next=p)
                else:
                    self.start = LL_Node[T](value=item, next=p)
                index += 1
                #self.length += 1

    def remove_first_item(self):
        """
        alters this list by removing the first item. If there is no first item, then throws an exception
        :return: None
        """
        if self.start is None:
            raise IndexError("Index out of range")
        else:
            second_node = self.start.get_next()
            self.start = second_node
        #self.length -=1

    def remove_item_at_index(self, i:int):
        """
        alters this list by removing the ith element. If i is out of the range of the list, throws an exception.
        :param index: item number to remove
        :return: None
        """
        if i < 0 or i > self.__len__():
            raise IndexError("Index out of range")
        else:
            p, back = self.pointers_for_index(i)
            if back is not None:
                back.set_next(p.get_next())
            else:
                self.remove_first_item()
            #self.length -= 1

    def remove_last_item(self):
        """
        removes the last item in this list, but does not return it. If list is empty, throw an exception
        (Note, since counting up the number of items in the list is O(N), try to avoid making two passes.)
        :return: None
        """
        if self.start is None:
            raise IndexError("Index out of range")

        else:
            p:LL_Node[T] = self.start
            index=0
            while p.has_next():
                index +=1
                p = p.get_next()
            p, back = self.pointers_for_index(index)
            back.set_next(None)
            #self.length += 1

    def remove(self, val:T, first_only=False):
        """
        removes either the first or all items that match val from this list, depending on the state of first_only
        :param val:
        :param first_only:
        :return: None
        """
        index = 0
        p: LL_Node[T] = self.start

        while index < self.__len__():
            if p is None:
                break
            if p.get_value() == val:
                self.remove_item_at_index(index)

                if first_only is True:
                    break
            else:
                index += 1
            p = p.next
            #self.length += 1

    def toList(self)->List[T]:
        """
        generates a list of items in the same order as this linked list.
        """
        # I've written this one for you.
        result = []
        p:LL_Node[T] = self.start
        while p != None:
            result.append(p.get_value())
            p = p.get_next()
        return result

# groceries = LinkedList()
# groceries.add_to_end("bananas")
# groceries.add_to_end("cookies")
# print(groceries.toList())
# groceries.add_to_start("milk")
# print(groceries.toList())
# empty = LinkedList()
# #empty.add_to_start("me")
# print(empty.toList())
# fruits=["orange","apple","kiwi"]
# groceries.add_all_to_end(fruits)
# print(groceries.toList())
# #empty.add_all_to_end(fruits)
# print(empty.toList())
# print(groceries.__len__())
# print(empty.__len__())
# print(groceries.__contains__("cookies"))
# print(groceries.__contains__("water"))
# groceries.add_to_end("cookies")
# print(groceries.toList())
# #print(groceries.index("water"))
# #print(empty.index("cookies"))
# alpha = ["a", "b","c"]
# groceries.insert_all_at_index(alpha,3)
# print(groceries.toList())
# groceries.remove_first_item()
# print(groceries.toList())
# empty.add_to_end("lexy")
# print(empty.toList())
# empty.remove_first_item()
# print(empty.toList())
# groceries.remove_item_at_index(2)
# print(groceries.toList())
# groceries.remove_last_item()
# print(groceries.toList())
# groceries.add_to_end("cookies")
# groceries.add_to_end("bananas")
# groceries.add_to_end("kiwi")
# print(groceries.toList())
# groceries.remove("kiwi")
# print(groceries.toList())
# groceries.remove("bananas")
# print(groceries.toList())
# groceries.remove("cookies",True)
# print(groceries.toList())
