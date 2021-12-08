

// CLIENT SIDE
var interactiveForm = function(){
    var CProj = $('#projection option:selected').val();
    // $('#movie') = 
    console.log(CProj);

    $.ajax({
        type: "POST",
        url: "/ajax",
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            console.log(result.result[CProj]);
            for (var i = 1; i <= result.result[CProj]; i++) {
                // if ()
                var stri = i.toString();
                $("#seats").append($('<option>', {value:stri, text:stri}));
            }

            var price = 5;
            var strprice = '<br>Price: '+ price.toString() + '€';
            $("#price").empty();
            $("#price").append(strprice);
        },
        error: function(error){
            console.log(error);
        },
    });

}   


$(function(){
    interactiveForm();
}
)