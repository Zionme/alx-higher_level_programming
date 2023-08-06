// script that fetches and prints how to say “Hello” depending on the language
// from https://www.fourtonfish.com/hellosalut/hello/
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data, stat) {
      $('DIV#hello').text(data.hello);
    });
  });
});
