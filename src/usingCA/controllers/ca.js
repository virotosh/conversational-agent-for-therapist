var spawn = require('child_process').spawn;

const CA = {
  /**
   * Create A CA
   * @param {object} req
   * @param {object} res
   * @returns {object}
   */
  async talk(req, res) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, PATCH");
    res.header("Access-Control-Allow-Headers", "Accept, Content-Type, Authorization, X-Requested-With");

    if (!req.body.code || !req.body.content || !req.body.participantID || !req.body.responseTime) {
      return res.status(400).send({'message': 'Some values are missing'});
    }

    try {
      var process = spawn('python3', ['./src/usingCA/controllers/topicmodel/app.py', req.body.content, req.body.num_recs]);
      process.stdout.on('data', function (data) {
            data = data.toString('utf8').replace(/(\r\n|\n|\r)/gm,"").replace(/["']+/g,'"');
            return res.status(201).send({ "code": "questionCode", "change_programs": JSON.parse(data) });
        });

    } catch(error) {
      return res.status(400).send(error);
    }
  }
}

export default CA; 
