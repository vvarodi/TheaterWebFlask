

// CLIENT SIDE
var interactiveForm = function(){
    var CProj = $('#projection option:selected').val();
    // $('#movie') = 
    console.log(CProj);

    $.ajax({
        url:"/ajax",
        type:"POST",
        dataType: "json",
        success: function(response){
            console.log(response)

        },
        error: function(error){
            console.log(error);
        },
        });

}   

//     // $.ajax({
//     //     type: "GET",
//     //     url: "/reservation/" + Cproj}).done(function(data){
//     //     $("#choosen").empty();
//     //     // if($("#vcenter").hasClass("category-filter")){
//     //     //   $("#datacenter").append(
//     //     //     $("<option></option>").attr("value", "0").text(" --- ")
//     //     //   );
//     //     });
// }

$(function(){
    interactiveForm();
}
)