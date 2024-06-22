myArr = [1, 3, -5, 6, 6, 14, 15, 689, 13, 11, -26, -356, -1.03, 56, 49, 97, 78];


function selectionSort(arr) {
  for(let i = 0; i < arr.length - 1; i++) {
    let minIndex = i;
    
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }
    
    [ arr[i], arr[minIndex] ] = [ arr[minIndex], arr[i] ];
  }
  
  return arr;
}

console.log(selectionSort(myArr))