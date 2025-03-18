const express = require("express");
const cors = require("cors");
require("./db/config");
const User = require('./db/User');
const Product = require('./db/Product');
const app = express();

app.use(express.json());
app.use(cors());

app.post("/register", async (req, resp) => {
    let user = new User(req.body);
    let result = await user.save();
    result = result.toObject();
    delete result.password;
    resp.send(result);
});

app.get("/products", async (req, resp) => {
    const products = await Product.find();
    if (products.length > 0) {
        resp.send(products);
    } else {
        resp.send({ result: "No product found" });
    }
});

app.post("/login", async (req, resp) => {
    if (req.body.password && req.body.email) {
        let user = await User.findOne(req.body).select("-password");
        if (user) {
            resp.send(user);
        } else {
            resp.send({ result: "no user found" });
        }
    } else {
        resp.send({ result: "no user found" });
    }
});

app.post("/add-product", async (req, resp) => {
    let product = new Product(req.body);
    let result = await product.save();
    resp.send(result);
});

app.delete("/product/:id", async (req, resp) => {
    if (!req.params.id.match(/^[0-9a-fA-F]{24}$/)) {
        return resp.status(400).send({ message: "Invalid ID format" });
    }
    try {
        let result = await Product.deleteOne({ _id: req.params.id });
        if (result.deletedCount === 0) {
            resp.status(404).send({ message: "Product not found" });
        } else {
            resp.send(result);
        }
    } catch (error) {
        resp.status(500).send({ message: "Error deleting product", error });
    }
});

app.get("/product/:id", async (req,resp) => {
    let result = await Product.findOne({_id:req.params.id})
    if(result){
       resp.send(result) 
    }else{
        resp.send({"result":"No record Found"})
    }
})

app.get("/search/:key",async (req,resp)=>{
    let result =await Product.find({
        "$or":[
           
            {
                category:{$regex:req.params.key},    
            },
            
            {
                name:{$regex:req.params.key},    
            },
            {
                company:{$regex:req.params.key}
            },
        ]
    })
    resp.send(result);
})

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
