from asyncio import sleep
import os
import time


class Node:
    def __init__(self, val: int, key: int, next=None, previous=None):
        self.val = val
        self.key = key
        self.next = next
        self.previous = previous


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_count = 0
        self.node_map: dict[int, Node] = {}
        self.lru: Node = None
        self.mru: Node = None

    def display(self, command: str):
        keys = []
        values = []
        info = []
        node = self.lru
        while node:
            for key in self.node_map.keys():
                if self.node_map[key] is node:
                    keys.append(str(key))

            values.append(str(node.val))
            info.append(str(hex(id(node))))
            node = node.next
        l1 = "Key: " + " <--------> ".join(keys)
        l2 = "Val: " + " <--------> ".join(values)
        l3 = "Addr " + " <--------> ".join(info)
        os.system("cls" if os.name == "nt" else "clear")
        if command:
            print(command)
        print(l1)
        print(l2)
        print(l3)
        print()

    def get(self, key: int) -> int:
        result = -1

        if key in self.node_map:
            target_node = self.node_map[key]
            result = target_node.val

            if target_node is self.lru and target_node is self.mru:
                pass

            elif target_node is self.lru:
                self.lru = target_node.next
                self.lru.previous = None

                target_node.next = None
                target_node.previous = self.mru

                self.mru.next = target_node
                self.mru = target_node

            elif target_node is self.mru:
                pass

            else:
                target_node.next.previous = target_node.previous
                target_node.previous.next = target_node.next
                target_node.next = None
                target_node.previous = self.mru
                self.mru.next = target_node
                self.mru = target_node

        return result

    def put(self, key: int, value: int) -> None:
        if len(self.node_map.keys()) == 0:
            new_node = Node(val=value, key=key, previous=None, next=None)
            self.current_count += 1
            self.lru = new_node
            self.mru = new_node
            self.node_map[key] = new_node

        elif key in self.node_map:
            self.node_map[key].val = value
            target_node = self.node_map[key]
            if target_node is self.lru and target_node is self.mru:
                pass

            elif target_node is self.lru:
                self.lru = target_node.next
                self.lru.previous = None

                target_node.next = None
                target_node.previous = self.mru

                self.mru.next = target_node
                self.mru = target_node

            elif target_node is self.mru:
                pass

            else:
                target_node.next.previous = target_node.previous
                target_node.previous.next = target_node.next
                target_node.next = None
                target_node.previous = self.mru
                self.mru.next = target_node
                self.mru = target_node

        else:
            new_node = Node(val=value, key=key, previous=self.mru, next=None)
            self.current_count += 1

            self.mru.next = new_node
            self.mru = new_node
            self.node_map[key] = new_node

        if self.current_count > self.capacity:
            lru = self.node_map.pop(self.lru.key)
            self.lru = lru.next
            self.current_count -= 1
