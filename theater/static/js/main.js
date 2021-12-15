
// client side
var interactiveForm = function(callback = null){
    var CProj = $('#projection option:selected').val();
    var numSeats = $('#seats option:selected').val();
    if (numSeats === undefined)
        numSeats = 1;
    $.ajax({
        type: "POST",
        url: "/ajax",
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            if (callback != null){
                callback(result)
            }
            else{
                // console.log(result.result[CProj]);
                // console.log(result.result);

                if (result.result[CProj] > 0)
                {
                    $("#more-seats").show();
                    $("#no-more-seats").hide();
                    $("#seats").find('option').not(':first').remove();
                    for (var i = 1; i <= result.result[CProj]; i++) {
                        var stri = i.toString();
                        if (i != 1){
                            $("#seats").append($('<option>', {value:stri, text:stri}));
                        }
                    }
                    var price = 5;  // think if use price as attribute or fixed
                    var totalPrice = price * numSeats;
                    var strprice = 'Price:&nbsp;&nbsp;('+ price.toString()+ 'x'+ numSeats +') = '+totalPrice.toString() + '€';
                    $("#price").empty();
                    $("#price").append(strprice);
                }else{
                    $("#more-seats").hide();
                    $("#no-more-seats").show();
                }

            }
            
        },
        error: function(error){
            console.log(error);
        },
    });

}  

var Price = function(){
    var CProj = $('#projection option:selected').val();
    var numSeats = $('#seats option:selected').val();
    if (numSeats === undefined)
        numSeats = 1;
    var price = 5;  // think if use price as attribute or fixed
    var totalPrice = price * numSeats;
    var strprice = 'Price:&nbsp;&nbsp;('+ price.toString()+ 'x'+ numSeats +') = '+totalPrice.toString() + '€';
    $("#price").empty();
    $("#price").append(strprice);
}  

$(document).ready(function(){
    
    interactiveForm (function(data) {
        // console.log(data['result']);

        for (var key in data['result']){
            if (data['result'][key] <= 0){
                $("#proj" + key.toString() + " td.seats").html("<p style='color:red;'>0<p>");
                $("#proj" + key.toString() + " td.sold").html("<a class='red'}}'>SOLD OUT</a>")
            }else{
                $("#proj" + key.toString() + " td.seats").html(data['result'][key]);
            }
        }
    });
    
})

$(function(){
    interactiveForm();
    Price();
})