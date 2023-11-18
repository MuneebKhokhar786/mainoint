import { useState, useEffect } from "react";
import Product from "../components/product.jsx";
import Collection from "../components/collection.jsx";
import handleRequest from "../axios.js";
import Newsletter from "../components/newsletter.jsx";

const Home = () => {
  const [products, setProducts] = useState([]);
  const [collections, setCollections] = useState([]);

  useEffect(() => {
    handleRequest("/v1/api/collections")
      .then((res) => {
        const collections = res.data;
        setCollections(collections);
      })
      .catch((err) => {
        console.error(err);
      });

    handleRequest("/v1/api/products")
      .then((res) => {
        const products = res.data;
        setProducts(products);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <>
      <div class="section">
        <div class="container">
          <div class="row">
            {collections.map((collection) => (
              <Collection collection={collection} />
            ))}
          </div>
        </div>
      </div>
      <div class="section">
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div class="section-title">
                <h3 class="title">Featured Products</h3>
                <div class="section-nav">
                  <ul class="section-tab-nav tab-nav">
                    <li class="active">
                      <a data-toggle="tab" href="#tab1">
                        Laptops
                      </a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab1">
                        Smartphones
                      </a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab1">
                        Cameras
                      </a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab1">
                        Accessories
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="col-md-12">
              <div class="row">
                <div class="products-tabs">
                  <div id="tab1" class="tab-pane active">
                    <div class="products-slick" data-nav="#slick-nav-1">
                      {products.map((product) => (
                        <Product product={product} />
                      ))}
                    </div>
                    <div id="slick-nav-1" class="products-slick-nav"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="hot-deal" class="section">
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div class="hot-deal">
                <ul class="hot-deal-countdown">
                  <li>
                    <div>
                      <h3>02</h3>
                      <span>Days</span>
                    </div>
                  </li>
                  <li>
                    <div>
                      <h3>10</h3>
                      <span>Hours</span>
                    </div>
                  </li>
                  <li>
                    <div>
                      <h3>34</h3>
                      <span>Mins</span>
                    </div>
                  </li>
                  <li>
                    <div>
                      <h3>60</h3>
                      <span>Secs</span>
                    </div>
                  </li>
                </ul>
                <h2 class="text-uppercase">hot deal this week</h2>
                <p>New Collection Up to 50% OFF</p>
                <a class="primary-btn cta-btn" href="#">
                  Shop now
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="section">
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div class="section-title">
                <h3 class="title">New Arrivals</h3>
                <div class="section-nav">
                  <ul class="section-tab-nav tab-nav">
                    <li class="active">
                      <a data-toggle="tab" href="#tab2">
                        Laptops
                      </a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab2">
                        Smartphones
                      </a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab2">
                        Cameras
                      </a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab2">
                        Accessories
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="col-md-12">
              <div class="row">
                <div class="products-tabs">
                  <div id="tab2" class="tab-pane fade in active">
                    <div class="products-slick" data-nav="#slick-nav-2">
                      {products.map((product) => (
                        <Product product={product} />
                      ))}
                    </div>
                    <div id="slick-nav-2" class="products-slick-nav"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Newsletter />
    </>
  );
};

export default Home;
