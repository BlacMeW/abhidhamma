const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const htmlFile = 'citta_cetasikas_visual_guide.html';
let htmlContent = fs.readFileSync(htmlFile, 'utf8');
const dom = new JSDOM(htmlContent);
const document = dom.window.document;

// 1. Add toggle buttons to the Citta header
const cittaHeader = document.querySelector('#sec-citta89 .text-center.max-w-3xl.mx-auto.space-y-2');
if (cittaHeader) {
    const toggleHTML = `
    <div class="flex justify-center items-center gap-2 mt-4 mb-2">
        <button onclick="toggleCittaView('list')" id="btn-citta-list" class="px-4 py-1.5 rounded-full text-xs font-bold transition bg-amber-500 text-white dark:bg-amber-600 shadow-sm"><i class="fa-solid fa-list-ul mr-1.5"></i> အုပ်စုလိုက် (List View)</button>
        <button onclick="toggleCittaView('grid')" id="btn-citta-grid" class="px-4 py-1.5 rounded-full text-xs font-bold transition bg-slate-200 text-slate-600 dark:bg-slate-700 dark:text-slate-300 hover:bg-slate-300 dark:hover:bg-slate-600"><i class="fa-solid fa-border-all mr-1.5"></i> ကတ်များ (Grid View)</button>
    </div>
    `;
    cittaHeader.insertAdjacentHTML('beforeend', toggleHTML);
}

// 2. Wrap existing content in citta-list-view
const secCitta89 = document.getElementById('sec-citta89');
const childrenToWrap = [];
// We want to wrap the total verification bar and the groups
// Basically, everything after the header up to the end of sec-citta89 (excluding what we just added)
let node = cittaHeader.nextElementSibling;
while(node) {
    childrenToWrap.push(node);
    node = node.nextElementSibling;
}

const listView = document.createElement('div');
listView.id = 'citta-list-view';
listView.className = 'space-y-6';
childrenToWrap.forEach(child => listView.appendChild(child));
secCitta89.appendChild(listView);

// 3. Create citta-grid-view
const gridView = document.createElement('div');
gridView.id = 'citta-grid-view';
gridView.className = 'hidden space-y-6';
gridView.innerHTML = `
    <!-- Filters -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-6 mt-4">
        <button onclick="renderCittaGrid('all')" id="citta-filter-all" class="px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-amber-500 text-white shadow-sm hover:bg-amber-600">အားလုံး (၈၉)</button>
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
        <!-- Cards injected by JS -->
    </div>
`;
secCitta89.appendChild(gridView);

