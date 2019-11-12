$(document).ready(() => {
    $('#board').dropdown({
        onChange: value => filter(value, 'board')
    });
    $('#grade').dropdown({
        onChange: value => filter(value, 'grade')
    });
    $('#subject').dropdown({
        onChange: value => filter(value, 'subject')
    });
    $('#chapter').dropdown({
        onChange: value => filter(value, 'chapter')
    });
    $('#question_type').dropdown({
        onChange: value => filter(value, 'question_type')
    });
    $('#question_weightage').dropdown({
        onChange: value => filter(value, 'question_weightage')
    });
    $('#text').keyup(function (e) { 
        e.preventDefault();
        filter(e.target.value, 'text');
    });
    $('.modal .actions .deny').click(function(e) {
        e.target.parentElement.previousElementSibling.children[0].value = '';
    })
    $('.modal .actions .positive').click(function(e) {
        let element = $(this).parent().prev().children('input');
        let data = {
            id: element.attr('question'),
            text: element.val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        }
        $.ajax({
            type: "post",
            url: "/edit_questions",
            data,
            dataType: "json",
            success: resp => {
                questions = questions.map(question => {
                    if (question.id === resp.id) question.text = resp.text;
                    return question
                })
                filter(null, 'chapter')
                new PNotify({
                    title: 'Success!',
                    text: 'Question successfully edited in the database',
                    type: 'success'
                });
            },
            error: err => {
                new PNotify({
                    title: 'Error',
                    text: err.responseJSON.error,
                    type: 'error'
                });
            }
        });
    })
    fill_rows(questions);
})

let questions = JSON.parse($('#questions')[0].innerHTML);
$('#questions').remove();
let filters = {
    board: [],
    grade: [],
    subject: [],
    chapter: [],
    question_type: [],
    question_weightage: [],
    text: ''
}

const fill_rows = questions => {
    let rows = ``
    for (var question of questions) {
        rows += `
            <tr question="${question.id}">
                <td>${question.board}</td>
                <td>${question.grade}</td>
                <td>${question.subject}</td>
                <td>${question.chapter}</td>
                <td>${question.question_type}</td>
                <td>${question.question_weightage}</td>
                <td class="selectable-field icon">
                    <span class="text">${question.text}</span>
                    <i class="pencil alternate icon"></i>
                </td>
            </tr>
        `
    }
    $('#questions_table').html(rows);
    $('.pencil').click(function(e) {
        $('.modal .content input').val(e.target.previousElementSibling.innerText);
        $('.modal .content input').attr('question', $(this).parent().parent().attr('question'));
        $('.ui.modal').modal('show');
    })
}


const filter = (value, field) => {
    if (value !== null) {
        const values = field != 'text' ? value.split(',') : [value];
        // console.log(values)
        filters[field] = values;
    }
    if (filters[field].includes("")) filters[field] = []
    // console.log(value)
    // console.log(filters)
    let filtered_questions = questions.filter(question => {
        let removed = false;
        // console.log(question)
        Object.keys(filters).forEach(filter => {
            if (removed) return;
            // console.log(filter)
            // console.log(question[filter])
            // console.log(filters[filter].length != 0 && !filters[filter].includes(question[filter]))
            if (filter == 'text') {
                if (filters[filter].length != 0 && !question[filter].toLowerCase().includes(filters[filter][0].toLowerCase())) {
                    removed = true;
                }
            }
            else if (filters[filter].length != 0 && !filters[filter].includes(question[filter])) {
                removed = true;
            }
        })
        return !removed;
    });
    fill_rows(filtered_questions);
}