# Create About Chhath Puja Page HTML
about_chhath_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Chhath Puja - Chhath Utsav Mahasangh</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
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
                    <li><a href="about-chhath.html" class="active">About Chhath</a></li>
                    <li><a href="events.html">Events</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="donate.html" class="btn btn-secondary">Donate</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>🌅 Chhath Puja</h1>
            <p>The ancient festival dedicated to the Sun God and Chhathi Maiya</p>
        </div>
    </section>

    <!-- Origins Section -->
    <section class="section">
        <div class="container">
            <h2 class="section-title">Origins and History</h2>
            <div class="grid grid-2">
                <div class="card">
                    <h3>Ancient Vedic Roots</h3>
                    <p>Chhath Puja is one of the oldest Hindu festivals, with references found in the Rigveda. The festival is dedicated to the Sun God (Surya) and his consort Usha (Dawn) and Pratyusha (Dusk).</p>
                    <p>Archaeological evidence suggests that the Sun worship traditions date back to the Indus Valley Civilization, making Chhath one of the most ancient forms of worship still practiced today.</p>
                </div>
                <div class="card">
                    <h3>Mythological Significance</h3>
                    <p>According to Hindu mythology, Chhath Puja was first performed by Draupadi and the Pandavas to solve their problems and regain their lost kingdom. The Sun God granted their wishes after they performed the rigorous puja with devotion.</p>
                    <p>Another legend mentions Karna, the warrior from Mahabharata, who was blessed by Surya and gained his legendary powers through Sun worship.</p>
                </div>
            </div>
            
            <div class="card" style="margin-top: 2rem; background: linear-gradient(135deg, rgba(255, 107, 53, 0.1), rgba(247, 147, 30, 0.1));">
                <h3>Historical Evolution</h3>
                <p>Originally practiced in the ancient kingdoms of Magadh (modern-day Bihar), Chhath Puja has evolved over millennia while maintaining its core essence. The festival represents humanity's gratitude toward nature and the life-giving force of the Sun.</p>
                <p>The tradition was carried forward by generations of devotees, particularly from the Bihar and Eastern Uttar Pradesh regions, and has now spread globally wherever these communities have settled.</p>
            </div>
        </div>
    </section>

    <!-- Ritual Steps Section -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">The Four Sacred Days</h2>
            <p class="section-subtitle">Each day of Chhath Puja has specific rituals and significance</p>
            
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="card">
                        <h3>Day 1: Nahay Khay (नहाय खाय)</h3>
                        <h4 style="color: var(--primary-color); margin-bottom: 1rem;">Purification and Preparation</h4>
                        <ul style="padding-left: 1.5rem;">
                            <li><strong>Holy Bath:</strong> Devotees take a purifying bath in holy water (river, sea, or clean pond)</li>
                            <li><strong>Clean Home:</strong> Houses are thoroughly cleaned and purified</li>
                            <li><strong>Sattvic Food:</strong> Only pure vegetarian food is consumed, typically chana dal, rice, and pumpkin</li>
                            <li><strong>Fasting Begins:</strong> The vratika (person observing fast) begins the sacred journey</li>
                        </ul>
                        <p style="margin-top: 1rem; font-style: italic;">This day symbolizes purification of body, mind, and soul before approaching the Sun God.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="card">
                        <h3>Day 2: Kharna (खरना)</h3>
                        <h4 style="color: var(--primary-color); margin-bottom: 1rem;">Day-long Fast and Evening Prasad</h4>
                        <ul style="padding-left: 1.5rem;">
                            <li><strong>Nirjala Fast:</strong> Complete fast without water from sunrise to sunset</li>
                            <li><strong>Evening Preparation:</strong> Preparation of kheer (rice pudding) with jaggery</li>
                            <li><strong>Moon Worship:</strong> Offering prayers to the moon after sunset</li>
                            <li><strong>Prasad Distribution:</strong> Sharing kheer and rotis with family and community</li>
                        </ul>
                        <p style="margin-top: 1rem; font-style: italic;">This day tests the devotee's determination and strengthens their spiritual resolve.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="card">
                        <h3>Day 3: Sandhya Arghya (संध्या अर्घ्य)</h3>
                        <h4 style="color: var(--primary-color); margin-bottom: 1rem;">Evening Offering to Setting Sun</h4>
                        <ul style="padding-left: 1.5rem;">
                            <li><strong>Preparation of Offerings:</strong> Making thekua, fruits, and other prasad items</li>
                            <li><strong>Ghat Decoration:</strong> Preparing the riverbank or seashore with diyas and rangoli</li>
                            <li><strong>Standing in Water:</strong> Devotees stand in water holding bamboo baskets of offerings</li>
                            <li><strong>Sunset Prayers:</strong> Offering arghya (water offerings) to the setting sun</li>
                            <li><strong>Overnight Vigil:</strong> Maintaining fast and staying awake through the night</li>
                        </ul>
                        <p style="margin-top: 1rem; font-style: italic;">The most visually spectacular day, symbolizing gratitude for the day's blessings.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="card">
                        <h3>Day 4: Usha Arghya (उषा अर्घ्य)</h3>
                        <h4 style="color: var(--primary-color); margin-bottom: 1rem;">Dawn Offering to Rising Sun</h4>
                        <ul style="padding-left: 1.5rem;">
                            <li><strong>Pre-dawn Gathering:</strong> Devotees gather at water bodies before sunrise</li>
                            <li><strong>Dawn Prayers:</strong> Offering arghya to the rising sun</li>
                            <li><strong>Final Offerings:</strong> Last prayers and offerings to Chhathi Maiya</li>
                            <li><strong>Prasad Distribution:</strong> Sharing blessed food with all devotees</li>
                            <li><strong>Fast Completion:</strong> Breaking the 36-hour fast with prasad</li>
                        </ul>
                        <p style="margin-top: 1rem; font-style: italic;">The culmination of the festival, welcoming new beginnings and divine blessings.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Cultural Significance Section -->
    <section class="section">
        <div class="container">
            <h2 class="section-title">Cultural and Spiritual Significance</h2>
            <div class="grid grid-3">
                <div class="card">
                    <h3>🌞 Sun Worship</h3>
                    <p>Chhath Puja is unique as it worships the Sun God directly, recognizing the sun as the source of all life and energy. This reflects ancient understanding of solar energy's importance for life on Earth.</p>
                </div>
                
                <div class="card">
                    <h3>🙏 Gender Equality</h3>
                    <p>The festival demonstrates remarkable gender inclusivity, with both men and women performing the same rigorous rituals. It's one of the few Hindu festivals where male participation in fasting is common and celebrated.</p>
                </div>
                
                <div class="card">
                    <h3>🌱 Environmental Harmony</h3>
                    <p>The festival promotes environmental consciousness through natural offerings, worship near water bodies, and the use of biodegradable materials like bamboo baskets and clay lamps.</p>
                </div>
                
                <div class="card">
                    <h3>👨‍👩‍👧‍👦 Family Unity</h3>
                    <p>Chhath Puja strengthens family bonds as entire families participate together, with different generations contributing to preparations and rituals, fostering cultural continuity.</p>
                </div>
                
                <div class="card">
                    <h3>🧘 Spiritual Discipline</h3>
                    <p>The rigorous fasting and ritual observances develop spiritual discipline, mental strength, and the ability to endure hardships for higher purposes.</p>
                </div>
                
                <div class="card">
                    <h3>🤝 Community Bonding</h3>
                    <p>The festival brings communities together, transcending social and economic barriers. Collective celebrations foster unity and mutual support among devotees.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Regional Observances Section -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">Regional Observances</h2>
            <div class="grid grid-2">
                <div class="card">
                    <h3>Bihar and Jharkhand</h3>
                    <p><strong>Primary Region:</strong> The heartland of Chhath Puja where traditions are most authentic and elaborate.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.5rem;">
                        <li>Celebrated with grand community gatherings at river ghats</li>
                        <li>Traditional folk songs (Chhath Geet) are sung throughout</li>
                        <li>Elaborate preparation of traditional sweets and offerings</li>
                        <li>Government declares public holidays for the festival</li>
                    </ul>
                </div>
                
                <div class="card">
                    <h3>Mumbai and Delhi</h3>
                    <p><strong>Diaspora Celebrations:</strong> Large migrant communities maintain traditions with adaptations.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.5rem;">
                        <li>Celebrated at beaches, lakes, and artificial ponds</li>
                        <li>Community organizations facilitate group celebrations</li>
                        <li>Cultural programs and awareness workshops</li>
                        <li>Emphasis on environmental sustainability</li>
                    </ul>
                </div>
                
                <div class="card">
                    <h3>International Observances</h3>
                    <p><strong>Global Reach:</strong> Celebrated by Indian diaspora worldwide.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.5rem;">
                        <li>USA, Canada, UK, Australia, Nepal, and Mauritius</li>
                        <li>Adapted to local conditions and regulations</li>
                        <li>Focus on cultural preservation and education</li>
                        <li>Inter-community celebrations with local participation</li>
                    </ul>
                </div>
                
                <div class="card">
                    <h3>Modern Adaptations</h3>
                    <p><strong>Contemporary Practices:</strong> Balancing tradition with modern realities.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.5rem;">
                        <li>Use of social media for community coordination</li>
                        <li>Live streaming for distant family members</li>
                        <li>Eco-friendly innovations in ritual materials</li>
                        <li>Health considerations in fasting practices</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action Section -->
    <section class="section">
        <div class="container">
            <div class="card" style="text-align: center; background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); color: white;">
                <h2>Experience the Sacred Festival</h2>
                <p style="font-size: 1.2rem; margin-bottom: 2rem;">Join us in celebrating this ancient tradition and discover the spiritual depth of Chhath Puja</p>
                <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2rem;">
                    <a href="events.html" class="btn" style="background: white; color: var(--primary-color);">🎯 Attend Puja</a>
                    <a href="contact.html" class="btn btn-secondary">📚 Join a Workshop</a>
                </div>
                
                <div class="grid grid-3" style="margin-top: 2rem; text-align: left;">
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: var(--border-radius);">
                        <h4>🎓 Cultural Workshops</h4>
                        <p>Learn about the rituals, songs, and significance of each ceremony from experienced practitioners.</p>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: var(--border-radius);">
                        <h4>🤝 Community Participation</h4>
                        <p>Experience the festival with thousands of devotees in a safe, organized, and spiritually enriching environment.</p>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: var(--border-radius);">
                        <h4>🌱 Eco-Friendly Celebration</h4>
                        <p>Participate in our sustainable practices while maintaining the sanctity and authenticity of traditions.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

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
                    <p><a href="events.html">Upcoming Events</a></p>
                    <p><a href="gallery.html">Photo Gallery</a></p>
                    <p><a href="blog.html">Latest News</a></p>
                </div>
                <div class="footer-section">
                    <h3>Get Involved</h3>
                    <p><a href="contact.html">Volunteer With Us</a></p>
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

# Save the About Chhath page
with open('about-chhath.html', 'w', encoding='utf-8') as f:
    f.write(about_chhath_html)

print("Created about-chhath.html")