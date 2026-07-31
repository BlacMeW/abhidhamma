const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('glossary.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously" });

// Wait for a tiny bit to let scripts execute
setTimeout(() => {
    const listEl = dom.window.document.getElementById('glossaryList');
    console.log("GlossaryList content length:", listEl.innerHTML.length);
    console.log("First 200 chars:", listEl.innerHTML.substring(0, 200));
    
    // Check if there were any errors
    const errors = dom.window.document.querySelectorAll('.error');
    console.log("Errors:", errors.length);
}, 500);

