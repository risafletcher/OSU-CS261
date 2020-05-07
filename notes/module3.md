# Linked Lists, Stacks, Queues, and Deques
## Stacks
Stacks are a linear ADT that imposes a **_last in, first out (LIFO)_** order on elements.

### Stack Operations
- `push(x)` - pushes an item `x` onto the top of the stack.
- `pop()` - removes the top item from the stack and returns its value
- `peek()` - returns they value of the top item in the stack without removing it

### Implementing a Stack Using a Linked List
A stack can be implemented using a singly-linked list, where the head of the list corresponds to the top of the stack. A `push` operation would push a value to the top, or “head” of the linked list. Subsequently `pop` would remove the head of the linked list.

### Implementing a Stack Using a Dynamic Array
When using a dynamic array as the underlying storage for a stack, it is easiest to use the end of the array to represent the head of the stack. This means we `push` and `pop` elements from the end of the array.
The `push()`operation for a stack built on top of a dynamic array is `O(1)+` (best-case: `O(1)`, worst-case: `O(n)`), but `pop()`is still `O(1)` (best-case, worst-case, and average).

## Queues
A queue is a data structure that imposes a **_first in, first out_** (or **_FIFO_**) ordering on the elements it stores. In other words, unlike with a stack, the first element to be removed from the queue is the first one that was placed into it. Before an element can be removed from a queue, it must wait f or the removal of all other elements that were inserted into the queue before it.

### Queue Operations
- `enqueue(x)` - Adds `x` to the back of the queue.
- `dequeue()` - Removes the first item in the queue and returns its value.
![][image-1]
- Unlike with a stack, elements are sequenced from a queue in the same order in which they are enqueued.

### Implementing a Queue Using a Linked List
Because we need to be able to work with both ends of a queue—enqueuing onto the back of the queue and dequeuing from the front—we must keep track of both the head and tail of the list. **_Enqueued values are inserted at the tail of the list and values are dequeued from the head_**.


[image-1]:	https://oregonstate.instructure.com/courses/1764380/files/79236251/preview?verifier=YlkvwBCtyTf6O2TNMwwQBHBs1EQ61ctxQLgMW3EY