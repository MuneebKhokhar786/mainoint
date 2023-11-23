import { useState, useEffect } from "react";
import Slider from "react-slick";
import Product from "../components/product.jsx";
import Collection from "../components/collection.jsx";
import handleRequest from "../axios.js";
import Newsletter from "../components/newsletter.jsx";

const Home = () => {
  const settings = {
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 786,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          centerMode: true,
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ],
  };

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
      <div className="section">
        <div className="container">
          <div className="row">
            {collections.map((collection) => (
              <Collection collection={collection} />
            ))}
          </div>
        </div>
      </div>
      <div className="section">
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <div className="section-title">
                <h3 className="title">Featured Products</h3>
                <div className="section-nav">
                  <ul className="section-tab-nav tab-nav">
                    <li className="active">
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
            <div className="col-md-12">
              <div className="row">
                    <Slider {...settings} className="product-carousel">
                      {products.map((product) => (
                        <Product product={product} />
                      ))}
                    </Slider>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="hot-deal" className="section">
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <div className="hot-deal">
                <ul className="hot-deal-countdown">
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
                <h2 className="text-uppercase">hot deal this week</h2>
                <p>New Collection Up to 50% OFF</p>
                <a className="primary-btn cta-btn" href="#">
                  Shop now
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="section">
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <div className="section-title">
                <h3 className="title">New Arrivals</h3>
                <div className="section-nav">
                  <ul className="section-tab-nav tab-nav">
                    <li className="active">
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
            <div className="col-md-12">
              <div className="row">
                <div className="products-tabs">
                  <div id="tab2" className="tab-pane fade in active">
                    <div className="products-slick" data-nav="#slick-nav-2">
                      {products.map((product) => (
                        <Product product={product} />
                      ))}
                    </div>
                    <div id="slick-nav-2" className="products-slick-nav"></div>
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
