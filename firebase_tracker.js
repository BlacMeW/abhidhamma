import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getDatabase, ref, onValue, set, onDisconnect, push, serverTimestamp, runTransaction } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDwgdFI1GWcQB0Ah9XYTCuJFrdMK7UfXa4",
  authDomain: "abhidhamma-web-2026.firebaseapp.com",
  databaseURL: "https://abhidhamma-web-2026-default-rtdb.firebaseio.com",
  projectId: "abhidhamma-web-2026",
  storageBucket: "abhidhamma-web-2026.firebasestorage.app",
  messagingSenderId: "204889172698",
  appId: "1:204889172698:web:9346e2878de07b8dc993e3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

// DOM Elements
const onlineUsersEl = document.getElementById('online-users-count');
const totalVisitorsEl = document.getElementById('total-visitors-count');

// 1. Handle Online Presence
const connectedRef = ref(db, '.info/connected');
const presenceRef = ref(db, 'presence');
let myConnectionsRef = null;

onValue(connectedRef, (snap) => {
    if (snap.val() === true) {
        // We're connected (or reconnected)!
        myConnectionsRef = push(presenceRef);
        
        // When I disconnect, remove this device
        onDisconnect(myConnectionsRef).remove();

        // Add this device to my connections list
        // this value could contain info about the device or a timestamp too
        set(myConnectionsRef, true);
    }
});

// Listen for total online users
onValue(presenceRef, (snap) => {
    const totalOnline = snap.size || 0;
    if (onlineUsersEl) {
        onlineUsersEl.textContent = totalOnline.toLocaleString('my-MM'); // Use Myanmar numbers if needed, or normal
    }
});

// 2. Handle Total Visitors Tracking
const visitorsRef = ref(db, 'stats/total_visitors');
let hasIncremented = sessionStorage.getItem('hasVisitedAbhidhamma');

if (!hasIncremented) {
    runTransaction(visitorsRef, (currentData) => {
        if (currentData === null) {
            return 1;
        } else {
            return currentData + 1;
        }
    }).then(() => {
        sessionStorage.setItem('hasVisitedAbhidhamma', 'true');
    }).catch(err => {
        console.error("Error updating visitors:", err);
    });
}

// Listen for total visitors updates
onValue(visitorsRef, (snap) => {
    const count = snap.val() || 0;
    if (totalVisitorsEl) {
        totalVisitorsEl.textContent = count.toLocaleString('en-US');
    }
});
