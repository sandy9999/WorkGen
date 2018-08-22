$(document).ready(function(){
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
	on: "click"
});

$('#subjectTest').dropdown({
	onChange: function (value, text, $selectedItem) {
		if(value == "Science") {
			$('#chapterTest .menu div').remove();
			$('<div class="item" data-value="Motion">Motion</div>').appendTo('#chapterTest .menu');
		}
		else if(value == "Math") {
			$('#chapterTest div div').remove();
			$('<div class="item" data-value="Rational Nos">Rational Nos</div>').appendTo('#chapterTest .menu');
		}
		},
		on: "click"
	});
	$('#chapterTest').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});
$('#subjectGeneric').dropdown({
	onChange: function (value, text, $selectedItem) {
		if(value == "Science") {
			$('#chapterGeneric .menu div').remove();
			$('<div class="item" data-value="Motion">Motion</div>').appendTo('#chapterGeneric .menu');
		}
		else if(value == "Math") {
			$('#chapterGeneric div div').remove();
			$('<div class="item" data-value="Rational Nos">Rational Nos</div>').appendTo('#chapterGeneric .menu');
		}
		},
		on: "click"
	});
	$('#chapterGeneric').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});
$('#subjectCustomized').dropdown({
	onChange: function (value, text, $selectedItem) {
		if(value == "Science") {
			$('#chapterCustomized .menu div').remove();
			$('<div class="item" data-value="Motion">Motion</div>').appendTo('#chapterCustomized .menu');
		}
		else if(value == "Math") {
			$('#chapterCustomized div div').remove();
			$('<div class="item" data-value="Rational Nos">Rational Nos</div>').appendTo('#chapterCustomized .menu');
		}
		},
		on: "click"
	});
	$('#chapterCustomized').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});

$('#qtypeTest').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});
$('#qtypeGeneric').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});
$('#qtypeCustomized').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});

$('#stud_name').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	on: "click"
});
$('#random_setting').dropdown({
        onChange: function (value, text, $selectedItem) {
        },
        on: "click"
});
$("#submit").click(function(e) {
	console.log("worked");
	e.preventDefault();
	$.ajaxSetup({
        headers: { "X-CSRFToken": csrftoken }
	});
	worksheetType = $('#worksheetType').dropdown('get value');
	if(worksheetType == 'testPaper')
	{
		$.ajax({
		
			type: "POST",
			url: "/download_test/",
			data: {
				subjectTest: $('#subjectTest').dropdown('get value'),
				chapterTest: $('#chapterTest').dropdown('get value')
			},
			success: function(result) {
				alert('ok');
			},
			error: function(result) {
				alert('error');
			}
		});	

	}
	else if(worksheetType == 'genericWorksheet')
	{
		random_setting: $('#random_setting').dropdown('get value');
		if(random_setting == 'random')
		{
			$.ajax({
		
				type: "POST",
				url: "/download_generic_random/",
				data: {
					subjectGeneric: $('#subjectGeneric').dropdown('get value'),
					chapterGeneric: $('#chapterGeneric').dropdown('get value'),
					qtypeGeneric: $('#qtypeGeneric').dropdown('get value'),
					noOfQ1Generic: $('#noOfQ1Generic').val(),
					noOfQ2Generic: $('#noOfQ2Generic').val(),
					noOfQ3Generic: $('#noOfQ3Generic').val(),
					noOfQ4Generic: $('#noOfQ4Generic').val(),
					noOfQ5Generic: $('#noOfQ5Generic').val(),
				},
				success: function(result) {
					alert('ok');
				},
				error: function(result) {
					alert('error');
				}
			});	
		}
		else if(random_setting == 'segregated')
		{
			$.ajax({
		
				type: "POST",
				url: "/download_generic_segregated/",
				data: {
					subjectGeneric: $('#subjectGeneric').dropdown('get value'),
					chapterGeneric: $('#chapterGeneric').dropdown('get value'),
					qtypeGeneric: $('#qtypeGeneric').dropdown('get value'),
					noOfQ1Generic: $('#noOfQ1Generic').val(),
					noOfQ2Generic: $('#noOfQ2Generic').val(),
					noOfQ3Generic: $('#noOfQ3Generic').val(),
					noOfQ4Generic: $('#noOfQ4Generic').val(),
					noOfQ5Generic: $('#noOfQ5Generic').val(),
				},
				success: function(result) {
					alert('ok');
				},
				error: function(result) {
					alert('error');
				}
			});	
		}
		
	}
	else if(worksheetType == 'customizedWorksheet')
	{
		/*$.ajax({
		
			type: "POST",
			url: "/download_customized/",
			data: {
				subjectCustomized: $('#subjectCustomized').dropdown('get value'),
				stud_name: $('#stud_name').dropdown('get value'),
				chapterCustomized: $('#chapterCustomized').dropdown('get value'),
				qtypeCustomized: $('#qtypeCustomized').dropdown('get value'),
				noOfQ1Customized: $('#noOfQ1Customized').val(),
				noOfQ2Customized: $('#noOfQ2Customized').val(),
				noOfQ3Customized: $('#noOfQ3Customized').val(),
				noOfQ4Customized: $('#noOfQ4Customized').val(),
				noOfQ5Customized: $('#noOfQ5Customized').val()
			},
			success: function(result) {
				alert('ok');
			},
			error: function(result) {
				alert('error');
			}
		});*/
		var form = $('#upload_form')[0];
		var data = new FormData(form);																																																																																																																																			
		$.ajax({
		
			type: "POST",
			enctype: 'multipart/form-data',
			url: "/download_customized/",
			data: data,
			cache: false,
			contentType: false,
			processData: false,
			success: function(data) {
				alert(data);
			},
			error: function(result) {
				alert('error');
			}
		});	
	}
});

})		
