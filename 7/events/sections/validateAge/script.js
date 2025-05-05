var today = new Date();
var currentYear = today.getFullYear();

let userYear = document.getElementById('bornYear');
let message = document.getElementById('result');
let btnCalculate = document.getElementById('calculateAge')

function calculateAge(){
    let fuserYear = parseInt(userYear.value)
    let fcurrentYear = parseInt(currentYear)
    let fage = fcurrentYear - fuserYear;

    //validate if the user pass a number in the year
    if (isNaN(fuserYear)) {
        alert("Please input a valid year");
        return;
    }

    //Need to fix the length as a property
    if(length(fuserYear) <= 3 || length(fuserYear) >= 5){
        alert("The length of the year are greater or less than the system except");
        return;
    }

    if(fuserYear > fcurrentYear){
        alert('The year that you write is greater than the current year, please modify')
        return;
    }

    message.innerText = `Your age is ${fage} aprox`
}

btnCalculate.addEventListener('click' ,calculateAge)