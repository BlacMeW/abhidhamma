const fs = require('fs');

const dir = '.';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace the old text with the new text
    const oldText = 'မောင်ဝဏ္ဏကို အားရည်စူးသော ဓမ္မဒါန တရားအလှူ';
    const oldText2 = 'မောင်ဝဏ္ဏကို (၀၅ ) အားရည်စူးသော ဓမ္မဒါန တရားအလှူ';
    const newText = 'မောင်ဝဏ္ဏကို (၀၅ ဇွန် ၂၀၁၀ - ၁၂ နိုဝင်ဘာ ၂၀၂၄) အားရည်စူးသော ဓမ္မဒါန တရားအလှူ';
    
    if (content.includes(oldText)) {
        content = content.replace(new RegExp(oldText, 'g'), newText);
        fs.writeFileSync(file, content);
        console.log('Updated footer in ' + file);
    } else if (content.includes(oldText2)) {
        content = content.replace(new RegExp(oldText2, 'g'), newText);
        fs.writeFileSync(file, content);
        console.log('Updated footer in ' + file);
    }
});
