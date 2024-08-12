$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET'
  })
    .done(function (data) {
      $('#hello').text(data.hello);
    })
    .fail(function (error) {
      console.error('There was a problem with the fetch operation:', error);
    });
});
