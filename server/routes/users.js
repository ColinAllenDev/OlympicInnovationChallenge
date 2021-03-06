const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router = express.Router();
const db = require('../db.js');

var database = new db('./db/teamolympic.db');

/* Get all users info */
router.get("/", (req, res, next) => {
  database.Query("SELECT * FROM Users", res);
});

/* Get user info by ID */
router.get("/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Users WHERE UserId=${req.params.id}`, res);
});


module.exports = router
