const path = require('path'); // Required for file paths
const express = require('express');
const cors = require('cors'); // Import cors

// Create express app
const app = express();

// Define CORS options
const corsOptions = {
	origin: '*',
  methods: 'GET,POST',
  allowedHeaders: 'Content-Type',
};

// Enable CORS with the specified options
app.use(cors(corsOptions));

const port = 4000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a route for serving the xss.js file with the correct MIME type
app.get('/xss.js', (req, res) => {
  // Set the Content-Type header to 'application/javascript'
  res.setHeader('Content-Type', 'application/javascript');

// Set the Content Security Policy header
  res.setHeader('Content-Security-Policy', "default-src 'self'");

	// Send the xss.js file
  res.sendFile(path.join(__dirname, 'public', 'xss.js'));
});

// Define your existing route
app.get('/callback', (req, res) => {
  // Collect minimal information
  const data = {
    id: req.query.id || '',
    title: req.query.title || 'Untitled',
    protocol: req.query.protocol || '',
    domain: req.query.domain || '',
    port: req.query.port || '',
    pathname: req.query.pathname || '',
    navigator_ua: req.query.navigator_ua || '',
    navigator_platform: req.query.navigator_platform || '',
    timestamp: req.query.timestamp || ''
  };

  // Report
  console.log('Data collected:', data);

  // Send response
  res.send('Data received successfully');
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
