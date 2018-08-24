$(document).ready(function(){
	$("#submit").click(function (e) {
		var worksheetType = $("#worksheetType").dropdown('get value');
		if (worksheetType == 'testPaper') {
			var subject = $("#subject").dropdown('get value');
			var chapters = $('#chapter').dropdown('get values');
			var formData = {
				"subject": subject,
				"chapters[]": chapters
			}
			$.ajax({
				url: "http://localhost:8000/get_test_paper",
				method : "get",
				data: formData,
				headers: { "X-CSRFToken": csrftoken,},
				success: function(response) {
					alert(response['token']);
				}
			});
		}
	});

	$('#worksheetType').dropdown({
		onChange: function (value, text, $selectedItem) {
			if(value == 'testPaper') {
				$("#test-div").show();
				$("#generic-div").hide();
				$("#customized-div").hide();
			} else if(value == 'genericWorksheet') {
				$("#test-div").hide();
				$("#generic-div").show();
				$("#customized-div").hide();
			} else if(value == 'customizedWorksheet') {
				$("#test-div").hide();
				$("#generic-div").hide();
				$("#customized-div").show();
			}
		},
	});

	$('#subject').dropdown({
		onChange: function (value, text, $selectedItem) {
				let formData = {
					subject: value,
				}
				$.ajax({
					url: "http://localhost:8000/get_chapters",
					method : "get",
					data: formData,
					headers: { "X-CSRFToken": csrftoken,},
					success: function(d) {
						$("#chapter-options-parent").empty();
						let chapters = d['chapters'];
						$("#chapter").show();
						for (var i=0; i<chapters.length; i++) {
							$("#chapter-options-parent").append(`<div class="item" data-value=${chapters[i]}>${chapters[i]}</div>`);
						}
					}
				});
			},
		});

	$('#chapter').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#qtype').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#stud_name').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

});