const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", (err) => {
  console.error("JSDOM Error:", err);
});
virtualConsole.on("jsdomError", (err) => {
  console.error("JSDOM Internal Error:", err);
});

const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
const window = dom.window;

setTimeout(() => {
    try {
        console.log("Calling toggleCittaView('grid')");
        window.toggleCittaView('grid');
        console.log("Success! Grid view classList:", window.document.getElementById('citta-grid-view').className);
    } catch(e) {
        console.error("Caught Exception:", e);
    }
}, 1000);
