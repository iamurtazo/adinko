import React from 'react';

export type InputSize = 'sm' | 'md' | 'lg';

interface InputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'size'> {
  label?: string;
  error?: string;
  size?: InputSize;
  icon?: React.ReactNode;
  helperText?: string;
}

const sizeStyles: Record<InputSize, string> = {
  sm: 'px-3 py-1.5 text-sm',
  md: 'px-4 py-2 text-base',
  lg: 'px-4 py-3 text-lg',
};

export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  (
    {
      label,
      error,
      size = 'md',
      icon,
      helperText,
      className = '',
      ...props
    },
    ref
  ) => {
    return (
      <div className="flex flex-col gap-1">
        {label && (
          <label className="text-sm font-medium text-gray-700">
            {label}
            {props.required && <span className="text-red-500 ml-1">*</span>}
          </label>
        )}
        <div className="relative flex items-center">
          <input
            ref={ref}
            className={`
              w-full border-2 rounded-lg transition-colors duration-200
              focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary
              placeholder-gray-400
              ${sizeStyles[size]}
              ${error ? 'border-red-500 focus:border-red-500' : 'border-border hover:border-gray-300'}
              ${icon ? 'pl-10' : ''}
              ${className}
            `}
            {...props}
          />
          {icon && (
            <div className="absolute left-3 text-gray-500 pointer-events-none">
              {icon}
            </div>
          )}
        </div>
        {error && <span className="text-sm text-red-500">{error}</span>}
        {helperText && !error && (
          <span className="text-sm text-gray-500">{helperText}</span>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';
