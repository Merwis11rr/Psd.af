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
- **Interactive Elements**: Smooth animations and hover effects
- **SEO Optimized**: Proper meta tags and structured markup

## 🚀 Live Demo

Visit the live website: [Your Domain Here]

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

## 🚀 GitHub Pages Deployment

### Quick Setup

1. **Fork this repository** or **create a new repository**
2. **Upload all files** to your repository
3. **Enable GitHub Pages**:
   - Go to repository **Settings**
   - Scroll to **Pages** section
   - Select **Deploy from a branch**
   - Choose **main** branch and **/ (root)** folder
   - Click **Save**

4. **Access Your Site**:
   - Your site will be available at: `https://yourusername.github.io/repository-name`
   - It may take a few minutes to deploy

## 🎨 Database Schema

### Models

- **Contact**: Customer inquiries and contact form submissions
- **Portfolio**: Design projects and portfolio showcase items
- **Testimonial**: Client feedback and reviews
- **BlogPost**: Design insights and company blog content
- **Service**: Available design services and pricing
- **Newsletter**: Email subscription management

## 📞 Contact Information

- **WhatsApp**: +93 123 456 789
- **Telegram**: @psdaf_official
- **Email**: info@psd.af
- **Instagram**: @psd.af

## 🔧 Customization

### Contact Information
Update contact details in all HTML files:
- WhatsApp number: Search for `93123456789` and replace
- Email: Search for `info@psd.af` and replace
- Social media links: Update href attributes

### Colors & Styling
Modify `css/style.css`:
- Primary colors: Search for `gold` and `orange`
- Background gradients: Look for `linear-gradient` and `radial-gradient`
- Typography: Modify font-family properties

### Content
- Replace placeholder text with your actual content
- Add real portfolio images
- Update company information and statistics

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mirvais** - PSD.af Team
- Website: [PSD.af](https://psd.af)
- Email: info@psd.af
- WhatsApp: [Contact Us](https://wa.me/93123456789)

## 🔄 Changelog

### v1.1.0 (July 20, 2025)
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

**Built with ❤️ for the Persian design community**
