# Create Blog Page HTML with Articles and Category Filters
blog_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - Chhath Utsav Mahasangh</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .blog-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .blog-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        
        .blog-meta {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            color: var(--text-light);
        }
        
        .blog-category {
            background: var(--primary-color);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        
        .blog-excerpt {
            color: var(--text-light);
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        
        .read-more {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        
        .read-more:hover {
            color: var(--secondary-color);
        }
        
        .featured-post {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: var(--border-radius);
            padding: 3rem;
            margin-bottom: 3rem;
            text-align: center;
        }
        
        .search-box {
            position: relative;
            max-width: 400px;
            margin: 0 auto 2rem;
        }
        
        .search-input {
            width: 100%;
            padding: 12px 45px 12px 15px;
            border: 2px solid #e2e8f0;
            border-radius: var(--border-radius);
            font-size: 1rem;
        }
        
        .search-btn {
            position: absolute;
            right: 5px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--primary-color);
            border: none;
            color: white;
            padding: 8px 12px;
            border-radius: var(--border-radius);
            cursor: pointer;
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
                    <li><a href="blog.html" class="active">Blog</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="donate.html" class="btn btn-secondary">Donate</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>📝 Stories & News</h1>
            <p>Read about our community, traditions, and the impact we're making together</p>
        </div>
    </section>

    <!-- Search and Filters -->
    <section class="section" style="padding-top: 2rem; padding-bottom: 1rem;">
        <div class="container">
            <!-- Search Box -->
            <div class="search-box">
                <input type="text" class="search-input" placeholder="Search articles..." id="searchInput">
                <button class="search-btn" onclick="searchArticles()">🔍</button>
            </div>
            
            <!-- Category Filters -->
            <div class="filters">
                <button class="filter-btn active" data-category="all">All Posts</button>
                <button class="filter-btn" data-category="traditions">🪔 Traditions</button>
                <button class="filter-btn" data-category="community">👥 Community</button>
                <button class="filter-btn" data-category="environment">🌱 Environment</button>
                <button class="filter-btn" data-category="coverage">📰 Media Coverage</button>
                <button class="filter-btn" data-category="volunteers">🤝 Volunteers</button>
                <button class="filter-btn" data-category="education">📚 Education</button>
            </div>
        </div>
    </section>

    <!-- Featured Post -->
    <section class="section" style="padding-top: 0;">
        <div class="container">
            <div class="featured-post">
                <span class="blog-category" style="background: rgba(255, 255, 255, 0.2);">Featured</span>
                <h2 style="margin: 1rem 0;">Chhath Puja 2024: A Record-Breaking Celebration</h2>
                <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem;">This year's Chhath Puja saw the highest participation in our 30-year history, with over 50,000 devotees joining us at Juhu Beach. Read about the beautiful moments, the challenges we overcame, and the incredible community spirit that made it all possible.</p>
                <a href="#" class="btn" style="background: white; color: var(--primary-color);">Read Full Story</a>
            </div>
        </div>
    </section>

    <!-- Blog Posts Grid -->
    <section class="section" style="padding-top: 0;">
        <div class="container">
            <div class="grid grid-2" id="blogGrid">
                
                <!-- Traditions Category -->
                <article class="blog-card card" data-category="traditions" data-title="significance thekua prasad chhath puja">
                    <span class="blog-category">Traditions</span>
                    <h3>The Significance of 'Thekua' in Chhath Puja</h3>
                    <div class="blog-meta">
                        <span>📅 October 15, 2024</span>
                        <span>👤 Radha Devi</span>
                        <span>📖 5 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Thekua, the traditional sweet offering, holds deep spiritual significance in Chhath Puja. Made with jaggery, wheat flour, and ghee, this prasad represents purity and devotion. Learn about the ritualistic preparation methods passed down through generations and why this simple sweet is considered the most sacred offering to Chhathi Maiya.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="community" data-title="call volunteers join us year">
                    <span class="blog-category">Community</span>
                    <h3>A Call for Volunteers: Join Us This Year</h3>
                    <div class="blog-meta">
                        <span>📅 September 28, 2024</span>
                        <span>👤 Ashok Singh</span>
                        <span>📖 3 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Our annual Chhath Puja celebration is made possible by hundreds of dedicated volunteers. From ghat preparation to devotee assistance, crowd management to prasad distribution - every role is crucial. Discover how you can contribute your time and skills to make this year's celebration memorable and safe for all.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="environment" data-title="commitment greener chhath sustainable celebration">
                    <span class="blog-category">Environment</span>
                    <h3>Our Commitment to a Greener Chhath</h3>
                    <div class="blog-meta">
                        <span>📅 September 10, 2024</span>
                        <span>👤 Environmental Team</span>
                        <span>📖 4 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Discover the steps we're taking to ensure our celebrations are eco-friendly and sustainable. From biodegradable offerings to waste management, solar-powered lighting to beach cleanup drives - learn how we're preserving traditions while protecting our environment for future generations.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="coverage" data-title="mumbai media highlights chhath celebrations">
                    <span class="blog-category">Media Coverage</span>
                    <h3>Mumbai Media Highlights Our Chhath Celebrations</h3>
                    <div class="blog-meta">
                        <span>📅 November 12, 2024</span>
                        <span>👤 Media Relations</span>
                        <span>📖 2 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Major Mumbai newspapers and television channels featured our Chhath Puja celebrations, highlighting the cultural significance and community participation. Times of India, Mumbai Mirror, and Zee News covered the grand celebration at Juhu Beach, showcasing the beautiful traditions maintained by the Bihari community.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="volunteers" data-title="spotlight heroes behind scenes volunteers">
                    <span class="blog-category">Volunteers</span>
                    <h3>Spotlight on the Heroes Behind the Scenes</h3>
                    <div class="blog-meta">
                        <span>📅 November 8, 2024</span>
                        <span>👤 Volunteer Coordinator</span>
                        <span>📖 6 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Meet the incredible volunteers who work tirelessly to make Chhath Puja possible. From the early morning ghat decorators to the late-night cleanup crew, these unsung heroes ensure every devotee has a safe and spiritual experience. Read their inspiring stories and dedication to community service.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="traditions" data-title="ancient rituals modern times preserving authenticity">
                    <span class="blog-category">Traditions</span>
                    <h3>Ancient Rituals in Modern Times: Preserving Authenticity</h3>
                    <div class="blog-meta">
                        <span>📅 October 25, 2024</span>
                        <span>👤 Cultural Committee</span>
                        <span>📖 7 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        How do we maintain the authenticity of 2,000-year-old rituals in a bustling metropolis like Mumbai? Explore the challenges and solutions in preserving traditional practices while adapting to urban settings. Learn about the careful balance between honoring ancient customs and meeting modern safety requirements.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="education" data-title="teaching children chhath traditions cultural workshops">
                    <span class="blog-category">Education</span>
                    <h3>Teaching Children About Chhath: Cultural Workshops</h3>
                    <div class="blog-meta">
                        <span>📅 October 20, 2024</span>
                        <span>👤 Education Team</span>
                        <span>📖 4 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Our special children's workshops teach young minds about the significance of Chhath Puja through interactive activities, storytelling, and hands-on learning. Discover how we're ensuring cultural knowledge passes to the next generation while making learning fun and engaging for kids aged 5-15.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="community" data-title="mumbai police support ensuring safe celebrations">
                    <span class="blog-category">Community</span>
                    <h3>Mumbai Police Support: Ensuring Safe Celebrations</h3>
                    <div class="blog-meta">
                        <span>📅 November 5, 2024</span>
                        <span>👤 Safety Committee</span>
                        <span>📖 3 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        The Mumbai Police's exemplary support ensures our Chhath celebrations remain safe and orderly. Learn about the comprehensive security arrangements, traffic management, and emergency response protocols that protect thousands of devotees during the four-day festival.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="environment" data-title="plastic free chhath success story environmental impact">
                    <span class="blog-category">Environment</span>
                    <h3>Plastic-Free Chhath: A Success Story</h3>
                    <div class="blog-meta">
                        <span>📅 November 15, 2024</span>
                        <span>👤 Green Team</span>
                        <span>📖 5 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Our five-year journey to eliminate single-use plastics from Chhath celebrations has been a remarkable success. Read about the innovative alternatives we've introduced, community cooperation, and the positive environmental impact of our plastic-free initiative.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="coverage" data-title="international recognition chhath mumbai global media">
                    <span class="blog-category">Media Coverage</span>
                    <h3>International Recognition: Chhath Mumbai Goes Global</h3>
                    <div class="blog-meta">
                        <span>📅 November 18, 2024</span>
                        <span>👤 Communications Team</span>
                        <span>📖 3 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Our Chhath celebrations at Juhu Beach gained international attention, with BBC, Reuters, and international Indian media covering the festival. The global coverage highlighted the cultural diversity of Mumbai and the significance of preserving traditions in diaspora communities.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="volunteers" data-title="medical team volunteers health safety devotees">
                    <span class="blog-category">Volunteers</span>
                    <h3>Medical Team Volunteers: Guardians of Health</h3>
                    <div class="blog-meta">
                        <span>📅 November 10, 2024</span>
                        <span>👤 Medical Coordinator</span>
                        <span>📖 4 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Meet our dedicated medical volunteers who ensure the health and safety of devotees during the demanding four-day fast and rituals. From providing first aid to managing emergency situations, these healthcare heroes work round the clock to keep our community safe.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

                <article class="blog-card card" data-category="education" data-title="chhath puja myths facts educational series">
                    <span class="blog-category">Education</span>
                    <h3>Chhath Puja: Myths vs Facts - Educational Series</h3>
                    <div class="blog-meta">
                        <span>📅 October 30, 2024</span>
                        <span>👤 Research Team</span>
                        <span>📖 8 min read</span>
                    </div>
                    <p class="blog-excerpt">
                        Our comprehensive educational series addresses common misconceptions about Chhath Puja while explaining the scientific and spiritual significance of the rituals. Discover the astronomical connections, health benefits of fasting, and the psychological impact of community worship.
                    </p>
                    <a href="#" class="read-more">Read More →</a>
                </article>

            </div>

            <!-- Load More Button -->
            <div style="text-align: center; margin-top: 3rem;">
                <button class="btn btn-primary" onclick="loadMorePosts()">Load More Articles</button>
            </div>
        </div>
    </section>

    <!-- Newsletter Signup -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container">
            <div class="card" style="text-align: center; background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); color: white;">
                <h2>📧 Subscribe to Our Newsletter</h2>
                <p style="font-size: 1.1rem; margin-bottom: 2rem;">Stay updated with the latest stories, events, and community news</p>
                <form style="max-width: 400px; margin: 0 auto;" onsubmit="subscribeNewsletter(event)">
                    <div style="display: flex; gap: 0.5rem;">
                        <input type="email" placeholder="Enter your email" style="flex: 1; padding: 12px; border: none; border-radius: var(--border-radius);" required>
                        <button type="submit" class="btn" style="background: white; color: var(--primary-color);">Subscribe</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <!-- JavaScript for Blog Functionality -->
    <script>
        // Filter functionality
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all buttons
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                // Add active class to clicked button
                btn.classList.add('active');
                
                const category = btn.dataset.category;
                const articles = document.querySelectorAll('.blog-card');
                
                articles.forEach(article => {
                    if (category === 'all' || article.dataset.category === category) {
                        article.style.display = 'block';
                    } else {
                        article.style.display = 'none';
                    }
                });
            });
        });

        // Search functionality
        function searchArticles() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const articles = document.querySelectorAll('.blog-card');
            
            articles.forEach(article => {
                const title = article.querySelector('h3').textContent.toLowerCase();
                const excerpt = article.querySelector('.blog-excerpt').textContent.toLowerCase();
                const searchData = article.dataset.title || '';
                
                if (title.includes(searchTerm) || excerpt.includes(searchTerm) || searchData.includes(searchTerm)) {
                    article.style.display = 'block';
                } else {
                    article.style.display = 'none';
                }
            });
        }

        // Real-time search
        document.getElementById('searchInput').addEventListener('input', searchArticles);

        // Load more posts
        function loadMorePosts() {
            alert('Loading more articles... (This would fetch additional posts from the server)');
        }

        // Newsletter subscription
        function subscribeNewsletter(event) {
            event.preventDefault();
            const email = event.target.querySelector('input[type="email"]').value;
            alert(`Thank you for subscribing with email: ${email}. You'll receive our latest updates!`);
            event.target.reset();
        }
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

# Save the Blog page
with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_html)

print("Created blog.html")