
'use client'

import Link from 'next/link'
import { ShoppingCart, Search, User, Menu } from 'lucide-react'

export function Header() {
  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link href="/" className="text-2xl font-bold text-red-600">
            LaptopShop
          </Link>
          
          <div className="hidden md:flex items-center space-x-8">
            <Link href="/products" className="text-gray-700 hover:text-red-600">
              Products
            </Link>
            <Link href="/categories" className="text-gray-700 hover:text-red-600">
              Categories
            </Link>
            <Link href="/about" className="text-gray-700 hover:text-red-600">
              About
            </Link>
            <Link href="/contact" className="text-gray-700 hover:text-red-600">
              Contact
            </Link>
          </div>
          
          <div className="flex items-center space-x-4">
            <button className="text-gray-700 hover:text-red-600">
              <Search size={20} />
            </button>
            <button className="text-gray-700 hover:text-red-600">
              <User size={20} />
            </button>
            <button className="text-gray-700 hover:text-red-600 relative">
              <ShoppingCart size={20} />
              <span className="absolute -top-2 -right-2 bg-red-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                0
              </span>
            </button>
            <button className="md:hidden text-gray-700 hover:text-red-600">
              <Menu size={20} />
            </button>
          </div>
        </div>
      </div>
    </header>
  )
}
