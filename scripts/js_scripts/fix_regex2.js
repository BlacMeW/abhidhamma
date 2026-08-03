const fs = require('fs');
let html = fs.readFileSync('missaka_sangaha.html', 'utf8');

// The string we want to search for and replace
const searchFor = "${item.desc.replace(/<b>.*?<\\\\/b>\\\\s*-\\\\s*/, '')}";
const replaceWith = "${item.desc.replace(/<b>.*?<\\/b>\\s*-\\s*/, '')}";

html = html.replace(searchFor, replaceWith);

fs.writeFileSync('missaka_sangaha.html', html);
