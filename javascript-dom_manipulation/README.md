# Javascript DOM Manipulation Learning!




# General Questions:




## How to select HTML elements in JavaScript?
In JavaScript, you can select HTML elements using various methods. Here are a few examples:

1. `getElementById`: This method gets an element by its ID.

```javascript
var element = document.getElementById('myId');
```

2. `getElementsByClassName`: This method gets elements by their class name.

```javascript
var elements = document.getElementsByClassName('myClass');
```

3. `getElementsByTagName`: This method gets elements by their tag name.

```javascript
var elements = document.getElementsByTagName('div');
```

4. `querySelector`: This method gets the first element that matches a specified CSS selector(s) in the document.

```javascript
var element = document.querySelector('.myClass');
```

5. `querySelectorAll`: This method gets all elements in the document that matches a specified CSS selector(s).

```javascript
var elements = document.querySelectorAll('.myClass');
```

Remember that `querySelector` and `querySelectorAll` are more versatile because they can use any CSS selector, while the other methods are
limited to selecting by id, class, or tag.




## What are differences between ID, class and tag name selectors?
In HTML and CSS, ID, class, and tag name are different types of selectors used to target elements. Here are the differences:

1. **ID Selector**: An ID is a unique identifier for an element within a web page. It can be used to select one specific element. An ID is
defined in HTML with the `id` attribute and in CSS, it is selected with a hash (`#`) before the ID name. For example:

```html
<div id="myId"></div>
```
```css
#myId {
  color: red;
}
```

2. **Class Selector**: A class can be used to select one or more elements. It is not unique like an ID; multiple elements can have the same
class. A class is defined in HTML with the `class` attribute and in CSS, it is selected with a dot (`.`) before the class name. For example:

```html
<div class="myClass"></div>
```
```css
.myClass {
  color: blue;
}
```

3. **Tag Name Selector**: A tag name selector selects all elements with the given tag name. It is the most general selector. In CSS, it is
selected by simply using the tag name. For example:

```html
<div></div>
```
```css
div {
  color: green;
}
```

In JavaScript, you can select elements by ID, class, or tag name using `document.getElementById`, `document.getElementsByClassName`, and
`document.getElementsByTagName` respectively.




## How to modify an HTML element style?
In JavaScript, you can modify an HTML element's style using the `style` property. This property is both readable and writable, and represents
the inline style of an element.

Here's an example of how to change the color of a `div` element with the id `myId` to red:

```javascript
var element = document.getElementById('myId');
element.style.color = 'red';
```

In this example, `color` is a CSS property that sets the color of the text. You can replace `color` with any CSS property you want to modify,
and 'red' with the value you want to set.

Note that CSS property names are written in camel case in JavaScript (e.g., `backgroundColor`), instead of kebab-case (e.g.,
`background-color`)
as in CSS.




## How to get and update an HTML element content?
In JavaScript, you can get and update an HTML element's content using the `innerHTML`, `textContent`, or `innerText` properties.

Here's an example of how to get and update the content of a `div` element with the id `myId`:

```javascript
// Get the element
var element = document.getElementById('myId');

// Get the current content
var currentContent = element.innerHTML;

// Update the content
element.innerHTML = 'New content';
```

In this example, `innerHTML` gets or sets the HTML content (inner HTML) of an element. If you want to work with the text content only, you
can use `textContent` or `innerText`. Note that `innerText` is aware of style and will not return hidden text, while `textContent` will
return the full text content, including what might be hidden due to CSS.




## How to modify the DOM?
Modifying the Document Object Model (DOM) in JavaScript can be done in several ways. Here are some common methods:

1. **Changing an element's content**: You can change the content of an HTML element using the `innerHTML`, `textContent`, or `innerText`
properties.

```javascript
var element = document.getElementById('myId');
element.innerHTML = 'New content';
```

2. **Changing an element's style**: You can change the style of an HTML element using the `style` property.

```javascript
var element = document.getElementById('myId');
element.style.color = 'red';
```

3. **Adding and removing elements**: You can add new elements using the `createElement` and `appendChild` methods, and remove them using the
`removeChild` method.

