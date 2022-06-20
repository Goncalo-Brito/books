function ValidateForm(){

	$("#form_update").validate({
		rules: {
			nome_livro : {
				required: true,
				minlength: 3,
				maxlength: 128
			},
			cat: {
				required: true,
			},
			autor: {
				required: true,
				minlength: 3,
				maxlength: 64
			},
			classi: {
				required: true,
				number: true,
				min: 0.1,
				max: 5
			}
		},
		messages : {
	  	nome_livro: {
	  		required: "O livro precisa de um nome",
	    	minlength: "O nome do livro é muito pequeno (no minimo 3 letras)",
	    	maxlength: "O nome do livro é muito grande (no maximo 128 letras)"
	  	},
	  	cat: {
	    	required: "O livro precisa de uma categoria",
	  	},
	  	autor: {
	    	required: "O livro precisa ter sido escrito por alguem",
	    	minlength: "O nome do autor é muito pequeno (no minimo 3 letras)",
	    	maxlength: "O nome do autor é muito grande (no maximo 64 letras)"	
	  	},
	  	classi: {
	    	required: "O livro precisa de ter uma classificação",
	    	number: "A classificação deve ser um numero",
	    	min: "A classificação deve ser no minimo 0.1",
	    	max: "A classificação deve ser no maximo 5"
	  	}
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

function multisel() {
	$('#cat').multiselect({
		enableFiltering:false,
		enableCaseInsensitiveFiltering:true,
		includeFilterClearBtn: true,
		nonSelectedText: '--Categoria--',
		buttonWidth: '100%',
	});
}

$(document).ready(function() {
	multisel();
	ValidateForm();
  	$("#salvar").click(function(e){
			if ($("#form_update").valid()){
				$("#form_update").submit()
			}
	});
});