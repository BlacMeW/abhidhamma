const fs = require('fs');
let content = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');

const regex = /            <!-- Citta Grid View -->/;
if (regex.test(content)) {
    content = content.replace(regex, '            </div>\n\n            <!-- Citta Grid View -->');
    fs.writeFileSync('citta_cetasikas_visual_guide.html', content, 'utf8');
    console.log("Successfully added closing div!");
} else {
    console.log("Could not find comment");
}
