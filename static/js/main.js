$(document).ready(function(){
    $( '#chicho' ).on( 'click', function() {
        if( $(this).is(':checked') ){
            $('body').css("background-color", "#272822");
            $('.card-panel').css("background-color", "#272822");
            $('.letras').css("color", "#E6E6E6");
        } else {
            $('body').css("background-color","white");
            $('.card-panel').css("background-color", "white");
            $('.letras').css("color", "#272822");
        }
    });
});
