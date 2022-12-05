class Node:
    __slots__ = ["val", "next", "prev"]

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.length = 0
        self.header = None

    def __len__(self):
        if self.header is None:
            return 0

        x = 0
        for _ in self:
            x += 1
        return x

    def add(self, value):
        new = Node(value)
        if self.header is None:
            self.header = new
        else:
            new.next = self.header
            cur = new.next
            self.header = new
            cur.prev = self.header
        self.length += 1

    def add_right(self, value):

        new = Node(value)
        if not self.header:
            self.header = new
        else:
            cur = self.header
            while cur.next:
                cur = cur.next
            cur.next = new
            new.prev = cur
        self.length += 1

    def remove(self, value):
        cur = self.header
        if value not in self:
            raise ValueError("No such value")
        elif cur.prev is None and cur.val == value:
            self.header = cur.next
        else:
            while cur.next:
                cur = cur.next
                pr = cur.prev
                if cur.val == value:
                    pr.next = cur.next
            self.length -= 1

    def __getitem__(self, item):
        if self.length == 0:
            raise IndexError('Index out of range')
        elif item >= self.length or item <= - self.length:
            raise IndexError('Index out of range')
        else:
            cur = self.header
            ind = 0
            ind1 = 0
            while cur:
                ind1 = ind - self.length
                if ind == item or ind1 == item:
                    return cur.val
                cur = cur.next
                ind += 1
            if ind != item or ind1 != item:
                raise IndexError("Out of range")

    def __contains__(self, item):
        cur = self.header
        while cur:
            if cur.val == item:
                return True
            cur = cur.next
        return False

    def __add__(self, other):
        cur = self.header
        cur1 = other.header
        if len(self) == len(other):
            newinst = DoubleLinkedList()
            while cur:
                mynode = cur.val + cur1.val
                newinst.add(mynode)
                cur = cur.next
                cur1 = cur1.next
            return newinst

    def __iter__(self):
        cur = self.header
        while cur:
            yield cur.val
            cur = cur.next

    def __repr__(self):
        if not self.header:
            return "DoubleLinkedList"

        cur = self.header
        rlist = [repr(cur.val)]
        while cur.next:
            cur = cur.next
            rlist.append(repr(cur.val))
        return f"DoubleLinkedList({' -> <-'.join(rlist)})"
