let notes = [];

async function addNote() {
    const input = document.getElementById('noteInput');
    const note = input.value.trim();
    if (note === '') return;
    const response = await fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ note })
    });
    notes = await response.json();
    input.value = '';
    renderNotes();
}

async function deleteNote(index) {
    const response = await fetch('/delete/' + index, { method: 'DELETE' });
    notes = await response.json();
    renderNotes();
}

async function loadNotes() {
    const response = await fetch('/notes');
    notes = await response.json();
    renderNotes();
}

function renderNotes() {
    const list = document.getElementById('noteList');
    list.innerHTML = '';
    notes.forEach((note, i) => {
        const li = document.createElement('li');
        li.textContent = note;
        const btn = document.createElement('button');
        btn.textContent = 'Delete';
        btn.onclick = () => deleteNote(i);
        li.appendChild(btn);
        list.appendChild(li);
    });
}

window.onload = loadNotes;
