const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('rupa_sangaha.html', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously" });
setTimeout(() => {
    try {
        const tbody = dom.window.document.getElementById('rupa-matrix-tbody');
        console.log("Tbody HTML length:", tbody.innerHTML.length);
        console.log(tbody.innerHTML.substring(0, 300));
    } catch(e) {
        console.error(e);
    }
}, 500);
