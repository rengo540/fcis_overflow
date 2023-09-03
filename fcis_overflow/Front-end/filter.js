const filterButton = document.getElementById("filterButton");
const filterMenu = document.querySelector(".filterMenu");
const applyButton = document.querySelector("#filterContainer button[type='submit']");
const apply = document.querySelector(".fltr");
const courseNameInput = document.querySelector("#filterContainer input[type='search']");
const selectedFilters = {};

filterButton.addEventListener("click", () => {
    console.log("Button clicked");
    filterMenu.classList.toggle("active");
});

document.addEventListener('DOMContentLoaded', function () {
    const courseNameInput = document.querySelector('#courseNameInput');
    courseNameInput.addEventListener('input', function() {
      selectedFilters.courseName = this.value; 
    });
    
    const selectedFilters = {
      noAnswers: false,
      answered: false,
      sortBy: '',
      courseName: '',
    };
   
    
    function updateFilters() {
        selectedFilters.noAnswers = document.querySelector('input[name="radio"][value="No answers"]').checked;
        selectedFilters.answered = document.querySelector('input[name="radio"][value="answered"]').checked;
        selectedFilters.sortBy = document.querySelector('input[name="filterType"]:checked').value;
        selectedFilters.courseName = courseNameInput.value;
        
        // Get the selected level from the <select> element
        const selectedLevel = document.querySelector('#lvls').value;
        selectedFilters.level = selectedLevel;
        
       
        console.log(selectedFilters); 
    }
  
    const applyButton = document.querySelector('button[type="submit"]');
    applyButton.addEventListener('click', () => {
        updateFilters();
        console.log(selectedFilters);
    });
  
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', updateFilters);
    });
  
    const radioButtons = document.querySelectorAll('input[name="filterType"]');
    radioButtons.forEach(radioButton => {
      radioButton.addEventListener('change', updateFilters);
    });
    apply.addEventListener('click' , ()=>{
      updateFilters();
      filterMenu.classList.remove("active");
    })
  });