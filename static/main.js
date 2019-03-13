// ---- Fade In Website ----

$(document).ready(function() {
  $('#landing-page, footer').hide();
  $('#landing-page').fadeIn(3000 , function() {
    $('footer').fadeIn(1500);
  });
});

// ---- AJAX POST Function (Non-Reloding / Non-Refreshing) ----
$(document).ready(function() {
  $('form').on('submit', function(event) {
      $.ajax({
          url: '/subscribed',
          type: 'POST',
          data: {
              email : $('#input').val()
          }
      })
      .done(function(data){
        // ---- Validating Input ----
        if(data.error) {
          // Error Message
          $('#error-box').addClass("error").text(data.error).animate({left:'0px', width: 'toggle', opacity: 'toggle'}, 500, function(){
          $('#error-box').delay(3000).animate({width: 'toggle', opacity: 'toggle'}, 300);
          });
        } else {
          // Success Message
          $('#error-box').addClass("success").text(data.success).animate({left:'0px', width: 'toggle', opacity: 'toggle'}, 500, function(){
          $('#error-box').delay(3000).animate({width: 'toggle', opacity: 'toggle'}, 300);
          });
        }
      });
      // Remove Class after Use
      $('#error-box').removeClass("error");
      $('#error-box').removeClass("success");
      event.preventDefault();
  });
});
