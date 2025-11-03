import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Button } from '../atomic';

export const Navbar: React.FC = () => {
  const location = useLocation();

  const isActive = (path: string) => location.pathname === path;

  return (
    <nav className="sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm">
      <div className="container-custom flex items-center justify-between h-16">
        {/* Logo and Links */}
        <div className="flex items-center gap-8">
          <Link to="/" className="text-2xl font-bold text-primary">
            AidKo
          </Link>

          <div className="hidden md:flex items-center gap-6">
            <Link
              to="/"
              className={`text-sm font-medium transition-colors ${
                isActive('/') ? 'text-primary' : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Home
            </Link>
            <Link
              to="/questions"
              className={`text-sm font-medium transition-colors ${
                isActive('/questions') ? 'text-primary' : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Questions
            </Link>
            <Link
              to="/community"
              className={`text-sm font-medium transition-colors ${
                isActive('/community') ? 'text-primary' : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Community
            </Link>
            <Link
              to="/blog"
              className={`text-sm font-medium transition-colors ${
                isActive('/blog') ? 'text-primary' : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Blog
            </Link>
          </div>
        </div>

        {/* Actions */}
        <div className="flex items-center gap-4">
          <Link to="/ask-question">
            <Button variant="primary" size="md">
              Ask Question
            </Button>
          </Link>
          <Button variant="outline" size="md">
            Sign In
          </Button>
        </div>
      </div>
    </nav>
  );
};
