import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import os
from datetime import datetime, timezone

# --- INDIA AI & TECH TOOLS CONFIG (Swap keywords anytime to adapt trends) ---
NICHE_TOPICS = [
    "free AI tools",
    "AI website students India",
    "ChatGPT Claude Gemini update",
    "free coding productivity tools",
    "AI automation side hustle"
]
GEO = "IN"
DM_KEYWORD = "TOOL"
HUB_DESCRIPTION = "the direct link + my Free 2026 AI Toolkit"
# ----------------------------------------------------------------------------


def fetch_rss(url, limit=5):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        root = ET.fromstring(resp.read())
    items = []
    for item in root.findall(".//item")[:limit]:
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        if title:
            items.append((title, link))
    return items


def build_indian_reel_script(topic_title):
    short_topic = topic_title[:65]
    return (
        f"### Topic: {topic_title}\n"
        f"- **0-3s Visual Hook (Text on Screen):** *\"Stop paying for this—new free AI tool just dropped\"*\n"
        f"- **0-3s Spoken Hook:** \"Agar aap abhi bhi manually kaam kar rahe ho, toh '{short_topic}' dekh lo.\"\n"
        f"- **3-20s Screen Recording:** Open the tool/news on screen and zoom into 2 specific clicks showing the exact result live.\n"
        f"- **20-27s CTA:** \"Comment **{DM_KEYWORD}** and I'll auto-DM you {HUB_DESCRIPTION}. Follow for daily AI hacks!\"\n"
        f"- **Caption:** Save this Reel before you forget the tool name. Comment **{DM_KEYWORD}** below #aitoolsindia #techindia #freeaitools #indianstudents\n"
    )


def send_telegram(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Telegram secrets not configured; skipping Telegram delivery.")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": message[:4000],
        "parse_mode": "Markdown"
    }).encode("utf-8")
    urllib.request.urlopen(urllib.request.Request(url, data=payload), timeout=15)


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = [f"# Daily India AI & Tech Reel Scripts ({today})\n"]

    # 1. Broad India rising trends for optional newsjacking
    trends_url = f"https://trends.google.com/trending/rss?geo={GEO}"
    try:
        broad_trends = fetch_rss(trends_url, limit=3)
        report.append("## Broad Rising Trends (India)\n")
        for title, _ in broad_trends:
            report.append(f"- **{title}**\n")
        report.append("\n")
    except Exception as e:
        report.append(f"*(Google Trends skipped: {e})*\n\n")

    # 2. Niche-specific AI & Tech Reel scripts
    report.append("## Ready-to-Record AI & Tech Reel Scripts\n")
    for niche in NICHE_TOPICS:
        q = urllib.parse.quote(niche)
        news_url = (
            f"https://news.google.com/rss/search?"
            f"q={q}+when:3d&hl=en-{GEO}&gl={GEO}&ceid={GEO}:en"
        )
        try:
            items = fetch_rss(news_url, limit=2)
            for title, _ in items:
                clean_title = title.rsplit(" - ", 1)[0]
                report.append(build_indian_reel_script(clean_title) + "\n---\n")
        except Exception as e:
            report.append(f"*(Fetch skipped for {niche}: {e})*\n")

    output = "\n".join(report)
    os.makedirs("daily_scripts", exist_ok=True)
    with open(f"daily_scripts/{today}.md", "w", encoding="utf-8") as f:
        f.write(output)

    send_telegram(output)
    print(f"Generated daily_scripts/{today}.md successfully.")


if __name__ == "__main__":
    main()
