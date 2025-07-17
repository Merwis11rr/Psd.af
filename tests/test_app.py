"""
Test suite for PSD.af application
"""
import pytest
import os
import tempfile
from app import app, db
from models import Contact, Portfolio, Testimonial


@pytest.fixture
def client():
    """Create test client"""
    # Create a temporary file for the test database
    db_fd, app.config['DATABASE_URL'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        
    os.close(db_fd)
    os.unlink(app.config['DATABASE_URL'])


@pytest.fixture
def sample_data():
    """Create sample data for testing"""
    portfolio = Portfolio(
        title='Test Portfolio',
        description='Test Description',
        category='brochure',
        featured=True
    )
    
    testimonial = Testimonial(
        client_name='Test Client',
        client_title='Test Title',
        content='Test testimonial content',
        rating=5,
        featured=True
    )
    
    db.session.add(portfolio)
    db.session.add(testimonial)
    db.session.commit()
    
    return {
        'portfolio': portfolio,
        'testimonial': testimonial
    }


class TestRoutes:
    """Test application routes"""
    
    def test_homepage(self, client):
        """Test homepage loads correctly"""
        response = client.get('/')
        assert response.status_code == 200
        assert 'به PSD.af خوش آمدید' in response.data.decode('utf-8')
    
    def test_brochures_page(self, client):
        """Test brochures page loads correctly"""
        response = client.get('/brochures')
        assert response.status_code == 200
        assert 'بروشورها' in response.data.decode('utf-8')
    
    def test_business_cards_page(self, client):
        """Test business cards page loads correctly"""
        response = client.get('/business-cards')
        assert response.status_code == 200
        assert 'کارت‌های ویزیت' in response.data.decode('utf-8')
    
    def test_archive_page(self, client):
        """Test archive page loads correctly"""
        response = client.get('/archive')
        assert response.status_code == 200
        assert 'آرشیو' in response.data.decode('utf-8')
    
    def test_contact_page_get(self, client):
        """Test contact page loads correctly"""
        response = client.get('/contact')
        assert response.status_code == 200
        assert 'تماس با ما' in response.data.decode('utf-8')
    
    def test_contact_form_submission(self, client):
        """Test contact form submission"""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '09123456789',
            'service': 'brochure',
            'message': 'Test message content'
        }
        
        response = client.post('/contact', data=form_data, follow_redirects=True)
        assert response.status_code == 200
        
        # Check if contact was saved to database
        contact = Contact.query.filter_by(email='test@example.com').first()
        assert contact is not None
        assert contact.name == 'Test User'
        assert contact.message == 'Test message content'
    
    def test_contact_form_validation(self, client):
        """Test contact form validation"""
        # Test with missing required fields
        form_data = {
            'name': '',
            'email': 'test@example.com',
            'message': ''
        }
        
        response = client.post('/contact', data=form_data, follow_redirects=True)
        assert response.status_code == 200
        
        # Check that no contact was saved
        contact = Contact.query.filter_by(email='test@example.com').first()
        assert contact is None
    
    def test_404_handler(self, client):
        """Test 404 error handler"""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404


class TestModels:
    """Test database models"""
    
    def test_contact_model(self, client):
        """Test Contact model creation"""
        with app.app_context():
            contact = Contact(
                name='Test User',
                email='test@example.com',
                phone='09123456789',
                service='brochure',
                message='Test message'
            )
            
            db.session.add(contact)
            db.session.commit()
            
            # Test model properties
            assert contact.name == 'Test User'
            assert contact.email == 'test@example.com'
            assert contact.status == 'new'  # Default status
            assert contact.created_at is not None
    
    def test_portfolio_model(self, client):
        """Test Portfolio model creation"""
        with app.app_context():
            portfolio = Portfolio(
                title='Test Portfolio',
                description='Test description',
                category='brochure',
                tags='tag1, tag2, tag3',
                featured=True
            )
            
            db.session.add(portfolio)
            db.session.commit()
            
            # Test model properties
            assert portfolio.title == 'Test Portfolio'
            assert portfolio.category == 'brochure'
            assert portfolio.featured is True
            assert portfolio.created_at is not None
            
            # Test tags method
            tags = portfolio.get_tags_list()
            assert len(tags) == 3
            assert 'tag1' in tags
            assert 'tag2' in tags
    
    def test_testimonial_model(self, client):
        """Test Testimonial model creation"""
        with app.app_context():
            testimonial = Testimonial(
                client_name='Test Client',
                client_title='Test Title',
                content='Test testimonial content',
                rating=5,
                featured=True
            )
            
            db.session.add(testimonial)
            db.session.commit()
            
            # Test model properties
            assert testimonial.client_name == 'Test Client'
            assert testimonial.rating == 5
            assert testimonial.featured is True
            assert testimonial.created_at is not None


class TestAdmin:
    """Test admin functionality"""
    
    def test_admin_contacts_page(self, client):
        """Test admin contacts page"""
        response = client.get('/admin/contacts')
        assert response.status_code == 200
        assert 'مدیریت پیام‌ها' in response.data.decode('utf-8')
    
    def test_sample_data_creation(self, client):
        """Test sample data creation"""
        response = client.get('/admin/sample-data')
        assert response.status_code == 302  # Redirect after creation
        
        # Check if sample data was created
        with app.app_context():
            portfolio_count = Portfolio.query.count()
            testimonial_count = Testimonial.query.count()
            
            assert portfolio_count > 0
            assert testimonial_count > 0


class TestDatabase:
    """Test database operations"""
    
    def test_database_connection(self, client):
        """Test database connection"""
        with app.app_context():
            # Test that we can query the database
            contacts = Contact.query.all()
            assert isinstance(contacts, list)
    
    def test_featured_items_query(self, client, sample_data):
        """Test featured items query"""
        with app.app_context():
            featured_portfolio = Portfolio.query.filter_by(featured=True).all()
            featured_testimonials = Testimonial.query.filter_by(featured=True).all()
            
            assert len(featured_portfolio) > 0
            assert len(featured_testimonials) > 0
            
            # Test that all returned items are indeed featured
            for item in featured_portfolio:
                assert item.featured is True
            
            for item in featured_testimonials:
                assert item.featured is True


class TestSecurity:
    """Test security aspects"""
    
    def test_sql_injection_prevention(self, client):
        """Test SQL injection prevention"""
        malicious_input = "'; DROP TABLE contacts; --"
        
        form_data = {
            'name': malicious_input,
            'email': 'test@example.com',
            'message': 'Test message'
        }
        
        response = client.post('/contact', data=form_data, follow_redirects=True)
        assert response.status_code == 200
        
        # Check that the malicious input was stored safely
        with app.app_context():
            contact = Contact.query.filter_by(email='test@example.com').first()
            assert contact is not None
            assert contact.name == malicious_input  # Stored as-is, not executed
    
    def test_xss_prevention(self, client):
        """Test XSS prevention"""
        xss_input = '<script>alert("XSS")</script>'
        
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': xss_input
        }
        
        response = client.post('/contact', data=form_data, follow_redirects=True)
        assert response.status_code == 200
        
        # Check that the script tag is not executed in the response
        assert '<script>' not in response.data.decode('utf-8')


if __name__ == '__main__':
    pytest.main([__file__])