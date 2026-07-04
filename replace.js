const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const oldFooter1 = '<div>&copy; <span id="year"></span> Admission Navigate Consultancy. All rights reserved.</div>';
const newFooter1 = '<div>&copy; <span id="year"></span> Admission Navigate Consultancy. All rights reserved. Designed and developed by dctechoffial <a href="https://www.instagram.com" target="_blank" style="margin-left:10px; color:var(--c-gold);"><i class="fab fa-instagram"></i></a></div>';

const oldFooter2 = '<p>&copy; <span id="footerYear"></span> AdmissionNavigator. All rights reserved. &nbsp;|&nbsp; Designed by <a href="#" style="color: var(--accent); opacity:1; font-weight:600;">DCTechOfficial</a></p>';
const newFooter2 = '<p>&copy; <span id="footerYear"></span> AdmissionNavigator. All rights reserved. Designed and developed by dctechoffial <a href="https://www.instagram.com" target="_blank" style="margin-left:10px; color:var(--c-gold);"><i class="fab fa-instagram"></i></a></p>';

for (const file of files) {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    let changed = false;

    if (content.includes(oldFooter1)) {
        content = content.replace(oldFooter1, newFooter1);
        changed = true;
    }
    if (content.includes(oldFooter2)) {
        content = content.replace(oldFooter2, newFooter2);
        changed = true;
    }

    if (changed) {
        fs.writeFileSync(filePath, content);
        console.log(`Updated footer in ${file}`);
    }
}
