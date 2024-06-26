(function($) {
	"use strict"

	function getCookie(name){
		let cookieValue=null;
		if(document.cookie && document.cookie !== ""){
		const cookies=document.cookie.split(";");
		for(let i=0; i<cookies.length; i++){
		const cookie=cookies[i].trim();
		// Does this cookie string begin with the name we want?
		if(cookie.substring(0, name.length+1)===(name+"=")){
		cookieValue=decodeURIComponent(cookie.substring(name.length+1));
		break;
		}
		}
		}
		return cookieValue;
		}

	$(".add-to-cart-btn").on('click', function () {
		let productId = $(this).data("product-id");
		let quantity = $(`#qty-${productId}`).val() || 1;

		$.ajax({
			type: "GET",
			url: `/add-to-cart/${productId}/${quantity}`,
			success: function (data) {
				if(data.not_authenticated)
          window.location.href = "/accounts/login";
				else
					$(".cart-qty").html(data.total_quantity)
			},
			error: function () {
				alert("Error adding product to cart!");
			},
		});
	});

	$("#categories-search").on("change", function(){
    let collection_name = $(this).val();
		$.ajax({
			type: "GET",
			url: `/${collection_name}/filtered_products`,
			success: function (data) {
				$("#products-search").html(data)
			},
			error: function () {
				alert("Error Fetching Product list!");
			},
		});
	});

	$("#product-search-form").on("submit", function(e){
		e.preventDefault();
		const product_slug = new FormData(this).get('product_slug');
    window.location.href = '/products/' + product_slug
	});
	
	$("#cart-container").on("show.bs.dropdown", function () {
		$("#cart-spinner").removeClass("hidden");
		$(".de-cart").addClass("hidden");
		$.ajax({
			type: "GET",
			url: `/update-cart`,
			success: function (data) {
				$(".cart-dropdown").replaceWith(data.cart_html);
				$("#cart-spinner").addClass("hidden");
				$(".de-cart").removeClass("hidden");
			},
			error: function () {
				alert("Error updating cart!");
			},
		});
		});

	// Mobile Nav toggle
	$('.menu-toggle > a').on('click', function (e) {
		e.preventDefault();
		$('#responsive-nav').toggleClass('active');
	})

	// Fix cart dropdown from closing
	$('.cart-dropdown').on('click', function (e) {
		e.stopPropagation();
	});

	/////////////////////////////////////////

	// Products Slick
	$('.products-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			slidesToShow: 4,
			slidesToScroll: 1,
			autoplay: true,
			infinite: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
			responsive: [{
	        breakpoint: 991,
	        settings: {
	          slidesToShow: 2,
	          slidesToScroll: 1,
	        }
	      },
	      {
	        breakpoint: 480,
	        settings: {
	          slidesToShow: 1,
	          slidesToScroll: 1,
	        }
	      },
	    ]
		});
	});

	// Products Widget Slick
	$('.products-widget-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			infinite: true,
			autoplay: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
		});
	});

	/////////////////////////////////////////

	// Product Main img Slick
	$('#product-main-img').slick({
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    fade: true,
    asNavFor: '#product-imgs',
  });

	// Product imgs Slick
  $('#product-imgs').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    focusOnSelect: true,
		centerPadding: 0,
		vertical: true,
    asNavFor: '#product-main-img',
		responsive: [{
        breakpoint: 991,
        settings: {
					vertical: false,
					arrows: false,
					dots: true,
        }
      },
    ]
  });

	// Product img zoom
	var zoomMainProduct = document.getElementById('product-main-img');
	if (zoomMainProduct) {
		$('#product-main-img .product-preview').zoom();
	}

	/////////////////////////////////////////

	// Input number
	$('.input-number').each(function() {
		var $this = $(this),
		$input = $this.find('input[type="number"]'),
		up = $this.find('.qty-up'),
		down = $this.find('.qty-down');

		down.on('click', function () {
			var value = parseInt($input.val()) - 1;
			value = value < 1 ? 1 : value;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})

		up.on('click', function () {
			var value = parseInt($input.val()) + 1;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})
	});

	var priceInputMax = document.getElementById('price-max'),
			priceInputMin = document.getElementById('price-min');

	priceInputMax.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	priceInputMin.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	function updatePriceSlider(elem , value) {
		if ( elem.hasClass('price-min') ) {
			console.log('min')
			priceSlider.noUiSlider.set([value, null]);
		} else if ( elem.hasClass('price-max')) {
			console.log('max')
			priceSlider.noUiSlider.set([null, value]);
		}
	}

	// Price Slider
	var priceSlider = document.getElementById('price-slider');
	if (priceSlider) {
		noUiSlider.create(priceSlider, {
			start: [1, 999],
			connect: true,
			step: 1,
			range: {
				'min': 1,
				'max': 999
			}
		});

		priceSlider.noUiSlider.on('update', function( values, handle ) {
			var value = values[handle];
			handle ? priceInputMax.value = value : priceInputMin.value = value
		});
	}

})(jQuery);
