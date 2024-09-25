
    function validateEmail(paramEmailID) {
      var filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;
      
      if (filter.test(paramEmailID)) {
        return true;
      } else {
        return false;
      }
    }

    // alert("Hello");

$("#btn_add").click(function (e) {
  //verification
  if ($("#selParent").val().trim().length < 1) {
    alert("Please Select parent");
    $("#selParent").focus();
    return false;
  }

  if ($("#txtName").val().trim().length < 1) {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  
 
  var formData = new FormData();
  
  formData.append("txtName", $("#txtName").val());
  formData.append("selParent", $("#selParent").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#dataTables-example").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/children_details/",
    type: "POST",
    // headers: {'X-CSRFToken': '{{ csrf_token }}'},
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {

        alert("Children Details Added Successfully");
        location.reload();
        table.ajax.reload();
        $("#add_modal").modal('hide');
      
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_add").attr("disabled", false);
    },
  });
});
// var sl_no = 0;
// ADD Testimnials data Table (DONE)
$(document).ready(function () {

  // $(window).on("load", function () {
    // alert("Hello");
    
  // });

  // $.fn.dataTableExt.errMode = 'ignore';
  //show data
  // var table = $("#tableData").DataTable();

  //   table.on( 'draw.dt', function () {
  //   var PageInfo = $('#tableData').DataTable().page.info();
  //        table.column(0, { page: 'current' }).nodes().each( function (cell, i) {
  //           cell.innerHTML = i + 1;
  //       });
  //   });

  //Edit modal submit click
  $(document).on("click", "#btn_update", function () {
    // alert("hi");

    if ($("#selParent1").val().trim().length < 1) {
      alert("Please Enter Parent Name");
      $("#selParent1").focus();
      return false;
    }

    if ($("#txtName1").val().trim().length < 1) {
      alert("Please Enter Name");
      $("#txtName1").focus();
      return false;
    }

    
    var formData = new FormData()
    formData.append("selParent1", $("#selParent1").val());
    formData.append("txtName1", $("#txtName1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");


    // var table = $("#dataTables-example").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/children_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Children Details Updated Succesfully");
        location.reload();
        table.ajax.reload();
        $("#edit_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_update").attr("disabled", false);
      },
    });
  });

  //Delete work step
  $(document).on("click", "#btn_delete", function () {

    var formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "delete");
    

    // var table = $("#dataTables-example").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
      },

      url: "/children_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Children Details deleted succesfully");
        location.reload();
        table.ajax.reload();
        $("#delete_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        // Reset Form
        //$("#view_field_form")[0].reset();
        $(".close").click();
      },
    });
  });

  $(document).on("click", "#add_user", function () {

    $("#txtName").val('');
    $("#txtEmail").val('');
    $("#txtMobileNo").val('');
    $("#txtPassword").val('');

  });
});

function getAdminData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");


  $.ajax({

      url: "/surrogate_parent_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // $("#dataTables-example tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].ap_id+'</td><td>'+response[i].ap_user_name+'</td><td>'+response[i].ap_user_email+'</td><td>'+response[i].ap_user_phone+'</td></tr>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}

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


function getRowsDelete() {
  $("#tableData tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      // alert(lclID);
      $("#delete_id").val(lclID);

  });
}

getAdminData();

  function getDoctorDetails(){
    var formData = new FormData();

    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());


      $.ajax({

      url: "/get_data/surrogate_parent/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log(response);
        // $("#dataTables-example tr:gt(0)").remove();
     
      for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#selParent").append("<option>"+response[i].ap_user_name+"</option>")
          $("#selParent1").append("<option>"+response[i].ap_user_name+"</option>")


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