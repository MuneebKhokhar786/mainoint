
'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'
import { ShoppingCart, Star } from 'lucide-react'
import { useCartStore } from '@/stores/cartStore'

interface ProductCardProps {
  product: {
    id: string
    name: string
    price: number
    priceCompareTo?: number
    slug: string
    images: Array<{ url: string; alt?: string; isPrimary: boolean }>
  }
}

export function ProductCard({ product }: ProductCardProps) {
  const addItem = useCartStore(state => state.addItem)
  
  const primaryImage = product.images?.find(img => img.isPrimary) || product.images?.[0]
  const discount = product.priceCompareTo 
    ? Math.round(((Number(product.priceCompareTo) - Number(product.price)) / Number(product.priceCompareTo)) * 100)
    : 0

  const handleAddToCart = (e: React.MouseEvent) => {
    e.preventDefault()
    e.stopPropagation()
    addItem({
      id: product.id,
      name: product.name,
      price: Number(product.price),
      image: primaryImage?.url || '/api/placeholder/300/200',
      quantity: 1
    })
  }

  return (
    <motion.div
      whileHover={{ y: -5 }}
      transition={{ duration: 0.2 }}
      className="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow border border-gray-100"
    >
      <Link href={`/products/${product.slug}`}>
        <div className="relative overflow-hidden rounded-t-xl">
          <img
            src={primaryImage?.url || '/api/placeholder/300/200'}
            alt={primaryImage?.alt || product.name}
            className="w-full h-48 object-cover transition-transform hover:scale-105"
          />
          
          {discount > 0 && (
            <div className="absolute top-3 left-3 bg-red-500 text-white px-2 py-1 rounded-md text-sm font-semibold">
              -{discount}%
            </div>
          )}
        </div>
        
        <div className="p-4">
          <h3 className="font-semibold text-gray-900 mb-2 line-clamp-2 hover:text-primary transition-colors">
            {product.name}
          </h3>
          
          <div className="flex items-center mb-2">
            <div className="flex">
              {[...Array(5)].map((_, i) => (
                <Star
                  key={i}
                  size={14}
                  className={`${i < 4 ? 'text-yellow-400 fill-current' : 'text-gray-300'}`}
                />
              ))}
            </div>
            <span className="text-sm text-gray-500 ml-2">(24)</span>
          </div>
          
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-lg font-bold text-gray-900">
                ${Number(product.price).toFixed(2)}
              </span>
              {product.priceCompareTo && (
                <span className="text-sm text-gray-500 line-through">
                  ${Number(product.priceCompareTo).toFixed(2)}
                </span>
              )}
            </div>
            
            <button
              onClick={handleAddToCart}
              className="bg-primary text-white p-2 rounded-lg hover:bg-primary-dark transition-colors"
            >
              <ShoppingCart size={18} />
            </button>
          </div>
        </div>
      </Link>
    </motion.div>
  )
}
