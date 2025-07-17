# PSD.af - Persian Design Portfolio

## Overview

PSD.af is a Persian (Farsi) graphic design portfolio website showcasing design services including brochures, business cards, and other graphic design work. The application is built as a simple Flask web application with a focus on showcasing design portfolios and providing contact functionality for potential clients.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5 RTL for right-to-left Persian text support
- **Styling**: Custom CSS with Persian typography using Vazirmatn font
- **Icons**: Font Awesome for iconography
- **Layout**: Responsive design with mobile-first approach
- **Direction**: RTL (Right-to-Left) layout for Persian language support

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Structure**: Simple MVC pattern with routes, templates, and static files
- **Session Management**: Flask sessions with configurable secret key
- **Error Handling**: Custom 404 and 500 error handlers
- **Proxy Support**: Werkzeug ProxyFix for deployment behind reverse proxies

## Key Components

### Application Structure
- **app.py**: Main Flask application factory with configuration
- **main.py**: Application entry point
- **routes.py**: Route definitions and request handlers
- **templates/**: Jinja2 HTML templates with base template inheritance
- **static/**: CSS, JavaScript, and asset files

### Page Components
1. **Homepage (index)**: Hero section with service preview cards
2. **Brochures**: Portfolio showcase for brochure designs
3. **Business Cards**: Portfolio showcase for business card designs
4. **Archive**: Company statistics and portfolio history
5. **Contact**: Contact form with WhatsApp integration

### Template Architecture
- **Base Template**: Common layout with navigation, meta tags, and footer
- **Page Templates**: Extend base template for specific content
- **Responsive Navigation**: Bootstrap navbar with mobile toggle
- **Persian Fonts**: Google Fonts integration for Vazirmatn typeface

## Data Flow

### Request Flow
1. Client requests route → Flask router → Route handler → Template rendering → Response
2. Static files served directly by Flask development server
3. Form submissions processed server-side with flash messaging
4. Error handling redirects to appropriate error pages

### Contact Form Processing
- Form data validation on submission
- Flash messages for user feedback (success/error)
- Currently displays messages only (no database/email integration)
- Future enhancement: Database storage or email integration

## External Dependencies

### Frontend Dependencies
- **Bootstrap 5 RTL**: CSS framework with right-to-left support
- **Font Awesome 6**: Icon library
- **Google Fonts (Vazirmatn)**: Persian typography
- **CDN Delivery**: All frontend assets loaded from CDNs

### Backend Dependencies
- **Flask**: Web framework
- **Werkzeug**: WSGI utilities and middleware

### Development Dependencies
- Python 3.x runtime environment
- Flask development server for local testing

## Deployment Strategy

### Current Configuration
- **Development Mode**: Flask development server with debug enabled
- **Host Configuration**: Binds to 0.0.0.0:5000 for external access
- **Proxy Support**: ProxyFix middleware for reverse proxy deployment
- **Environment Variables**: Session secret key configurable via environment

### Production Considerations
- Session secret key should be set via SESSION_SECRET environment variable
- Debug mode should be disabled in production
- Consider WSGI server (Gunicorn, uWSGI) for production deployment
- Static file serving should be handled by web server (Nginx, Apache)

### Scalability Notes
- Current implementation is stateless and suitable for horizontal scaling
- No database dependencies in current version
- Contact form functionality needs enhancement for production use
- Consider adding database integration for contact form submissions and portfolio management