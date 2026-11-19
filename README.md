# India AI & Tech Instagram Funnel

A free-tier content workflow and mobile-first Link Hub for an India-focused AI & Tech Instagram account. The trend engine uses public Google Trends and Google News RSS feeds and creates daily Reel script drafts. It does not publish to Instagram or send Instagram DMs.

## Daily trend workflow

GitHub Actions runs `.github/workflows/daily_trends.yml` daily at 08:00 IST and can also be started manually from **Actions → Daily Instagram Trend Engine → Run workflow**. Generated reports are committed under `daily_scripts/`. The workflow has `contents: write` permission for this commit step.

To enable Telegram delivery, open **Settings → Secrets and variables → Actions → New repository secret** and add:

- `TELEGRAM_BOT_TOKEN` — create a bot with Telegram's official `@BotFather` and copy its token directly into GitHub Secrets.
- `TELEGRAM_CHAT_ID` — the destination chat ID for the bot.

Never commit tokens or passwords. The workflow safely skips Telegram delivery when either secret is missing.

## GitHub Pages Link Hub

In **Settings → Pages**, select **Deploy from a branch**, branch `main`, folder `/ (root)`, then save. The Link Hub will be served at `https://<github-username>.github.io/ig-ai-funnel/` after the Pages build completes.

Edit `index.html` to replace these placeholders with your real destinations:

- `YOUR_TOPMATE_PRODUCT_LINK` — your ₹149 PDF product page.
- `YOUR_FEATURED_REEL_TOOL_LINK` — current featured tool link.
- `YOUR_HOSTINGER_AFFILIATE_LINK` — optional Hostinger India affiliate URL.
- `YOUR_AMAZON_IN_AFFILIATE_LINK` — optional Amazon Associates India link.

Commit the edit to `main`; GitHub Pages will redeploy. Disclose affiliate relationships as required by the relevant platform and applicable rules.

## Account safety

This repository does not automate Instagram logins, posting, or DMs. Set up publishing manually through Meta Business Suite and use an official Meta OAuth flow for any comment-to-DM provider. Never share account passwords with a bot or store them in this repository.
