$(document).ready(function() {

    $('form').on('submit', function(event)) {

		$.ajax({
			data : {
				layer_type : $('#layer_type').val(),
				neurons_number : $('#neurons_number').val()
			},
			type : 'POST',
			url : '/results'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});