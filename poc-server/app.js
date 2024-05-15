const express = require('express');
const bodyParser = require('body-parser');
const low = require('lowdb');
const FileSync = require('lowdb/adapters/FileSync');
const path = require('path'); // Required for file paths

// Create express app
const app = express();

// Parse requests of content-type - application/json
app.use(bodyParser.json());

// Parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Initialize database
const adapter = new FileSync('db.json');
const db = low(adapter);

// Set default data structure in the database
db.defaults({ users: [] }).write();

// Endpoint to save user input to the database
app.post('/user', (req, res) => {
    const { name, email } = req.body;
    if (!name || !email) {
        return res.status(400).send('Name and email are required');
    }
    db.get('users')
        .push({ name, email })
        .write();
    res.send('User added successfully');
});

// Endpoint to serve the HTML form
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Endpoint to return users in table format
app.get('/users', (req, res) => {
    const users = db.get('users').value();
    let html = '<!DOCTYPE html><html><head><title>Users List</title></head><body>';
    html += '<h1>Users List</h1><table border="1">';
    html += '<tr><th>Name</th><th>Email</th></tr>';
    users.forEach(user => {
        html += `<tr><td>${user.name}</td><td>${user.email}</td></tr>`;
    });
    html += '</table></body></html>';
    res.send(html);
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
