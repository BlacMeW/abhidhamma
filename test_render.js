const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('glossary.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("jsdomError", (error) => {
  console.error("JSDOM Error:", error.message, error.detail);
});
virtualConsole.on("error", (error) => {
  console.error("Console Error:", error);
});

const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
setTimeout(() => {
    console.log("GlossaryList HTML length:", dom.window.document.getElementById('glossaryList').innerHTML.length);
    console.log("Count element:", dom.window.document.getElementById('resultCount').textContent);
}, 1000);
