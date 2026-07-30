const fs = require('fs');
const content = fs.readFileSync('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/paccaya_sangaha.html', 'utf8');
const scriptMatch = content.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
    try {
        const { Script } = require('vm');
        new Script(scriptMatch[1]);
        console.log("Syntax OK");
    } catch (e) {
        console.error("Syntax Error:", e);
    }
}
