const router = require("express").Router();

router.get("/get-users",(req,res)=>
{
    res.send("user has been retrieved");
})

module.exports = router;   