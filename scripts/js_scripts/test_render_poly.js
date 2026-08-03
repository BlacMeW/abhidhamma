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

const dom = new JSDOM(html, { 
    runScripts: "dangerously", 
    virtualConsole,
    url: "http://localhost/"
});

// Polyfill localStorage BEFORE the script runs. 
// Wait, the script runs immediately. So we need to modify the HTML to inject a mock localStorage first.
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
const jsCode = scriptMatch[1];
const mockDom = new JSDOM('<html><body><div id="resultCount"></div><div id="alphabetIndex"></div><div id="glossaryList"></div><div id="categoryFilters"></div></body></html>', { runScripts: "outside-only" });
const window = mockDom.window;
window.localStorage = {
    getItem: () => null,
    setItem: () => {}
};

try {
    window.eval(jsCode);
    console.log("Evaluated successfully.");
    console.log("GlossaryList HTML length:", window.document.getElementById('glossaryList').innerHTML.length);
} catch (e) {
    console.error("Evaluation error:", e);
}
