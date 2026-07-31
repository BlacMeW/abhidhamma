const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('http://localhost:8000/glossary.html'); // Assuming python server on 8000
  await page.setViewport({ width: 1280, height: 800 });
  
  // Wait a bit
  await new Promise(r => setTimeout(r, 1000));
  
  // Click Kammatthana
  await page.click('[data-cat="kammatthana"]');
  await new Promise(r => setTimeout(r, 500));
  
  await page.screenshot({path: 'screenshot_test.png'});
  
  // get innerHTML of listEl
  const html = await page.$eval('#glossaryList', el => el.innerHTML);
  console.log("HTML length:", html.length);
  
  await browser.close();
})();
