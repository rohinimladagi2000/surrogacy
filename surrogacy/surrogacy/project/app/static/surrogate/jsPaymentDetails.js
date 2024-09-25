function getAdminData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

  $.ajax({

      url: "/payment_details_surrogate/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // $("#dataTables-example tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].re_id+'</td><td>'+response[i].re_hospital_name+'</td><td>'+response[i].re_parent_name+'</td><td>'+response[i].re_child_count+'</td><td>'+response[i].re_amount+'</td></tr>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}

getAdminData();
