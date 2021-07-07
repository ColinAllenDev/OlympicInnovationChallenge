const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router = express.Router();

/* Database Connection */
var db = new sqlite3.Database('./db/teamolympic.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) console.error(err.message);

  console.log("Connected to database")
});

/* Post user info */
router.post('/:id', (req, res, next) => {
  res.send(req.params.id)
});

/*==== User GET Requests =====*/

// TODO: MOVE THIS TO DATABASE CLASS

/* Get all users info */
router.get("/", (req, res, next) => {
  var params = [];
  db.all("SELECT * FROM Users", params, (err, rows) => {
    if(err) {
      res.status(400).json({"error":err.message});
      return;
    }
    res.json({
      "message":"success",
      "data":rows
    });
  });
});

/* Get user info by ID */
router.get("/:id", (req, res, next) => {
  var params = [];
  db.all(`SELECT * FROM Users WHERE UserId=${req.params.id}`, params, (err, rows) => {
    if (err) {
      res.status(400).json({"error":err.message});
      return;
    }
    res.json({
      "message":"success",
      "data": rows
    })
  });

});

module.exports = router;
