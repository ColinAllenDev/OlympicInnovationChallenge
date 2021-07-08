const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router = express.Router();
const db = require('../db.js');

var database = new db('./db/teamolympic.db');

router.get("/:id", (req, res, next) => {
  database.Query(`SELECT * FROM UserWatchesMovie WHERE MovieID=${req.params.id}`, res);
});

router.get("/user/:id", (req, res, next) => {
  database.Query(`SELECT * FROM UserWatchesMovie WHERE UserId=${req.params.id}`, res);
});

router.get("/duration/:id", (req, res, next) => {
  database.Query(`SELECT * FROM UserWatchesMovie WHERE DurationWatched=${req.params.id}`, res);
});

module.exports = router
