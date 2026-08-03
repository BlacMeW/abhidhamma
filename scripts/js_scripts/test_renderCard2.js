const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('glossary.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("jsdomError", (error) => { console.error("JSDOM Error:", error); });
virtualConsole.on("error", (error) => { console.error("Console Error:", error); });
virtualConsole.on("warn", (warn) => { console.warn("Console Warn:", warn); });
virtualConsole.on("log", (log) => { console.log("Console Log:", log); });

const dom = new JSDOM(html, { 
    url: "http://localhost/", // Fix localstorage opaque origin
    runScripts: "dangerously", 
    virtualConsole 
});

setTimeout(() => {
    const listEl = dom.window.document.getElementById('glossaryList');
    console.log("GlossaryList HTML length:", listEl.innerHTML.length);
    console.log("GlossaryList text content length:", listEl.textContent.trim().length);
    
    // Simulate Kammatthana click
    dom.window.document.querySelector('[data-cat="kammatthana"]').click();
    console.log("GlossaryList HTML length after click:", listEl.innerHTML.length);
    console.log("Result count text:", dom.window.document.getElementById('resultCount').textContent);
    console.log("First 500 chars of HTML:", listEl.innerHTML.substring(0, 500));
}, 500);
