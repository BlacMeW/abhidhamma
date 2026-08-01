const fs = require('fs');
let content = fs.readFileSync('citta_cetasikas_visual_guide.html', 'utf8');

const regex = /const filtered = cittaData\.filter\(item => \{[\s\S]*?hover:border-sky-400";\n            \}/m;

const newLogic = `const filtered = cittaData.filter(item => {
            if (filter === 'all') return true;
            if (filter === 'kamavacara') {
                return ['akusala', 'ahetuka', 'sobhana54'].includes(item.group);
            }
            if (filter === 'rupavacara') return item.group === 'rupa';
            if (filter === 'arupavacara') return item.group === 'arupa';
            if (filter === 'lokuttara') return item.group === 'lokuttara';
            return item.group === filter;
        });

        if (emptyState) {
            emptyState.classList.toggle('hidden', filtered.length > 0);
        }

        filtered.forEach(item => {
            let badgeClass = "bg-slate-100 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 border-slate-500/30";
            let hoverBorder = "hover:border-slate-400";

            if (item.group === 'akusala') {
                badgeClass = "bg-rose-100 dark:bg-rose-500/20 text-rose-700 dark:text-rose-300 border-rose-500/30";
                hoverBorder = "hover:border-rose-400";
            } else if (item.group === 'sobhana54' || item.group === 'rupa' || item.group === 'arupa') {
                badgeClass = "bg-emerald-100 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border-emerald-500/30";
                hoverBorder = "hover:border-emerald-400";
            } else if (item.group === 'lokuttara') {
                badgeClass = "bg-amber-100 dark:bg-amber-500/20 text-amber-700 dark:text-amber-300 border-amber-500/30";
                hoverBorder = "hover:border-amber-400";
            } else if (item.group === 'ahetuka') {
                badgeClass = "bg-sky-100 dark:bg-sky-500/20 text-sky-700 dark:text-sky-300 border-sky-500/30";
                hoverBorder = "hover:border-sky-400";
            }`;

if (regex.test(content)) {
    content = content.replace(regex, newLogic);
    fs.writeFileSync('citta_cetasikas_visual_guide.html', content, 'utf8');
    console.log("Successfully replaced logic via regex!");
} else {
    console.log("Could not find logic via regex either");
}
