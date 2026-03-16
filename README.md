# BD2 Command Center

Sales intelligence platform built for Cardone Ventures. Single-page app powered by Claude AI, hosted on GitHub Pages.

## Quick Start

1. Open [ducommun509.github.io/bd2-command-center](https://ducommun509.github.io/bd2-command-center/)
2. Enter the access password when prompted
3. Enter your Anthropic API key (starts with `sk-ant-`) to activate AI features
4. You're in — the key saves automatically for next time

## Features

- **Dashboard** — Daily stats, targets, activity feed, XP tracking
- **Deal Builder** — Pipeline management with stage tracking (Prospecting → Close)
- **Calls** — Call logging, history, and performance stats
- **1 Call Closer** — Guided close workflow
- **AI Brain** — Claude-powered sales intelligence and chat
- **Briefing** — Daily prep and AI-generated insights
- **Workflows** — Automated sales processes
- **Knowledge** — Sales playbook and reference material
- **Agents** — AI agent configurations
- **Analytics** — Performance dashboards and trends
- **Data OS** — Data management layer
- **Dialer.io** — Integrated dialing

## How It Works

BD2 is a **single HTML file** (`index.html`) hosted via GitHub Pages. All data is stored in the browser's `localStorage` — there's no backend database. This means:

- Data is **per-device, per-browser** (Chrome on your laptop ≠ Safari on your phone)
- Clearing browser data will reset your BD2 state
- The Anthropic API key is stored locally and sent directly to `api.anthropic.com`

## Getting an Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Navigate to **Settings → API Keys**
4. Click **Create Key**, copy it
5. Paste it into BD2 when prompted (or in the key input field on first load)

## Editing & Deploying

Since BD2 is hosted on GitHub Pages, **pushing to `main` automatically deploys**. Changes go live within 1–2 minutes.

### Option A: Edit from Any Device via Codespaces

1. Go to [github.com/Ducommun509/bd2-command-center](https://github.com/Ducommun509/bd2-command-center)
2. Click the green **Code** button → **Codespaces** tab → **Create codespace on main**
3. Edit `index.html` in the VS Code editor
4. Open the terminal in Codespaces and run:
   ```bash
   python3 deploy.py
   ```
   Or manually:
   ```bash
   git add index.html
   git commit -m "your change description"
   git push
   ```

### Option B: Edit Locally

```bash
git clone https://github.com/Ducommun509/bd2-command-center.git
cd bd2-command-center
# make your edits to index.html
python3 deploy.py
```

### Option C: Quick Deploy Script

```bash
python3 deploy.py "description of your change"
```

The deploy script handles staging, committing, and pushing in one command.

## Testing Locally

Open `index.html` directly in your browser — everything works locally since it's a self-contained HTML file. No server needed.

```bash
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

## Project Structure

```
bd2-command-center/
├── index.html          # The entire app (HTML + CSS + JS)
├── deploy.py           # One-command deploy script
├── .devcontainer/      # Codespaces configuration
│   └── devcontainer.json
└── README.md           # This file
```

## Troubleshooting

**AI features not responding?**
→ Check that your API key is valid at [console.anthropic.com](https://console.anthropic.com). Re-enter it in BD2 if needed.

**Data missing after switching devices?**
→ BD2 stores data in localStorage (browser-specific). Data doesn't sync across devices automatically.

**Page won't load after a push?**
→ GitHub Pages can take 1–2 minutes to redeploy. Check the deployment status at [github.com/Ducommun509/bd2-command-center/deployments](https://github.com/Ducommun509/bd2-command-center/deployments).

**Access password not working?**
→ The session expires after 24 hours. Re-enter the password to continue.
