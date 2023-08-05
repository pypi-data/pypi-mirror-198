
class OperatorBase:
    def union_op(self, x):
        """
        This makes u = a+b identical to:
        u = union()(a, b )
        """
        from . import builtins
        res = builtins.union()

        #add self or all its children to res
        if isinstance(self, builtins.union):
            for c in self.children:
                res.add(c)
        else:
            res.add(self)

        #add x or all its children to res
        if isinstance(x, builtins.union):
            for c in x.children:
                res.add(c)
        else:
            res.add(x)

        return res

    def difference_op(self, x):
        """
        This makes u = a - b identical to:
        u = difference()(a, b )
        """
        from . import builtins
        res = builtins.difference()

        if isinstance(self, builtins.difference) and len(self.children):
            for c in self.children:
                res.add(c)
        else:
            res.add(self)

        res.add(x)
        return res

    def intersection_op(self, x):
        """
        This makes u = a * b identical to:
        u = intersection()(a, b )
        """
        from . import builtins
        res = builtins.intersection()

        if isinstance(self, builtins.intersection) and len(self.children):
            for c in self.children:
                res.add(c)
        else:
            res.add(self)

        if isinstance(x, builtins.intersection):
            for c in x.children:
                res.add(c)
        else:
            res.add(x)

        return res

    def __add__(self, x): return self.union_op(x)
    def __or__(self, x): return self.union_op(x)
    def __radd__(self, x): return self.union_op(x)
    def __sub__(self, x): return self.difference_op(x)
    def __mul__(self, x): return self.intersection_op(x)
    def __and__(self, x): return self.intersection_op(x)
    def __invert__(self): from . import builtins; return builtins.debug()(self)

