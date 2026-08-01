const fs = require('fs');
let html = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');

const htmlToAdd = `
            <!-- Citta Grid View -->
            <div id="citta-grid-view" class="hidden mt-6">
                <!-- Filters -->
                <div class="flex flex-wrap gap-2 mb-6" role="group" aria-label="Citta Group Filters">
                    <button onclick="renderCittaGrid('all')" id="citta-filter-all" class="px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-amber-500 text-white shadow-sm hover:bg-amber-600">အားလုံး (၈၉/၁၂၁)</button>
                    <button onclick="renderCittaGrid('kamavacara')" id="citta-filter-kamavacara" class="px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700">ကာမာဝစရ (၅၄)</button>
                    <button onclick="renderCittaGrid('rupavacara')" id="citta-filter-rupavacara" class="px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700">ရူပါဝစရ (၁၅)</button>
                    <button onclick="renderCittaGrid('arupavacara')" id="citta-filter-arupavacara" class="px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700">အရူပါဝစရ (၁၂)</button>
                    <button onclick="renderCittaGrid('lokuttara')" id="citta-filter-lokuttara" class="px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700">လောကုတ္တရာ (၈)</button>
                </div>
                <!-- Empty State -->
                <div id="citta-grid-empty" class="hidden py-12 text-center text-slate-500">
                    <i class="fa-regular fa-folder-open text-4xl mb-3 opacity-50"></i>
                    <p>ရှာဖွေမှုနှင့် ကိုက်ညီသော စိတ် မရှိပါ။</p>
                </div>
                <!-- Grid -->
                <div id="citta-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                </div>
            </div>
`;

// Find where to insert it. The best place is before the closing tag of section id="sec-citta89"
// Wait, let's just insert it right before: '        </section>'
// We should check if it already exists
if (!html.includes('id="citta-grid-view"')) {
    // let's insert it before the closing section tag of sec-citta89
    // sec-citta89 is defined as `<section id="sec-citta89" class="tab-content hidden space-y-12 pb-12">`
    // We will look for `</section>` that comes after `<div id="citta-list-view"`
    const secParts = html.split('<section id="sec-citta89"');
    if (secParts.length === 2) {
        const innerParts = secParts[1].split('</section>');
        innerParts[0] = innerParts[0] + htmlToAdd + '\n        ';
        html = secParts[0] + '<section id="sec-citta89"' + innerParts.join('</section>');
        fs.writeFileSync('citta_cetasikas_visual_guide.html', html, 'utf8');
        console.log('Successfully injected HTML.');
    } else {
        console.log('Could not find sec-citta89 properly.');
    }
} else {
    console.log('citta-grid-view already exists.');
}
