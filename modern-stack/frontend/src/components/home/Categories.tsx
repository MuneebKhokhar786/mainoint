
'use client'

export function Categories() {
  const categories = [
    { name: 'Gaming Laptops', image: '/api/placeholder/300/200', count: 45 },
    { name: 'Business Laptops', image: '/api/placeholder/300/200', count: 32 },
    { name: 'Ultrabooks', image: '/api/placeholder/300/200', count: 28 },
    { name: 'Workstations', image: '/api/placeholder/300/200', count: 15 },
  ]

  return (
    <section className="py-16 bg-white">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-12">Shop by Category</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {categories.map((category) => (
            <div
              key={category.name}
              className="group cursor-pointer bg-gray-50 rounded-lg overflow-hidden hover:shadow-lg transition-shadow duration-300"
            >
              <div className="aspect-video bg-gray-200 group-hover:scale-105 transition-transform duration-300" />
              <div className="p-4 text-center">
                <h3 className="font-semibold text-gray-900 mb-1">{category.name}</h3>
                <p className="text-sm text-gray-600">{category.count} products</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
