function ValidateForm(){

	$("#form_add").validate({
		rules: {
			nome_cat : {
				required: true,
				minlength: 3,
				maxlength: 64
			}
		},
		messages : {
	  		nome_cat: {
	  			required: "Qual o nome da categoria",
	    		minlength: "A categoria é muito pequena (no minimo 3 letras)",
	    		maxlength: "A categoria é muito grande (no maximo 64 letras)"
		  	},
		},
		errorElement: "span",
    errorClass: "help-block",
    highlight: function (element, errorClass, validClass) {
        $(element).closest('.form-group').addClass('has-error');
    },
    unhighlight: function (element, errorClass, validClass) {
        $(element).closest('.form-group').removeClass('has-error');
    },
    errorPlacement: function (error, element) {
        if (element.parent('.input-group').length || element.prop('type') === 'checkbox' || element.prop('type') === 'radio') {
            error.insertAfter(element.parent());
        } else {
            error.insertAfter(element);
        }
    }
	});
}
$(document).ready(function() {
		ValidateForm();
  	$("#salvar").click(function(e){
			if ($("#form_add").valid()){
				$("#form_add").submit()
			}
	});
});