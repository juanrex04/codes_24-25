let totalProduct = 0
let result = 0

function updateValue(){
    totalProduct = parseInt(document.getElementById("total_product").value)
}

function totalPay(){
    result = totalProduct * 100

    document.getElementById("print_result").textContent = "Total to pay: " + result
}