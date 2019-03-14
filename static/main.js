// ---- Fade In Website ----

// $(document).ready(function() {
//   $('#landing-page, footer').hide();
//   $('#landing-page').fadeIn(3000, function() {
//     $('footer').fadeIn(1500);
//   });
// });

// ---- AJAX POST Function (Non-Reloding / Non-Refreshing) ----
$(document).ready(function() {
  $('form').on('submit', function(event) {
    $.ajax({
        url: '/subscribed',
        type: 'POST',
        data: {
          email: $('#input').val()
        }
      })
      .done(function(data) {
        $('#subscibe_btn').toggle();
        // ---- Validating Input ----
        if (data.error) {
          // Show the error icon
          $('#error-icon').css({
            'width': ($('#subscibe_btn').outerWidth())
          }).toggle();
          //Error Effect (Shake)
          $(function() {
            var l = 20;

            for (var i = 0; i <= 10; i++) {
              $('form').animate({
                'margin-left': '+=' + (l = -l) + 'px',
                'margin-right': '-=' + l + 'px'
              }, 50, function() {
                $('form').css({
                  'margin-left': '0px',
                  'margin-right': '0px'
                })
              });
            }
          });

          // Success Process
          $('#error-box').addClass("error").css({
            'width': ($('input').outerWidth())
          }).animate({
            left: '0px',
            width: 'toggle',
            opacity: 'toggle'
          }, 500, function() {
            $(this).delay(700).html(data.error);
            $(this).delay(3000).animate({
              width: 'toggle',
              opacity: 'toggle'
            }, 500, function() {
              $('#subscibe_btn').toggle();
              $('#error-icon').toggle();
            });
          });
        } else {
          // Success Message

          // Show the error icon
          $('#success-icon').css({
            'width': ($('#subscibe_btn').outerWidth())
          }).toggle();

          // Success Process
          $('#error-box').addClass("success").css({
            'width': ($('input').outerWidth())
          }).animate({
            left: '0px',
            width: 'toggle',
            opacity: 'toggle'
          }, 500, function() {
            $(this).delay(700).html(data.success);
            $(this).delay(3000).animate({
              width: 'toggle',
              opacity: 'toggle'
            }, 500, function() {
              $('#subscibe_btn').toggle();
              $('#success-icon').toggle();
            });
          });
        }
      });
    // Remove Temporary Used Configurations
    $('#error-box').removeClass("error").removeClass("success").empty();
    event.preventDefault();
  });
});
