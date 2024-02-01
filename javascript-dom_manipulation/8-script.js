// Wait for the document to be ready before executing any code.
document.addEventListener('DOMContentLoaded', function () {
    // Fetch URL info.
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // Select 'hello' element.
            let header = document.querySelector('#hello');

            // Add the greeting to the 'hello' element.
            header.textContent = data.hello;
        });
});
