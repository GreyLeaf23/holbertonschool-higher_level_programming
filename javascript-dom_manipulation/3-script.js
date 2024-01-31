// Select the html elemnt 'toggle_header'.
const toggle_header = document.getElementById('toggle_header');

// Listen for a click event on the html element 'toggle_header'.
toggle_header.addEventListener('click', function() {
    // Select the header element.
    const header = document.querySelector('header');
    // Check the current class of the header element and toggle it.
    if (header.classList.contains('red')) {
        header.classList.toggle('green');
    } else {
        header.classList.toggle('red');
    }
});
