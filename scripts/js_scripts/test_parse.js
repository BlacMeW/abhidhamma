const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('glossary.html', 'utf8');

const dom = new JSDOM(html);
const document = dom.window.document;

console.log("Parents of glossaryList:");
let el = document.getElementById('glossaryList');
while(el) {
    console.log(el.tagName, el.className);
    el = el.parentElement;
}
