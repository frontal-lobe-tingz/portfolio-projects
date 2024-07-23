const mongoose = require('mongoose');
const { Schema }= mongoose;

const productModel = new Schema({
    title:{
        type: String,
        required: true,
        unique: true
    },
    desc:{
        type: String,
        required: true,
        
    },
    image:{
        type: String,
        required: true
    },
    categories:{
        type: [String],
        default: []
    },
    size:{
        type: String,
        
    },
    color:{
        type: String,
    },
    price:{
        type: Number,
    
    }
},{
    timestamp:true,
});

modeule.exports = mongoose.model("Product",productModel);