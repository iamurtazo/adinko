import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, Badge } from '../components/atomic';

export const HomePage: React.FC = () => {
  const categories = [
    { id: 1, name: 'Housing', icon: '🏠' },
    { id: 2, name: 'Community', icon: '👥' },
    { id: 3, name: 'Language', icon: '💬' },
    { id: 4, name: 'Local Life', icon: '🗺️' },
    { id: 5, name: 'Support', icon: '❓' },
  ];

  const recentQuestions = [
    { id: 1, title: 'How to get an ARC card?', category: 'Documentation', answers: 12 },
    { id: 2, title: 'Best areas to live in Seoul?', category: 'Housing', answers: 8 },
    { id: 3, title: 'Korean bank account setup', category: 'Banking', answers: 15 },
  ];

  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <section className="text-center py-16 bg-gradient-to-br from-primary-light via-white to-white rounded-lg">
        <h1 className="text-5xl font-bold text-gray-900 mb-4">
          Get Help Living in Korea
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Connect with experienced expats and get answers to your questions
        </p>
        <div className="flex justify-center gap-4">
          <Link to="/ask-question">
            <Button variant="primary" size="lg">
              Ask a Question
            </Button>
          </Link>
          <Link to="/questions">
            <Button variant="outline" size="lg">
              Browse Questions
            </Button>
          </Link>
        </div>
      </section>

      {/* Categories */}
      <section>
        <h2 className="text-3xl font-bold mb-8">Browse Categories</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
          {categories.map((category) => (
            <Card
              key={category.id}
              hoverable
              className="text-center cursor-pointer hover:border-primary"
            >
              <div className="text-4xl mb-3">{category.icon}</div>
              <h3 className="font-semibold text-gray-900">{category.name}</h3>
            </Card>
          ))}
        </div>
      </section>

      {/* Recent Questions */}
      <section>
        <h2 className="text-3xl font-bold mb-8">Recent Questions</h2>
        <div className="space-y-4">
          {recentQuestions.map((question) => (
            <Card key={question.id} hoverable>
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <Link to={`/questions/${question.id}`}>
                    <h3 className="text-lg font-semibold text-primary hover:underline">
                      {question.title}
                    </h3>
                  </Link>
                  <div className="mt-3 flex items-center gap-4">
                    <Badge variant="secondary">{question.category}</Badge>
                    <span className="text-sm text-gray-600">
                      {question.answers} answers
                    </span>
                  </div>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </section>

      {/* Stats */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-8 py-12 bg-primary-light rounded-lg p-8">
        <div className="text-center">
          <div className="text-5xl font-bold text-primary mb-2">10,000+</div>
          <div className="text-gray-700 font-medium">Community Members</div>
        </div>
        <div className="text-center">
          <div className="text-5xl font-bold text-primary mb-2">5,000+</div>
          <div className="text-gray-700 font-medium">Questions Answered</div>
        </div>
        <div className="text-center">
          <div className="text-5xl font-bold text-primary mb-2">1,000+</div>
          <div className="text-gray-700 font-medium">Expert Contributors</div>
        </div>
      </section>
    </div>
  );
};
