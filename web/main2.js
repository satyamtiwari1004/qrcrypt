function readQRCode() {
	var data = document.getElementById("data").value
	eel.read_qr(data)
}

eel.expose(success);
function success() {
	swal("Good  Job","Qr Code Generated Successfully","success");
}

eel.expose(errr);
function errr() {
	swal("Sorry","Some error has occurred","error");
}