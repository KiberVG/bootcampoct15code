const flashcardContainer = document.getElementById('flashcardContainer');

// Imagine you got these cards after querying your database
let cards = [
    {Term: "HTML", Definition: "Markup language"},
    {Term: "CSS", Definition: "Style sheet language"},
    {Term: "JavaScript", Definition: "Programming language for the web"},
    {Term: "Python", Definition: "High-level programming language"},
    {Term: "SQL", Definition: "Language for managing databases"},
    {Term: "API", Definition: "Application Programming Interface"},
    {Term: "JSON", Definition: "JavaScript Object Notation"},
    {Term: "Node.js", Definition: "JavaScript runtime environment"}
];

// Function to initialize predefined cards
function initializeCards() {
    for (let card of cards) {
        createFlashcard(card.Term, card.Definition)
    }
}

// Function to create and display a flashcard
function createFlashcard(term, definition) {
    let flashcard = document.createElement('div')
    flashcard.classList.add('flashcard')
    flashcard.dataset.term = term;
    flashcard.dataset.definition = definition;
    flashcard.innerText = term;
    flashcardContainer.appendChild(flashcard)

    flashcard.addEventListener('click', ()=> {
        toggleCard(flashcard)
    })

}

// Add card function for user input
function addCard() {
    const termInput = document.getElementById('termInput').value;
    const definitionInput = document.getElementById('definitionInput').value;
    
    // Creating a new card and updating the list
    createFlashcard(termInput, definitionInput);

    // Resetting the input
    document.getElementById('termInput').value = '';
    document.getElementById('definitionInput').value = '';
   
}


// Function to toggle between showing term and definition
function toggleCard(card) {
    if (card.classList.contains('flipped')) {
        card.classList.remove('flipped')
        card.innerText = card.dataset.term
    } else {
        card.classList.add('flipped')
        card.innerText = card.dataset.definition
    }
}


// Initialize predefined flashcards
initializeCards();


// Advantages of using dataset
// Save time and avoid having to loop through an array and updating an array or map for memory
// Also think about having to delete