$(document).ready(function () {
    var $drop_down_value;


    $('.dropdown-item').click(function () {
        $drop_down_value = $(this).text()
        console.log($(this).text());
      $(".btn:first-child").html($(this).text()+' <span class="caret"></span>');

    });



    $('#recipe-search-from').keypress(function (event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        console.log($('#recipe-search-from').val())
        console.log($drop_down_value)

        if (keycode == '13') {
            window.location.assign("/searchByName/" + $('#recipe-search-from').val());
        }

    });

    $('#ingredients-search-from').keypress(function (event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        console.log($('#ingredients-search-from').val())
        console.log($drop_down_value)

        if (keycode == '13') {
            window.location.assign("/searchByIngredient/" + $('#ingredients-search-from').val());
        }

    });
    //  $('#ingredientCard').click(function () {
    //      console.log( $('#ingredientCard').val())
    //      window.location.assign("/searchById/" + $('#ingredientCard').val());
    //
    //
    // });
    $('#goBackButton').on('click', function(e){
    e.preventDefault();
    window.history.back();
    });


})


