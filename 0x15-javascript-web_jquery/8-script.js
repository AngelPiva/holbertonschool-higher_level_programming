$.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    dataType: 'json'
}).done(function(data) {
    const movies = data.results;

    for (let m = 0; m < movies.length; m++) {
        $('UL#list_movies').append('<li>' + movies[m].title + '</li>');
    }
});
