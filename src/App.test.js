import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';


test('Home button disappears', () => {
  render(<App />);
  const HomeButtonElement = screen.getByText('Home');
  expect(HomeButtonElement).toBeInTheDocument();
 
});


test('Applied button disappears', () => {
  render(<App />);
  const AppliedButtonElement = screen.getByText('Applied');
  expect(AppliedButtonElement).toBeInTheDocument();
 
});

test('Favorites button disappears', () => {
  render(<App />);
  const HomeButtonElement = screen.getByText('Home');
  expect(HomeButtonElement).toBeInTheDocument();
 
});

