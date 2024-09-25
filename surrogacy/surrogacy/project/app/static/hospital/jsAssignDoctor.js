function getAdminData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

  $.ajax({

      url: "/get_data/parent_info/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log(response)
        $("#dataTables-example tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].ap_id+'</td><td>'+response[i].ap_user_name+'</td><td>'+response[i].ap_user_email+'</td><td>'+response[i].ap_user_phone+'</td><td>'+response[i].ap_doctor+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-bs-toggle="modal" data-bs-target="#edit_modal"  class="text-primary" onClick="getRowsUpdate();">Assign Doctor</a></td></tr>');
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

function getRowsUpdate() {
  $("#tableData tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      var lclName = currentRow.find("td:eq(2)").text();
      var lclEmail = currentRow.find("td:eq(3)").text();
      var lclMobile = currentRow.find("td:eq(4)").text();
      var lclRole = currentRow.find("td:eq(5)").text();
      // alert(lclID);  
      $("#txtName1").val(lclName);
      $("#txtEmail1").val(lclEmail);
      $("#txtMobileNo1").val(lclMobile);
      $("#selRole1").val(lclRole);
      $("#edit_id").val(lclID);

  });
}

  $(document).on("click", "#btn_update", function () {
    // alert("hi");

    if ($("#selDoctor").val().trim().length < 1) {
      alert("Please Select Doctor");
      $("#selDoctor").focus();
      return false;
    }

    var formData = new FormData();
    formData.append("id", $("#edit_id").val());
    formData.append("selDoctor", $("#selDoctor").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({

        url: "/assignDoctor/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          // $("#dataTables-example tr:gt(0)").remove();
          alert("Doctor Assigned succesfully");
          location.reload();
          table.ajax.reload();
        },
        error: function (request, error) {
          console.error(error);
        },
        complete: function () {

        },
      });

 
  });


  function getDoctorDetails(){
    var formData = new FormData();

    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

      $.ajax({

      url: "/get_data/doctor/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log(response);
        // $("#dataTables-example tr:gt(0)").remove();
     
      for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#selDoctor").append("<option>"+response[i].dc_name+"</option>")

      }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });
  }
  getDoctorDetails();