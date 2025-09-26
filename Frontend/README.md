# Resume Builder Frontend

A React.js frontend application for the Resume Builder project, built with Vite and styled with Tailwind CSS.

## Features

- Modern and responsive form interface
- Real-time form validation
- PDF download functionality
- Professional styling with Tailwind CSS
- Error handling and loading states
- Form auto-reset after successful submission

## Tech Stack

- **React 19.1.1** - Frontend framework
- **Vite 7.1.7** - Build tool and development server
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls
- **ESLint** - Code linting

## Getting Started

### Prerequisites

- Node.js (version 16 or higher)
- npm or yarn package manager

### Installation

1. Navigate to the Frontend directory:
   ```bash
   cd Frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and navigate to `http://localhost:5173`

## Form Fields

The form collects the following required information:

- **Full Name** - User's complete name
- **Email Address** - Contact email
- **Phone Number** - Contact phone number
- **Education** - Educational background and qualifications
- **Work Experience** - Professional experience and job history
- **Skills** - Technical and professional skills

## API Integration

The frontend communicates with the FastAPI backend at `http://localhost:8000/api/resume_build/generate_resume`.

Make sure the backend server is running before using the form.

## Build and Deploy

To build the project for production:

```bash
npm run build
```

The built files will be in the `dist` directory.

## Development Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request+ Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
