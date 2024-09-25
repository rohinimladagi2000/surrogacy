function getAdminData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("action", "getData");
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

  $.ajax({

      url: "/child_info_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // $("#dataTables-example tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].ch_id+'</td><td>'+response[i].ch_name+'</td><td>'+response[i].ch_hospital_name+'</td><td>'+response[i].ch_parent_name+'</td></tr>');
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