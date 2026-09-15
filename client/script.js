// Fetch all events from the backend and render each one on page load
fetch("http://localhost:5000/events")
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  });

// Handle new event submissions
document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault(); // stop the page from reloading on submit

  const titleInput = document.querySelector("#title");
  const title = titleInput.value;

  // Send the new event title to the backend
  fetch("http://localhost:5000/events", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  })
  .then(response => response.json())
  .then(event => {
    renderEvent(event);   // add the new event to the page
    titleInput.value = ""; // clear the input for the next entry
  });
});

// Create a list item for an event and append it to the event list
function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  document.querySelector("#event-list").appendChild(li);
}