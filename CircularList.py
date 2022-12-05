class Node1:
    __slots__ = ("val", "next")

    def __init__(self, val):
        self.val = val
        self.next = None


class CircularList:

    def __init__(self):
        self.header = None
        self.length = 0

    def add(self, value):
        new = Node1(value)
        cur = self.header
        new.next = self.header
        if self.header is not None:
            while cur.next != self.header:
                cur = cur.next
            cur.next = new
        else:
            new.next = new
        self.header = new
        self.length += 1

    def add_right(self, value):
        new = Node1(value)
        if self.header is None:
            new.next = new
            self.header = new
        else:
            cur = self.header
            while cur.next != self.header:
                cur = cur.next
            cur.next = new
            new.next = self.header
        self.length += 1

    def remove(self, value):
        prev = self.header
        cur = prev.next
        while prev.next != self.header:
            if prev.val == value:
                self.header = prev.next
            if cur.val == value:
                prev.next = cur.next
            cur = cur.next
            prev = prev.next
        self.length -= 1

    def __contains__(self, item):
        for el in self:
            if el == item:
                return True
        return False

    def __getitem__(self, item):
        if self.length == 0:
            raise IndexError('Index out of range')
        elif item >= self.length or item <= - self.length:
            raise IndexError('Index out of range')
        else:
            cur = self.header
            ind = 0
            while cur:
                ind1 = ind - self.length
                if ind == item or ind1 == item:
                    return cur.val
                cur = cur.next
                ind += 1

    def __add__(self, other):
        new = CircularList()
        cur = self.header
        cur1 = other.header
        if self.length == other.length:
            while cur:
                val = cur.val + cur1.val
                new.add_right(val)
                if cur.next == self.header:
                    break
                cur = cur.next
                cur1 = cur1.next
        return new

    def __iter__(self):
        cur = self.header
        while cur:
            yield cur.val
            cur = cur.next
            if cur.next == self.header:
                yield cur.val
                break

    def __repr__(self):
        mylist = []
        for el in self:
            mylist.append(repr(el))
        return f'CircularList: {"->".join(mylist)}->'
