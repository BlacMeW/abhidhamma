const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('glossary.html', 'utf8');

const dom = new JSDOM(html, { url: "http://localhost/", runScripts: "dangerously" });

setTimeout(() => {
    const listEl = dom.window.document.getElementById('glossaryList');
    dom.window.document.querySelector('[data-cat="kammatthana"]').click();
    fs.writeFileSync('dump.html', listEl.innerHTML);
    console.log("Dumped to dump.html");
}, 500);
