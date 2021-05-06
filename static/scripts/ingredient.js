$(document).ready(function () {
  var $drop_down_value;

  // $('#recipe-search-from').keypress(function(event){
  //       var keycode = (event.keyCode ? event.keyCode : event.which);
  //       console.log(keycode)
  //       if(keycode == '13'){
  //          alert('You pressed a "enter" key in textbox, here submit your form');
  //          window.location.assign("/search/" + $('#recipe-search-from').val());
  //       }
  //   });


  $('#recipe-search-from').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        console.log(keycode)
        if(keycode == '13'){
           alert('You pressed a "enter" key in textbox, here submit your form');
           window.location.assign("/search/" + $('#recipe-search-from').val());
        }
    });
})


