

// CLIENT SIDE


var interactiveForm = function(){
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
            
            console.log(result.result[CProj]);
            console.log(result.result);

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
                $("#no-more-seats").show();
                $("#more-seats").hide();
                
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


$(function(){
    interactiveForm();
    Price();
}
)