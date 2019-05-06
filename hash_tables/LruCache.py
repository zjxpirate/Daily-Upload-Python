

# 6. Implement an ISBN cache

import collections


class LruCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity


    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price


    def insert(self, isbn, price):
        # we add the value for key only if key is not present - we don't update existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price


    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None


ll = LruCache(10)
ll.insert(0000, 2.5)

print(ll.erase(0000))


