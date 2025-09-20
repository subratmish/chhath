# Create Contact Page HTML with Google Maps and Contact Form
contact_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Chhath Utsav Mahasangh</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .contact-info-card {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: var(--border-radius);
            padding: 2rem;
            margin-bottom: 2rem;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .contact-icon {
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
        }
        
        .map-container {
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            margin-bottom: 2rem;
        }
        
        .ghat-location {
            background: white;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: var(--shadow);
            border-left: 4px solid var(--primary-color);
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }
        
        .social-link {
            width: 45px;
            height: 45px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            color: white;
            font-size: 1.2rem;
            transition: all 0.3s ease;
        }
        
        .social-link:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .emergency-contact {
            background: #dc2626;
            color: white;
            padding: 1.5rem;
            border-radius: var(--border-radius);
            text-align: center;
            margin-bottom: 2rem;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="nav">
                <a href="index.html" class="logo">🪔 Chhath Utsav Mahasangh</a>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about-us.html">About Us</a></li>
                    <li><a href="about-chhath.html">About Chhath</a></li>
                    <li><a href="events.html">Events</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="contact.html" class="active">Contact</a></li>
                    <li><a href="donate.html" class="btn btn-secondary">Donate</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>📞 Contact Us</h1>
            <p>Get in touch with us for volunteering, support, or any inquiries about Chhath Puja</p>
        </div>
    </section>

    <!-- Emergency Contact Banner -->
    <section class="section" style="padding-top: 2rem; padding-bottom: 1rem;">
        <div class="container">
            <div class="emergency-contact">
                <h3>🚨 Emergency Contact During Festival</h3>
                <p style="margin-bottom: 1rem;">For immediate assistance during Chhath Puja celebrations</p>
                <div style="display: flex; gap: 2rem; justify-content: center; flex-wrap: wrap;">
                    <div><strong>📞 Emergency Helpline:</strong> +91 99999 12345</div>
                    <div><strong>🏥 Medical Emergency:</strong> +91 99999 67890</div>
                    <div><strong>🚔 Security:</strong> +91 99999 54321</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Information and Form -->
    <section class="section" style="padding-top: 1rem;">
        <div class="container">
            <div class="grid grid-2">
                <!-- Contact Information -->
                <div>
                    <div class="contact-info-card">
                        <h2 style="margin-bottom: 2rem;">Get in Touch</h2>
                        
                        <div class="contact-item">
                            <div class="contact-icon">📍</div>
                            <div>
                                <h4>Main Office</h4>
                                <p>Juhu Beach Area, Mumbai<br>Maharashtra 400049, India</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">📞</div>
                            <div>
                                <h4>Phone Numbers</h4>
                                <p>Main: +91 98765 43210<br>Alternate: +91 98765 43211</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">✉️</div>
                            <div>
                                <h4>Email Addresses</h4>
                                <p>General: info@chhathutsav.org<br>Volunteers: volunteer@chhathutsav.org</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">🕐</div>
                            <div>
                                <h4>Office Hours</h4>
                                <p>Mon-Fri: 10:00 AM - 6:00 PM<br>During Festival: 24/7 Support</p>
                            </div>
                        </div>
                        
                        <div class="social-links">
                            <a href="#" class="social-link" title="Facebook">📘</a>
                            <a href="#" class="social-link" title="Instagram">📷</a>
                            <a href="#" class="social-link" title="Twitter">🐦</a>
                            <a href="#" class="social-link" title="YouTube">📺</a>
                            <a href="#" class="social-link" title="WhatsApp">💬</a>
                        </div>
                    </div>
                </div>

                <!-- Contact Form -->
                <div>
                    <div class="card">
                        <h3>Send Us a Message</h3>
                        <form id="contactForm" onsubmit="submitForm(event)">
                            <div class="form-group">
                                <label class="form-label">Full Name *</label>
                                <input type="text" class="form-input" required>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Email Address *</label>
                                <input type="email" class="form-input" required>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Phone Number</label>
                                <input type="tel" class="form-input">
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Subject *</label>
                                <select class="form-select" required>
                                    <option value="">Select a subject</option>
                                    <option value="volunteer">Volunteer Opportunities</option>
                                    <option value="donation">Donation Inquiry</option>
                                    <option value="event">Event Information</option>
                                    <option value="media">Media Coverage</option>
                                    <option value="partnership">Partnership/Sponsorship</option>
                                    <option value="complaint">Complaint/Feedback</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Message *</label>
                                <textarea class="form-textarea" rows="6" placeholder="Please describe your inquiry in detail..." required></textarea>
                            </div>
                            
                            <div class="form-group">
                                <label style="display: flex; align-items: center; gap: 0.5rem;">
                                    <input type="checkbox" required>
                                    <span>I agree to the <a href="#" style="color: var(--primary-color);">Privacy Policy</a> and consent to being contacted.</span>
                                </label>
                            </div>
                            
                            <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Google Maps Section -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">Our Ghat Locations</h2>
            
            <!-- Main Map -->
            <div class="map-container">
                <!-- Google Maps Embed -->
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3769.0169656687765!2d72.82680631490324!3d19.107894187042404!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c9c676018b05%3A0x95ad518e1279151!2sJuhu%20Beach!5e0!3m2!1sen!2sin!4v1635784756847!5m2!1sen!2sin" 
                    width="100%" 
                    height="400" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy"
                    title="Juhu Beach Chhath Ghat Location">
                </iframe>
            </div>
            
            <!-- Ghat Details -->
            <div class="grid grid-2">
                <div class="ghat-location">
                    <h3>🏖️ Main Chhath Ghat - Juhu Beach</h3>
                    <p><strong>Address:</strong> Juhu Beach, near ISKCON Temple<br>
                    Juhu, Mumbai, Maharashtra 400049</p>
                    <p><strong>Facilities:</strong></p>
                    <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                        <li>✅ 24/7 Security during festival</li>
                        <li>✅ Medical aid station</li>
                        <li>✅ Clean drinking water</li>
                        <li>✅ Restroom facilities</li>
                        <li>✅ LED lighting system</li>
                        <li>✅ Prasad distribution area</li>
                    </ul>
                    <p><strong>Best Time to Visit:</strong> Sandhya Arghya (6:00 PM) and Usha Arghya (6:00 AM)</p>
                </div>
                
                <div class="ghat-location">
                    <h3>🌊 Secondary Ghat - Versova Beach</h3>
                    <p><strong>Address:</strong> Versova Beach, near Fishermen's Colony<br>
                    Versova, Andheri West, Mumbai 400061</p>
                    <p><strong>Facilities:</strong></p>
                    <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                        <li>✅ Smaller, peaceful setting</li>
                        <li>✅ Basic medical support</li>
                        <li>✅ Parking available</li>
                        <li>✅ Local volunteer support</li>
                        <li>✅ Connected to main ghat via shuttle</li>
                    </ul>
                    <p><strong>Best For:</strong> Elderly devotees and families with children</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Transportation and Directions -->
    <section class="section">
        <div class="container">
            <h2 class="section-title">How to Reach Us</h2>
            <div class="grid grid-3">
                <div class="card" style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🚌</div>
                    <h3>By Public Transport</h3>
                    <p><strong>Nearest Station:</strong> Vile Parle (Western Line)</p>
                    <p><strong>Auto/Taxi:</strong> 15 minutes from station</p>
                    <p><strong>BEST Buses:</strong> Routes 28, 38, 56, 222</p>
                    <p><strong>Special Festival Buses:</strong> Available during Chhath Puja</p>
                </div>
                
                <div class="card" style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🚗</div>
                    <h3>By Private Vehicle</h3>
                    <p><strong>From Airport:</strong> 20 minutes via Western Express Highway</p>
                    <p><strong>Parking:</strong> Designated areas near beach</p>
                    <p><strong>Traffic Alert:</strong> Heavy congestion during festival</p>
                    <p><strong>Recommendation:</strong> Use public transport during peak times</p>
                </div>
                
                <div class="card" style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🛺</div>
                    <h3>App-Based Cabs</h3>
                    <p><strong>Uber/Ola:</strong> Widely available</p>
                    <p><strong>Drop Point:</strong> Juhu Beach Main Entrance</p>
                    <p><strong>Festival Period:</strong> Surge pricing may apply</p>
                    <p><strong>Tip:</strong> Book shared rides to reduce costs</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">Frequently Asked Questions</h2>
            <div class="grid grid-2">
                <div class="card">
                    <h4>❓ When should I contact the emergency helpline?</h4>
                    <p>Use the emergency helpline for medical emergencies, lost persons, security concerns, or any urgent assistance needed during the festival period.</p>
                </div>
                
                <div class="card">
                    <h4>❓ How can I volunteer for Chhath Puja?</h4>
                    <p>Fill out our contact form with subject "Volunteer Opportunities" or email volunteer@chhathutsav.org. We'll get back to you with available roles and requirements.</p>
                </div>
                
                <div class="card">
                    <h4>❓ Is there parking available near the ghat?</h4>
                    <p>Yes, designated parking areas are available, but spaces are limited during the festival. We recommend using public transportation for easier access.</p>
                </div>
                
                <div class="card">
                    <h4>❓ What should I do if I lose something at the event?</h4>
                    <p>Report lost items immediately to our volunteer coordinators at the information desk or call our helpline. We maintain a lost and found service throughout the festival.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- JavaScript for Contact Form -->
    <script>
        function submitForm(event) {
            event.preventDefault();
            
            // Get form data
            const formData = new FormData(event.target);
            const name = event.target.querySelector('input[type="text"]').value;
            const email = event.target.querySelector('input[type="email"]').value;
            const subject = event.target.querySelector('select').value;
            
            // Simulate form submission
            alert(`Thank you ${name}! Your message has been sent successfully. We'll respond to ${email} within 24 hours regarding your ${subject} inquiry.`);
            
            // Reset form
            event.target.reset();
        }

        // Add smooth scrolling to anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    </script>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Contact Info</h3>
                    <p>📍 Juhu Beach, Mumbai</p>
                    <p>📞 +91 98765 43210</p>
                    <p>✉️ info@chhathutsav.org</p>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <p><a href="about-us.html">About Our Organization</a></p>
                    <p><a href="about-chhath.html">About Chhath Puja</a></p>
                    <p><a href="events.html">Upcoming Events</a></p>
                    <p><a href="gallery.html">Photo Gallery</a></p>
                </div>
                <div class="footer-section">
                    <h3>Get Involved</h3>
                    <p><a href="#">Volunteer With Us</a></p>
                    <p><a href="donate.html">Make a Donation</a></p>
                    <p><a href="#">Join Newsletter</a></p>
                    <p><a href="#">Share Our Mission</a></p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Chhath Utsav Mahasangh. Serving devotion, culture & community since 1993.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

# Save the Contact page
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("Created contact.html")