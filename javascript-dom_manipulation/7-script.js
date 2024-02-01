// Fetch the URL info.
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        // Select 'ul' element.
        let ul = document.querySelector('#list_movies');

        // Loop through the movies.
        for (let i = 0; i < data.results.length; i++) {
            // Create a new element 'li'.
            let li = document.createElement('li');

            // Add the title of the movie to the new element 'li'.
            li.textContent = data.results[i].title;

            // Add the new element 'li' to the 'ul' element.
            ul.appendChild(li);
        }
    });
