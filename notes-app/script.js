let darkMode = false;

document.getElementById('dark-mode').addEventListener('click', function() {
    if (darkMode === false) {
        document.body.classList.add('dark')
        darkMode = true;
    } else {
        document.body.classList.remove('dark')
        darkMode = false;
    } 
})


let notesList = [
    { title: "Take dog out", message: "Please remember to take the dog out today" },
    { title: "Grocery shopping", message: "Buy milk, eggs, bread, and coffee" },
    { title: "Meeting with John", message: "Discuss project updates at 3 PM" },
    { title: "Call mom", message: "Catch up and see how she's doing" },
    { title: "Submit assignment", message: "Finish and upload the essay by Friday" },
    { title: "Dentist appointment", message: "Scheduled for 10 AM on Thursday" },
    { title: "Yoga class", message: "Attend online session at 7 PM tonight" }
];


function updateScreen() {
    for (note of notesList) {
        let noteDiv = document.createElement('div');
        noteDiv.classList.add('note');
        noteDiv.innerHTML = `
            <h2> ${note.title} </h2>
            <p> ${note.message}</p>
        `
        document.getElementById('notes').appendChild(noteDiv);
    }
}


document.getElementById('add-note').addEventListener('click', function() {
    let myTitle = document.getElementById('note-title').value;
    let myMessage = document.getElementById('message').value;
    notesList.push({
        title: myTitle,
        message: myMessage
    })
    updateScreen();

})

updateScreen();