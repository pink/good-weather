const express = require('express');
const locationController = require('../controllers/location.controller'); 
const router = express.Router();

/* GET locations. */
router.get('/', locationController.getLocations);

module.exports = router;
