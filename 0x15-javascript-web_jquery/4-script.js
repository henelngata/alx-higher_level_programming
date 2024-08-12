$(document).ready(function () {
  // Attach a click event handler to the <div id="red_header">
  $('DIV#toggle_header').click(function () {
    // Select the <header> element and add the class 'red'
    $('header').addClass('red');
    if ($('header').hasClass('red')) {
      $('header').addClass('green');
    } else {
      $('header').addClass('red');
    }
  });
});
