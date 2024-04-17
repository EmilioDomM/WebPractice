
function comparacion(){
    let firstNumber = Number(prompt("Please enter Number: "))
    let secondNumber = Number(prompt("Please enter second Number: "))

    if(firstNumber == secondNumber){
        alert(firstNumber + " and " + secondNumber + " are equal")
    } 
    else if(firstNumber > secondNumber){
        alert(firstNumber + " is bigger")
    } else{
        alert(secondNumber + " is bigger")
    }

}

function logic(){
    let a = true
    let b = false

    console.log(a && b)
    console.log(a || b)
}

function suma(a,b,c){
    console.log(a + b + c)
}

function multiplica(a,b,c){
    console.log(a*b*c)
}

function esString(x,y,z){
    
}

function verificaVocales(x){
    if (x == a || x == e || x == i || x == o || x == u){
        console.log(x + " es una vocal")
    } else{
        console.log(x + " no es una vocal")
    }
}

function array(){
    let nombres = ["Ana", "Luis", "Maria"]

    nombres.push("Juan")
    console.log(nombres)
    nombres.pop()
    console.log(nombres)

    let index = nombres.indexOf("Luis")
    if(index !== -1){
        console.log("El nombre se encuentra en el arreglo")
    } else{
        console.log("El nombre no se encuentra en el arreglo")
    }
}

function map(){

}

// let miString = "Hello World"
// let miNumero = 42
// let miBooleano = false
// let miNull = null
// let miUndefined
// let miBigInte = BigInt(123)

// console.log(typeof miString)
// console.log(typeof miNumer)
// console.log(typeof miBoolea)
// console.log(typeof)
// console.log(typeof)
// console.log(typeof)
// console.log(typeof)
// console.log(typeof)