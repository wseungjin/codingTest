function transform(n,decimalNum){
    var answer = "" 
    while(decimalNum !== 0){
        answer = str(decimalNum % 2) + answer
        decimalNum = decimalNum / 2
    }
    return answer
}

main(2,14)