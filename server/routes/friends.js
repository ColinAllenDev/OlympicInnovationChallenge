const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router = express.Router();
const db = require('../db.js');

var database = new db('./db/teamolympic.db');

router.get("/", (req, res, next) => {
    database.Query(`SELECT * FROM Friends`, res);
  });

router.get("/user1/:id", (req, res, next) => {
  database.Query(`SELECT * FROM Friends WHERE UserID1=${req.params.id}`, res);
});

router.get("/user2/:id", (req, res, next) => {
    database.Query(`SELECT * FROM Friends WHERE UserID2=${req.params.id}`, res);
});

router.get("/time/", (req, res, next) => {
    database.Query(`SELECT * FROM Friends WHERE Time=${req.params.id}`, res);
});

module.exports = router
