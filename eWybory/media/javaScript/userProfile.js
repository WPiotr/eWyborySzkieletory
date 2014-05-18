$(document).ready(function(){
	$('#emailBar').hide();
	$('#passBar').hide();	
	
	$( '#changePass' ).click(function() {
 		$('#passBar').fadeToggle();	
	});
	
	$( '#changeEmail' ).click(function() {
 		$('#emailBar').fadeToggle();	
	});
	$('#redirect').load('aaaaaaa',function(responseTxt,statusTxt,xhr){
		if(statusTxt=="success")
      		alert("External content loaded successfully!");	
		if(statusTxt=="error")
      		window.location = '/';
	});
	
	
	
});	



