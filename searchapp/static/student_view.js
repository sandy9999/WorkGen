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
	$('#subject').dropdown({
		onChange: function (value, text, $selectedItem) {
		if(value == "Science")
		{
			$('#chapter .menu div').remove();
			$('<div class="item" data-value="Motion">Motion</div>').appendTo('#chapter .menu');
		}
		else if(value == "Math")
		{
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
