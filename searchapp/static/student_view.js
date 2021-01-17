$(document).ready(function(){

    let flag = 1;
    let num = 1;
	// on selecting type of worksheet
	$('#worksheetType').dropdown({
		onChange: () => {
          if(flag == 1)
            $('#format').removeClass('hide-display').addClass('show-display');
          else {
            let worksheetType = $("#worksheetType").dropdown('get value');
            if(worksheetType == 'test') {
              $('#test-div').show();
              $('#generic-div').hide();
              $('#customized-div').hide();
            }
            else if(worksheetType == 'generic') {
              $('#test-div').hide();
              $('#generic-div').show();
              $('#customized-div').hide();
            }
            else if(worksheetType == 'customized') {
              $('#test-div').hide();
              $('#generic-div').hide();
              $('#customized-div').show();
            }
          }
		},
	});

	// function called when submit button clicked
	function submit_click(e) {
		let worksheetType = $("#worksheetType").dropdown('get value');
        let format = $("#format").dropdown('get value');
		if (worksheetType == 'test') {
			let subject = $("#test-subject").dropdown('get value');
			let chapters = $('#test-chapter').dropdown('get values');
			let board = $('#test-board').dropdown('get value');
            if(format == 'phypaper') {
              let formData = {
                  "subject": subject,
                  "board": board,
                  "chapters[]": chapters
              }
              let urlToGo = '/get_test_paper'
              $.ajax({
				url: BASE_DIR + urlToGo,
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
            }
            else if(format == 'form') {
              let heading = $('#heading').val();
              let required = []
              for(let i = 1; i <= num; i++) {
                let type = $(`#required-field-${num}`).dropdown('get value');
                let desc = $(`#field-desc-${num}`).val();
                required.push({"type": type, "title": desc})
              }
              let formData = {
                  "subject": subject,
                  "board": board,
                  "chapters[]": chapters,
                  "required": JSON.stringify(required),
                  "heading": heading,
              }
              let urlToGo = '/get_test_form';
              $.ajax({
                url: BASE_DIR + urlToGo,
                method: "get",
                data: formData,
                headers: {"X-CSRFToken": csrftoken,},
                success: (response) => {
                  console.log(response);
                  let thing = $.param(response);
                  window.location = BASE_DIR + '/get_form_data?' + thing;
                }
              });
            }

			
		} else if (worksheetType == 'generic') {
			let subject = $("#generic-subject").dropdown('get value');
			let chapters = $("#generic-chapter").dropdown('get values');
			let q1a = $('#generic-noOfQ1a').val() || 0;
			let q1b = $('#generic-noOfQ1b').val() || 0;
			let q2 = $('#generic-noOfQ2').val() || 0;
			let q3 = $('#generic-noOfQ3').val() || 0;
			let q4 = $('#generic-noOfQ4').val() || 0;
			let q5 = $('#generic-noOfQ5').val() || 0;
			let random_setting = $("#random-setting").dropdown('get value');
			let formData = {
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
			let subject = $("#customized-subject").dropdown('get value');
			let chapters = $("#customized-chapter").dropdown('get values');
			let q1a = $('#customized-noOfQ1a').val() || 0;
			let q1b = $('#customized-noOfQ1b').val() || 0;
			let q2 = $('#customized-noOfQ2').val() || 0;
			let q3 = $('#customized-noOfQ3').val() || 0;
			let q4 = $('#customized-noOfQ4').val() || 0;
			let q5 = $('#customized-noOfQ5').val() || 0;
			let student_names = $("#stud_name").dropdown('get values');
			let file_data = $('#realfile').prop("files")[0];
			let formData = new FormData();
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
				error: err => {
					new PNotify({
						title: err.responseJSON.error,
						text: 'Click here to login',
						type: 'error',
					});
					$('.brighttheme-error').click(() => window.location.href = '/login?next=/student_view')
				}
		});
	}
}

function upload_click(e) {
	let worksheetType = $("#worksheetType").dropdown('get value');
	if (worksheetType == 'customized') {
		let subject = $("#customized-subject").dropdown('get value');
		let file_data = $('#realfile').prop("files")[0];
		let formData = new FormData();
		formData.append("file", file_data);
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
				chapters.forEach(function(chapter){
					$(`#${worksheetType}-chapter-options-parent`).append(`<div class="item" data-value=${chapter['chapter_id']}>${chapter['chapter_name']}</div>`);
				})
				$(`#stud_name-options-parent`).empty();
				let student_names = response['stud_name'];
				$(`#stud_name`).removeClass('hide-display').addClass('show-display');
				student_names.forEach(function(student_name){
						$(`#stud_name-options-parent`).append(`<div class="item" data-value=${student_name}>${student_name}</div>`);
				})
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

function populate_grades(value,text, $selectedItem) {
	let worksheetType = document.getElementById("worksheetType") ? $("#worksheetType").dropdown('get value') : 'paper';
	let boardData = {
		"board": $(`#${worksheetType}-board`).dropdown('get value')
	};
	$.ajax({
		url: BASE_DIR + "/get_grades",
		method : "get",
		data: boardData,
		headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
		success: function(response) {
			$(`#${worksheetType}-grade-options-parent`).empty();
			$(`#${worksheetType}-grade`).removeClass('hide-display').addClass('show-display');
			let grades = response['grade_list'];
			grades.forEach(function(grade){
				let gradeElement = `<div class="item" data-value=${grade['grade_id']}>${grade['grade_name']}</div>`;
				$(`#${worksheetType}-grade-options-parent`).append(gradeElement);
			})
		}
	});
}

function populate_subjects(value,text, $selectedItem) {
	let worksheetType = document.getElementById("worksheetType") ? $("#worksheetType").dropdown('get value') : 'paper';
	let gradeData = {
		"grade": $(`#${worksheetType}-grade`).dropdown('get value')
	};
	$.ajax({
		url: BASE_DIR + "/get_subjects",
		method : "get",
		data: gradeData,
		headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
		success: function(response) {
			$(`#${worksheetType}-subject-options-parent`).empty();
			$(`#${worksheetType}-subject`).removeClass('hide-display').addClass('show-display');
			let subjects = response['subject_list'];
			subjects.forEach(function(subject){
				let subjectElement = `<div class="item" data-value=${subject['subject_id']}>${subject['subject_name']}</div>`;
				$(`#${worksheetType}-subject-options-parent`).append(subjectElement);
			})
		}
	});
}

	function populate_chapters(value, text, $selectedItem) {
		let worksheetType = document.getElementById("worksheetType") ? $("#worksheetType").dropdown('get value') : 'paper';
		let formData = {
			"subject": $(`#${worksheetType}-subject`).dropdown('get value'),
			"board": $(`#${worksheetType}-board`).dropdown('get value')
		};
		$.ajax({
			url: BASE_DIR + "/get_chapters",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(response) {
				$(`#${worksheetType}-chapter-options-parent`).empty();
				$(`#${worksheetType}-chapter`).removeClass('hide-display').addClass('show-display');


				let chapters = response['chapters'];
				let subject_breakup = response['subject_breakup'];

				chapters.forEach(function(chapter){
					$(`#${worksheetType}-chapter-options-parent`).append(`<div class="item" data-value=${chapter['chapter_id']}>${chapter['chapter_name']}</div>`);
				})

				if(worksheetType == 'paper')
				{
					$('#paper-subject-splits').dropdown('clear');

					$(`#paper-subject-splits-options-parent`).empty();

					$(`#subject_splits`).removeClass('show-display').addClass('hide-display');
					$('h3').removeClass('show-display').addClass('hide-display');
					$(`#chapter-operations`).removeClass('hide-display').addClass('show-display');
					$('#add-subject-split').removeClass('hide-display').addClass('show-display');

					subject_breakup.forEach(function(breakup){
						$(`#paper-subject-splits-options-parent`).append(`<div class="item" data-value=${breakup}>${breakup}</div>`);
					})
				}
			}
		});
	}

	function add_chapter(e)
	{
		let chapter = $('input[name=add-chapter-input]').val().trim();
		let subject = $("#paper-subject").dropdown('get value');
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
				success: function(response) {
					new PNotify({
						title: 'Success!',
						text: 'Chapter successfully added',
						type: 'success'
					});
					populate_chapters();
					$('input[name="add-chapter-input"]').val('');
				}
			});
		}
	}

	function delete_chapters(e)
	{
		let subject = $("#paper-subject").dropdown('get value');
		let chapters = $('#paper-chapter').dropdown('get values');
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
				success: function(response) {
					new PNotify({
						title: 'Success!',
						text: 'Chapters successfully deleted',
						type: 'success'
					});
					populate_chapters();
					$('#paper-chapter').dropdown('clear');
				}
			});
		}
	}

	function add_subject_split(e)
	{
		let board = $("#paper-board").dropdown('get value');
		let question_weightage = $('#question-weightage').dropdown('get values');
		let question_type = $('#question-type').dropdown('get values');
		let split_name = $('input[name=split-name]').val().trim();
		let total_questions = $('input[name=total-questions]').val();
		var questions_to_attempt = $('input[name=questions-to-attempt]').val();
		let formData = {
			"board": board,
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
			success: function(response) {
				new PNotify({
					title: 'Success!',
					text: 'Subject split successfully added',
					type: 'success'
				});
				populate_chapters();
				$('#question-weightage').dropdown('clear');
				$('#question-type').dropdown('clear');
				$('input[name="split-name"').val('');
				$('input[name="total-questions"').val('');
				$('input[name="questions-to-attempt"').val('');

			}

		});
  }

  function base64ToArrayBuffer(base64) {
    let binaryString = window.atob(base64.replace(/\s/g, ''));
    let binaryLen = binaryString.length;
    let bytes = new Uint8Array(binaryLen);
    for (let i = 0; i < binaryLen; i++) {
       let ascii = binaryString.charCodeAt(i);
       bytes[i] = ascii;
    }
    return bytes;
 }

  function saveByteArray(reportName, byte, type) {
		let blob = new Blob([byte], {type: type});
    saveAs(blob, reportName);
  };

  function download_tracker(e) {
    let subject = $("#paper-subject").dropdown('get value');
    let splits = $('#paper-subject-splits').dropdown('get values');
    if (splits.length != 1) {
      new PNotify({
        title: 'Error',
        text: 'We currently support only one subject split at a time for dummy tracker download',
        type: 'error'
      });
      return;
    }
		let formData = {
			"subject": subject,
			"split_name": splits[0],
		};
		$.ajax({
      url: BASE_DIR + "/get_dummy_tracker",
      method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(response) {
        let sampleArr = base64ToArrayBuffer(response);
        saveByteArray("dummy_tracker.xlsx", sampleArr, 'multipart/form-data');
      }
    });
  }

	function display_split_table(e)
	{
		let board = $("#paper-board").dropdown('get value');
		let splits = $('#paper-subject-splits').dropdown('get values');
		let formData = {
			"board": board,
			"splits": splits
		};
		$.ajax({
			url: BASE_DIR + "/display_split_table",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(response) {
				let subject_splits = document.getElementById('subject_splits');
				subject_breakup = response['subject_breakup'];
				$(`#subject_splits`).removeClass('hide-display').addClass('show-display');
				$('h3').removeClass('hide-display').addClass('show-display');
				let rowCount = subject_splits.rows.length;
        		for (let i = rowCount - 1; i > 0; i--) {
					subject_splits.deleteRow(i);
				}
				for (let i=0; i<subject_breakup.length; i++) {
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

		let id = this.id;
		let formData = {
			"id": id,
		};

		$.ajax({
			url: BASE_DIR + "/delete_subject_split",
			method : "get",
			data: formData,
			headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
			success: function(response) {
				new PNotify({
					title: 'Success!',
					text: 'Subject split successfully deleted',
					type: 'success'
				});
				populate_chapters();
			}
		});
	});
    
    function get_required() {
      let submit = document.getElementById('submit');
      let worksheetType = document.getElementById("worksheetType") ? $("#worksheetType").dropdown('get value') : 'paper';
      let format = $('#format').dropdown('get value');
      if(format == 'phypaper') {
          submit.innerHTML = 'DOWNLOAD'
          $('#GoogleForm').hide();
            if(worksheetType == 'test') {
				$("#test-div").show();
				$("#generic-div").hide();
				$("#customized-div").hide();
			} else if(worksheetType == 'generic') {
				$("#test-div").hide();
				$("#generic-div").show();
				$("#customized-div").hide();
			} else if(worksheetType == 'customized') {
				$("#test-div").hide();
				$("#generic-div").hide();
				$("#customized-div").show();
			}
      }
      else if(format == 'form') {
          submit.innerHTML = "GENERATE";
          $('#GoogleForm').show();
          if(flag == 1)
            $(`#${worksheetType}-div`).hide();
          else
            $(`#${worksheetType}-div`).show();
      }
    }

    document.getElementById('heading').addEventListener('change', () => {
      $('#required-field-1').removeClass('hide-display').addClass('show-display');
      $('#required-field-desc-1').removeClass('hide-display').addClass('show-display');
      $('#next-options').removeClass('hide-display').addClass('show-display');
    }, false);
    document.getElementById('addMore').addEventListener('click', create_fields, false);
    document.getElementById('done').addEventListener('click', show_board, false);

    function show_board() {
      flag = 0;
      let worksheetType = document.getElementById("worksheetType") ? $("#worksheetType").dropdown('get value') : 'paper';
      $('#next-options').removeClass('show-display').addClass('hide-display');
      $(`#${worksheetType}-div`).show();
    }

    function create_fields() {
      let type = $(`#required-field-${num}`)
      let desc = $(`#field-desc-${num}`)
      if(type.dropdown('get value') === '') {
        type.focus();
        return;
      }
      if(desc.val() === '') {
        desc.focus();
        return;
      }
      let data = document.getElementById('fields');
      num += 1;
      data.insertAdjacentHTML('beforeend', `<div id="required-field-${num}" class="ui selection dropdown format show-display">
          <input name="Type" type="hidden">
          <i class="dropdown icon"></i>
          <div class="default text">Select the type of field required</div>
          <div class="menu">
              <div class="item" data-value="text">Text</div>
              <div class="item" data-value="email">Email</div>
              <div class="item" data-value="number">Number</div>
          </div>
      </div>
      <br>
      <div id="required-field-desc-${num}" class="ui input format show-display">
          <input id="field-desc-${num}" type="text" placeholder="Description">
      </div>
      <br>`);
      $(`#required-field-${num}`).dropdown('clear');
    }

    $('#required-field-1').dropdown('clear');

    $('#format').dropdown('clear');

    $('#format').dropdown({
      onChange: get_required,    
      });

	// methods for TEST worksheet
	$('#test-board').dropdown('clear');

	$('#test-board').dropdown({
		onChange: populate_grades,
	});

	$('#test-grade').dropdown({
		onChange: populate_subjects,
	});

	$('#test-subject').dropdown({
		onChange: populate_chapters,
	});

	$('#test-chapter').dropdown({
		onChange: function (value, text, $selectedItem) {
		},
	});


  //methods for SUBJECT SPLITS.
	$('#paper-board').dropdown('clear');
	$('#paper-grade').dropdown('clear');
	$('#paper-subject').dropdown('clear');
	$('#paper-chapter').dropdown('clear');

	$('#paper-board').dropdown({
		onChange: populate_grades,
	});

	$('#paper-grade').dropdown({
		onChange: populate_subjects,
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


	// methods for GENERIC worksheet
	$('#generic-board').dropdown('clear');

	$('#generic-board').dropdown({
		onChange: populate_grades,
	});

	$('#generic-grade').dropdown({
		onChange: populate_subjects,
	});

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
	$('#customized-board').dropdown('clear');

	$('#customized-board').dropdown({
		onChange: populate_grades,
	});

	$('#customized-grade').dropdown({
		onChange: populate_subjects,
	});

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
  	$("#download-tracker-button").click(download_tracker);
	$("#add-split-button").click(add_subject_split);


	$('#question-type').dropdown({
	});

	$('#question-weightage').dropdown({
	});
});

function download_token(token) {
		let request = new XMLHttpRequest();
		let url = BASE_DIR + '/download_test_and_generic_docx';
		let params = `token=${token}`;
		request.open('GET', `${url}?${params}`, true);
		request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
		request.responseType = 'blob';
		request.onload = function() {
			if(request.status === 200) {
				let blob = new Blob([request.response], { type: 'application/pdf' });
				let link = document.createElement('a');
				link.href = window.URL.createObjectURL(blob);
				link.download = "workgen_document.docx";
				document.body.appendChild(link);
				link.click();
			}
		};
		request.send();
	}
