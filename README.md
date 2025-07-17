# PSD.af - Persian Design Portfolio

A professional Persian (Farsi) graphic design portfolio website built with Flask, featuring modern dark theme design and comprehensive portfolio management system.

## 🌟 Features

- **Persian/RTL Layout**: Fully optimized for Persian language with right-to-left text direction
- **Modern Dark Theme**: Elegant gradient backgrounds with gold accents
- **Responsive Design**: Mobile-first approach with Bootstrap RTL support
- **Portfolio Management**: Dynamic portfolio showcase with categories
- **Contact System**: Contact form with database storage and admin interface
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Admin Panel**: Backend management for contacts and content

## 🚀 Live Demo

Visit the live website: [Your Domain Here]

## 📸 Screenshots

![Homepage](screenshots/homepage.png)
![Portfolio](screenshots/portfolio.png)
![Contact Form](screenshots/contact.png)

## 🛠️ Tech Stack

### Frontend
- **HTML5/CSS3** with RTL support
- **Bootstrap 5 RTL** for responsive design
- **Vazirmatn Font** for Persian typography
- **Font Awesome 6** for icons
- **Vanilla JavaScript** for interactivity

### Backend
- **Flask** (Python web framework)
- **PostgreSQL** database
- **SQLAlchemy ORM** for database operations
- **Gunicorn** WSGI server
- **Werkzeug** middleware

### Development Tools
- **Python 3.11+**
- **pip** package manager
- **Git** version control

## 📁 Project Structure

```
psd-af-portfolio/
├── app.py                  # Flask application setup
├── main.py                 # Application entry point
├── routes.py               # URL routes and handlers
├── models.py               # Database models
├── requirements.txt        # Python dependencies
├── templates/              # Jinja2 HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Homepage
│   ├── brochures.html     # Brochures portfolio
│   ├── business_cards.html # Business cards portfolio
│   ├── archive.html       # Archive page
│   ├── contact.html       # Contact form
│   └── admin_contacts.html # Admin contact management
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── js/
│       └── main.js        # JavaScript functionality
└── README.md              # This file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- PostgreSQL database
- Git

### Local Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/psd-af-portfolio.git
cd psd-af-portfolio
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
export DATABASE_URL="postgresql://username:password@localhost/psd_af_db"
export SESSION_SECRET="your-secret-key-here"
```

5. **Initialize database:**
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

6. **Run the application:**
```bash
python main.py
```

Visit `http://localhost:5000` to see the website.

### Docker Setup (Optional)

```bash
# Build Docker image
docker build -t psd-af-portfolio .

# Run with Docker Compose
docker-compose up -d
```

## 🎨 Database Schema

### Models

- **Contact**: Customer inquiries and contact form submissions
- **Portfolio**: Design projects and portfolio showcase items
- **Testimonial**: Client feedback and reviews
- **BlogPost**: Design insights and company blog content
- **Service**: Available design services and pricing
- **Newsletter**: Email subscription management

### Sample Data

To populate the database with sample data:
```bash
# Visit /admin/sample-data in your browser
# Or run programmatically:
python -c "from routes import create_sample_data; create_sample_data()"
```

## 🚀 Deployment

### Heroku Deployment

1. **Create Heroku app:**
```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:mini
```

2. **Set environment variables:**
```bash
heroku config:set SESSION_SECRET=your-secret-key
```

3. **Deploy:**
```bash
git push heroku main
```

### VPS Deployment

1. **Set up server with Nginx and Gunicorn**
2. **Configure SSL with Let's Encrypt**
3. **Set up process manager (systemd/supervisor)**

## 📝 Usage

### Admin Functions

- **View Contacts**: `/admin/contacts` - Manage customer inquiries
- **Sample Data**: `/admin/sample-data` - Populate database with demo content

### API Endpoints

- `GET /` - Homepage with featured portfolio
- `GET /brochures` - Brochures portfolio page
- `GET /business-cards` - Business cards portfolio
- `GET /archive` - Complete portfolio archive
- `GET /contact` - Contact form
- `POST /contact` - Submit contact form

## 🎯 Features to Implement

### High Priority
- [ ] User authentication and admin dashboard
- [ ] Image upload and gallery management
- [ ] Blog system for design insights
- [ ] Newsletter subscription system
- [ ] Multi-language support (Persian/English)

### Medium Priority
- [ ] Online payment integration
- [ ] Project management system
- [ ] Client portal for project tracking
- [ ] SEO optimization
- [ ] Analytics integration

### Low Priority
- [ ] Social media integration
- [ ] Live chat support
- [ ] Email marketing integration
- [ ] Mobile app
- [ ] API for third-party integrations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code style
- Use meaningful commit messages
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mirvais** - PSD.af Team
- Website: [PSD.af](https://psd.af)
- Email: info@psd.af
- WhatsApp: [Contact Us](https://wa.me/93123456789)

## 🙏 Acknowledgments

- Bootstrap team for RTL support
- Google Fonts for Vazirmatn typeface
- Font Awesome for beautiful icons
- Flask community for excellent documentation

## 📞 Support

For support, email info@psd.af or join our WhatsApp group.

## 🔄 Changelog

### v1.1.0 (July 17, 2025)
- ✅ Added PostgreSQL database integration
- ✅ Created comprehensive data models
- ✅ Implemented contact form database storage
- ✅ Added admin interface for contact management
- ✅ Created sample data population system
- ✅ Enhanced portfolio and testimonial management

### v1.0.0 (Initial Release)
- ✅ Basic Flask application structure
- ✅ Persian RTL layout implementation
- ✅ Dark theme with gold accents
- ✅ Responsive design with Bootstrap RTL
- ✅ Portfolio showcase pages
- ✅ Contact form with WhatsApp integration
- ✅ Static content management

---

Made with ❤️ for the Persian design community