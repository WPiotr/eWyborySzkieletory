$(document).ready(function(){
	$('#emailBar').hide();
	$('#passBar').hide();	
	
	$( "#changePass" ).click(function() {
 		$('#passBar').fadeToggle();	
	});
	
	$( "#changeEmail" ).click(function() {
 		$('#emailBar').fadeToggle();	
	});
	
});	



