/* SQLite databse connector */

/*
const sqlite3 = require('sqlite3').verbose();

var db_connector = new sqlite3.Database('./db/teamolympic.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) console.error(err.message);

    console.log("Connected to database")
});
*/

/* 
db.serialize(() => {
    db.each(`SELECT * FROM Users`, (err, row) => {
        if (err) console.log(err.message);

        console.log(row);
    });
});

db.close((err) => {
    if (err) console.error(err.message);
    
    console.log('Closed database connection');
})
*/
