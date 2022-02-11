const getLocations  = async (req, res) => {
  const { lat, lon } = req.body;
  res.status(200).send();
  
}

module.exports = {
  getLocations,
};