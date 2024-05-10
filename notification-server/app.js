const path = require('path'); // Required for file paths
const express = require('express');

const app = express();
const port = 4000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/callback', (req, res) => {
  // Collect minimal information
  const data = {
    id: req.query.id || '',
    title: req.query.title || 'Untitled',
    protocol: req.query.protocol || '',
    domain: req.query.hostname || '',
    port: req.query.port || '',
    pathname: req.query.pathname || '',
    navigator_ua: req.query.navigator_ua || '',
    navigator_platform: req.query.navigator_platform || '',
    timestamp: req.query.timestamp || ''
  };

  // Report
  console.log('Data collected:', data);

  // You can perform further processing here, such as logging data to a database or sending it to another service

  // Send response
  res.send('Data received successfully');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
