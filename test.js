// Get references to the button and the container
const myButton = document.getElementById('myButton');
const myContainer = document.getElementById('myContainer');

// Define a function to handle the replacement
function replaceElement() {
  // Create the new element
  const newElement = document.createElement('p'); // Example: creating a new paragraph
  newElement.textContent = 'This is the new content!';
  newElement.classList.add('new-style'); // Optional: add a class for styling

  // Clear the existing content of the container
  myContainer.innerHTML = '';

  // Append the new element to the container
  myContainer.appendChild(newElement);
}

// Attach an event listener to the button
myButton.addEventListener('click', replaceElement);