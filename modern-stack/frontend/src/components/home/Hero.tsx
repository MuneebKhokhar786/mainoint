
'use client'

import { motion } from 'framer-motion'
import Link from 'next/link'
import { ShoppingBag, Star, TrendingUp } from 'lucide-react'

export function Hero() {
  return (
    <section className="relative bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900 overflow-hidden">
      <div className="absolute inset-0 bg-black/20"></div>
      
      <div className="relative container mx-auto px-4 py-20 lg:py-32">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-white"
          >
            <h1 className="text-4xl lg:text-6xl font-bold mb-6 leading-tight">
              Premium Laptops for
              <span className="text-yellow-400"> Every Need</span>
            </h1>
            
            <p className="text-xl mb-8 text-gray-200 leading-relaxed">
              Discover our collection of high-performance laptops from top brands. 
              Get the best deals with fast shipping and expert support.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 mb-8">
              <Link 
                href="/products"
                className="bg-yellow-400 text-black px-8 py-4 rounded-lg font-semibold hover:bg-yellow-300 transition-colors flex items-center justify-center gap-2"
              >
                <ShoppingBag size={20} />
                Shop Now
              </Link>
              
              <Link 
                href="/categories"
                className="border-2 border-white text-white px-8 py-4 rounded-lg font-semibold hover:bg-white hover:text-black transition-colors flex items-center justify-center gap-2"
              >
                <TrendingUp size={20} />
                Browse Categories
              </Link>
            </div>
            
            <div className="flex items-center gap-8">
              <div className="flex items-center gap-2">
                <div className="flex">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} size={16} className="text-yellow-400 fill-current" />
                  ))}
                </div>
                <span className="text-sm">4.9/5 Rating</span>
              </div>
              
              <div className="text-sm">
                <div className="font-semibold">50,000+</div>
                <div className="text-gray-300">Happy Customers</div>
              </div>
            </div>
          </motion.div>
          
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="relative"
          >
            <div className="relative z-10">
              <img
                src="/api/placeholder/600/400"
                alt="Premium Laptop"
                className="w-full h-auto rounded-2xl shadow-2xl"
              />
            </div>
            
            <div className="absolute inset-0 bg-gradient-to-tr from-yellow-400/20 to-purple-400/20 rounded-2xl blur-3xl transform scale-110"></div>
          </motion.div>
        </div>
      </div>
    </section>
  )
}
