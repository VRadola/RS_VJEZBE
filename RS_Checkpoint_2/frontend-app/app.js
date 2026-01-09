let token = "";
const ACCOUNT_ID = 1;
const ACCOUNT_NAMES = {
  1: "User",
  2: "Savings"
};

function setStatus(msg) {
  document.getElementById("status").innerText = msg;
}

async function login() {
  const u = document.getElementById("username").value.trim();
  const p = document.getElementById("password").value.trim();
  setStatus("Logging in...");

  try {
    const res = await fetch(
      `http://localhost:8000/login?username=${encodeURIComponent(u)}&password=${encodeURIComponent(p)}`,
      { method: "POST" }
    );
    if (!res.ok) {
      setStatus("Login failed.");
      return;
    }
    const data = await res.json();
    token = data.access_token;
    setStatus("Logged in.");
    await loadAccounts();
    await loadActivity();

  } catch (e) {
    console.error(e);
    setStatus("Cannot reach auth-service.");
  }
}

async function loadBalance() {
  if (!token) return alert("Login first.");

  const res = await fetch(`http://localhost:8001/accounts/${ACCOUNT_ID}`, {
    headers: { Authorization: "Bearer " + token }
  });

  if (!res.ok) return alert("Balance failed (401 = token invalid).");

  const data = await res.json();
  document.getElementById("balance").innerText = data.balance + " EUR";
}

async function loadAccounts() {
  if (!token) return alert("Login first.");

  const res = await fetch("http://localhost:8001/accounts", {
    headers: { Authorization: "Bearer " + token }
  });

  if (!res.ok) return alert("Failed to load accounts.");

  const data = await res.json();
  const el = document.getElementById("accounts");
  el.innerHTML = "";

  data.forEach(acc => {
    el.innerHTML += `
      <div class="rowitem">
        <div>${acc.name}</div>
        <div class="amt">${acc.balance} EUR</div>
      </div>
    `;
  });
}


async function doTransfer() {
  if (!token) return alert("Login first.");

  const from = Number(document.getElementById("fromAccount").value);
  const to = Number(document.getElementById("toAccount").value);
  const amount = Number(document.getElementById("transferAmount").value);

  if (amount <= 0) return alert("Amount must be > 0.");
  if (from === to) return alert("Choose different accounts.");

  const note = `${ACCOUNT_NAMES[from] || from} → ${ACCOUNT_NAMES[to] || to}`;

  const res = await fetch(
    `http://localhost:8002/transfer?frm=${from}&to=${to}&amount=${amount}&note=${encodeURIComponent(note)}`,
    { method: "POST", headers: { Authorization: "Bearer " + token } }
  );

  if (!res.ok) {
    const txt = await res.text();
    return alert("Transfer failed: " + txt);
  }

  await loadAccounts();
  await loadActivity();
}

async function payBill() {
  if (!token) return alert("Login first.");

  const biller = document.getElementById("biller").value.trim();
  const amount = Number(document.getElementById("billAmount").value);

  const res = await fetch(
    `http://localhost:8003/pay?account_id=${ACCOUNT_ID}&biller=${encodeURIComponent(biller)}&amount=${amount}`,
    { method: "POST", headers: { Authorization: "Bearer " + token } }
  );

  if (!res.ok) return alert("Payment failed.");
  await loadAccounts();
  await loadActivity;
}

async function loadActivity() {
  if (!token) return;

  const [trRes, payRes] = await Promise.all([
    fetch(`http://localhost:8002/transactions?account_id=${ACCOUNT_ID}`, {
      headers: { Authorization: "Bearer " + token }
    }),
    fetch(`http://localhost:8003/payments?account_id=${ACCOUNT_ID}`, {
      headers: { Authorization: "Bearer " + token }
    })
  ]);

  if (!trRes.ok || !payRes.ok) {
    return alert("Failed to load activity.");
  }

  const transactions = await trRes.json();
  const payments = await payRes.json();

  const activity = [];

  transactions.forEach(t => {
    const fromName = ACCOUNT_NAMES[t.from] || `Account ${t.from}`;
    let toLabel = ACCOUNT_NAMES[t.to] || `Account ${t.to}`;

    if (t.to === 999 && t.note) {
      toLabel = t.note;
    }

    activity.push({
      timestamp: t.timestamp,
      title: `${fromName} → ${toLabel}`,
      amount: (t.from === ACCOUNT_ID ? -t.amount : +t.amount),
      id: `tx-${t.id}`
    });
  });

  activity.sort((a, b) => (a.timestamp < b.timestamp ? 1 : -1));

  const el = document.getElementById("activity");
  el.innerHTML = "";

  activity.forEach(a => {
    const sign = a.amount >= 0 ? "+" : "";
    el.innerHTML += `
      <div class="rowitem">
        <div>${a.timestamp}</div>
        <div>${a.title}</div>
        <div class="amt">${sign}${a.amount} EUR</div>
      </div>
    `;
  });
}

function logout() {
  token = "";
  setStatus("Logged out.");
  document.getElementById("balance").innerText = "—";
  document.getElementById("transactions").innerHTML = "";
  document.getElementById("payments").innerHTML = "";
}