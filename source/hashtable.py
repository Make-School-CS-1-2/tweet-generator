#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n)/O(bl) where n = the # of items, b = the # of buckets, and l = the average bucket length,
            because we have to iterate through all of the nodes of every bucket"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n)/O(bl) where n = the # of items, b = the # of buckets, and l = the average bucket length,
            because we have to iterate through all of the nodes of every bucket"""
        # DONE: Loop through all buckets
        # DONE: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n)/O(bl) where n = the # of items, b = the # of buckets, and l = the average bucket length,
            because we have to iterate through all of the nodes of every bucket"""
        # Runtime of O(n) has to iterate through each pair
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n)/O(bl) where n = the # of items, b = the # of buckets, and l = the average bucket length,
            because we have to iterate through all of the nodes of every bucket"""
        # DONE: Loop through all buckets
        # DONE: Count number of key-value entries in each bucket
        length = 0
        for bucket in self.buckets:
            length += bucket.length()
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n/k) where n is the number of key-value pairs and k is the number of buckets,
            because of the linked list find function"""
        # DONE: Find bucket where given key belongs
        hashed_key = hash(key)
        ll = self.buckets[hashed_key % len(self.buckets)]
        # DONE: Check if key-value entry exists in bucket
        if ll.find(lambda data: data[0] == key):
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(l), where l is the average amount of nodes in a bucket,
            because it has to iterate through all the nodes of a single bucket"""
        # DONE: Find bucket where given key belongs
        hashed_key = hash(key)
        ll = self.buckets[hashed_key % len(self.buckets)]
        # DONE: Check if key-value entry exists in bucket
        node_data = ll.find(lambda data: data[0] == key)
        # DONE: If found, return value associated with given key
        if node_data:
            return node_data[1]
        # DONE: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l) where l is the average bucket length,
            because we must search through a single bucket for a key"""
        # Runtime of O(n) for find()
        # DONE: Find bucket where given key belongs
        hashed_key = hash(key)
        ll = self.buckets[hashed_key % len(self.buckets)]
        # DONE: Check if key-value entry exists in bucket
        node_data = ll.find(lambda data: data[0] == key)
        # DONE: If found, update value associated with given key
        # DONE: Otherwise, insert given key-value entry into bucket
        if node_data:
            ll.delete(node_data)
        ll.prepend((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        DONE: Running time: O(l) where l is the average bucket length,
            because we have to iterate through a single bucket"""
        # Runtime of O(n) because of find() of linkedlist
        # DONE: Find bucket where given key belongs
        hashed_key = hash(key)
        ll = self.buckets[hashed_key % len(self.buckets)]
        # DONE: Check if key-value entry exists in bucket
        node_data = ll.find(lambda data: data[0] == key)
        # DONE: If found, delete entry associated with given key
        # DONE: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        if node_data:
            ll.delete(node_data)
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
