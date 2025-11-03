import React from 'react';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
  hoverable?: boolean;
  padding?: 'sm' | 'md' | 'lg';
}

const paddingStyles = {
  sm: 'p-3',
  md: 'p-4',
  lg: 'p-6',
};

export const Card = React.forwardRef<HTMLDivElement, CardProps>(
  (
    { children, hoverable = false, padding = 'md', className = '', ...props },
    ref
  ) => {
    return (
      <div
        ref={ref}
        className={`
          bg-white rounded-lg shadow-md border border-gray-200
          ${hoverable ? 'hover:shadow-lg transition-shadow duration-200 cursor-pointer' : ''}
          ${paddingStyles[padding]}
          ${className}
        `}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Card.displayName = 'Card';
