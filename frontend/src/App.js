import './App.css';



import Header from './components/header';
import Footer from './components/footer';
import Home from './pages/home';
import ProductIndex from './pages/product_index';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


function App() {
  return (
		<Router>
			<div>
				<Header />
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/:collection/products" element={<ProductIndex />} />
				</Routes>
				<Home />
				<Footer />
			</div>
		</Router>
  );
}

export default App;
