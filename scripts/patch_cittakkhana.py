import re

cittakkhana_html = """
            <!-- Cittakkhana (Micro-Animation) -->
            <div class="glass-card rounded-2xl p-5 md:p-8 max-w-4xl mx-auto border border-sky-500/30 glow-blue space-y-6">
                <style>
                    @keyframes khana-uppada {
                        0% { transform: scale(0); opacity: 0; filter: blur(4px); }
                        100% { transform: scale(1); opacity: 1; filter: blur(0); }
                    }
                    @keyframes khana-thiti {
                        0% { transform: scale(1); opacity: 1; }
                        50% { transform: scale(1.1); opacity: 0.9; filter: brightness(1.2); }
                        100% { transform: scale(1); opacity: 1; }
                    }
                    @keyframes khana-bhanga {
                        0% { transform: scale(1); opacity: 1; filter: blur(0); }
                        100% { transform: scale(0); opacity: 0; filter: blur(4px); }
                    }
                    .animate-uppada { animation: khana-uppada 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }
                    .animate-thiti { animation: khana-thiti 1.6s ease-in-out infinite; }
                    .animate-bhanga { animation: khana-bhanga 0.8s ease-in forwards; }
                    
                    .khana-container {
                        perspective: 1000px;
                    }
                </style>
                
                <div class="text-center space-y-2">
                    <h3 class="font-bold text-sky-300 text-lg flex items-center justify-center gap-2">
                        <i class="fa-solid fa-stopwatch-20 text-sky-400"></i> စိတ်ခဏ (Cittakkhaṇa) နှင့် ဥပါဒ်၊ ဌီ၊ ဘင်
                    </h3>
                    <p class="text-sm text-slate-300 max-w-2xl mx-auto">စိတ်တစ်ခုဖြစ်ပေါ်ရာတွင် အလွန်တိုတောင်းသော အချိန်လေး (ခဏငယ်) သုံးခု ပါဝင်ပါသည်။ မျက်စိတစ်မှိတ် လျှပ်တစ်ပြက်အတွင်းမှာပင် ဤစိတ်ခဏပေါင်း ကုဋေတစ်သိန်းမက ဖြစ်ပျက်သွားပါသည်။</p>
                </div>
                
                <div class="khana-container bg-slate-900/80 rounded-xl p-8 border border-slate-700/50 flex flex-col md:flex-row items-center justify-around gap-8 md:gap-4 relative overflow-hidden">
                    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNSkiLz48L3N2Zz4=')] opacity-50 pointer-events-none"></div>
                    
                    <div class="flex flex-col items-center gap-4 relative z-10 w-full md:w-1/3" id="stage-uppada">
                        <div class="h-24 flex items-center justify-center">
                            <div class="w-16 h-16 rounded-full bg-emerald-500/20 border-2 border-emerald-400 flex items-center justify-center shadow-[0_0_15px_rgba(52,211,153,0.5)]" id="orb-uppada">
                                <i class="fa-solid fa-plus text-emerald-300 text-xl"></i>
                            </div>
                        </div>
                        <div class="text-center">
                            <span class="font-bold text-emerald-400 block text-lg">ဥပါဒ် (Uppāda)</span>
                            <span class="text-xs text-slate-400">စတင်ဖြစ်ပေါ်ခြင်း</span>
                        </div>
                    </div>
                    
                    <div class="hidden md:block w-8 text-center text-slate-600"><i class="fa-solid fa-arrow-right"></i></div>
                    <div class="md:hidden h-8 text-center text-slate-600"><i class="fa-solid fa-arrow-down"></i></div>
                    
                    <div class="flex flex-col items-center gap-4 relative z-10 w-full md:w-1/3 opacity-30 transition-opacity duration-300" id="stage-thiti">
                        <div class="h-24 flex items-center justify-center">
                            <div class="w-16 h-16 rounded-full bg-amber-500/20 border-2 border-amber-400 flex items-center justify-center shadow-[0_0_15px_rgba(251,191,36,0.5)]" id="orb-thiti">
                                <i class="fa-solid fa-pause text-amber-300 text-xl"></i>
                            </div>
                        </div>
                        <div class="text-center">
                            <span class="font-bold text-amber-400 block text-lg">ဌီ (Ṭhiti)</span>
                            <span class="text-xs text-slate-400">တည်နေခြင်း</span>
                        </div>
                    </div>
                    
                    <div class="hidden md:block w-8 text-center text-slate-600"><i class="fa-solid fa-arrow-right"></i></div>
                    <div class="md:hidden h-8 text-center text-slate-600"><i class="fa-solid fa-arrow-down"></i></div>
                    
                    <div class="flex flex-col items-center gap-4 relative z-10 w-full md:w-1/3 opacity-30 transition-opacity duration-300" id="stage-bhanga">
                        <div class="h-24 flex items-center justify-center">
                            <div class="w-16 h-16 rounded-full bg-rose-500/20 border-2 border-rose-400 flex items-center justify-center shadow-[0_0_15px_rgba(244,63,94,0.5)]" id="orb-bhanga">
                                <i class="fa-solid fa-minus text-rose-300 text-xl"></i>
                            </div>
                        </div>
                        <div class="text-center">
                            <span class="font-bold text-rose-400 block text-lg">ဘင် (Bhaṅga)</span>
                            <span class="text-xs text-slate-400">ချုပ်ပျောက်ခြင်း</span>
                        </div>
                    </div>
                </div>
                
                <div class="flex justify-center pt-2">
                    <button onclick="playCittakkhana()" class="px-5 py-2 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/50 hover:bg-sky-500/30 transition flex items-center gap-2 font-bold text-sm">
                        <i class="fa-solid fa-play"></i> ပြန်လည်ပြသရန်
                    </button>
                </div>
            </div>
            
            <script>
                function playCittakkhana() {
                    const su = document.getElementById('stage-uppada');
                    const st = document.getElementById('stage-thiti');
                    const sb = document.getElementById('stage-bhanga');
                    const ou = document.getElementById('orb-uppada');
                    const ot = document.getElementById('orb-thiti');
                    const ob = document.getElementById('orb-bhanga');
                    
                    // Reset
                    su.style.opacity = '1'; st.style.opacity = '0.3'; sb.style.opacity = '0.3';
                    ou.className = 'w-16 h-16 rounded-full bg-emerald-500/20 border-2 border-emerald-400 flex items-center justify-center shadow-[0_0_15px_rgba(52,211,153,0.5)]';
                    ot.className = 'w-16 h-16 rounded-full bg-amber-500/20 border-2 border-amber-400 flex items-center justify-center shadow-[0_0_15px_rgba(251,191,36,0.5)]';
                    ob.className = 'w-16 h-16 rounded-full bg-rose-500/20 border-2 border-rose-400 flex items-center justify-center shadow-[0_0_15px_rgba(244,63,94,0.5)]';
                    
                    // Sequence
                    ou.classList.add('animate-uppada');
                    
                    setTimeout(() => {
                        su.style.opacity = '0.3';
                        st.style.opacity = '1';
                        ot.classList.add('animate-thiti');
                    }, 1200);
                    
                    setTimeout(() => {
                        st.style.opacity = '0.3';
                        sb.style.opacity = '1';
                        ot.classList.remove('animate-thiti');
                        ob.classList.add('animate-bhanga');
                    }, 2800);
                }
                
                // Auto play on load if possible, or leave it for button
                setTimeout(playCittakkhana, 1000);
            </script>
"""

filename = 'citta_cetasikas_visual_guide.html'
with open(filename, 'r') as f:
    content = f.read()

content = re.sub(r'(<!-- Live Vithi Animation \(dedicated, continuous, decorative \+ informative\) -->)', cittakkhana_html + r'\n            \1', content)

with open(filename, 'w') as f:
    f.write(content)
print("Added Cittakkhana animation successfully!")
