/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {
      colors: {
        custom: {
          peach: '#f9cb9c',
          orange: '#fda64a',
          cream: '#fce5cd',
          greenLight: '#b6d7a8',
          greenDark: '#93c47d',
        },
      },
    },
  },
  plugins: [],
}

