# Create Donation Page HTML with Payment Options and Transparency
donate_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate - Chhath Utsav Mahasangh</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .donation-amounts {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .amount-btn {
            padding: 1rem;
            border: 2px solid var(--primary-color);
            background: white;
            color: var(--primary-color);
            border-radius: var(--border-radius);
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            text-align: center;
        }
        
        .amount-btn.active,
        .amount-btn:hover {
            background: var(--primary-color);
            color: white;
        }
        
        .payment-option {
            border: 2px solid #e2e8f0;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .payment-option:hover,
        .payment-option.selected {
            border-color: var(--primary-color);
            background: rgba(255, 107, 53, 0.05);
        }
        
        .payment-method {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .payment-icon {
            width: 50px;
            height: 50px;
            background: var(--bg-light);
            border-radius: var(--border-radius);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }
        
        .impact-card {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: var(--border-radius);
            padding: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .security-badge {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: #10b981;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        
        .transparency-chart {
            background: white;
            border-radius: var(--border-radius);
            padding: 2rem;
            box-shadow: var(--shadow);
        }
        
        .expense-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .expense-bar {
            width: 100%;
            height: 8px;
            background: #e2e8f0;
            border-radius: 4px;
            margin-top: 0.5rem;
            overflow: hidden;
        }
        
        .expense-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }
        
        .qr-code {
            width: 200px;
            height: 200px;
            background: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: var(--border-radius);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1rem;
            font-size: 3rem;
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
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="donate.html" class="active btn btn-secondary">Donate</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>🤲 Support Our Mission</h1>
            <p>Help us preserve traditions and serve the community with your generous contribution</p>
        </div>
    </section>

    <!-- Impact Section -->
    <section class="section" style="padding-top: 2rem;">
        <div class="container">
            <div class="impact-card">
                <h2>Your Donation Makes a Real Difference</h2>
                <p style="font-size: 1.1rem; margin-bottom: 2rem;">Every contribution helps us create safer, more inclusive, and environmentally conscious celebrations</p>
                <div class="grid grid-3" style="text-align: left;">
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: var(--border-radius);">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏗️</div>
                        <h4>Infrastructure</h4>
                        <p>Safe ghat construction, lighting, and facilities for devotees</p>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: var(--border-radius);">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏥</div>
                        <h4>Safety & Medical</h4>
                        <p>Medical aid stations, security, and emergency response teams</p>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: var(--border-radius);">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌱</div>
                        <h4>Environment</h4>
                        <p>Eco-friendly initiatives and beach cleanup programs</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Donation Form -->
    <section class="section" style="padding-top: 0;">
        <div class="container">
            <div class="grid grid-2">
                <!-- Donation Form -->
                <div class="card">
                    <div class="security-badge">
                        <span>🔒</span>
                        <span>SSL Secured & Bank-Grade Encryption</span>
                    </div>
                    
                    <h3>Make a Donation</h3>
                    
                    <!-- Donation Type -->
                    <div class="form-group">
                        <label class="form-label">Donation Type</label>
                        <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                            <label style="display: flex; align-items: center; gap: 0.5rem;">
                                <input type="radio" name="donationType" value="one-time" checked onchange="updateDonationType()">
                                <span>One-time</span>
                            </label>
                            <label style="display: flex; align-items: center; gap: 0.5rem;">
                                <input type="radio" name="donationType" value="monthly" onchange="updateDonationType()">
                                <span>Monthly</span>
                            </label>
                        </div>
                    </div>
                    
                    <!-- Donation Amounts -->
                    <div class="form-group">
                        <label class="form-label">Select Amount (₹)</label>
                        <div class="donation-amounts">
                            <button class="amount-btn" onclick="selectAmount(500)">₹500</button>
                            <button class="amount-btn" onclick="selectAmount(1000)">₹1,000</button>
                            <button class="amount-btn" onclick="selectAmount(2500)">₹2,500</button>
                            <button class="amount-btn" onclick="selectAmount(5000)">₹5,000</button>
                            <button class="amount-btn" onclick="selectAmount(10000)">₹10,000</button>
                            <button class="amount-btn" onclick="selectAmount('custom')">Custom</button>
                        </div>
                        <input type="number" id="customAmount" class="form-input" placeholder="Enter custom amount" min="100" style="display: none;">
                    </div>
                    
                    <!-- Donor Information -->
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
                        <label class="form-label">PAN Number (for 80G tax exemption)</label>
                        <input type="text" class="form-input" placeholder="AAAAA0000A">
                        <small style="color: var(--text-light);">Required for tax exemption certificate</small>
                    </div>
                    
                    <!-- Purpose -->
                    <div class="form-group">
                        <label class="form-label">Donation Purpose</label>
                        <select class="form-select">
                            <option value="general">General Support</option>
                            <option value="infrastructure">Infrastructure Development</option>
                            <option value="medical">Medical & Safety Services</option>
                            <option value="environment">Environmental Initiatives</option>
                            <option value="cultural">Cultural Programs</option>
                            <option value="emergency">Emergency Fund</option>
                        </select>
                    </div>
                    
                    <!-- Anonymous Donation -->
                    <div class="form-group">
                        <label style="display: flex; align-items: center; gap: 0.5rem;">
                            <input type="checkbox">
                            <span>Make this an anonymous donation</span>
                        </label>
                    </div>
                    
                    <button class="btn btn-primary" style="width: 100%;" onclick="proceedToPayment()">
                        Proceed to Payment
                    </button>
                </div>

                <!-- Payment Methods -->
                <div>
                    <h3 style="margin-bottom: 1.5rem;">Payment Options</h3>
                    
                    <!-- UPI Payment -->
                    <div class="payment-option" onclick="selectPayment('upi')">
                        <div class="payment-method">
                            <div class="payment-icon">📱</div>
                            <div>
                                <h4>UPI Payment</h4>
                                <p>Pay directly using Google Pay, PhonePe, Paytm, or any UPI app</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- QR Code Payment -->
                    <div class="payment-option" onclick="selectPayment('qr')">
                        <div class="payment-method">
                            <div class="payment-icon">📷</div>
                            <div>
                                <h4>QR Code Scan</h4>
                                <p>Scan QR code with your banking app for instant payment</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Credit/Debit Card -->
                    <div class="payment-option" onclick="selectPayment('card')">
                        <div class="payment-method">
                            <div class="payment-icon">💳</div>
                            <div>
                                <h4>Credit/Debit Card</h4>
                                <p>Secure payment with Visa, MasterCard, RuPay cards</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Net Banking -->
                    <div class="payment-option" onclick="selectPayment('netbanking')">
                        <div class="payment-method">
                            <div class="payment-icon">🏦</div>
                            <div>
                                <h4>Net Banking</h4>
                                <p>Direct bank transfer from your online banking account</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- PayPal -->
                    <div class="payment-option" onclick="selectPayment('paypal')">
                        <div class="payment-method">
                            <div class="payment-icon">💙</div>
                            <div>
                                <h4>PayPal</h4>
                                <p>International donors can use PayPal for secure payments</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Bank Transfer -->
                    <div class="payment-option" onclick="selectPayment('transfer')">
                        <div class="payment-method">
                            <div class="payment-icon">🏛️</div>
                            <div>
                                <h4>Direct Bank Transfer</h4>
                                <p>RTGS/NEFT transfer to our bank account</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Quick UPI Section -->
    <section class="section" style="background-color: var(--bg-light); padding-top: 2rem; padding-bottom: 2rem;">
        <div class="container">
            <div class="card" style="text-align: center; max-width: 500px; margin: 0 auto;">
                <h3>Quick UPI Donation</h3>
                <p style="margin-bottom: 2rem;">Scan the QR code below to make an instant donation</p>
                
                <div class="qr-code">
                    📱 QR
                </div>
                
                <p style="font-weight: 600; color: var(--primary-color); margin-bottom: 1rem;">
                    UPI ID: chhathutsav@paytm
                </p>
                
                <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2rem;">
                    <button class="btn btn-primary" onclick="quickDonate(100)">₹100</button>
                    <button class="btn btn-primary" onclick="quickDonate(500)">₹500</button>
                    <button class="btn btn-primary" onclick="quickDonate(1000)">₹1,000</button>
                </div>
                
                <small style="color: var(--text-light);">
                    After payment, please WhatsApp screenshot to +91 98765 43210 for receipt
                </small>
            </div>
        </div>
    </section>

    <!-- Transparency Section -->
    <section class="section">
        <div class="container">
            <h2 class="section-title">Financial Transparency</h2>
            <p class="section-subtitle">See exactly how your donations are utilized</p>
            
            <div class="grid grid-2">
                <!-- Expense Breakdown -->
                <div class="transparency-chart">
                    <h3 style="margin-bottom: 2rem;">Fund Allocation (2023-24)</h3>
                    
                    <div class="expense-item">
                        <div>
                            <h4>Infrastructure & Facilities</h4>
                            <small>Ghat setup, lighting, safety barriers</small>
                        </div>
                        <div style="text-align: right;">
                            <strong>45%</strong>
                        </div>
                    </div>
                    <div class="expense-bar">
                        <div class="expense-fill" style="width: 45%; background: var(--primary-color);"></div>
                    </div>
                    
                    <div class="expense-item">
                        <div>
                            <h4>Medical & Safety Services</h4>
                            <small>First aid, ambulance, security personnel</small>
                        </div>
                        <div style="text-align: right;">
                            <strong>25%</strong>
                        </div>
                    </div>
                    <div class="expense-bar">
                        <div class="expense-fill" style="width: 25%; background: var(--secondary-color);"></div>
                    </div>
                    
                    <div class="expense-item">
                        <div>
                            <h4>Environmental Programs</h4>
                            <small>Cleanup drives, eco-friendly materials</small>
                        </div>
                        <div style="text-align: right;">
                            <strong>15%</strong>
                        </div>
                    </div>
                    <div class="expense-bar">
                        <div class="expense-fill" style="width: 15%; background: #10b981;"></div>
                    </div>
                    
                    <div class="expense-item">
                        <div>
                            <h4>Cultural & Educational</h4>
                            <small>Workshops, cultural programs</small>
                        </div>
                        <div style="text-align: right;">
                            <strong>10%</strong>
                        </div>
                    </div>
                    <div class="expense-bar">
                        <div class="expense-fill" style="width: 10%; background: var(--accent-color);"></div>
                    </div>
                    
                    <div class="expense-item" style="border-bottom: none;">
                        <div>
                            <h4>Administrative Costs</h4>
                            <small>Documentation, communications</small>
                        </div>
                        <div style="text-align: right;">
                            <strong>5%</strong>
                        </div>
                    </div>
                    <div class="expense-bar">
                        <div class="expense-fill" style="width: 5%; background: #6b7280;"></div>
                    </div>
                </div>
                
                <!-- Impact Statistics -->
                <div>
                    <div class="card" style="margin-bottom: 2rem;">
                        <h3>2023-24 Impact Report</h3>
                        <div style="margin-top: 1.5rem;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                                <span>Total Donations Received:</span>
                                <strong>₹42,50,000</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                                <span>Devotees Served:</span>
                                <strong>50,000+</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                                <span>Medical Aids Provided:</span>
                                <strong>1,200+</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                                <span>Volunteers Supported:</span>
                                <strong>500+</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <span>Waste Properly Disposed:</span>
                                <strong>2.5 Tons</strong>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <h3>Recognition & Certifications</h3>
                        <ul style="padding-left: 1.5rem; margin-top: 1rem;">
                            <li>✅ 80G Tax Exemption Certificate</li>
                            <li>✅ FCRA Registration for International Donations</li>
                            <li>✅ Charity Commissioner Registration</li>
                            <li>✅ ISO 9001:2015 Quality Management</li>
                            <li>✅ GuideStar India Seal of Transparency</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Security Notice -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container">
            <div class="card" style="border-left: 4px solid #10b981;">
                <h3>🔒 Security & Privacy Notice</h3>
                <div class="grid grid-2" style="margin-top: 1.5rem;">
                    <div>
                        <h4>Payment Security</h4>
                        <ul style="padding-left: 1.5rem;">
                            <li>SSL 256-bit encryption for all transactions</li>
                            <li>PCI DSS compliant payment processing</li>
                            <li>No storage of payment card information</li>
                            <li>Multi-factor authentication for large donations</li>
                        </ul>
                    </div>
                    <div>
                        <h4>Data Protection</h4>
                        <ul style="padding-left: 1.5rem;">
                            <li>Donor information kept strictly confidential</li>
                            <li>GDPR compliant data handling</li>
                            <li>Option for anonymous donations</li>
                            <li>Secure backup and recovery systems</li>
                        </ul>
                    </div>
                </div>
                <p style="margin-top: 1.5rem; color: var(--text-light);">
                    <strong>Important:</strong> We will never ask for your payment details via phone or email. Always ensure you're on our official website (chhathutsav.org) before making any donation.
                </p>
            </div>
        </div>
    </section>

    <!-- JavaScript for Donation Functionality -->
    <script>
        let selectedAmount = null;
        let selectedPayment = null;

        function selectAmount(amount) {
            // Remove active class from all amount buttons
            document.querySelectorAll('.amount-btn').forEach(btn => btn.classList.remove('active'));
            
            if (amount === 'custom') {
                document.getElementById('customAmount').style.display = 'block';
                document.getElementById('customAmount').focus();
            } else {
                document.getElementById('customAmount').style.display = 'none';
                selectedAmount = amount;
                // Add active class to clicked button
                event.target.classList.add('active');
            }
        }

        function selectPayment(method) {
            // Remove selected class from all payment options
            document.querySelectorAll('.payment-option').forEach(option => option.classList.remove('selected'));
            
            // Add selected class to clicked option
            event.target.closest('.payment-option').classList.add('selected');
            selectedPayment = method;
        }

        function updateDonationType() {
            const type = document.querySelector('input[name="donationType"]:checked').value;
            const amountButtons = document.querySelectorAll('.amount-btn');
            
            // You could update the amounts or messaging based on one-time vs monthly
            console.log('Donation type updated to:', type);
        }

        function proceedToPayment() {
            const form = event.target.closest('.card');
            const formData = new FormData();
            
            // Get amount
            const customAmount = document.getElementById('customAmount');
            const amount = customAmount.style.display !== 'none' ? customAmount.value : selectedAmount;
            
            if (!amount || amount < 100) {
                alert('Please select or enter a valid donation amount (minimum ₹100)');
                return;
            }
            
            // Get form data
            const name = form.querySelector('input[type="text"]').value;
            const email = form.querySelector('input[type="email"]').value;
            
            if (!name || !email) {
                alert('Please fill in all required fields');
                return;
            }
            
            if (!selectedPayment) {
                alert('Please select a payment method');
                return;
            }
            
            // Simulate payment processing
            alert(`Processing donation of ₹${amount} via ${selectedPayment}. You will be redirected to the secure payment gateway.`);
        }

        function quickDonate(amount) {
            alert(`Quick donation of ₹${amount} initiated. Please scan the QR code or use UPI ID: chhathutsav@paytm`);
        }

        // Handle custom amount input
        document.getElementById('customAmount').addEventListener('input', function() {
            selectedAmount = this.value;
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
                    <h3>Legal</h3>
                    <p><a href="#">Terms & Conditions</a></p>
                    <p><a href="#">Privacy Policy</a></p>
                    <p><a href="#">Refund Policy</a></p>
                    <p><a href="#">80G Tax Certificate</a></p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Chhath Utsav Mahasangh. Serving devotion, culture & community since 1993.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

# Save the Donation page
with open('donate.html', 'w', encoding='utf-8') as f:
    f.write(donate_html)

print("Created donate.html")