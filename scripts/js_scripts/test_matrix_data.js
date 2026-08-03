const matrixGroups = [
    { key: 'hetu', label: 'ဟေတု' },
    { key: 'jhananga', label: 'ဈာနင်္ဂ' },
    { key: 'magganga', label: 'မဂ္ဂင်္ဂ' },
    { key: 'indriya', label: 'ဣန္ဒြိယ' },
    { key: 'bala', label: 'ဗလ' },
    { key: 'adhipati', label: 'အဓိပတိ' },
    { key: 'ahara', label: 'အာဟာရ' }
];

const baseParamatthas = [
    // --- Citta ---
    { name: 'စိတ်', type: 'citta', map: { indriya: ['မနိန္ဒြေ'], adhipati: ['စိတ္တာဓိပတိ'], ahara: ['ဝိညာဏာဟာရ'] } },
    
    // --- Cetasika (Aññasamāna) ---
    { name: 'ဝေဒနာ', type: 'cetasika-anna', map: { jhananga: ['သောမနဿ', 'ဒေါမနဿ', 'ဥပေက္ခာ'], indriya: ['သုခ', 'ဒုက္ခ', 'သောမနဿ', 'ဒေါမနဿ', 'ဥပေက္ခာ'] } },
    { name: 'ဧကဂ္ဂတာ (သမာဓိ)', type: 'cetasika-anna', map: { jhananga: ['ဧကဂ္ဂတာ'], magganga: ['သမ္မာသမာဓိ', 'မိစ္ဆာသမာဓိ'], indriya: ['သမာဓိန္ဒြေ'], bala: ['သမာဓိဗလ'] } },
    { name: 'ဝီရိယ', type: 'cetasika-anna', map: { magganga: ['သမ္မာဝါယာမ', 'မိစ္ဆာဝါယာမ'], indriya: ['ဝီရိယိန္ဒြေ'], bala: ['ဝီရိယဗလ'], adhipati: ['ဝီရိယာဓိပတိ'] } },
    { name: 'ဝိတက်', type: 'cetasika-anna', map: { jhananga: ['ဝိတက်'], magganga: ['သမ္မာသင်္ကပ္ပ', 'မိစ္ဆာသင်္ကပ္ပ'] } },
    { name: 'ဇီဝိတ', type: 'cetasika-anna', map: { indriya: ['ဇီဝိတိန္ဒြေ (နာမ်)'] } }, // Note: Rupa Jivita is also there
    { name: 'ဖဿ', type: 'cetasika-anna', map: { ahara: ['ဖဿာဟာရ'] } },
    { name: 'စေတနာ', type: 'cetasika-anna', map: { ahara: ['မနောသဉ္စေတနာဟာရ'] } },
    { name: 'ဝိစာရ', type: 'cetasika-anna', map: { jhananga: ['ဝိစာရ'] } },
    { name: 'ပီတိ', type: 'cetasika-anna', map: { jhananga: ['ပီတိ'] } },
    { name: 'ဆန္ဒ', type: 'cetasika-anna', map: { adhipati: ['ဆန္ဒာဓိပတိ'] } },

    // --- Cetasika (Akusala) ---
    { name: 'လောဘ', type: 'cetasika-akusala', map: { hetu: ['လောဘ'] } },
    { name: 'ဒေါသ', type: 'cetasika-akusala', map: { hetu: ['ဒေါသ'] } },
    { name: 'မောဟ', type: 'cetasika-akusala', map: { hetu: ['မောဟ'] } },
    { name: 'ဒိဋ္ဌိ', type: 'cetasika-akusala', map: { magganga: ['မိစ္ဆာဒိဋ္ဌိ'] } },
    { name: 'အဟိရိက', type: 'cetasika-akusala', map: { bala: ['အဟိရိကဗလ'] } },
    { name: 'အနောတ္တပ္ပ', type: 'cetasika-akusala', map: { bala: ['အနောတ္တပ္ပဗလ'] } },

    // --- Cetasika (Sobhana) ---
    { name: 'ပညာ (အမောဟ)', type: 'cetasika-sobhana', map: { hetu: ['အမောဟ'], magganga: ['သမ္မာဒိဋ္ဌိ'], indriya: ['ပညိန္ဒြေ', 'အနညတညဿာမီတိန္ဒြေ', 'အညိန္ဒြေ', 'အညာတာဝိန္ဒြေ'], bala: ['ပညာဗလ'], adhipati: ['ဝီမံသာဓိပတိ'] } },
    { name: 'သတိ', type: 'cetasika-sobhana', map: { magganga: ['သမ္မာသတိ'], indriya: ['သတိန္ဒြေ'], bala: ['သတိဗလ'] } },
    { name: 'သဒ္ဓါ', type: 'cetasika-sobhana', map: { indriya: ['သဒ္ဓိန္ဒြေ'], bala: ['သဒ္ဓါဗလ'] } },
    { name: 'အလောဘ', type: 'cetasika-sobhana', map: { hetu: ['အလောဘ'] } },
    { name: 'အဒေါသ', type: 'cetasika-sobhana', map: { hetu: ['အဒေါသ'] } },
    { name: 'သမ္မာဝါစာ', type: 'cetasika-sobhana', map: { magganga: ['သမ္မာဝါစာ'] } },
    { name: 'သမ္မာကမ္မန္တ', type: 'cetasika-sobhana', map: { magganga: ['သမ္မာကမ္မန္တ'] } },
    { name: 'သမ္မာအာဇီဝ', type: 'cetasika-sobhana', map: { magganga: ['သမ္မာအာဇီဝ'] } },
    { name: 'ဟိရီ', type: 'cetasika-sobhana', map: { bala: ['ဟိရီဗလ'] } },
    { name: 'ဩတ္တပ္ပ', type: 'cetasika-sobhana', map: { bala: ['ဩတ္တပ္ပဗလ'] } },

    // --- Rupa ---
    { name: 'ပသာဒရုပ် ၅ ပါး', type: 'rupa', map: { indriya: ['စက္ခုန္ဒြေ', 'သောတိန္ဒြေ', 'ဃာနိန္ဒြေ', 'ဇိဝှိန္ဒြေ', 'ကာယိန္ဒြေ'] } },
    { name: 'ဘာဝရုပ် ၂ ပါး', type: 'rupa', map: { indriya: ['ဣတ္ထိန္ဒြေ', 'ပုရိသိန္ဒြေ'] } },
    { name: 'ဇီဝိတရုပ်', type: 'rupa', map: { indriya: ['ဇီဝိတိန္ဒြေ (ရုပ်)'] } },
    { name: 'ဩဇာ (ရုပ်အစာ)', type: 'rupa', map: { ahara: ['ကဗဠီကာရာဟာရ'] } }
];

let totalMapped = 0;
baseParamatthas.forEach(p => {
    Object.values(p.map).forEach(arr => totalMapped += arr.length);
});

console.log("Total Mapped Items:", totalMapped);
// Note: Some Jivita is both Nama & Rupa. Jivitindriya is 1 in the 22 Indriyas, but technically two paramatthas (Nama Jivita, Rupa Jivita).
// So total might be 65 instead of 64. Let's see: Hetu(6) + Jhananga(7) + Magganga(12) + Indriya(22) + Bala(9) + Adhipati(4) + Ahara(4) = 64.
// My map for Indriya: Sukha, Dukkha, Somanassa, Domanassa, Upekkha (5), Manindriya (1), Saddha (1), Viriya (1), Sati (1), Samadhi (1), Panna+3 (4), Pasada (5), Bhava (2), Jivita (2). Total = 5+1+1+1+1+1+4+5+2+2 = 23. Wait. The 22 Indriyas have 1 Jivitindriya, which represents BOTH Nama and Rupa Jivita. 
