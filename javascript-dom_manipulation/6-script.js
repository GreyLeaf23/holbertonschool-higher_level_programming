// Send requst and fecth data from URL.
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
    // Select element with the 'character' id.
    let character = document.getElementById('character');
    let name = data.name;

    // Add the name of the character to the html element 'character'.
    character.textContent = "Character: " + name;
});

