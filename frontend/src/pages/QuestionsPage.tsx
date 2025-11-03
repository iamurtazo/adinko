import React, { useState } from 'react';
import { Button, Card, Badge, Input } from '../components/atomic';

interface Question {
  id: number;
  title: string;
  category: string;
  votes: number;
  answers: number;
  views: number;
}

export const QuestionsPage: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');

  const questions: Question[] = [
    {
      id: 1,
      title: 'How to get an ARC card as a student in Seoul?',
      category: 'Documentation',
      votes: 4,
      answers: 3,
      views: 45,
    },
    {
      id: 2,
      title: 'Best neighborhoods for expats in Seoul',
      category: 'Housing',
      votes: 12,
      answers: 8,
      views: 234,
    },
    {
      id: 3,
      title: 'How to open a bank account',
      category: 'Banking',
      votes: 8,
      answers: 5,
      views: 156,
    },
  ];

  const categories = [
    { id: 'all', name: 'All Categories' },
    { id: 'documentation', name: 'Documentation' },
    { id: 'housing', name: 'Housing' },
    { id: 'language', name: 'Language' },
    { id: 'healthcare', name: 'Healthcare' },
    { id: 'banking', name: 'Banking' },
  ];

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
      {/* Sidebar */}
      <aside className="lg:col-span-1">
        <Card padding="md">
          <h3 className="font-bold text-lg mb-4">Categories</h3>
          <div className="space-y-2">
            {categories.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id)}
                className={`w-full text-left px-3 py-2 rounded transition-colors ${
                  selectedCategory === cat.id
                    ? 'bg-primary text-white'
                    : 'hover:bg-gray-100 text-gray-700'
                }`}
              >
                {cat.name}
              </button>
            ))}
          </div>
        </Card>

        <Card padding="md" className="mt-6">
          <h3 className="font-bold text-lg mb-4">Filter By</h3>
          <div className="space-y-2">
            {['Most Recent', 'Most Answered', 'Most Viewed', 'Unanswered'].map((filter) => (
              <button
                key={filter}
                className="w-full text-left px-3 py-2 rounded hover:bg-gray-100 text-gray-700 transition-colors"
              >
                {filter}
              </button>
            ))}
          </div>
        </Card>
      </aside>

      {/* Main Content */}
      <main className="lg:col-span-3">
        {/* Search Bar */}
        <Card padding="md" className="mb-6">
          <div className="flex gap-4">
            <div className="flex-1">
              <Input
                placeholder="Search questions..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                icon="🔍"
              />
            </div>
            <select className="px-4 py-2 border border-border rounded-lg">
              <option>Newest First</option>
              <option>Most Votes</option>
              <option>Most Views</option>
            </select>
          </div>
        </Card>

        {/* Questions List */}
        <div className="space-y-4">
          {questions.map((question) => (
            <Card key={question.id} hoverable padding="md">
              <div className="flex gap-6">
                {/* Stats */}
                <div className="flex flex-col items-center gap-4 text-center">
                  <div>
                    <div className="text-2xl font-bold text-gray-900">
                      {question.votes}
                    </div>
                    <div className="text-xs text-gray-600">votes</div>
                  </div>
                  <div className={question.answers > 0 ? 'text-green-600' : ''}>
                    <div className="text-2xl font-bold">{question.answers}</div>
                    <div className="text-xs">answers</div>
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-gray-900">
                      {question.views}
                    </div>
                    <div className="text-xs text-gray-600">views</div>
                  </div>
                </div>

                {/* Content */}
                <div className="flex-1">
                  <h3 className="text-lg font-semibold text-primary hover:underline cursor-pointer mb-3">
                    {question.title}
                  </h3>
                  <div className="flex items-center gap-4">
                    <Badge variant="secondary">{question.category}</Badge>
                    <span className="text-xs text-gray-500">5 days ago</span>
                  </div>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </main>
    </div>
  );
};
