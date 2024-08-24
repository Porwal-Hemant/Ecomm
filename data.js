import axios from 'axios'

 const getData=async ()=>{
     const res= axios.get('http://localhost:3000/top-products').then(res=>console.log(res.data));
     return res;
 }
console.log(getData());