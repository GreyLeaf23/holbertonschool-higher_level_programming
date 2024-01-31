// Select the header element.
const red_header = document.getElementById('red_header');

// Listen for a click event on the html element 'red_header'.
red_header.addEventListener('click', function() {
    const header = document.querySelector('header');
    // Add the class 'red' to the header element.
    header.classList.add('red');
    });
