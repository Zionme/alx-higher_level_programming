// script that fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, stats) {
      $(data.results).each(function (ind, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    });
});
