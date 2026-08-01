const fs = require('fs');
const html = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');
const { JSDOM } = require('jsdom');
const dom = new JSDOM(html);
const document = dom.window.document;

const listView = document.getElementById('citta-list-view');
const gridView = document.getElementById('citta-grid-view');

if (listView && gridView) {
    console.log("listView exists.");
    console.log("gridView exists.");
    console.log("Is gridView a child of listView?", listView.contains(gridView));
    console.log("gridView parent:", gridView.parentElement.id);
    console.log("listView parent:", listView.parentElement.id);
} else {
    console.log("One of them is missing.");
}
