const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('missaka_sangaha.html', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously" });
setTimeout(() => {
    try {
        const tbody = dom.window.document.getElementById('matrix-tbody');
        console.log("Tbody HTML length:", tbody.innerHTML.length);
        console.log(tbody.innerHTML.substring(0, 500));
    } catch(e) {
        console.error(e);
    }
}, 500);
