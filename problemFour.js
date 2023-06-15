/*
Escribe una función llamada isAnagram que acepte dos cadenas de texto como parámetros y determine si son anagramas 
(es decir, si tienen exactamente las mismas letras, pero en diferente orden).
*/

function isAnagram(str1, str2, removeSpaces = true) {
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();

  if (removeSpaces) {
    str1 = str1.replace(/\s/g, "");
    str2 = str2.replace(/\s/g, "");
  }

  if (str1.length !== str2.length) {
    return false;
  }

  const arr1 = str1.split("").sort();
  const arr2 = str2.split("").sort();

  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }
  
  return true;
}

