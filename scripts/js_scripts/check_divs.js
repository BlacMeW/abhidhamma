const fs = require('fs');
const html = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');
const lines = html.split('\n');
let divCount = 0;
let inListView = false;
for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.includes('<div id="citta-list-view"')) {
        inListView = true;
        console.log(`Found citta-list-view at line ${i+1}`);
    }
    if (inListView) {
        const opens = (line.match(/<div/g) || []).length;
        const closes = (line.match(/<\/div>/g) || []).length;
        divCount += opens - closes;
        if (line.includes('<!-- Citta Grid View -->')) {
            console.log(`At Grid View comment, line ${i+1}, div balance is ${divCount}`);
            break;
        }
    }
}
