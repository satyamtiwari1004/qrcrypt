function generateQRCode() {
	var data = document.getElementById("data").value
	eel.generate_qr(data)(setImage)
}

function setImage(base64) {
	document.getElementById("qr").src = base64
	success();
}

eel.expose(success);
function success() {
	swal("Good  Job","Qr Code Generated Successfully","success");
}

eel.expose(errr);
function errr() {
	swal("Sorry","Some error has occurred","error");
}