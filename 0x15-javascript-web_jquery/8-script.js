$.get('http://swapi.co/api/films?format=json', (data) => {
  for (let y = 0; y < data.results.length; y++) {
    $('ul#list_movies').append('<li>' + data.results[y].title + '</li>');
  }
});
