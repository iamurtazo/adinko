import React from 'react';
import { Button, Card, Badge } from '../components/atomic';

export const CommunityPage: React.FC = () => {
  const members = [
    {
      id: 1,
      name: 'Sarah Kim',
      badge: 'Top Contributor',
      bio: 'Teaching professional with 5+ years experience in Korea',
      rating: 4.9,
      comments: 234,
    },
    {
      id: 2,
      name: 'John Park',
      badge: 'Language Expert',
      bio: 'Korean language instructor and cultural consultant',
      rating: 4.8,
      comments: 186,
    },
    {
      id: 3,
      name: 'Emily Chen',
      badge: 'Business Mentor',
      bio: 'Startup founder and business development expert',
      rating: 4.7,
      comments: 156,
    },
  ];

  const events = [
    {
      id: 1,
      date: '25',
      month: 'May',
      title: 'Korean Language Exchange',
      location: 'Gangnam, Seoul',
      time: '18:30 - 20:30',
    },
    {
      id: 2,
      date: '28',
      month: 'May',
      title: 'Business Networking Mixer',
      location: 'Yeouido, Seoul',
      time: '19:00 - 21:00',
    },
    {
      id: 3,
      date: '30',
      month: 'May',
      title: 'Cultural Workshop Series',
      location: 'Hongdae, Seoul',
      time: '14:00 - 16:00',
    },
  ];

  return (
    <div className="space-y-12">
      {/* Hero */}
      <section className="text-center py-12 bg-primary-light rounded-lg">
        <h1 className="text-4xl font-bold mb-3">Welcome to Our Community</h1>
        <p className="text-lg text-gray-600 mb-8">
          Connect with fellow expats, share experiences, and support each other
        </p>
        <div className="flex justify-center gap-8 text-center">
          <div>
            <div className="text-3xl font-bold text-primary">15,000+</div>
            <div className="text-gray-700">Members</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-primary">5,000+</div>
            <div className="text-gray-700">Questions Answered</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-primary">100+</div>
            <div className="text-gray-700">Events Hosted</div>
          </div>
        </div>
      </section>

      {/* Featured Members */}
      <section>
        <h2 className="text-3xl font-bold mb-8">Featured Community Members</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {members.map((member) => (
            <Card key={member.id} padding="lg">
              <div className="flex flex-col items-center text-center">
                <div className="w-16 h-16 bg-gray-300 rounded-full mb-4" />
                <h3 className="text-xl font-bold">{member.name}</h3>
                <Badge variant="primary" className="mt-2">
                  {member.badge}
                </Badge>
                <p className="text-sm text-gray-600 mt-3">{member.bio}</p>
                <div className="mt-4 flex justify-center gap-4 text-sm">
                  <span>⭐ {member.rating}</span>
                  <span>💬 {member.comments}</span>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </section>

      {/* Upcoming Events */}
      <section>
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-3xl font-bold">Upcoming Community Events</h2>
          <Button variant="outline">View All Events</Button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {events.map((event) => (
            <Card key={event.id} padding="lg">
              <div className="flex gap-4">
                <div className="bg-primary text-white rounded-lg p-3 text-center min-w-fit">
                  <div className="text-2xl font-bold">{event.date}</div>
                  <div className="text-sm">{event.month}</div>
                </div>
                <div className="flex-1">
                  <h3 className="font-bold mb-2">{event.title}</h3>
                  <p className="text-sm text-gray-600 mb-1">📍 {event.location}</p>
                  <p className="text-sm text-gray-600 mb-3">🕐 {event.time}</p>
                  <Button variant="primary" size="sm">
                    RSVP Now
                  </Button>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </section>

      {/* Forums */}
      <section>
        <h2 className="text-3xl font-bold mb-8">Popular Discussion Forums</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              title: 'Working in Korea',
              icon: '💼',
              description: 'Discuss job opportunities, work culture, and career development',
              stats: ['2.5k Topics', '15.3k Posts'],
            },
            {
              title: 'Language Exchange',
              icon: '🗣️',
              description: 'Practice Korean, find language partners, and share learning tips',
              stats: ['1.8k Topics', '12.1k Posts'],
            },
            {
              title: 'Lifestyle & Culture',
              icon: '🎌',
              description: 'Share experiences, tips, and cultural insights',
              stats: ['2.1k Topics', '14.2k Posts'],
            },
          ].map((forum, idx) => (
            <Card key={idx} hoverable padding="lg">
              <div className="text-4xl mb-3">{forum.icon}</div>
              <h3 className="text-lg font-bold mb-2">{forum.title}</h3>
              <p className="text-sm text-gray-600 mb-4">{forum.description}</p>
              <div className="text-xs text-gray-500 space-y-1">
                {forum.stats.map((stat, i) => (
                  <div key={i}>{stat}</div>
                ))}
              </div>
            </Card>
          ))}
        </div>
      </section>
    </div>
  );
};
