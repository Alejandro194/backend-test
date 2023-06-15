/*
Escribe una función llamada findCommonElements que acepte una lista de listas como parámetro y 
devuelva una lista con los elementos comunes a todas las sub-listas.
*/


function findCommonElements(lists) {
  if (lists.length === 0) {
    return [];
  }

  const referenceList = lists[0];

  const commonElements = new Set();

  for (let i = 0; i < referenceList.length; i++) {
    const element = referenceList[i];
    if (lists.every((list) => list.includes(element))) {
      commonElements.add(element);
    }
  }

  return Array.from(commonElements);
}

