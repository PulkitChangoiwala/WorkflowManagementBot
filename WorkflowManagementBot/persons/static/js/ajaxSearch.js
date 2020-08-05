$(function()
    {
        $("#user-input-name, #user-input-company, #user-input-designation").keyup(function()
             {
                $.ajax(
                    {
                      type :"POST",
                      url  : "searchList",
                      data :
                        {
                          'search_name': $('#user-input-name').val(),
                          'search_company':$('#user-input-company').val(),
                          'search_designation':$('#user-input-designation').val(),
                          'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                        },
                        success: searchSuccess,
                        dataType: 'html'
                    })

             })

    });


 /*


$(function()
    {
        $("#user-input-company").keyup(function()
             {
                $.ajax(
                    {
                      type :"POST",
                      url  : "searchList",
                      data :
                        {
                          'search_name': $('#user-input-name').val(),
                          'search_company':$('#user-input-company').val(),
                          'search_designation':$('#user-input-designation').val(),
                          'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                        },
                        success: searchSuccess,
                        dataType: 'html'
                    })

             })

    });

$(function()
{
    $("#user-input-designation").keyup(function()
         {
            $.ajax(
                {
                  type :"POST",
                  url  : "searchList",
                  data :
                    {
                      'search_name': $('#user-input-name').val(),
                      'search_company':$('#user-input-company').val(),
                      'search_designation':$('#user-input-designation').val(),
                      'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                    },
                    success: searchSuccess,
                    dataType: 'html'
                })

         })

});





 */

function searchSuccess(data, textStatus, jqXHR)
{
     let lis = document.getElementById("mainList");
     //console.log(lis.childNodes.length    )
     lis.style.display = "none";
     //console.log(data);
    $('#replaceable-content').html(data)
}