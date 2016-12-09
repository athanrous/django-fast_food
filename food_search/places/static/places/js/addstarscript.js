$(document).ready(function() {	
	var SelectedOptionClass = $('option:checked').attr('class');
	$('div.ui-select').addClass(SelectedOptionClass);
	
	$('#votes').live('change', function(){	 
		$('div.ui-select').removeClass(SelectedOptionClass);
		
		SelectedOptionClass = $('option:checked').attr('class');
		$('div.ui-select').addClass(SelectedOptionClass);		
		
	 });
	
  
});
