const req = require('request');
const uri = `https://swapi-api.alx-tools.com/api/films/:${process.argv[2]}`;
req.get(uri, function (err, data) {
  if (err) throw err;
  console.log(`code: ${data.statusCode}`);
});
