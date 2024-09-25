  function getParentDetails(){
    var formData = new FormData();

    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

      $.ajax({

      url: "/get_data/parent_info/",
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

      }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });
  }
  getParentDetails();



$("#selParent").change(function(){

  // alert($("#selParent").val());

    var formData = new FormData();
    formData.append("selParent", $("#selParent").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

      $.ajax({

      url: "/get_child_info/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // alert(response.length);
        // $("#dataTables-example tr:gt(0)").remove();
        let amount = 20000;
        let finalAmount = amount*response.length;

     
      for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#no_of_children").val(response.length);
          $("#amount").val(finalAmount);


      }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });
});


$("#generate").click(function(){
    var formData = new FormData();
    formData.append("selParent", $("#selParent").val());
    formData.append("no_of_children", $("#no_of_children").val());
    formData.append("amount", $("#amount").val());

    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

      $.ajax({

      url: "/generate_receipt/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        if(response == "1"){
          alert("Receipt already generated");
        }else{
          alert("Receipt generated Successfully");
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });
})