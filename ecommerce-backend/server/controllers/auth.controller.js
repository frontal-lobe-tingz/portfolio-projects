const User = require("../models/user.model.js");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");




const register =async (req,res)=>{
    try{
        const hashedPassword = bcrypt.hashSync(req.body.password,10)
const newUser = new User({
    username: req.body.username,
    email: req.body.email,
    password: hashedPassword
});
 await newUser.save();

 const{ password, ...info} = newUser._doc;
 res.status(200).json({message: "User registered successfully",
 data: info,
 
 }); 

    }catch(error){
   console.log(error);
   res.status(500).json({message: "Registration failed", error: error.message});
    }

}

const login = async (req,res)=>{
    try{
        //const {email,password}=req.body;

        const user = await User.findOne({email: req.body.email});
        if(!user){
            return res.status(400).json({message: "Email not found"});
        }
    
        const comparedPassword = await bcrypt.compare(req.body.password, user.password);
        if(!comparedPassword){
            return res.status(400).json({
                message: "Invalid password"});
        }

        const token = jwt.sign({
            userId:user._id,
            isAdmin:user.isAdmin
        },process.env.JWT_KEY,{
            expiresIn: "5d"
        });

        const { password,...info} = user._doc;

        res.status(200).json({
            data: {info,token},
            message:"login successful"});
    }catch(error){
        console.log(error);
        res.status(500).json({message: "Login failed",
             error: error});
    }

  
};

module.exports = {
    register,login
};