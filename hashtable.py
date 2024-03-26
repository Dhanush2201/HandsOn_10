class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def _hash_function(self, key):
        return key % self.capacity

    def _resize_table(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * new_capacity
        self.size = 0

        for chain_head in old_table:
            current = chain_head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        if self.size / self.capacity >= 0.75:
            self._resize_table(self.capacity * 2)

        index = self._hash_function(key)
        if not self.table[index]:
            self.table[index] = HashNode(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = HashNode(key, value)
        self.size += 1

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return current.key, current.value
            prev = current
            current = current.next
        return None, None

if __name__ == "__main__":
    ht = SeparateChainingHashTable()
    
    index = int(input("Enter the index: "))
    value = input("Enter the value: ")
    ht.insert(index, value)

    search_key = int(input("Enter the key to search: "))
    print(ht.search(search_key))  

    remove_key = int(input("Enter the key to remove: "))
    removed_key, removed_value = ht.remove(remove_key)
    print(f"Removed Key: {removed_key}, Removed Value: {removed_value}")
