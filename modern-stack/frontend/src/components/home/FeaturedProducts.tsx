
'use client'

import { useQuery } from '@tanstack/react-query'
import { productsAPI } from '@/lib/api'
import { ProductCard } from '@/components/products/ProductCard'
import { Skeleton } from '@/components/ui/Skeleton'

export function FeaturedProducts() {
  const { data: products, isLoading, error } = useQuery({
    queryKey: ['featured-products'],
    queryFn: () => productsAPI.getFeaturedProducts().then(res => res.data),
  })

  if (error) {
    return (
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <div className="text-center text-red-600">
            Failed to load featured products
          </div>
        </div>
      </section>
    )
  }

  return (
    <section className="py-16 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-4">
            Featured Products
          </h2>
          <p className="text-gray-600 text-lg">
            Discover our most popular and highly-rated laptops
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {isLoading
            ? Array.from({ length: 8 }).map((_, index) => (
                <Skeleton key={index} className="h-80 rounded-lg" />
              ))
            : products?.map((product: any) => (
                <ProductCard key={product.id} product={product} />
              ))
          }
        </div>
      </div>
    </section>
  )
}
