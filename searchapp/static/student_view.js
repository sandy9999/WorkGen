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
					$(function(){
						new PNotify({
							title: 'Success!',
							text: 'Your document is currently being generated.',
							type: 'success'
						});
					});
						download_token(response.token);
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
						download_token(response.token);
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
			"subject": $("#paper-subject").dropdown('get value')
		};
		let worksheetType = document.getElementById("worksheetType") ? $("#worksheetType").dropdown('get value') : 'paper';
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
						$(`#${worksheetType}-breakup-options-parent`).append(paperElement);
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
				$('#paper-chapter').dropdown('clear');
				$('#paper-subject-splits').dropdown('clear');
				$(`#${worksheetType}-chapter-options-parent`).empty();
				$(`#paper-subject-splits-options-parent`).empty();
				let chapters = d['chapters'];
				let subject_breakup = d['subject_breakup'];
				$(`#subject_splits`).removeClass('show-display').addClass('hide-display');
				$('h3').removeClass('show-display').addClass('hide-display');
				$(`#chapter-operations`).removeClass('hide-display').addClass('show-display');
				$('#add-subject-split').removeClass('hide-display').addClass('show-display');
				for (var i=0; i<chapters.length; i++) {
					$(`#${worksheetType}-chapter-options-parent`).append(`<div class="item" data-value=${chapters[i]['chapter_id']}>${chapters[i]['chapter_name']}</div>`);
				}
				for (var i=0; i<subject_breakup.length; i++) {
					$(`#paper-subject-splits-options-parent`).append(`<div class="item" data-value=${subject_breakup[i]['breakup_id']}>${subject_breakup[i]['breakup_name']}</div>`);
				}
			}
		});
	}

	function add_chapter(e)
	{
		var chapter = $('input[name=add-chapter-input]').val().trim();
		var subject = $("#paper-subject").dropdown('get value');
		if(chapter.length> 0 && subject.length > 0)
		{
			let formData = {
				"subject": subject,
				"chapter": chapter
			};

			$.ajax({
				url: BASE_DIR + "/add_chapter",
				method : "get",
				data: formData,
				headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
				success: function(d) {
					new PNotify({
						title: 'Success!',
						text: 'Chapter successfully added',
						type: 'success'
					});
					populate_chapters();
				}
			});
		}
	}

	function delete_chapters(e)
	{
		var subject = $("#paper-subject").dropdown('get value');	
		var chapters = $('#paper-chapter').dropdown('get values');
		if(chapters.length> 0)
		{
			let formData = {
				"subject": subject,
				"chapters": chapters
			};

			$.ajax({
				url: BASE_DIR + "/delete_chapters",
				method : "get",
				data: formData,
				headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
				success: function(d) {
					new PNotify({
						title: 'Success!',
						text: 'Chapters successfully deleted',
						type: 'success'
					});
					populate_chapters();
				}
			});
		}
	}

	function add_subject_split(e)
	{
		var subject = $("#paper-subject").dropdown('get value');	
		var question_weightage = $('#question-weightage').dropdown('get values');
		var question_type = $('#question-type').dropdown('get values');
		var split_name = $('input[name=split-name]').val().trim();
		var total_questions = $('input[name=total-questions]').val();
		var questions_to_attempt = $('input[name=questions-to-attempt]').val();
		let formData = {
			"subject": subject,
			"question_type": question_type,
			"question_weightage": question_weightage,
			"split_name": split_name,
			"total_questions": total_questions,
			"questions_to_attempt": questions_to_attempt
		};
		$.ajax({
			url: BASE_DIR + "/add_subject_split",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(d) {
				new PNotify({
					title: 'Success!',
					text: 'Subject split successfully added',
					type: 'success'
				});
				populate_chapters();
			}

		});
	}

	function display_split_table(e)
	{
		var subject = $("#paper-subject").dropdown('get value');
		var splits = $('#paper-subject-splits').dropdown('get values');	
		let formData = {
			"subject": subject,
			"splits": splits
		};
		$.ajax({
			url: BASE_DIR + "/display_split_table",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(d) {
				var subject_splits = document.getElementById('subject_splits');
				subject_breakup = d['subject_breakup'];
				$(`#subject_splits`).removeClass('hide-display').addClass('show-display');
				$('h3').removeClass('hide-display').addClass('show-display');
				var rowCount = subject_splits.rows.length;
        		for (var i = rowCount - 1; i > 0; i--) {
					subject_splits.deleteRow(i);
				}
				for (var i=0; i<subject_breakup.length; i++) {
					$(`#subject_splits tbody`).append(`<tr>
					<td data-label="Name">${subject_breakup[i]['name']}</td>
					<td data-label="Question Type">${subject_breakup[i]['question_type']}</td>
					<td data-label="Question Weightage">${subject_breakup[i]['question_weightage']}</td>
					<td data-label="Total Questions">${subject_breakup[i]['total_questions']}</td>
					<td data-label="Questions to Attempt">${subject_breakup[i]['questions_to_attempt']}</td>
					<td data-label=""><button id='${subject_breakup[i]['breakup_id']}' class="ui button delete-subject-split">x</button></td>
				  </tr>`);
				}
			}

		});
	}

	$(document).on('click','.delete-subject-split', function() 
	{
		
		var id = this.id;
		var subject = $("#paper-subject").dropdown('get value');
		let formData = {
			"id": id,
			"subject": subject
		};

		$.ajax({
			url: BASE_DIR + "/delete_subject_split",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(d) {
				new PNotify({
					title: 'Success!',
					text: 'Subject split successfully deleted',
					type: 'success'
				});
				populate_chapters();
			}
		});
	});


	// methods for TEST worksheet

	$('#test-subject').dropdown({
		onChange: populate_chapters,
	});

	$('#paper-subject').dropdown({
		onChange: populate_chapters,
	});

	$('#paper-chapter').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#paper-subject-splits').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});

	$('#paper-breakup').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
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
	});

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
	$("#add-chapter-button").click(add_chapter);
	$("#delete-chapters-button").click(delete_chapters);
	$("#display-splits-button").click(display_split_table);
	$("#add-split-button").click(add_subject_split);
	
	
	$('#question-type').dropdown({
	});

	$('#question-weightage').dropdown({
	});
});

function download_token(token) {
		var request = new XMLHttpRequest();
		var url = BASE_DIR + '/download_test_and_generic_docx';
		var params = `token=${token}`;
		request.open('GET', `${url}?${params}`, true);
		request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
		request.responseType = 'blob';
		request.onload = function() {
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
