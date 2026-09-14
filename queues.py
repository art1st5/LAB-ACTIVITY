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
            raise ValuerError("capacity must be atleast 1 ")
        self._items = [] * capacity
        self._capacity = capacity
        self._front = 0
        self._count = 0
        """Step 1. A list of `capacity` Nones, a front index, and a count.

        Raise ValueError if capacity is less than 1.

        Keep a COUNT, not a rear index alone. With only front and rear you
        cannot tell a full queue from an empty one: both give front == rear.
        A count answers both questions with no ambiguity.
        """
        raise NotImplementedError("Step 1: validate capacity, then set up the slots, front, and count")

    def enqueue(self, item):
        if self.is_full():
            rear = (self._front + self._count) % self._capacity
        self._items[rear] = item
        self._count += 1
        
        """Step 2. Add at the rear. Raise OverflowError when full.

        You are not storing a rear index, so compute it:
            rear = (front + count) % capacity
        Write the item there, then increase the count.
        """
        raise NotImplementedError("Step 2: guard for full, compute the rear with modulo, store, count up")

    def dequeue(self):

        if self.is_empty():
            raise ValueError ("dequeuefrom an empty queue")
            item = self._items[self._front]
            self._items[self._front] = None

        """Step 3. Remove and return the front item. IndexError when empty.

        Read the item at front, clear that slot to None so nothing stale is
        left behind, advance front with modulo, decrease the count, return.
        """
        raise NotImplementedError("Step 3: guard for empty, read front, clear it, advance front, count down")

    def peek(self):

        if self.is_empty():
                raise IndexError("peek from an empty stack")
                return self._items[-1]

    def is_empty(self):
        return self._top  

    def is_full(self):
        if self_count == capacity:
            return is_full
        """Step 6. True when the count has reached the capacity."""
        raise NotImplementedError("Step 6: return whether the count equals the capacity")

    def size(self):
        return self._items
        """Step 7. Return the count."""
        raise NotImplementedError("Step 7: return the count")

    def slots(self):
        """Written for you. Returns a copy of the raw list.

        For inspecting wraparound during the demonstration. Not part of the
        ADT, and your other methods must never call it.
        """
        return list(self._items)


class Deque:
    """A queue you may add to and remove from at both ends."""

    def __init__(self):
        """Step 8. Create the empty list."""
        raise NotImplementedError("Step 8: create self._items as an empty list")

    def add_front(self, item):
        """Step 9. Insert at position 0."""
        raise NotImplementedError("Step 9: insert the item at index 0")

    def add_rear(self, item):
        """Step 10. Append at the end."""
        raise NotImplementedError("Step 10: append the item")

    def remove_front(self):
        """Step 11. Remove and return index 0. IndexError when empty."""
        raise NotImplementedError("Step 11: guard for empty, then pop index 0")

    def remove_rear(self):
        """Step 12. Remove and return the last item. IndexError when empty."""
        raise NotImplementedError("Step 12: guard for empty, then pop the last item")

    def is_empty(self):
        """Step 13. True when there is nothing in the deque."""
        raise NotImplementedError("Step 13: return whether the list is empty")

    def size(self):
        """Step 14. Return how many items are held."""
        raise NotImplementedError("Step 14: return the length of self._items")


def is_palindrome(text):
    """Step 15. True when text reads the same both ways.

    Ignore anything that is not a letter, and ignore case. Load the letters
    into a Deque, then compare front against rear until one or zero letters
    remain. A word of odd length ends with one letter in the middle, which
    always matches itself, so stop while size is greater than 1.
    """
    raise NotImplementedError("Step 15: load the letters into a Deque, then compare from both ends")
