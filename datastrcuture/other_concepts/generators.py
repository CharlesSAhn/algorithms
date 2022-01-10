'''
An iterator is an object that represents a stream of data. This is different from a list, which is also an iterable, but is not an iterator because it is not a stream of data.

Generators are a simple way to create iterators using functions. You can also define iterators using classes, which you can read more about here.

Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or
when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.

Ex

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1


for x in my_range(5):
    print(x)
'''


lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here

    while start < len(iterable) + 1:
        yield start, iterable[start-1]
        start += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


'''
Quiz: Chunker
If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), 
being able to take and use chunks of it at a time can be very valuable.

Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

'''

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))