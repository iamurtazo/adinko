import React from 'react';
import { Navbar } from '../composite/Navbar';

interface LayoutProps {
  children: React.ReactNode;
}

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <main className="container-custom py-8">
        {children}
      </main>
    </div>
  );
};
