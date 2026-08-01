const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously" });
const window = dom.window;

// Wait for DOMContentLoaded equivalent
setTimeout(() => {
    try {
        console.log("cittaData length:", window.cittaData ? window.cittaData.length : "undefined");
        window.toggleCittaView('grid');
        console.log("citta-grid innerHTML length:", window.document.getElementById('citta-grid').innerHTML.length);
        console.log("citta-grid child count:", window.document.getElementById('citta-grid').children.length);
    } catch(e) {
        console.error(e);
    }
}, 1000);
