function validate() {
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	
	var y = document.forms.input.password.value;
	
	if((atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length) && y.length < 6)/*Username and password incorrect*/
		alert("Both the username and password are incorrect");
	else
	{
		if((atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length) && y.length > 6)/*Username incorrect and password correct*/
			alert("The username is incorrect");
		else
		{
			if((atPos > 1 || dotPos > atPos+2 || dotPos + 2 < x.length) && y.length < 6)/*Username correct and password incorrect*/
				alert("The password is incorrect");
			else
				alert("Success!");
		}
	}
}