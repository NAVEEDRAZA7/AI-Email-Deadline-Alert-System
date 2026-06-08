{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4e5b377c-380e-4c8a-9a50-50ff7118b4a6",
   "metadata": {},
   "source": [
    "# ———————— SMART DEADLINE REMINDER SYSTEM ——————————"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4fb95da-6a6b-4c7c-a453-d32242804ae0",
   "metadata": {},
   "source": [
    "## —— Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c4b7270-2686-4228-914a-720c7ad69823",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re                  # Pattern matching / regex\n",
    "import time                # Delay / timer control\n",
    "import email               # Read email content\n",
    "import sqlite3             # Local database storage\n",
    "import datetime as dt      # Date and time handling\n",
    "import imaplib             # Gmail IMAP connection\n",
    "import threading           # Background parallel tasks\n",
    "import tkinter as tk       # Popup GUI alerts\n",
    "import pandas as pd        # Dataset loading / CSV\n",
    "\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer   # Text to numerical vectors\n",
    "from sklearn.linear_model import LogisticRegression           # ML classification model\n",
    "from sklearn.pipeline import Pipeline                         # ML workflow pipeline"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd683d00-e86d-448c-b54f-db2dcb2a2913",
   "metadata": {},
   "source": [
    "## — CONFIGURATION  (GMAIL) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62915013-4664-465e-b440-98910d4ecbad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creates SQLite database to permanently store tasks and alert status.\n",
    "\n",
    "USE_GMAIL = True\n",
    "\n",
    "GMAIL_EMAIL = \"ncworkbases@gmail.com\"\n",
    "GMAIL_APP_PASSWORD = \"ezcd dcdp wjjc qhio\"\n",
    "\n",
    "\n",
    "emails_manual = [\n",
    "    \"Meeting at 11:45 AM today\"\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2acf12f6-2c55-4c4c-824f-a855414e6831",
   "metadata": {},
   "source": [
    "## —  DATABASE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e8faea1-fb56-4b82-91ba-dce4d3d9fdae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ============================================================\n",
    "# DATABASE\n",
    "# ============================================================\n",
    "\n",
    "conn = sqlite3.connect(\"tasks.db\", check_same_thread=False)\n",
    "cursor = conn.cursor()\n",
    "\n",
    "cursor.execute(\"\"\"\n",
    "CREATE TABLE IF NOT EXISTS tasks (\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "    text TEXT,\n",
    "    deadline TEXT,\n",
    "    alerted INTEGER DEFAULT 0\n",
    ")\n",
    "\"\"\")\n",
    "conn.commit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50c6a16d-9ecc-4972-aadd-69e5bcd97419",
   "metadata": {},
   "source": [
    "## ——  ML Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a56174a-9aa4-43ac-ac58-549a6edfa447",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Trains Logistic Regression model using dataset to classify important emails.\n",
    "\n",
    "def train_model():\n",
    "    df = pd.read_csv(\"email_dataset_1000.csv\")\n",
    "\n",
    "    model = Pipeline([\n",
    "        (\"tfidf\", TfidfVectorizer()),\n",
    "        (\"clf\", LogisticRegression(max_iter=1000))\n",
    "    ])\n",
    "\n",
    "    model.fit(df[\"text\"], df[\"label\"])\n",
    "    return model\n",
    "\n",
    "\n",
    "ml_model = train_model()\n",
    "\n",
    "\n",
    "def is_important(text):\n",
    "    return ml_model.predict([text])[0] == 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2e2b5c4-3202-4d7d-acce-01f2655cf874",
   "metadata": {},
   "source": [
    "## —  TIME PARSER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76a48471-a620-479a-a5e9-cd4815a10205",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extracts time/date from email text and converts into proper datetime.\n",
    "\n",
    "def normalize_time(text):\n",
    "    match = re.search(r'(\\d{1,2})(?::(\\d{2}))?\\s*(am|pm)?', text.lower())\n",
    "\n",
    "    if not match:\n",
    "        return None\n",
    "\n",
    "    h = int(match.group(1))\n",
    "    m = int(match.group(2) or 0)\n",
    "    p = match.group(3)\n",
    "\n",
    "    if p == \"pm\" and h != 12:\n",
    "        h += 12\n",
    "    if p == \"am\" and h == 12:\n",
    "        h = 0\n",
    "\n",
    "    return h, m\n",
    "\n",
    "\n",
    "def resolve_date(text):\n",
    "    if \"tomorrow\" in text.lower():\n",
    "        return dt.date.today() + dt.timedelta(days=1)\n",
    "    return dt.date.today()\n",
    "\n",
    "\n",
    "def build_datetime(text):\n",
    "    t = normalize_time(text)\n",
    "    if not t:\n",
    "        return None\n",
    "    return dt.datetime.combine(resolve_date(text), dt.time(*t))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c1d5fba-fd20-4c9e-bf84-2bee25a3a709",
   "metadata": {},
   "source": [
    "## — EMAIL FETCH"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc4260bb-e28f-41d7-bba3-9ddd61f7d119",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fetches unread Gmail subjects or manual emails depending on mode.\n",
    "\n",
    "def fetch_gmail():\n",
    "    inbox = []\n",
    "\n",
    "    try:\n",
    "        mail = imaplib.IMAP4_SSL(\"imap.gmail.com\")\n",
    "        mail.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)\n",
    "        mail.select(\"inbox\")\n",
    "\n",
    "        _, messages = mail.search(None, \"UNSEEN\")\n",
    "\n",
    "        for num in messages[0].split():\n",
    "            _, data = mail.fetch(num, \"(RFC822)\")\n",
    "\n",
    "            for part in data:\n",
    "                if isinstance(part, tuple):\n",
    "                    msg = email.message_from_bytes(part[1])\n",
    "                    subject = msg[\"Subject\"]\n",
    "                    if subject:\n",
    "                        inbox.append(subject)\n",
    "\n",
    "        mail.logout()\n",
    "\n",
    "    except Exception as e:\n",
    "        print(\"IMAP ERROR:\", e)\n",
    "\n",
    "    return inbox\n",
    "\n",
    "\n",
    "def get_emails():\n",
    "    return fetch_gmail() if USE_GMAIL else emails_manual"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05a704d5-1ef8-430f-bed0-c6cdba150c2f",
   "metadata": {},
   "source": [
    "## — DATABASE SAVE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7cd75fc-f5a2-435b-92c3-f17e118552eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saves only unique important tasks and tracks pending alerts.\n",
    "\n",
    "def save_task(text, deadline):\n",
    "\n",
    "    cursor.execute(\n",
    "        \"SELECT id FROM tasks WHERE text=? AND deadline=?\",\n",
    "        (text, str(deadline))\n",
    "    )\n",
    "\n",
    "    if cursor.fetchone():\n",
    "        return\n",
    "\n",
    "    cursor.execute(\n",
    "        \"INSERT INTO tasks (text, deadline, alerted) VALUES (?, ?, 0)\",\n",
    "        (text, str(deadline))\n",
    "    )\n",
    "\n",
    "    conn.commit()\n",
    "\n",
    "\n",
    "def load_tasks():\n",
    "    cursor.execute(\"SELECT id, text, deadline FROM tasks WHERE alerted=0\")\n",
    "\n",
    "    tasks = []\n",
    "\n",
    "    for r in cursor.fetchall():\n",
    "        tasks.append({\n",
    "            \"id\": r[0],\n",
    "            \"text\": r[1],\n",
    "            \"deadline\": dt.datetime.fromisoformat(r[2])\n",
    "        })\n",
    "\n",
    "    return tasks\n",
    "\n",
    "\n",
    "def mark_alerted(task_id):\n",
    "    cursor.execute(\"UPDATE tasks SET alerted=1 WHERE id=?\", (task_id,))\n",
    "    conn.commit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a9f2d71-f605-4e83-b61a-f851f93a008a",
   "metadata": {},
   "source": [
    "## — ALERT SYSTEM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6ddf7ac-2fe6-4d43-a758-e124a932cc5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Shows popup alert window when deadline reminder time arrives.\n",
    "\n",
    "def show_popup(text):\n",
    "\n",
    "    window = tk.Tk()\n",
    "    window.geometry(\"320x150\")\n",
    "    window.configure(bg=\"#87CEEB\")\n",
    "    window.overrideredirect(True)\n",
    "\n",
    "    # =========================================\n",
    "    # CUSTOM TITLE BAR (DEEP BLUE)\n",
    "    # =========================================\n",
    "    title_bar = tk.Frame(window, bg=\"#0A2A66\")\n",
    "    title_bar.pack(fill=\"x\")\n",
    "\n",
    "    title_label = tk.Label(\n",
    "        title_bar,\n",
    "        text=\"⏰ ALERT\",\n",
    "        bg=\"#0A2A66\",\n",
    "        fg=\"white\",\n",
    "        font=(\"Segoe UI\", 12, \"bold\")\n",
    "    )\n",
    "    title_label.pack(side=\"left\", padx=12, pady=6)\n",
    "\n",
    "    close_button = tk.Button(\n",
    "        title_bar,\n",
    "        text=\"✖\",\n",
    "        bg=\"#0A2A66\",\n",
    "        fg=\"white\",\n",
    "        bd=0,\n",
    "        activebackground=\"#08204D\",\n",
    "        activeforeground=\"white\",\n",
    "        font=(\"Segoe UI\", 11, \"bold\"),\n",
    "        command=window.destroy\n",
    "    )\n",
    "    close_button.pack(side=\"right\", padx=10)\n",
    "\n",
    "    # =========================================\n",
    "    # MAIN ALERT AREA\n",
    "    # =========================================\n",
    "    tk.Label(\n",
    "        window,\n",
    "        text=\"—— DEADLINE ALERT ——\",\n",
    "        bg=\"#87CEEB\",\n",
    "        fg=\"#0A2A66\",\n",
    "        font=(\"Segoe UI\", 16, \"bold\")\n",
    "    ).pack(pady=18)\n",
    "\n",
    "    tk.Label(\n",
    "        window,\n",
    "        text=text,\n",
    "        bg=\"#87CEEB\",\n",
    "        fg=\"black\",  # off-black\n",
    "        font=(\"Segoe UI\", 12, \"bold\"),\n",
    "        wraplength=360,\n",
    "        justify=\"center\"\n",
    "    ).pack(pady=10)\n",
    "\n",
    "    # Center window\n",
    "    window.update_idletasks()\n",
    "    width = window.winfo_width()\n",
    "    height = window.winfo_height()\n",
    "    x = (window.winfo_screenwidth() // 2) - (width // 2)\n",
    "    y = (window.winfo_screenheight() // 2) - (height // 2)\n",
    "    window.geometry(f\"{width}x{height}+{x}+{y}\")\n",
    "\n",
    "    window.mainloop()\n",
    "\n",
    "def trigger(task):\n",
    "    print(\"ALERT:\", task[\"text\"])\n",
    "    show_popup(task[\"text\"])\n",
    "    mark_alerted(task[\"id\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bc1fd2f-83d7-484d-a428-614f8782c2f3",
   "metadata": {},
   "source": [
    "## — SMART SCHEDULER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebeea883-9f19-4d98-87d5-19d17a3e66ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Filters emails using ML, extracts deadlines, and saves valid tasks.\n",
    "\n",
    "\n",
    "scheduled = set()\n",
    "\n",
    "def schedule(task):\n",
    "\n",
    "    key = task[\"id\"]\n",
    "    if key in scheduled:\n",
    "        return\n",
    "\n",
    "    now = dt.datetime.now()\n",
    "    deadline = task[\"deadline\"]\n",
    "\n",
    "    diff = (deadline - now).total_seconds()\n",
    "\n",
    "    if diff <= 0:\n",
    "        return\n",
    "\n",
    "    # YOUR RULES\n",
    "    if diff > 3 * 3600:\n",
    "        alert_time = deadline - dt.timedelta(hours=3)\n",
    "\n",
    "    elif 2 * 3600 < diff <= 3 * 3600:\n",
    "        alert_time = now + dt.timedelta(minutes=30)\n",
    "\n",
    "    elif 1 * 3600 < diff <= 2 * 3600:\n",
    "        alert_time = now + dt.timedelta(minutes=10)\n",
    "\n",
    "    else:\n",
    "        alert_time = now + dt.timedelta(minutes=1)\n",
    "\n",
    "    delay = max((alert_time - now).total_seconds(), 1)\n",
    "\n",
    "    scheduled.add(key)\n",
    "\n",
    "    threading.Timer(delay, trigger, args=(task,)).start()\n",
    "\n",
    "    print(\"Scheduled:\", task[\"text\"], \"->\", alert_time)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9dd37c23-e07c-441c-b7bb-86491f51986e",
   "metadata": {},
   "source": [
    "## — PROCESS PIPELINE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d96c4ffc-6bbc-4c4a-b99a-5fe2fa386f9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Filters emails using ML, extracts deadlines, and saves valid tasks.\n",
    "\n",
    "def process():\n",
    "\n",
    "    emails = get_emails()\n",
    "\n",
    "    for text in emails:\n",
    "\n",
    "        if not is_important(text):\n",
    "            continue\n",
    "\n",
    "        deadline = build_datetime(text)\n",
    "\n",
    "        if deadline:\n",
    "            save_task(text, deadline)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c100030-2e71-495c-905e-c2f7cb68f98d",
   "metadata": {},
   "source": [
    "## — MAIN LOOP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "312a51eb-5b2c-4b6a-b99d-6a74524b7468",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Continuously checks emails, schedules tasks, and repeats forever.\n",
    "\n",
    "def run():\n",
    "\n",
    "    while True:\n",
    "\n",
    "        process()\n",
    "\n",
    "        tasks = load_tasks()\n",
    "\n",
    "        for t in tasks:\n",
    "            schedule(t)\n",
    "\n",
    "        time.sleep(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbb1b844-940f-4490-94d8-f70572b6f235",
   "metadata": {},
   "source": [
    "## — START POINT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20563f09-6306-4846-a125-ffa300f0bd4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Starts background reminder engine and keeps program alive.\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    print(\"System Started...\")\n",
    "\n",
    "    threading.Thread(target=run, daemon=True).start()\n",
    "\n",
    "    while True:\n",
    "        time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10aef496-031b-4a85-b8b9-79087e9bad46",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37744116-5d74-4b20-b27a-73e3e0329e76",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
