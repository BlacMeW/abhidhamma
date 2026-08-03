const fs = require('fs');
let content = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');

const startMarker = '    // --- CITTA GRID VIEW LOGIC ---';
const endMarker = '    // --- END CITTA GRID VIEW LOGIC ---';

const startIndex = content.indexOf(startMarker);
const endIndex = content.indexOf(endMarker) + endMarker.length;

if (startIndex !== -1 && endIndex !== -1) {
    const logicBlock = content.substring(startIndex, endIndex);
    
    // Remove the block from its current position
    content = content.replace(logicBlock, '');
    
    // Find the end of the DOMContentLoaded listener
    const insertAfter = '        });\n    </script>';
    
    if (content.includes(insertAfter)) {
        content = content.replace(insertAfter, '        });\n\n' + logicBlock + '\n    </script>');
        fs.writeFileSync('citta_cetasikas_visual_guide.html', content, 'utf8');
        console.log('Moved CITTA GRID VIEW LOGIC outside of DOMContentLoaded.');
    } else {
        console.log('Could not find insert position.');
    }
} else {
    console.log('Could not find logic block.');
}
