$(document).ready(function(){ 

  $('#worksheetType').dropdown({
    onChange: function (value, text, $selectedItem) {
      //console.log(value);
      if(value == 'testPaper')
      {
	console.log(value);
	$('#upload').css('display','none');
	$('#randomize').css('display','none');
	$('#segregate').css('display','none');
	$('#stud_name').css('display','none');
	$('#subject').css('display','block');
	$('#chapter').css('display','block');
	$('#submit').css('display','block');
        $('#qtype').css('display','none');
	$('#noOfQ').css('display','none');
	$('#noofQ').css('display','none');
      }
      else if(value == 'genericWorksheet')
      {
	console.log(value);
	$('#upload').css('display','none');
	$('#randomize').css('display','block');
	$('#segregate').css('display','block');
	$('#stud_name').css('display','none');
	$('#subject').css('display','block');
	$('#chapter').css('display','block');
	$('#qtype').css('display','block');
	$('#noOfQ').css('display','block');
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
	$('#noOfQ').css('display','block');
      }
    },
    forceSelection: false, 
    selectOnKeydown: false, 
    showOnFocus: false,
    on: "hover" 
  
});
 $('#subject').dropdown({
    onChange: function (value, text, $selectedItem) {
      console.log(value);
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
    on: "hover" 
  
});

  $('#chapter').dropdown({
    onChange: function (value, text, $selectedItem) {
      console.log(value.split(/\s*,\s*/));
    },
    forceSelection: false, 
    selectOnKeydown: false, 
    showOnFocus: false,
    on: "hover" 
  });
 $('#qtype').dropdown({
    onChange: function (value, text, $selectedItem) {
      console.log(value.split(/\s*,\s*/));
    },
    forceSelection: false, 
    selectOnKeydown: false, 
    showOnFocus: false,
    on: "hover" 
  });
  $('#stud_name').dropdown({
    onChange: function (value, text, $selectedItem) {
      console.log(value.split(/\s*,\s*/));
    },
    forceSelection: false,
    selectOnKeydown: false,
    showOnFocus: false,
    on: "hover"
  });	
});
