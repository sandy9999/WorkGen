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
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"
});

$('#subject').dropdown({
	onChange: function (value, text, $selectedItem) {
		if(value == "Science") {
			$('#chapter .menu div').remove();
			$('<div class="item" data-value="Motion">Motion</div>').appendTo('#chapter .menu');
		}
		else if(value == "Math") {
			$('#chapter div div').remove();
			$('<div class="item" data-value="Rational Nos">Rational Nos</div>').appendTo('#chapter .menu');
		}
		},
		forceSelection: false,
		selectOnKeydown: false,
		showOnFocus: false,
		on: "click"
	});
	$('#chapter').dropdown({
	onChange: function (value, text, $selectedItem) {
	},
	forceSelection: false,
	selectOnKeydown: false,
	showOnFocus: false,
	on: "click"
});

$('#qtype').dropdown({
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