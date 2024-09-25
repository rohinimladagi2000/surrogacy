function checkUserSession() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("action", "getData");
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

  $.ajax({

      url: "/check_user_session/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
       
        if (response == 1) {
            $("#profile").show();
            $("#webLogout").show();
             $("#webLogin").hide();
            $("#webRegister").hide();
        }else{
            $("#webLogin").show();
            $("#webRegister").show();
            $("#profile").hide();
            $("#webLogout").hide();

        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}

checkUserSession();