// 4. Inject JS logic for toggling and rendering
const scriptNode = document.createElement('script');
scriptNode.textContent = `
    function toggleCittaView(view) {
        const listView = document.getElementById('citta-list-view');
        const gridView = document.getElementById('citta-grid-view');
        const btnList = document.getElementById('btn-citta-list');
        const btnGrid = document.getElementById('btn-citta-grid');
        
        if (view === 'grid') {
            listView.classList.add('hidden');
            gridView.classList.remove('hidden');
            
            btnGrid.className = 'px-4 py-1.5 rounded-full text-xs font-bold transition bg-amber-500 text-white dark:bg-amber-600 shadow-sm';
            btnList.className = 'px-4 py-1.5 rounded-full text-xs font-bold transition bg-slate-200 text-slate-600 dark:bg-slate-700 dark:text-slate-300 hover:bg-slate-300 dark:hover:bg-slate-600';
            
            // First time render
            if (document.getElementById('citta-grid').innerHTML.trim() === '') {
                renderCittaGrid('all');
            }
        } else {
            gridView.classList.add('hidden');
            listView.classList.remove('hidden');
            
            btnList.className = 'px-4 py-1.5 rounded-full text-xs font-bold transition bg-amber-500 text-white dark:bg-amber-600 shadow-sm';
            btnGrid.className = 'px-4 py-1.5 rounded-full text-xs font-bold transition bg-slate-200 text-slate-600 dark:bg-slate-700 dark:text-slate-300 hover:bg-slate-300 dark:hover:bg-slate-600';
        }
    }

    function renderCittaGrid(filter = 'all') {
        const grid = document.getElementById('citta-grid');
        const emptyState = document.getElementById('citta-grid-empty');
        grid.innerHTML = '';
        
        // Update filter buttons styling
        const filters = ['all', 'kamavacara', 'rupavacara', 'arupavacara', 'lokuttara'];
        filters.forEach(f => {
            const btn = document.getElementById('citta-filter-' + f);
            if (btn) {
                if (f === filter) {
                    btn.className = 'px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-amber-500 text-white shadow-sm hover:bg-amber-600';
                } else {
                    btn.className = 'px-4 py-1.5 rounded-full text-xs md:text-sm font-semibold transition bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700';
                }
            }
        });
        
        if (typeof cittaData === 'undefined') return;
        
        const filtered = cittaData.filter(item => {
            if (filter === 'all') return true;
            if (filter === 'kamavacara') {
                return ['akusala', 'ahetuka', 'sobhana'].includes(item.cat) || item.group === 'kama';
            }
            return item.group === filter;
        });
        
        if (emptyState) {
            emptyState.classList.toggle('hidden', filtered.length !== 0);
        }
        
        filtered.forEach(item => {
            let badgeClass = "bg-slate-100 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 border-slate-500/30";
            let hoverBorder = "hover:border-slate-400";
            
            if (item.cat === 'akusala') {
                badgeClass = "bg-rose-100 dark:bg-rose-500/20 text-rose-700 dark:text-rose-300 border-rose-500/30";
                hoverBorder = "hover:border-rose-400";
            } else if (item.cat === 'sobhana' || item.group === 'rupa' || item.group === 'arupa') {
                badgeClass = "bg-emerald-100 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border-emerald-500/30";
                hoverBorder = "hover:border-emerald-400";
            } else if (item.group === 'lokuttara') {
                badgeClass = "bg-amber-100 dark:bg-amber-500/20 text-amber-700 dark:text-amber-300 border-amber-500/30";
                hoverBorder = "hover:border-amber-400";
            } else if (item.cat === 'ahetuka') {
                badgeClass = "bg-sky-100 dark:bg-sky-500/20 text-sky-700 dark:text-sky-300 border-sky-500/30";
                hoverBorder = "hover:border-sky-400";
            }

            const card = document.createElement('div');
            card.className = \`citta-card glass-card rounded-xl p-4 border border-slate-200 dark:border-slate-800 \${hoverBorder} cursor-pointer transition duration-200 flex flex-col justify-between group focus:outline-none focus:ring-2 focus:ring-amber-400\`;
            card.setAttribute('tabindex', '0');
            card.setAttribute('role', 'button');
            card.setAttribute('aria-label', \`\${item.name} (\${item.pali}) အသေးစိတ်ကြည့်ရန်\`);
            card.onclick = () => openModal(item);
            card.onkeydown = (e) => {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(item); }
            };
            
            card.innerHTML = \`
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] font-bold px-2.5 py-0.5 rounded-full border \${badgeClass}">\${item.sub || item.group}</span>
                        <span class="text-xs text-slate-500 dark:text-slate-500 font-mono">#\${mm(item.id)}</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-lg bg-slate-50 dark:bg-slate-800 flex items-center justify-center text-slate-700 dark:text-slate-300 group-hover:scale-110 transition">
                            <i class="fa-solid \${item.icon || 'fa-brain'}"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-slate-900 dark:text-slate-100 text-base group-hover:text-amber-700 dark:text-amber-400 transition">\${item.name}</h4>
                            <p class="text-[13px] md:text-[14px] font-medium text-slate-600 dark:text-slate-400 font-mono">\${item.pali}</p>
                        </div>
                    </div>
                    <p class="text-xs text-slate-700 dark:text-slate-300 line-clamp-2">\${item.desc}</p>
                </div>
                <div class="mt-4 pt-2 border-t border-slate-200 dark:border-slate-800/80 flex items-center justify-between text-[11px] text-slate-600 dark:text-slate-400">
                    <span>နှိပ်၍ အသေးစိတ်ကြည့်ပါ</span>
                    <i class="fa-solid fa-chevron-right text-[10px] group-hover:text-amber-500 transition-colors"></i>
                </div>
            \`;
            grid.appendChild(card);
        });
    }
\`;

document.body.appendChild(scriptNode);

fs.writeFileSync(htmlFile, dom.serialize(), 'utf8');
console.log('Successfully injected Citta grid view!');