```javascript
// Create a new element
var newElement = document.createElement('div');
newElement.innerHTML = 'New element';

// Add the new element to the body
document.body.appendChild(newElement);

// Remove the new element
document.body.removeChild(newElement);
```

4. **Adding and removing attributes**: You can add new attributes using the `setAttribute` method, and remove them using the
`removeAttribute` method.

```javascript
var element = document.getElementById('myId');
element.setAttribute('class', 'myClass'); // Add a new attribute
element.removeAttribute('class'); // Remove an attribute
```

Remember that all these modifications will only affect the current page and will be lost when the page is reloaded, unless they are saved
and reapplied somehow (like in a database or local storage).




## How to make a request with XmlHTTPRequest?
The `XMLHttpRequest` object is used to interact with servers. You can retrieve data from a URL without having to do a full page refresh.
Here's an example of how to make a GET request:

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data', true);
xhr.onreadystatechange = function () {
  if (xhr.readyState == 4 && xhr.status == 200)
    console.log(xhr.responseText);
}
xhr.send();
```

In this example:

- A new `XMLHttpRequest` object is created.
- The `open` method initializes a request. The first argument is the HTTP method, the second argument is the URL, and the third argument is
a boolean indicating whether the request should be asynchronous.
- The `onreadystatechange` event listener is set to a function that will be called whenever the `readyState` property changes. When
`readyState` is 4 (the request is complete) and `status` is 200 (OK), the response text is logged to the console.
- The `send` method sends the request.

Remember to replace `'https://api.example.com/data'` with the URL you want to make a request to.




## How to make a request with Fetch API?
The Fetch API provides a more modern and powerful alternative to `XMLHttpRequest` for making HTTP requests. Here's an example of how to make
a GET request using the Fetch API:

```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There has been a problem with your fetch operation:', error));
```

In this example:

- The `fetch` function is called with the URL as an argument.
- The `fetch` function returns a `Promise` that resolves to the `Response` object representing the response to the request.
- The `then` method is called on the `Promise` to handle the response when it's available. The `Response` object's `json` method is used to
parse the response body as JSON, and this also returns a `Promise`.
- Another `then` method is called to handle the resulting data when it's available.
- The `catch` method is called to handle any errors that may have occurred.

Remember to replace `'https://api.example.com/data'` with the URL you want to make a request to.




## How to listen/bind to DOM events?
In JavaScript, you can listen to or bind to DOM events using the `addEventListener` method. This method is called on an HTML element and
takes two arguments: the name of the event to listen for, and a function to execute when the event occurs.

Here's an example of how to listen for a click event on a button with the id `myButton`:

```javascript
var button = document.getElementById('myButton');
button.addEventListener('click', function(event) {
  console.log('Button was clicked!');
});
```

In this example, the `addEventListener` method is called on the button element. The first argument is the string `'click'`, which is the
name of the event to listen for. The second argument is a function that will be executed whenever the button is clicked. This function takes
one argument, `event`, which is an object containing information about the event.

You can replace `'click'` with the name of any event you want to listen for, such as `'mouseover'`, `'keydown'`, `'load'`, etc. The function
can contain any code you want to execute when the event occurs.




## How to listen/bind to user events?
Listening to user events in JavaScript is similar to listening to DOM events. User events are essentially a subset of DOM events that
specifically involve interaction with the user, such as clicks, key presses, mouse movements, etc.

You can use the `addEventListener` method to listen for these events. Here's an example of how to listen for a keydown event:

```javascript
window.addEventListener('keydown', function(event) {
  console.log('A key was pressed!');
});
```

In this example, the `addEventListener` method is called on the `window` object to listen for a keydown event anywhere in the window. The
first argument is the string `'keydown'`, which is the name of the event to listen for. The second argument is a function that will be
executed whenever a key is pressed. This function takes one argument, `event`, which is an object containing information about the event.

You can replace `'keydown'` with the name of any user event you want to listen for, such as `'click'`, `'mousemove'`, `'keyup'`, etc. The
function can contain any code you want to execute when the event occurs.
