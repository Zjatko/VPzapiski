const express = require("express");
const router = express.Router();

const config = require("../../config");

router.get("/badjwks", (req, res) => {
	return res.status(200).json({
		pubkey: config.PUBLIC_KEY,
	});
});

module.exports = router;
