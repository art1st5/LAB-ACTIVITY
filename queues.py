"""ITECC04 Laboratory 4, Part D: the circular queue and the deque.

This part is on your own. No guided walkthrough, and the tests are the only
feedback you get, exactly as in the coding quiz.

WHY CIRCULAR. A queue over a plain list, dequeuing with pop(0), shifts every
remaining element one place left. That is O(n) for an operation that should
be O(1). Moving the FRONT INDEX forward instead of moving the data is the
whole idea, and the modulo operator is what makes the index wrap back to 0
when it runs off the end.

The queue holds a fixed number of slots. It does not grow.
"""


class CircularQueue:

    def __init__(self, capacity):
     
        if capacity < 1:
            raise ValueError("capacity must be atleast 1 ")
        self._items = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._count = 0

    def enqueue(self, item):
   
        if self.is_full():
            raise OverflowError("enqueue on a full queue")
        rear = (self._front + self._count) % self._capacity
        self._items[rear] = item
        self._count += 1

    def dequeue(self):
     
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._items[self._front]

    def is_empty(self):
        return self._count == 0

    def is_full(self):
        return self._count == self._capacity

    def size(self):
        return self._count

    def slots(self):
       
        return list(self._items)


class Deque:
    """A queue you may add to and remove from at both ends."""

    def __init__(self):
        """Step 8. Create the empty list."""
        self._items = []

    def add_front(self, item):
        """Step 9. Insert at position 0."""
        self._items.insert(0, item)

    def add_rear(self, item):
        """Step 10. Append at the end."""
        self._items.append(item)

    def remove_front(self):
        """Step 11. Remove and return index 0. IndexError when empty."""
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        return self._items.pop(0)

    def remove_rear(self):
        """Step 12. Remove and return the last item. IndexError when empty."""
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        return self._items.pop()

    def is_empty(self):
        """Step 13. True when there is nothing in the deque."""
        return len(self._items) == 0

    def size(self):
        """Step 14. Return how many items are held."""
        return len(self._items)


def is_palindrome(text):

    deque = Deque()
    for char in text:
        if char.isalpha():
            deque.add_rear(char.lower())

    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False

    return True