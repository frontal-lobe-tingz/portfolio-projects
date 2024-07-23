const express = require('express');
const dbConnect= require('./dbConnect/dbConnection');
const app = express();
const routes = require('./routes/routes.js');

app.use(express.json());


app.use("/",routes);

app.get('/', (req, res)=>{
    //console.log(req);
    res.send('Welcome to the E-commerce API');
})

app.listen(process.env.PORT || 5100,() =>{
    console.log(`Server running on port  ${process.env.PORT || 5100  }`); 
    dbConnect();
});



