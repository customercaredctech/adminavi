import os
import re

files_to_update = ['blog.html', 'blog-sds-visa.html', 'blog-canada-permit.html']

header_replacement = """  <!-- ════════ HEADER ════════ -->
  <header class="header">
    <div class="container header-wrap">
      <a href="index.html" class="logo">
        <img src="assets/logo.jpg" alt="Admission Navigate Consultancy">
      </a>
      
      <nav class="nav">
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="study-canada.html">Study in Canada</a></li>
          <li><a href="colleges.html">Colleges</a></li>
          <li><a href="blog.html" class="active">Resources</a></li>
        </ul>
      </nav>
      
      <a href="book-consultation.html" class="btn btn-navy">Book Consultation</a>
      
      <button class="mobile-toggle" id="menuBtn">
        <i class="fas fa-bars"></i>
      </button>
    </div>
  </header>

  <!-- Mobile Menu -->
  <div class="mobile-menu" id="mobileMenu">
    <a href="index.html">Home</a>
    <a href="about.html">About Us</a>
    <a href="services.html">Services</a>
    <a href="study-canada.html">Study in Canada</a>
    <a href="colleges.html">Colleges</a>
    <a href="blog.html">Resources</a>
    <a href="book-consultation.html" class="btn btn-navy" style="text-align: center;">Book Consultation</a>
  </div>"""

footer_replacement = """  <!-- ════════ FOOTER ════════ -->
  <footer class="footer">
    <div class="container">
      <div class="foot-grid">
        <div class="foot-brand">
          <img src="assets/logo.jpg" alt="Admission Navigate Consultancy Logo">
          <p>Admission Navigate Consultancy is your trusted partner for navigating college and university admissions across Canada.</p>
          <div class="socials">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
          </div>
        </div>
        
        <div class="foot-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="study-canada.html">Study in Canada</a></li>
            <li><a href="colleges.html">Partner Colleges</a></li>
          </ul>
        </div>
        
        <div class="foot-col">
          <h4>Contact Us</h4>
          <ul>
            <li><i class="fas fa-map-marker-alt"></i> 123 Education Blvd, Suite 400</li>
            <li><i class="fas fa-envelope"></i> info@admissionnavigate.com</li>
            <li><i class="fas fa-phone"></i> +1 (778) 889-7490</li>
          </ul>
        </div>
        
        <div class="foot-col">
          <h4>Newsletter</h4>
          <p style="font-size: 0.9rem; color: rgba(255,255,255,0.7); margin-bottom: 0;">Get the latest updates on Canadian intakes and visa rules.</p>
          <form class="nl-form" onsubmit="event.preventDefault(); alert('Subscribed!');">
            <input type="email" placeholder="Email Address" required>
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>
      
      <div class="foot-disclaimer">
        <strong>Disclaimer:</strong> Admission Navigate Consultancy provides educational consulting and admission guidance services for institutions across Canada. We do not guarantee admission decisions. Any immigration-related information is general only and is not legal or regulated immigration advice.
      </div>
      
      <div class="foot-bottom">
        <div>&copy; <span id="year"></span> Admission Navigate Consultancy. All rights reserved. Designed and developed by dctechoffial <a href="https://www.instagram.com" target="_blank" style="margin-left:10px; color:var(--c-gold);"><i class="fab fa-instagram"></i></a></div>
        <div class="foot-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms & Conditions</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- WhatsApp Button -->
  <a href="https://wa.me/17788897490" target="_blank" class="wa-btn" title="Chat on WhatsApp">
    <i class="fab fa-whatsapp"></i>
  </a>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('active'));
    }
  </script>
</body>
</html>"""

for file in files_to_update:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header block (everything from <header... to </header>)
    # But some have <!-- Header Navigation -->, so we regex from <!-- Header Navigation --> up to </header>
    # Actually the blog pages have:
    # <header class="header"> ... </header>
    # Let's match from <header class="header"> to </header>
    content = re.sub(r'<!-- Header Navigation -->\s*<header class="header">.*?</header>', header_replacement, content, flags=re.DOTALL)
    
    # In some pages, they might not have <!-- Header Navigation -->, just <header class="header">
    if header_replacement not in content:
        content = re.sub(r'<header class="header">.*?</header>', header_replacement, content, flags=re.DOTALL)

    # Replace footer block (everything from <!-- Footer --> to </html>)
    # The blog pages have <footer class="footer"> ... </footer> ... </body> </html>
    content = re.sub(r'<!-- Footer -->\s*<footer class="footer">.*?</html>', footer_replacement, content, flags=re.DOTALL)

    if footer_replacement not in content:
        content = re.sub(r'<footer class="footer">.*?</html>', footer_replacement, content, flags=re.DOTALL)

    # Remove main.js script tag since mobile menu script is now inline
    content = re.sub(r'<script src="main.js"></script>', '', content)

    # Change buttons to use new design system classes
    # e.g. btn-secondary -> btn-navy, btn-accent -> btn-gold
    content = content.replace('btn-secondary', 'btn-navy')
    content = content.replace('btn-accent', 'btn-gold')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
