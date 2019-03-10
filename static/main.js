//Fade In Website

$(document).ready(function() {
  $('section').hide().fadeIn(1500);
});

//Window = Section Size//

$(document).ready(function() {
  function setHeight() {
    windowHeight = $(window).innerHeight();
    windowWidth = $(window).width();
    $('section').css('min-height', windowHeight);
    $('section').css('width', w);
  };
  setHeight();

  $(window).resize(function() {
    setHeight();
  });
});
