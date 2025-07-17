from flask import render_template, request, flash, redirect, url_for
from app import app

@app.route('/')
def index():
    """Homepage with hero section and portfolio preview"""
    return render_template('index.html')

@app.route('/brochures')
def brochures():
    """Brochures portfolio page"""
    return render_template('brochures.html')

@app.route('/business-cards')
def business_cards():
    """Business cards portfolio page"""
    return render_template('business_cards.html')

@app.route('/archive')
def archive():
    """Design archive page"""
    return render_template('archive.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form and WhatsApp integration"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real application, you would save this to a database or send an email
        if name and email and message:
            flash('پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.', 'success')
        else:
            flash('لطفاً تمام فیلدها را پر کنید.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html'), 500
