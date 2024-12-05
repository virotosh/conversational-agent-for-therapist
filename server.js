 // server.js
import express from 'express';
import CA from './src/usingCA/controllers/ca';
import cors from 'cors';
import fs from 'fs'
import https from 'https'

var app = express()
var privateKey  = fs.readFileSync('/etc/ssl/key.pem', 'utf8');
var certificate = fs.readFileSync('/etc/ssl/cert.pem', 'utf8');
var credentials = {key: privateKey, cert: certificate};

app.use(express.json())
app.use(cors())

app.get('/', (req, res) => {
  return res.status(200).send({'message': 'YAY! Congratulations! Your endpoint is working'});
});

app.all('/ca',CA.talk);

var httpsServer = https.createServer(credentials, app);

httpsServer.listen(443);
console.log('app running on port ', 443);
