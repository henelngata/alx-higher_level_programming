$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list :last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').children().remove();
  });
});
