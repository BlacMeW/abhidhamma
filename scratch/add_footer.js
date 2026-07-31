const fs = require('fs');
const path = require('path');

const dir = '.';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const footerCode = `
    <!-- Footer Dedication -->
    <footer class="mt-20 py-8 border-t border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/50 text-center transition-colors duration-300">
        <div class="max-w-7xl mx-auto px-4">
            <p class="text-slate-500 dark:text-slate-400 text-sm md:text-base font-medium flex items-center justify-center gap-2">
                <i class="fa-solid fa-dharmachakra text-amber-500 animate-spin-slow" style="animation-duration: 10s;"></i>
                မောင်ဝဏ္ဏကို (၀၅ ဇွန်  ၂၀၁၀ - ၁၂ နိုဝင်ဘာ ၂၀၂၄) အားရည်စူးသော ဓမ္မဒါန တရားအလှူ
                <i class="fa-solid fa-dharmachakra text-amber-500 animate-spin-slow" style="animation-duration: 10s;"></i>
            </p>
        </div>
    </footer>
`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Check if footer already exists
    if (!content.includes('<!-- Footer Dedication -->')) {
        // Insert right before </body>
        if (content.includes('</body>')) {
            content = content.replace('</body>', footerCode + '\n</body>');
            fs.writeFileSync(file, content);
            console.log('Added footer to ' + file);
        } else {
            console.log('No </body> found in ' + file);
        }
    }
});
