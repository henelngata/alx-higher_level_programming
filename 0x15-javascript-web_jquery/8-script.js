$.get(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus, jqXHR) {
    $.each(data.results, function (index, movieTitle) {
      $('UL#list_movies').append('<li>' + movieTitle.title + '</li>');
    });
  }
);
