import { Link } from "react-router-dom";
import { CLOUDINARY_URL } from "../constants";

const Collection= ({ collection }) => (
  <>
    <div class="col-md-4 col-xs-6">
    <Link to={`/${collection.name}/products`}>
        <div class="shop">
          <div class="shop-img">
            <img
              loading="lazy"
              src={`${CLOUDINARY_URL}/${collection.image}`}
              alt={collection.description}
              referrerpolicy="no-referrer"
            />
          </div>
          <div class="shop-body">
            <h3>
              { collection.name } <br />
              Collection
            </h3>
            <Link
              to={`/${collection.name}/products`}
              class="cta-btn"
              >Shop now <i class="fa fa-arrow-circle-right"></i
            ></Link>
          </div>
        </div>
      </Link>
      </div>
  </>
)

export default Collection
