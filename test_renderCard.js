const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('glossary.html', 'utf8');

// Use virtual console to catch errors
const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("jsdomError", (error) => {
  console.error("JSDOM Error:", error);
});
virtualConsole.on("error", (error) => {
  console.error("Console Error:", error);
});
virtualConsole.on("warn", (warn) => {
  console.warn("Console Warn:", warn);
});
virtualConsole.on("log", (log) => {
  console.log("Console Log:", log);
});

const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });

setTimeout(() => {
    const listEl = dom.window.document.getElementById('glossaryList');
    console.log("GlossaryList content length:", listEl.innerHTML.length);
    
    // Simulate Kammatthana click
    dom.window.document.querySelector('[data-cat="kammatthana"]').click();
    console.log("GlossaryList content length after click:", listEl.innerHTML.length);
    if(listEl.innerHTML.length < 100) {
        console.log("HTML:", listEl.innerHTML);
    }
}, 500);
