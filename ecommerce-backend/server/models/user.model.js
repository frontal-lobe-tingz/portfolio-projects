const mongoose = require('mongoose');
const { Schema }= mongoose;

const userModel = new Schema({
    username:{
        type: String,
        required: true,
        unique: true
    },
    email:{
        type: String,
        required: true,
        unique: true
    },
    password:{
        type: String,
        required: true
    },
    isAdmin:{
        type: Boolean,
        default: false
    },
},{
    timestamp:true,
});

module.exports = mongoose.model("User",userModel);