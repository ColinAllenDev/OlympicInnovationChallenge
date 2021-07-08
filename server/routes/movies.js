const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router = express.Router();
const db = require('../db.js');

var database = new db('./db/teamolympic.db');

router.get("/", (req, res, next) => {
  database.Query(`SELECT * FROM Movies`, res);
});

router.get("/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Movies WHERE MovieID=${req.params.id}`, res);
});

router.get("/title/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Movies WHERE MovieTitle=${req.params.id}`, res);
});

router.get("/director/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Movies WHERE MovieDirector=${req.params.id}`, res);
});

router.get("/genre/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Movies WHERE MovieGenre=${req.params.id}`, res);
});

router.get("/length/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Movies WHERE MovieLength=${req.params.id}`, res);
});


module.exports = router
