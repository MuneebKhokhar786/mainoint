
# Modern Laptop Shop

A modern, high-performance e-commerce application built with FastAPI and Next.js.

## Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - Python SQL toolkit and ORM
- **PostgreSQL** - Robust relational database
- **Redis** - In-memory data store for caching
- **JWT Authentication** - Secure token-based authentication
- **Pydantic** - Data validation using Python type annotations

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **TanStack Query** - Data fetching and caching
- **Zustand** - State management

## Features

- **High Performance**: Optimized database queries, Redis caching, and efficient frontend
- **Modern UI**: Responsive design with smooth animations
- **Secure Authentication**: JWT-based auth with role-based access
- **Type Safety**: Full TypeScript coverage
- **Scalable Architecture**: Modular backend with clean separation of concerns
- **Real-time Updates**: Optimistic updates and background synchronization

## Quick Start

### Backend Setup

1. Navigate to backend directory:
```bash
cd modern-stack/backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp ../.env.example .env
# Edit .env with your actual values
```

4. Run the backend:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd modern-stack/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

## Performance Optimizations

- Database connection pooling
- Redis caching for frequently accessed data
- Optimized SQL queries with proper indexing
- Image optimization and lazy loading
- Code splitting and tree shaking
- Server-side rendering where appropriate

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

See `.env.example` for required environment variables.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request
