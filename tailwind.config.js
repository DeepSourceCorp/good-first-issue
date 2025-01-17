/** @type {import('tailwindcss').Config} */
// Tailwind CSS configuration file. This defines custom styles and settings for the project.

export default {
  // Specifies the files where Tailwind should look for class usage.
  content: [],  // Add paths to your template files here (e.g., ['./src/**/*.html']).

  theme: {
    // Extends the default theme to add custom styles.
    extend: {
      colors: {
        transparent: 'transparent',  // No color (fully transparent).
        current: 'currentColor',    // Inherits the current text color.
        
        // Custom colors used in the project.
        juniper: '#33cb9a',         // A green shade for branding or highlights.
        light_juniper: '#2EB78B',   // A lighter green shade.
        robin: '#4568dc',           // A blue shade.
        slate: '#52575c',           // A neutral gray shade.
        cherry: '#df6145',          // A red shade, possibly for warnings or errors.
        honey: '#f6d87c',           // A yellow shade, suitable for accents.
        aqua: '#23c4f8',            // A light blue shade.
        gitlab: '#6753B5',          // A purple shade, possibly used for GitLab branding.

        // Shades of white and gray for vanilla tones.
        vanilla: {
          100: '#ffffff',           // Pure white.
          200: '#f5f5f5',           // Light gray.
          300: '#eeeeee',           // Medium gray.
          400: '#c0c1c3'            // Darker gray.
        },
        
        // Shades of black and gray for ink tones.
        ink: {
          100: '#373c49',           // Light ink tone.
          200: '#2c303a',           // Medium ink tone.
          300: '#21242c',           // Dark ink tone.
          400: '#16181d'            // Darkest ink tone.
        }
      },

      // Defines custom font families used in the project.
      fontFamily: {
        sans: [ // Sans-serif fonts for general usage.
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
        serif: [ // Serif fonts for formal or traditional designs.
          'Georgia',
          'Cambria',
          '"Times New Roman"',
          'Times',
          'serif'
        ],
        mono: [ // Monospace fonts for code or technical designs.
          'Menlo',
          'Monaco',
          'Consolas',
          '"Liberation Mono"',
          '"Courier New"',
          'monospace'
        ]
      }
    }
  },
  
  // Plugins used to extend Tailwind CSS functionality.
  plugins: []
}