import React from 'react';
import { Button, Card, Badge, Input } from '../components/atomic';

export const BlogPage: React.FC = () => {
  const blogPosts = [
    {
      id: 1,
      title: 'Korean Language Learning Strategies',
      description: 'Effective methods to accelerate your Korean language skills',
      category: 'Language',
      readTime: '4 min read',
    },
    {
      id: 2,
      title: 'Hidden Gems of Seoul\'s Food Scene',
      description: 'Explore beyond tourist favorites to local culinary treasures',
      category: 'Food',
      readTime: '6 min read',
    },
    {
      id: 3,
      title: 'Navigating Korean Bureaucracy',
      description: 'Essential tips for handling administrative processes',
      category: 'Lifestyle',
      readTime: '5 min read',
    },
  ];

  return (
    <div className="space-y-12">
      {/* Hero */}
      <section className="text-center py-16 bg-gradient-to-br from-primary-light via-white to-white rounded-lg">
        <h1 className="text-5xl font-bold mb-3">Expat Life in Korea</h1>
        <p className="text-xl text-gray-600 mb-8">Discover, Learn, and Connect</p>
        <div className="max-w-md mx-auto">
          <Input placeholder="Search blog posts..." icon="🔍" />
        </div>
      </section>

      {/* Featured Post */}
      <section>
        <h2 className="text-3xl font-bold mb-8">Featured Post</h2>
        <Card padding="lg">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-gray-200 rounded-lg h-64 flex items-center justify-center">
              <span className="text-6xl">📚</span>
            </div>
            <div>
              <Badge variant="primary" className="mb-4">
                Featured
              </Badge>
              <h2 className="text-3xl font-bold mb-4">
                Mastering Korean Work Culture: An Insider's Guide
              </h2>
              <p className="text-gray-600 mb-6">
                Navigate the nuanced world of Korean professional environments with confidence and
                cultural sensitivity.
              </p>
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 bg-gray-300 rounded-full" />
                <div>
                  <div className="font-semibold">Sarah Kim</div>
                  <div className="text-sm text-gray-600">May 15, 2024 • 5 min read</div>
                </div>
              </div>
              <Button variant="primary">Read More</Button>
            </div>
          </div>
        </Card>
      </section>

      {/* Recent Posts */}
      <section>
        <h2 className="text-3xl font-bold mb-8">Latest Blog Posts</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {blogPosts.map((post) => (
            <Card key={post.id} hoverable>
              <div className="bg-gray-200 h-40 rounded-lg flex items-center justify-center mb-4">
                <span className="text-5xl">✍️</span>
              </div>
              <div className="p-4">
                <h3 className="text-lg font-bold mb-2 hover:text-primary cursor-pointer">
                  {post.title}
                </h3>
                <p className="text-sm text-gray-600 mb-4">{post.description}</p>
                <div className="flex justify-between items-center">
                  <Badge variant="secondary">{post.category}</Badge>
                  <span className="text-xs text-gray-500">{post.readTime}</span>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </section>

      {/* Newsletter */}
      <section className="py-12 bg-primary-light rounded-lg text-center">
        <h2 className="text-3xl font-bold mb-3">Stay Informed, Stay Connected</h2>
        <p className="text-gray-600 mb-6">
          Get the latest expat tips, stories, and insights delivered straight to your inbox
        </p>
        <div className="max-w-md mx-auto flex gap-3">
          <Input placeholder="Enter your email address" type="email" />
          <Button variant="primary">Subscribe</Button>
        </div>
      </section>
    </div>
  );
};
