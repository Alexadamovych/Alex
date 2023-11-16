my_list  = [1,2,3,4,6,8]
# for i in my_list:
#     print(i)
interator = iter(my_list)
print(interator)

print (next(interator))
print (next(interator))
print (next(interator))
print (next(interator))
print (next(interator))
print (next(interator))

print("-"*30)

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise  StopIteration
        return  self.i

counter = Counter(5)
for element in counter:
    print(element)

print("-"*30)

counter = Counter(5)
print(counter.__next__())
print(counter.__next__())