import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Button, Card, Input } from '../components/atomic';

const questionSchema = z.object({
  title: z.string().min(10, 'Title must be at least 10 characters'),
  category: z.string().min(1, 'Please select a category'),
  details: z.string().min(20, 'Details must be at least 20 characters'),
  tags: z.string().optional(),
});

type QuestionFormData = z.infer<typeof questionSchema>;

export const AskQuestionPage: React.FC = () => {
  const [isPreviewOpen, setIsPreviewOpen] = useState(false);
  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm<QuestionFormData>({
    resolver: zodResolver(questionSchema),
  });

  const formData = watch();

  const onSubmit = (data: QuestionFormData) => {
    console.log('Form submitted:', data);
    alert('Question submitted! (This is a demo)');
  };

  return (
    <div className="max-w-3xl mx-auto space-y-8">
      {/* Header */}
      <section className="text-center">
        <h1 className="text-4xl font-bold mb-4">Ask a Question</h1>
        <p className="text-lg text-gray-600">
          Get help from our community of expats and locals in Korea
        </p>
      </section>

      {/* Guidelines */}
      <section>
        <h2 className="text-2xl font-bold mb-6">Writing a good question</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              icon: '🔍',
              title: 'Search first',
              description: "Make sure your question hasn't been asked before",
            },
            {
              icon: '#️⃣',
              title: 'Be specific',
              description: 'Include details and background in your question',
            },
            {
              icon: '🏷️',
              title: 'Add relevant tags',
              description: 'Tags help others find and answer your question',
            },
          ].map((guideline, idx) => (
            <Card key={idx} padding="md" className="text-center">
              <div className="text-4xl mb-3">{guideline.icon}</div>
              <h3 className="font-semibold mb-2">{guideline.title}</h3>
              <p className="text-sm text-gray-600">{guideline.description}</p>
            </Card>
          ))}
        </div>
      </section>

      {/* Form */}
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        {/* Title */}
        <Card padding="lg">
          <label className="block font-semibold mb-2">Title</label>
          <p className="text-sm text-gray-600 mb-3">
            Be specific and imagine you're asking another person
          </p>
          <Input
            placeholder="e.g., How do I register for health insurance as a foreign student in Seoul?"
            {...register('title')}
          />
          {errors.title && <span className="text-red-500 text-sm mt-1">{errors.title.message}</span>}
        </Card>

        {/* Category */}
        <Card padding="lg">
          <label className="block font-semibold mb-2">Category</label>
          <p className="text-sm text-gray-600 mb-3">
            Select the most relevant category for your question
          </p>
          <select
            {...register('category')}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
          >
            <option value="">Select a category</option>
            <option value="documentation">Documentation</option>
            <option value="housing">Housing</option>
            <option value="language">Language</option>
            <option value="healthcare">Healthcare</option>
            <option value="banking">Banking</option>
            <option value="lifestyle">Lifestyle</option>
          </select>
          {errors.category && (
            <span className="text-red-500 text-sm mt-1">{errors.category.message}</span>
          )}
        </Card>

        {/* Details */}
        <Card padding="lg">
          <label className="block font-semibold mb-2">Details</label>
          <p className="text-sm text-gray-600 mb-3">
            Include all the information someone would need to answer your question
          </p>
          <textarea
            {...register('details')}
            rows={10}
            placeholder="Explain your situation in detail..."
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary resize-none"
          />
          {errors.details && (
            <span className="text-red-500 text-sm mt-1">{errors.details.message}</span>
          )}
        </Card>

        {/* Tags */}
        <Card padding="lg">
          <label className="block font-semibold mb-2">Tags</label>
          <p className="text-sm text-gray-600 mb-3">
            Add up to 5 tags to describe what your question is about
          </p>
          <Input placeholder="e.g., visa, student, healthcare" {...register('tags')} />
          <div className="mt-3 flex flex-wrap gap-2">
            {['student', 'visa', 'healthcare', 'documentation'].map((tag) => (
              <button
                key={tag}
                type="button"
                className="px-3 py-1 bg-gray-100 hover:bg-primary hover:text-white rounded text-sm transition-colors"
              >
                {tag}
              </button>
            ))}
          </div>
        </Card>

        {/* Preview */}
        <Card padding="lg">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold">Preview</h3>
            <button
              type="button"
              onClick={() => setIsPreviewOpen(!isPreviewOpen)}
              className="text-primary hover:underline text-sm"
            >
              {isPreviewOpen ? 'Hide' : 'Show'} Preview
            </button>
          </div>
          {isPreviewOpen && (
            <div className="p-4 bg-gray-50 rounded border border-gray-200">
              <h3 className="font-bold mb-2">{formData.title || 'Your question title'}</h3>
              <p className="text-sm text-gray-600 mb-3">{formData.details || 'Your question details...'}</p>
            </div>
          )}
        </Card>

        {/* Actions */}
        <Card padding="lg" className="flex gap-4">
          <Button variant="outline" type="button">
            Preview
          </Button>
          <Button variant="primary" type="submit">
            Post Your Question
          </Button>
        </Card>
      </form>
    </div>
  );
};
