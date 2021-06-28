var express = require('express');
var router = express.Router();

/* Get user info */
router.get("/:id", (req, res, next) => {
  res.send(req.params.id);
});

module.exports = router;
