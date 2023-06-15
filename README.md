# backend-test

Análisis de la complejidad computacional de todas las operaciones implementadas en el problema tres


La complejidad computacional de la operación insert en un árbol binario depende en gran medida de la estructura que presente el árbol, es decir, que tan balanceado se encuentre. En el mejor caso la complejidad es constante O(1). Este caso ocurre cuando se inserta la raíz del árbol. Para el peor de los casos la complejidad computacional es de O(n) donde n representa todos los nodos del árbol. Para este caso el árbol se encuentra totalmente desequilibrado, es decir, todas las inserciones se realizan en un solo subárbol, por lo que para realizar una nueva inserción se necesitaría recorrer todos los nodos del árbol. En caso que el árbol se encuentre equilibrado la complejidad se reduce con respecto al caso anterior siendo de O(log n). Esto sucede porque la organización de los nodos permite realizar una búsqueda binaria para encontrar donde se va a insertar el nuevo nodo
