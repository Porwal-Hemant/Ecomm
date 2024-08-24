const mongoose = require("mongoose");

// Define a schema for the product
const productSchema = new mongoose.Schema({
  Title: { type: String, required: true },
  Category: { type: String, required: true },
  SubCategory: { type: String, required: true },
  Price: { type: Number, default: null }, // Optional field with a default value of null
  Ratings: { type: Number, default: null }, // Optional field with a default value of null
  TotalRatings: { type: Number, default: null }, // Optional field with a default value of null
  ProductUrl: { type: String, required: true },
});

// Create and export the model
module.exports = mongoose.model("Product", productSchema);
// iska plural form database mai khud ba khud hee store ho jayga
// ab mai Products naam ke database mai saare elements csv file seah upload kar dunga aur fir kaam ho jayga 

