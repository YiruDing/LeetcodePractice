class NestedIterator(object):
    # The object() function returns an empty object. You cannot add new properties or methods to this object. This object is the base for all classes, it holds the built-in properties and methods which are default for all classes.
    # Object − A unique instance of a data structure that is defined by its class. An object comprises both data members (class variables and instance variables) and methods.
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
            # 3/16 這一行是什麼意思呢？
        return False


# 另解：
# https://www.youtube.com/watch?v=PtJ6APpEhOU
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        def flatten(nI):
            tmp = []
            for i in nI:
                if i.isInteger():
                    tmp.append(i.getInteger())
                    # Record.GetInteger(field)


# Return the value of field as an integer where possible. field must be an integer.
# https://docs.python.org/3/library/msilib.html#msilib.Record.GetInteger
                else:
                    tmp.extend(flatten(i.getList()))
                    # https://stackoverflow.com/questions/11190070/django-getlist
            return tmp

        self.n = deque(flatten(nestedList))

    def next(self):
        """
        :rtype: int
        """
        return self.n.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n