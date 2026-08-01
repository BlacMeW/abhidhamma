const fs = require('fs');
const html = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');
const scripts = html.match(/<script>([\s\S]*?)<\/script>/gi);
if (scripts) {
    scripts.forEach((script, i) => {
        const code = script.replace(/<\/?script>/g, '');
        try {
            new Function(code);
            console.log(`Script ${i} syntax OK`);
        } catch(e) {
            console.error(`Script ${i} syntax ERROR:`, e);
        }
    });
}
