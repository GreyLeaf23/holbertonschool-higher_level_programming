// Select element with the 'add_item' id.
let add_item = document.getElementById('add_item');

// Listen for a click event on the html element 'add_item'.
add_item.addEventListener('click', function() {
    // Create a new element 'li'.
    let li = document.createElement('li');

    // Add the text 'Item' to the new element 'li'.
    li.textContent = 'Item';

    // Select the html element 'my_list'.
    let my_list = document.querySelector('.my_list');

    // Add the new element 'li' to the html element 'my_list'.
    my_list.appendChild(li);
});
