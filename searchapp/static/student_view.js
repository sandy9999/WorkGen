$(document).ready(function(){
	$('#worksheetType').dropdown({
		onChange: function (value, text, $selectedItem) {
		if(value == 'testPaper')
		{
			$('#upload').css('display','none');
			$('#randomize').css('display','none');
			$('#segregate').css('display','none');
			$('#stud_name').css('display','none');
			$('#subject').css('display','block');
			$('#chapter').css('display','block');
			$('#submit').css('display','block');
		        $('#qtype').css('display','none');
			$('#noOfQ1').css('display','none');
			$('#noOfQ2').css('display','none');
			$('#noOfQ3').css('display','none');
			$('#noOfQ4').css('display','none');
			$('#noOfQ5').css('display','none');


      		}
		else if(value == 'genericWorksheet')
		{
			$('#upload').css('display','none');
			$('#randomize').css('display','block');
			$('#segregate').css('display','block');
			$('#stud_name').css('display','none');
			$('#subject').css('display','block');
			$('#chapter').css('display','block');
			$('#qtype').css('display','block');
			$('#noOfQ1').css('display','block');
			$('#noOfQ2').css('display','block');
			$('#noOfQ3').css('display','block');
			$('#noOfQ4').css('display','block');
			$('#noOfQ5').css('display','block');
			$('#submit').css('display','block');
			$('#stud_name').css('display','none');
		}
		else if(value == 'customizedWorksheet')
		{
			$('#upload').css('display','block');
			$('#randomize').css('display','none');
			$('#segregate').css('display','none');
			$('#stud_name').css('display','block');
			$('#chapter').css('display','block');
			$('#submit').css('display','block');
			$('#subject').css('display','none');
			$('#qtype').css('display','block');
			$('#noOfQ1').css('display','block');
			$('#noOfQ2').css('display','block');
			$('#noOfQ3').css('display','block');
			$('#noOfQ4').css('display','block');
			$('#noOfQ5').css('display','block');
		}
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
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
		forceSelection: false,
		selectOnKeydown: false,
		showOnFocus: false,
		on: "click"
	});

$('#chapterTest').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
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
		forceSelection: false,
		selectOnKeydown: false,
		showOnFocus: false,
		on: "click"
});

$('#chapterGeneric').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
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
		forceSelection: false,
		selectOnKeydown: false,
		showOnFocus: false,
		on: "click"
});

$('#chapterCustomized').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"
});

$('#qtypeTest').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"
});

$('#qtypeGeneric').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"
});

$('#qtypeCustomized').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"
});

$('#stud_name').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"

});
	});
$('#random-setting').dropdown({
        onChange: function (value, text, $selectedItem) {
        },
        forceSelection: false,
        selectOnKeydown: false,
        showOnFocus: false,
        on: "click"
        });
});
