import * as utils from './utils/utils.js';

$(document).on('click','#download-question-format-button', function() {
  console.log("got in");
  $.ajax({
    url: BASE_DIR + "/get_dummy_question_paper_format",
    method : "get",
    data: {},
    headers: { "X-CSRFToken": csrftoken, crossOrigin: false},
    success: function(response) {
      let sampleArr = utils.base64ToArrayBuffer(response);
      utils.saveByteArray("dummy_question_bank.xlsx", sampleArr, 'multipart/form-data');
    }
  });

});
