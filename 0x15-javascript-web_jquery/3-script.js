$(document).ready(function() {
    // Attach a click event handler to the <div id="red_header">
    $('#red_header').click(function() {
        // Select the <header> element and add the class 'red'
        $('header').addClass('red');
    });
});