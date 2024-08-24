const mongoose = require("mongoose");

// Define a schema for the person
const personSchema = new mongoose.Schema({
  Name: { type: String, required: true },
  Age: { type: Number, required: true },
  Address: { type: String, required: true },
  Email: { type: String, required: true, unique: true }, // Ensuring unique emails
  Password: { type: String, required: true },
});

// Create and export the model
module.exports = mongoose.model("Person", personSchema);
