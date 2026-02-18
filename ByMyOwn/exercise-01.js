/* 
Dado uma array de números que pode ou não conter arrays de números internas,
escreva uma função que retorne uma array de números não repetidos
*/

// Base
const array_simples = [1, 2, 2, 3, 3, 4, 5]
const newArray = new Set(array_simples)
console.log(newArray)

const seen = []
for (let i = 0; i < array_simples.length; i++){
    if (!seen.includes(array_simples[i])){
        seen.push(array_simples[i])
    }
}

console.log(seen)


// Resolução
const array = [1, 2, 3, [1, 2, 5, 6, 7], 8, 9, [7, 0], 8, 9, 2, 10];

function flatterWithRecursive(arr, result = []){
    for(let i = 0; i < arr.length; i++){
        if(Array.isArray(arr[i])){
            flatterWithRecursive(arr[i], result)
        } else{
            if(!result.includes(arr[i])){
                result.push(arr[i])
            }
        }
    }
    return result
}

console.log(array)
console.log(`Depois: ${flatterWithRecursive(array)}`)

// Outras Formas
function flatterWithForEach(arr){
    const flatArray = arr.flat(Infinity)
    const result = []

    flatArray.forEach(n => {
        if(!result.includes(n)){
            result.push(n)
        }
    })
    return result
}

function flatterWithFilter(arr){
    const flatArray = arr.flat(Infinity)
    return flatArray.filter((value, index) => flatArray.indexOf(value) === index)
}


function flatterWithSet(arr){
    return [...new Set(arr.fla(Infinity))]
}

console.log(flatterWithForEach(array))
console.log(flatterWithFilter(array))