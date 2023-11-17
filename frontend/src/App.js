import './App.css';
import { useState, useEffect } from 'react';

import handleRequest  from './axios.js'

function App() {

  const [products, setProducts] = useState([]);

  useEffect(() => {
    handleRequest('/v1/api/products').then((res) => {
      const products = res.data;
      setProducts(products);
    }).catch((err) => { console.error(err); });
  }, []);



  return (
    <div>
      {products.map((product) => (
        <div>
            <p>{product.name} </p>
            <img src={product.image} alt=""/>
        </div>
      ))}
    </div>
  );
}

export default App;
