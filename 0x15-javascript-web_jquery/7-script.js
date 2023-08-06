// script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data, stats) {
      $('DIV#character').append(data.name);
    });
});
