let entryHour = document.getElementById("entryHour");
let exitHour = document.getElementById("exitHour");
let selectionVehicle = document.getElementById("vehicleType");
const btnCalculate = document.getElementById("calculate");
let message = document.getElementById("result");

function calculatePayment() {
	let entry = parseFloat(entryHour.value);
	let exit = parseFloat(exitHour.value);
	let expendTime = exit - entry;
	let formatExpendTime = expendTime.toFixed(2);
	let priceCar = 2500;
	let priceMotor = 1500;
	let priceBike = 120;
	let payment = 0;


	if (isNaN(entry) || isNaN(exit)) {
		message.textContent = `Please input properly hours`;
		return
	}

	if (exit <= entry) {
		message.textContent = "The entry hour can't be less than the exit hour, remember use the 24 hour format"
	}

	switch (selectionVehicle.value) {
		case "car":
			if (formatExpendTime <= 0.30) {
				payment = "Free time!"
			} else {
				payment = formatExpendTime * priceCar;
			}
			break;
		case "motor":
			if (formatExpendTime <= 0.30) {
				payment = "Free time!"
			} else {
				payment = formatExpendTime * priceMotor;
			}
			break;
		case "bike":
			if (formatExpendTime <= 1) {
				payment = "Free time!"
			} else {
				payment = formatExpendTime * priceBike;
			}
			break;
		default:
			alert("Error, choice the vehicle correctly");
			break;
	}
	message.textContent = `The total time is: ${formatExpendTime} The total to pay is: ${payment}`;
}

btnCalculate.addEventListener("click", calculatePayment);
