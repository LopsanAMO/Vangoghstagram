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

    (function( $ ){
       $.fn.get_csrf = function() {
           var end, start;
           start = document.cookie.indexOf('csrftoken=');
           end = document.cookie.indexOf(";", start);
           if (-1 === end) {
             end = document.cookie.length;
           }
           csrftoken = document.cookie.substring(start, end).replace('csrftoken=', '');
           return csrftoken;
       };
   })( $ );
   var random = Math.floor(Math.random()*10);
    $.ajax({
            method: 'POST',
            url: '/user/image/',
            headers: {
                'x-csrftoken': $().get_csrf()
            },
            data:{
                img_url: $('.img_van').eq(random ? random > 0 : 1).attr('src')
            },
            success: function (data) {
                console.log(data);
                $(".img_van").eq(random ? random > 0 : 1).attr("src", data.img_url);
            },
            error: function(data, qXRH, status, throwStatus) {
                console.log('holis, fallo algo');
            }
        });

});
