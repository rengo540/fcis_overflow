const tagsInput = document.getElementById('tagsInput');
const tagsContainer = document.getElementById('tagsContainer');
const savedTagsContainer = document.getElementById('savedTagsContainer');
const savedTagsDisplay = document.getElementById('savedTagsDisplay');
const savedTags = []; // Array to store saved tags
const Tags = ["operating", "algorithms", "physics"];
let isProcessingEnter = false;

tagsInput.addEventListener('keydown', handleKeyDown);
tagsInput.addEventListener('input', handleInput);

function handleKeyDown(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    if (!isProcessingEnter) {
      isProcessingEnter = true;
      const tag = tagsInput.value.trim();
      if (tag !== '') {
        savedTags.push(tag); // Save the tag in the array
        addTag(tag);
        tagsInput.value = '';
        displaySavedTags(); // Display saved tags
      }
      isProcessingEnter = false;
    }
  }
}

function handleInput() {
  const inputText = tagsInput.value.toLowerCase();
  const filteredTags = Tags.filter(tag => tag.includes(inputText));
  displayRecommendedTags(filteredTags);
}

function displayRecommendedTags(tags) {
  tagsContainer.innerHTML = '';
  tags.forEach(tag => {
    const tagElement = document.createElement('span');
    tagElement.classList.add('tag');
    tagElement.textContent = tag;
    tagElement.addEventListener('click', () => addSuggestedTag(tag));
    tagsContainer.appendChild(tagElement);
  });
}

function addSuggestedTag(tag) {
  savedTags.push(tag); // Save the tag in the array
  tagsInput.value = tag; // Set the clicked tag as input value
  addTag(tag); // Add the tag visually
  tagsContainer.innerHTML = ''; // Clear suggested tags
  displaySavedTags(); // Display saved tags
}

function displaySavedTags() {
  savedTagsContainer.innerHTML = ''; // Clear the container first

  savedTags.forEach(tag => {
    const savedTagElement = document.createElement('span');
    savedTagElement.classList.add('tag');
    savedTagElement.textContent = tag;
    savedTagsContainer.appendChild(savedTagElement);
  });

  // Update the tagsInput value
  tagsInput.value = savedTags.join(', ');
}

function addTag(tag) {
  const tagElement = document.createElement('span');
  tagElement.classList.add('tag');
  tagElement.textContent = tag;
  tagsContainer.appendChild(tagElement);
  console.log(savedTags);
}
