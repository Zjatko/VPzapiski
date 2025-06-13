const express = require('express');
const jwt = require("jsonwebtoken");
const router = express.Router();

const config = require('../../config');
const models = require('../models/auth');

router.get('/auth/login', (req, res) => res.render('auth_login'));

router.post('/auth/login', (req, res) => {
	const { username, password } = req.body;
	for (const user of models.users) {
		if (user.username === username && user.password === password) {
			const token = jwt.sign(
				{ sub: user.id, username: user.username },
				config.PRIVATE_KEY,
				{ expiresIn: '1h' , algorithm: 'RS256'}
			);
			res.cookie('session', token, { httpOnly: true });
			return res.redirect('/');
		}
	}
	return res.redirect('/auth/login');
});

module.exports = router;
