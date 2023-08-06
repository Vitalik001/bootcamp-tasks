class Node:

    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.newest = Node(0, 0)
        self.oldest = Node(0, 0)

        self.newest.prev, self.oldest.next = self.oldest, self.newest

    def get(self, key: int) -> int:
        if self.cache.get(key) is not None:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def add(self, node):
        prev_node = self.newest.prev
        prev_node.next = self.newest.prev = node
        node.prev, node.next = prev_node, self.newest

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) is not None:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            to_del = self.oldest.next
            self.remove(to_del)
            del self.cache[to_del.key]
