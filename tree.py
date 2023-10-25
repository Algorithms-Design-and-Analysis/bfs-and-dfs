import sys

def profundidad(v, visitado, padre, grafo):
    visitado[v] = True

    for i in grafo[v]:
        if not visitado[i]:
            if profundidad(i, visitado, v, grafo):
                return True
        elif padre != i:
            return True
    return False
def esArbol(grafo):
    n = len(grafo)
    visitado = [False] * n
    
    if profundidad(0, visitado, -1, grafo):
        return False
    for i in visitado:
        if not i:
            return False
            
    return True

def main():
    entrada = sys.stdin.readlines()
    T = int(entrada[0].strip())
    for line in entrada[1:]:
        grafo = eval(line.strip())
        print(esArbol(grafo))

if __name__ == '__main__':
    main()
