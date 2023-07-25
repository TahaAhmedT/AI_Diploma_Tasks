import queue


# Define a custom class that implements the comparison logic
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    # lt stands for less than, it compares the priorities of two Task objects
    def __lt__(self, other):
        # here I can do any comparison logic that I want
        return self.priority < other.priority


# Create a priority queue
priority_queue = queue.PriorityQueue()

# Add items to the queue
priority_queue.put(Task('task1', 5))
priority_queue.put(Task('task2', 3))
priority_queue.put(Task('task3', 7))

# Get items from the queue in priority order
while not priority_queue.empty():
    task = priority_queue.get()
    print(task.name)