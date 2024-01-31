// Select element with the 'update_header' id.
let update_header = document.getElementById('update_header');

// Listen for a click event on the html element 'update_header'.
update_header.addEventListener('click', function() {
    // Select the html element 'header'.
    let header = document.querySelector('header');

    // Change the text of the html element 'header'.
    header.textContent = 'New Header!!!';
});
