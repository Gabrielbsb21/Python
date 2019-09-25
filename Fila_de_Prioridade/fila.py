import heapq

class FilaDePrioridade:

    def __init__(self):
        self.fila = []
        self.indice = 0
    
    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.indice, item))

    def remover(self):
        return heapq.heappop(self.fila) [-1]
