let number1 = document.getElementById("number1");
let number2 = document.getElementById("number2");
let selectOperation = document.getElementById("operation");
let resultPrint = document.getElementById("result");
let btnCalculate = document.getElementById("calculate");

//function calculate, this will be use in the both components to calculate the result
function calculateFunction() {
  let fnumber1 = parseFloat(number1.value);
  let fnumber2 = parseFloat(number2.value);
  let choiceOperation = selectOperation.value;
  let result = 0;

  //Validate the inputs if are numbers
    if (isNaN(fnumber1) || isNaN(fnumber2)){
        alert("Please enter valid numbers.")
        console.log(fnumber1, fnumber2)
        return;
    }

    //switch case to select the operation
    switch (choiceOperation) {
        case "add":
            result = fnumber1 + fnumber2;
            break;
        case "subs":
            result = fnumber1 - fnumber2;
            break;
        case "multi":
            result = fnumber1 * fnumber2;
            break;
        case "div":
            if (fnumber1 === 0 || fnumber2 === 0){
                alert("Please enter a valid number on the inputs fields.")
                return;
            } else {
                result= fnumber1 / fnumber2;
            }
            break;
        default:
            alert("Please select a valid operation.")
            return;
    }

    //Print the result
    resultPrint.innerHTML = `The result is: ${result}`
}

//Add the event listener to the button and select
btnCalculate.addEventListener("click",calculateFunction)
selectOperation.addEventListener("change",calculateFunction)