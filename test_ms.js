const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('missaka_sangaha.html', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously" });
setTimeout(() => {
    try {
        dom.window.openModal('h-lobha');
        console.log(dom.window.document.getElementById('modal-content').innerHTML.substring(0, 500));
    } catch(e) {
        console.error(e);
    }
}, 500);
