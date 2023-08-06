// script that adds a <li> element to a list when
// the user clicks on the tag DIV#add_item
$(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
