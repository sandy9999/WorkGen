$(document).ready(function(){

	// on selecting type of worksheet
	$('#worksheetType').dropdown({
		onChange: function (value, text, $selectedItem) {
			if(value == 'test') {
				$("#test-div").show();
				$("#generic-div").hide();
				$("#customized-div").hide();
			} else if(value == 'generic') {
				$("#test-div").hide();
				$("#generic-div").show();
				$("#customized-div").hide();
			} else if(value == 'customized') {
				$("#test-div").hide();
				$("#generic-div").hide();
				$("#customized-div").show();
			}
		},
	});

	// function called when submit button clicked
	function submit_click(e) {
		var worksheetType = $("#worksheetType").dropdown('get value');
		if (worksheetType == 'test') {
			console.log("submit click called");
			var subject = $("#test-subject").dropdown('get value');
			var chapters = $('#test-chapter').dropdown('get values');
			var papertype = $('#test-breakup').dropdown('get value');
			var formData = {
				"subject": subject,
				"papertype": papertype,
				"chapters[]": chapters
			}
			$.ajax({
				url: BASE_DIR + "/get_test_paper",
				method : "get",
				data: formData,
				headers: { "X-CSRFToken": csrftoken,},
				success: function(response) {
					console.log(response.token);

					$(function(){
						new PNotify({
							title: 'Success!',
							text: 'Your document is currently being generated.',
							type: 'success'
						});
					});
				if(window.confirm("Do you want to download")){
						download_token(response.token);
					}
				},
			});
		} else if (worksheetType == 'generic') {
			var subject = $("#generic-subject").dropdown('get value');
			var chapters = $("#generic-chapter").dropdown('get values');
			var q1a = $('#generic-noOfQ1a').val() || 0;
			var q1b = $('#generic-noOfQ1b').val() || 0;
			var q2 = $('#generic-noOfQ2').val() || 0;
			var q3 = $('#generic-noOfQ3').val() || 0;
			var q4 = $('#generic-noOfQ4').val() || 0;
			var q5 = $('#generic-noOfQ5').val() || 0;
			var random_setting = $("#random-setting").dropdown('get value');
			var formData = {
				subject: subject,
				chapters: chapters,
				breakup: [q1a, q1b, q2, q3, q4, q5],
				random_setting: random_setting,
			};

			$.ajax({
				url: BASE_DIR + "/get_generic_paper",
				method : "get",
				data: formData,
				headers: { "X-CSRFToken": csrftoken,},
				success: function(response) {
					$(function(){
						new PNotify({
							title: 'Success!',
							text: 'Your document is currently being generated.',
							type: 'success'
						});
						if(window.confirm('Do you want to download')){
						download_token(response.token)
					}
					});
				},
			});
		} else if (worksheetType == 'customized') {
			var subject = $("#customized-subject").dropdown('get value');
			var chapters = $("#customized-chapter").dropdown('get values');
			var q1a = $('#customized-noOfQ1a').val() || 0;
			var q1b = $('#customized-noOfQ1b').val() || 0;
			var q2 = $('#customized-noOfQ2').val() || 0;
			var q3 = $('#customized-noOfQ3').val() || 0;
			var q4 = $('#customized-noOfQ4').val() || 0;
			var q5 = $('#customized-noOfQ5').val() || 0;
			var student_names = $("#stud_name").dropdown('get values');
			var file_data = $('#realfile').prop("files")[0];
			var formData = new FormData();
			formData.append("file",file_data);
			formData.append('subject',subject);
			formData.append('chapters[]',chapters);
			formData.append('breakup[]',[q1a,q1b,q2,q3,q4,q5]);
			formData.append('student_names[]',student_names);
			$.ajax({
				enctype: 'multipart/form-data',
				url: BASE_DIR + "/get_customize_paper",
				method : "post",
				data: formData,
				processData: false,
				cache: false,
				contentType: false,
				headers: { "X-CSRFToken": csrftoken,},
				success: function(response) {
					$(function(){
						new PNotify({
							title: 'Success!',
							text: 'Your document is currently being generated.',
							type: 'success'
						});
					});
				},
		});
	}
}

function upload_click(e) {
	var worksheetType = $("#worksheetType").dropdown('get value');
	if (worksheetType == 'customized') {
		var subject = $("#customized-subject").dropdown('get value');
		var file_data = $('#realfile').prop("files")[0];
		var formData = new FormData();
		formData.append("file",file_data);
		formData.append('subject',subject);
		$.ajax({
			enctype: 'multipart/form-data',
			url: BASE_DIR + "/generate_optional_inputs",
			method : "post",
			data: formData,
			processData: false,
			cache: false,
			contentType: false,
			headers: { "X-CSRFToken": csrftoken,},
			success: function(response) {
				$(`#${worksheetType}-chapter-options-parent`).empty();
				let chapters = response['chapters'];
				$(`#${worksheetType}-chapter`).removeClass('hide-display').addClass('show-display');
				for (var i=0; i<chapters.length; i++) {
					$(`#${worksheetType}-chapter-options-parent`).append(`<div class="item" data-value=${chapters[i]['chapter_id']}>${chapters[i]['chapter_name']}</div>`);}

				$(`#stud_name-options-parent`).empty();
				let student_names = response['stud_name'];
				$(`#stud_name`).removeClass('hide-display').addClass('show-display');
				for (var i=0; i<student_names.length; i++) {
					$(`#stud_name-options-parent`).append(`<div class="item" data-value=${student_names[i]}>${student_names[i]}</div>`);}
				$("#customized-qtype").removeClass("hide-display").addClass("show-display");
				$(function(){
					new PNotify({
						title: 'Success!',
						text: 'Processing your data!',
						type: 'success'
					});

				});
			},
	});
}
}
	function populate_chapters(value, text, $selectedItem) {
		let formData = {
			subject: value,
		}
		let worksheetType = $("#worksheetType").dropdown('get value');
		if (worksheetType == 'test') {
			$.ajax({
				url: BASE_DIR + "/get_test_format",
				method : "get",
				data: formData,
				headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
				success: function(d) {
					let papers = d['papers'];
					for (var i=0; i<papers.length; i++) {
						let paperElement = `<div class="item" data-value=${papers[i]}>${papers[i]}</div>`;
						$('#test-breakup-options-parent').append(paperElement);
					}
				}
			});
		}
		$.ajax({
			url: BASE_DIR + "/get_chapters",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(d) {
				$(`#${worksheetType}-chapter-options-parent`).empty();
				let chapters = d['chapters'];
				$(`#${worksheetType}-chapter`).removeClass('hide-display').addClass('show-display');
				for (var i=0; i<chapters.length; i++) {
					$(`#${worksheetType}-chapter-options-parent`).append(`<div class="item" data-value=${chapters[i]['chapter_id']}>${chapters[i]['chapter_name']}</div>`);
				}
			}
		});
	}

	// methods for TEST worksheet

	$('#test-subject').dropdown({
		onChange: populate_chapters,
	});

	$('#test-chapter').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#test-breakup').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});


	// methods for GENERIC worksheet

	$('#generic-subject').dropdown({
		onChange: populate_chapters,
	});

	$('#generic-chapter').dropdown({
		onChange: function (value, text, $selectedItem) {
			$("#generic-qtype").removeClass("hide-display").addClass("show-display");
		},
	});

	$('#generic-qtype').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#random-setting').dropdown({
	})

	// methods for CUSTOMIZED worksheet

	$('#customized-subject').dropdown({
		onChange: populate_chapters,
	});

	$('#customized-chapter').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#customized-qtype').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#stud_name').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#upload').click(upload_click);
	$("#submit").click(submit_click);


});

function download_token(token) {
		var request = new XMLHttpRequest();
		var url = BASE_DIR + '/download_test_and_generic_docx';
		var params = `token=${token}`;
		request.open('GET', `${url}?${params}`, true);
		request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
		request.responseType = 'blob';
		console.log("here");
		request.onload = function() {
			console.log(request.status);
			console.log(request.response)
			if(request.status === 200) {
				console.log("Done");
				var blob = new Blob([request.response], { type: 'application/pdf' });
				var link = document.createElement('a');
				link.href = window.URL.createObjectURL(blob);
				link.download = "workgen_document.docx";
				document.body.appendChild(link);
				link.click();
			}
		};
		request.send();
	}
