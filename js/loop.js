function displayEvenNumbersWhileLoop(){
	var n = parseInt(document.getElementById("maxNumber").value)
	var i=2;
	var result="";

	while(i<=n){
		result=result+i+", ";
		i=i+2;
	}
	alert("even "+result);
}


function displayEvenNumbersForLoop(){
	var n = parseInt(document.getElementById("maxNumber").value)
	var result="";
	for(var i=2; i<=n; i=i+2){
		result=result+i+", ";
	}
	alert("even "+result);
}


function displayBackwardNumberWhileLoop(){
	var n = parseInt(document.getElementById("maxNumber").value)
	var i=n;
	var result="";

	while(i>=0){
		result=result+i+", ";
		i = i-1;
	}
	alert("backward "+result);
}

function displayBackwardEvenNumbersForLoop(){
	var n = parseInt(document.getElementById("maxNumber").value)
	var i = n;
	if (n%2!=0){
		i=n-1
	}
	var result="";

	for(var j=i; j>=0; j=j-2){
		result=result+j+", ";
	}
	alert("backward even "+result);

}

function displayBackwardOddNumbersForLoop(){
	var n = parseInt(document.getElementById("maxNumber").value)
	var i = n;
	if (n%2==0){
		i=n-1
	}
		var result="";

	for(var j=i; j>=0; j=j-2){
		result=result+j+", ";
	}
	alert("backward odd "+result);
}

