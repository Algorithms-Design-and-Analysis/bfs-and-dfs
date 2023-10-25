import queue

def bfs(grafo, nodo_inicio, nodo_fin):

    if not (0 <= nodo_inicio <= len(grafo)-1) or not (0 <= nodo_fin <= len(grafo)-1):
        return False
    
    else:

        output = False

        cola = queue.Queue()
        vistados = [False for _ in range(len(grafo))]

        cola.put(nodo_inicio)
        vistados[nodo_inicio] = True

        while not cola.empty():
            nodo = cola.get()
            if nodo == nodo_fin:
                output = True
            for adyacente in grafo[nodo]:
                if vistados[adyacente] == False:
                    cola.put(adyacente)
                    vistados[adyacente] = True
        
        return output

def main():
    cantidad = input()
    for _ in range(int(cantidad)):
        grafo, nodos = eval(input()), input().split(",")
        inicio, fin = int(nodos[0]), int(nodos[1]) 
        print(bfs(grafo, inicio, fin))

if __name__=='__main__':
    main()