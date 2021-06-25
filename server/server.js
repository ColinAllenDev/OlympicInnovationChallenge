const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 1738

/* SQL Database Config */
var db = mysql.createConnection({
    host: 'localhost',
    user: 'database_username',
    password: 'database_password',
    database: 'olympicdb'
});

/* Get data from SQL Database */
db.connect();
db.query('', (error, rows, fields) => {

});

/* Entrypoint Route */
app.get('/', (req, res) => {
  res.send();
});

/* DB Requests */
app.get('/user/name', (req, res) => {
    res.send();
});

/* Server listen on port 1738 */
app.listen(port, () => {
  console.log(`Listening on port ${port}...`)
});