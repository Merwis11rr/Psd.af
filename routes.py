from flask import render_template, request, flash, redirect, url_for
from app import app, db
from models import Contact, Portfolio, Testimonial, BlogPost, Service
from datetime import datetime

@app.route('/')
def index():
    """Homepage with hero section and portfolio preview"""
    # Get featured portfolio items
    featured_portfolio = Portfolio.query.filter_by(featured=True).limit(6).all()
    
    # Get recent testimonials
    recent_testimonials = Testimonial.query.filter_by(featured=True).limit(3).all()
    
    return render_template('index.html', 
                         featured_portfolio=featured_portfolio,
                         testimonials=recent_testimonials)

@app.route('/brochures')
def brochures():
    """Brochures portfolio page"""
    brochure_items = Portfolio.query.filter_by(category='brochure').order_by(Portfolio.created_at.desc()).all()
    return render_template('brochures.html', portfolio_items=brochure_items)

@app.route('/business-cards')
def business_cards():
    """Business cards portfolio page"""
    business_card_items = Portfolio.query.filter_by(category='business-card').order_by(Portfolio.created_at.desc()).all()
    return render_template('business_cards.html', portfolio_items=business_card_items)

@app.route('/archive')
def archive():
    """Design archive page"""
    # Get all portfolio items grouped by category
    all_portfolio = Portfolio.query.order_by(Portfolio.created_at.desc()).all()
    
    # Group by category
    portfolio_by_category = {}
    for item in all_portfolio:
        if item.category not in portfolio_by_category:
            portfolio_by_category[item.category] = []
        portfolio_by_category[item.category].append(item)
    
    # Get testimonials
    testimonials = Testimonial.query.filter_by(featured=True).limit(3).all()
    
    return render_template('archive.html', 
                         portfolio_items=all_portfolio,
                         portfolio_by_category=portfolio_by_category,
                         testimonials=testimonials)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form and WhatsApp integration"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')
        
        if name and email and message:
            # Save to database
            try:
                contact_submission = Contact(
                    name=name,
                    email=email,
                    phone=phone,
                    service=service,
                    message=message
                )
                db.session.add(contact_submission)
                db.session.commit()
                
                flash('پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.', 'success')
            except Exception as e:
                db.session.rollback()
                flash('خطایی در ارسال پیام رخ داد. لطفاً دوباره تلاش کنید.', 'error')
                print(f"Database error: {e}")
        else:
            flash('لطفاً تمام فیلدهای ضروری را پر کنید.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/admin/sample-data')
def create_sample_data():
    """Create sample data for demonstration (remove in production)"""
    try:
        # Create sample portfolio items
        sample_portfolio = [
            Portfolio(
                title='بروشور شرکت نرم‌افزاری',
                description='طراحی مدرن و حرفه‌ای برای معرفی خدمات شرکت با استفاده از رنگ‌های گرم',
                category='brochure',
                client_name='شرکت تکنولوژی پردازش',
                project_year=2023,
                tags='شرکتی, مدرن, تکنولوژی',
                featured=True
            ),
            Portfolio(
                title='کارت ویزیت دکتر احمدی',
                description='طراحی مناسب برای پزشکان و متخصصان با رنگ‌های آرام و طراحی حرفه‌ای',
                category='business-card',
                client_name='دکتر علی احمدی',
                project_year=2023,
                tags='پزشکی, حرفه‌ای, مینیمال',
                featured=True
            ),
            Portfolio(
                title='لوگوی رستوران سنتی',
                description='طراحی لوگوی خلاقانه برای رستوران غذاهای سنتی ایرانی',
                category='logo',
                client_name='رستوران کوهستان',
                project_year=2022,
                tags='لوگو, سنتی, رستوران',
                featured=True
            ),
            Portfolio(
                title='بروشور کلینیک زیبایی',
                description='طراحی زیبا و جذاب برای معرفی خدمات کلینیک زیبایی',
                category='brochure',
                client_name='کلینیک زیبایی آرامش',
                project_year=2023,
                tags='زیبایی, مدرن, شیک',
                featured=False
            ),
            Portfolio(
                title='کارت ویزیت مهندس عمران',
                description='طراحی تکنیکی و دقیق مناسب برای مهندسان و متخصصان فنی',
                category='business-card',
                client_name='مهندس محمد رضایی',
                project_year=2022,
                tags='مهندسی, تکنیکی, حرفه‌ای',
                featured=False
            ),
            Portfolio(
                title='طراحی کاتالوگ محصولات',
                description='کاتالوگ جامع برای معرفی محصولات صنعتی',
                category='catalog',
                client_name='شرکت صنعتی پارس',
                project_year=2023,
                tags='کاتالوگ, صنعتی, محصولات',
                featured=True
            )
        ]

        # Create sample testimonials
        sample_testimonials = [
            Testimonial(
                client_name='احمد محمدی',
                client_title='مدیر شرکت',
                content='کیفیت کار عالی و تحویل به موقع. کارت ویزیت طراحی شده برای من بسیار حرفه‌ای و زیبا بود.',
                rating=5,
                featured=True
            ),
            Testimonial(
                client_name='فاطمه احمدی',
                client_title='صاحب کسب‌وکار',
                content='طراحی بروشور شرکت ما فوق‌العاده شد. تیم PSD.af واقعاً حرفه‌ای هستند.',
                rating=5,
                featured=True
            ),
            Testimonial(
                client_name='علی رضایی',
                client_title='طراح گرافیک',
                content='پشتیبانی عالی و قیمت مناسب. قطعاً دوباره از خدمات آن‌ها استفاده خواهم کرد.',
                rating=5,
                featured=True
            )
        ]

        # Create sample services
        sample_services = [
            Service(
                name='طراحی بروشور',
                description='طراحی حرفه‌ای بروشور برای معرفی خدمات و محصولات شما',
                base_price=500000,
                delivery_days=5,
                features='طراحی اختصاصی, فایل‌های قابل ویرایش, 3 بار اصلاح رایگان',
                active=True
            ),
            Service(
                name='طراحی کارت ویزیت',
                description='کارت ویزیت منحصربه‌فرد و حرفه‌ای برای کسب‌وکار شما',
                base_price=200000,
                delivery_days=3,
                features='طراحی دورو, فایل آماده چاپ, انتخاب کاغذ مناسب',
                active=True
            ),
            Service(
                name='طراحی لوگو',
                description='لوگوی خلاقانه و به‌یادماندنی برای برند شما',
                base_price=800000,
                delivery_days=7,
                features='چندین گزینه طراحی, فرمت‌های مختلف, راهنمای استفاده',
                active=True
            )
        ]

        # Add all sample data to database
        for item in sample_portfolio:
            existing = Portfolio.query.filter_by(title=item.title).first()
            if not existing:
                db.session.add(item)

        for testimonial in sample_testimonials:
            existing = Testimonial.query.filter_by(client_name=testimonial.client_name).first()
            if not existing:
                db.session.add(testimonial)

        for service in sample_services:
            existing = Service.query.filter_by(name=service.name).first()
            if not existing:
                db.session.add(service)

        db.session.commit()
        
        flash('نمونه داده‌ها با موفقیت ایجاد شدند!', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        db.session.rollback()
        flash(f'خطا در ایجاد داده‌ها: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/admin/contacts')
def view_contacts():
    """View all contact submissions (admin only)"""
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template('admin_contacts.html', contacts=contacts)

@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html'), 500
