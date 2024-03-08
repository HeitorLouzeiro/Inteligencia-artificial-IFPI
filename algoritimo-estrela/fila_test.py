from queue import PriorityQueue

fila = PriorityQueue()

fila.put((2, "Lira"))
fila.put((3, "Marcus"))
fila.put((1, "João"))

print(fila.queue)

"""
print(fila.queue)
print(fila.get())
print(fila.queue)
print(fila.get())
print(fila.queue)
"""
