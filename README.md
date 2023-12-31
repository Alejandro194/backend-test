# backend-test

## Análisis de la complejidad computacional de todas las operaciones implementadas en el problema 3

### insert

La complejidad computacional de la operación "insert" en un árbol binario depende en gran medida de la estructura que presente el árbol, es decir, que tan balanceado se encuentre. En el mejor caso la complejidad es constante O(1). Este caso ocurre cuando se inserta la raíz del árbol. Para el peor de los casos la complejidad computacional es de O(n) donde n representa todos los nodos del árbol. Para este caso el árbol se encuentra totalmente desequilibrado, es decir, todas las inserciones se realizan en un solo subárbol, por lo que para realizar una nueva inserción se necesitaría recorrer todos los nodos del árbol. En caso que el árbol se encuentre equilibrado la complejidad se reduce con respecto al caso anterior siendo de O(log n). Esto sucede porque la organización de los nodos permite realizar una búsqueda binaria para encontrar donde se va a insertar el nuevo nodo

### search

La complejidad computacional de la operación “search” en un árbol binario esta determinada por el numero de nodos presente en el árbol y que tan balanceado este se encuentre. En el mejor de los casos la complejidad es constante O(1). Este caso se da cuando el nodo que se busca es la raíz. En el peor de los casos la complejidad computacional seria de O(n), donde n es la cantidad de nodos que posee el árbol. Este caso ocurre cuando el árbol esta completamente desequilibrado. Para un árbol balanceado la complejidad de esta operación sería de O(log n), ya que empleando el método de búsqueda binaria apoyándose en la estructura del árbol no es necesario recorrer todos los nodos del árbol. 

### print_inorder

La complejidad de la función "print_inorder", al igual que en los casos anteriores, esta determinada por la cantidad de nodos y el balance del árbol. Esta operación es realizada visitando de manera recursiva el nodo izquierdo, el nodo raíz y el nodo derecho. A diferencia de las operaciones anteriores en el caso de un árbol completamente desequilibrado la complejidad computacional es mejor que para un árbol balanceado. En el caso de un árbol completamente desequilibrado la complejidad computacional es de O(n) ya que en cada nodo tiene a lo mas un hijo. Sin embargo, en un árbol binario equilibrado (como un árbol AVL la altura del árbol es O(log n). En este caso, la complejidad del recorrido es O(n log n), ya que para cada nivel del árbol se visita un número proporcional a n de nodos, y el número de niveles es O(log n).

## Análisis del uso del método de búsqueda binaria en el problema 8

La principal ventaja de la utilización de este método es la reducción de cantidad de operaciones con respecto a una búsqueda secuencial. En una búsqueda secuencial se recorre la lista comprobando cada uno de sus elementos. Esta operación tiene una complejidad computacional de O(n) en el peor caso, donde n es la cantidad de elementos en la lista y el elemento buscado es el ultimo de la lista. La búsqueda binaria aprovecha que los elementos de la lista están ordenados y de esta manera evita realizar comprobaciones en todos los elementos de la lista. La complejidad computacional de este método es de O(log n), sustancialmente menor al de la búsqueda secuencial.

En el marco general de la solución al problema la función de búsqueda se ejecuta dentro de una función map por cada elemento de una segunda lista. La complejidad computacional seria O(m * s)   donde m es la cantidad de elementos de la segunda lista y s la complejidad computacional de la función de búsqueda. Comparando el método de búsqueda secuencial con el método de búsqueda binaria tenemos que O(m * n) > O(m * log n) ya que O(n) > O(log n). De esta forma podemos concluir que la utilización del método de búsqueda binaria en la solución nos permite disminuir la complejidad computacional con respecto a la utilización de una búsqueda secuencial.

