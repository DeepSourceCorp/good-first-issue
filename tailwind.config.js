/** @type {import('tailwindcss').Config} */
export default {
  content: [],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        juniper: '#33cb9a',
        light_juniper: '#2EB78B',
        robin: '#2c3450',
        slate: '#52575c',
        cherry: '#782614',
        honey: '#f6d87c',
        aqua: '#2596bb',
        gitlab: '#6753B5',
        vanilla: {
          100: '#514949',
          200: '#beb0b0',
          300: '#eeeeee',
          400: '#1659de'
        },
        ink: {
          100: '#373c49',
          200: '#2c303a',
          300: '#21242c',
          400: '#16181d'
        }
      },
      fontFamily: {
        sans: [
          'Inter',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          '"Noto Sans"',
          'sans-serif',
          '"Apple Color Emoji"',
          '"Segoe UI Emoji"',
          '"Segoe UI Symbol"',
          '"Noto Color Emoji"'
        ],
        serif: ['Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif'],
        mono: ['Menlo', 'Monaco', 'Consolas', '"Liberation Mono"', '"Courier New"', 'monospace']
      }
    }
  },
  plugins: []
}
