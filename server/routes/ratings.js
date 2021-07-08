const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router = express.Router();
const db = require('../db.js');

var database = new db('./db/teamolympic.db');

router.get("/", (req, res, next) => {
  database.Query(`SELECT * FROM Ratings`, res);
});

router.get("/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Ratings WHERE UserID=${req.params.id}`, res);
});

router.get("/movie/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Ratings WHERE MovieID=${req.params.id}`, res);
});

router.get("/rating/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Ratings WHERE Rating=${req.params.id}`, res);
});

module.exports = router