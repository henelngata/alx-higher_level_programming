$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    if (event.type === 'click' || event.which === 13) {
      const lang = $('#language_code').val();
      $.get(
        'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang,
        function (data) {
          $('#hello').text(data.hello);
        }
      );
    }
  });
});
