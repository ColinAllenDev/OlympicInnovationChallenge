/* SQLite databse connector */
const sqlite3 = require('sqlite3').verbose();

class db {
    constructor(path) {
        this.connector = new sqlite3.Database(path, sqlite3.OPEN_READWRITE, (err) => {
            if (err) console.error(err.message);
        });
    }

    Query = function(q, res) {
        this.connector.all(q, [], (err, rows) => {
            if(err) {
                res.status(400).json({"error": err.message});
                return;
            }
            res.json({rows});
        });
    }



    Close = function() {
        this.connector.close((err) => {
            if (err) console.error(err.message);
            console.log('Closed database connection');
        })
    }
}

module.exports = db;