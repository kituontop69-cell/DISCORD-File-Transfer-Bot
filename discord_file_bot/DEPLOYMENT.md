# Deployment Guide for Railway

This guide will walk you through deploying your Discord bot on Railway.

## What is Railway?

Railway is a modern deployment platform that makes it easy to deploy applications. It's free to start and scales with your needs.

## Prerequisites

Before you start:
- ✅ Completed Discord bot setup locally
- ✅ Bot token (from Discord Developer Portal)
- ✅ GitHub account
- ✅ Railway account (free at railway.app)

## Complete Deployment Steps

### Phase 1: Prepare Your Code (5 minutes)

#### 1.1 Create .gitignore

Make sure `.gitignore` exists and includes:
```
.env
__pycache__/
*.pyc
logs/
```

#### 1.2 Create Procfile

Already created: `Procfile`
```
worker: python main.py
```

#### 1.3 Create runtime.txt

Already created: `runtime.txt`
```
python-version = "3.11"
```

### Phase 2: Push to GitHub (5 minutes)

#### 2.1 Initialize Repository

```bash
cd discord_file_bot
git init
git add .
git commit -m "Discord file bot - initial commit"
```

#### 2.2 Create Repository on GitHub

1. Go to https://github.com/new
2. Name it `discord-file-bot`
3. Click "Create repository"

#### 2.3 Push Code

```bash
git remote add origin https://github.com/YOUR_USERNAME/discord-file-bot.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### Phase 3: Deploy on Railway (5 minutes)

#### 3.1 Connect Railway to GitHub

1. Go to https://railway.app
2. Click "Deploy Now" button
3. Authorize GitHub
4. Select your `discord-file-bot` repository

#### 3.2 Add Environment Variables

After selecting the repo, Railway will show "Environment Variables" section:

1. Click "Add Variable"
2. Add these variables:

| Variable | Value | Required |
|----------|-------|----------|
| DISCORD_TOKEN | your_bot_token | ✅ Yes |
| COMMAND_PREFIX | ! | ⭕ Optional |
| LOG_LEVEL | INFO | ⭕ Optional |

#### 3.3 Deploy

1. Click "Deploy" button
2. Railway builds and deploys automatically
3. Wait for green checkmark (✅ Success)

**This takes 1-2 minutes**

#### 3.4 Verify Deployment

1. Go to your project in Railway
2. Click on the service
3. Click "Logs" tab
4. Look for:
   ```
   ✅ Bot logged in as YourBotName
   ✅ Bot is ready and online!
   ```

### Phase 4: Test Your Bot

#### 4.1 Online Test

In your Discord server:
```
!fileinfo
```

You should see bot response with file information.

#### 4.2 File Transfer Test

1. Upload a `.rar` file
2. Run: `!sendfile @someone`
3. Check if file appears in user's DM

#### 4.3 Check Logs

In Railway dashboard:
- Go to Logs tab
- You'll see all bot activity in real-time

---

## Auto-Deployment

After initial setup, Railway automatically redeploys when you push to GitHub:

```bash
# Make changes locally
# ... edit files ...

# Commit and push
git add .
git commit -m "Added new feature"
git push origin main

# Railway automatically redeploys (takes 1-2 minutes)
```

---

## File Structure for Railway

Railway expects this structure:
```
discord_file_bot/
├── main.py                 # Entry point (Procfile runs this)
├── Procfile                # How to run the app
├── runtime.txt             # Python version
├── requirements.txt        # Dependencies
├── config/
├── commands/
├── events/
├── utils/
└── .gitignore
```

All files are already set up correctly! ✅

---

## Troubleshooting Railway Deployment

### ❌ Deployment Failed

**Check these things:**

1. **Invalid DISCORD_TOKEN**
   - Go to Variables
   - Verify token is correct (no spaces)
   - Token should start with `MzA...` or `Nzg...`

2. **Missing requirements.txt**
   - File should exist in root directory
   - Should contain: `discord.py==2.4.0` and `python-dotenv==1.0.0`

3. **Wrong Python version**
   - Check `runtime.txt` says `python-version = "3.11"`

4. **Missing .env variables**
   - DISCORD_TOKEN is required
   - Other variables have defaults

### ❌ Bot Logs Show Errors

Check the error type:

```
❌ DISCORD_TOKEN environment variable is not set!
→ Add DISCORD_TOKEN to Railway Variables

❌ Connection refused
→ Discord API issue, retry in 1 minute

❌ Invalid token
→ Token is expired, get new one from Developer Portal
```

### ❌ Bot is Online but Not Responding

1. Check bot has permissions in server
2. Verify prefix is correct (`!` by default)
3. Restart service in Railway (restart button)

### ❌ Memory/CPU Issues

Railway free tier includes:
- 500 hours/month runtime
- 100MB RAM (enough for this bot)
- No sleep mode needed

If hitting limits, upgrade to paid plan.

---

## Monitoring

### View Real-Time Logs

```
Railway Dashboard → Project → Logs
```

### Check Bot Status

```
Railway Dashboard → Project → Deployments
```

Shows:
- Current status
- Deployment history
- Resource usage

### Save Important Logs

```bash
# Download logs periodically
# Right-click in Logs tab → Copy → Save to file
```

---

## Maintenance

### Update Bot Code

```bash
# Edit files locally
# Test locally
# Push to GitHub
git add .
git commit -m "description"
git push origin main

# Railway auto-deploys in 1-2 minutes
```

### Update Dependencies

```bash
# Add new dependency
pip install new_package

# Update requirements.txt
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Updated dependencies"
git push origin main
```

### Rotate Token

If token is compromised:
1. Go to Discord Developer Portal
2. Regenerate bot token
3. Update DISCORD_TOKEN in Railway Variables
4. Restart bot service

---

## Cost Analysis

**Railway Pricing:**
- First $5/month: FREE
- This bot costs: ~$0-2/month
- Generous free tier ✅

**What you get:**
- Always-on hosting
- Automatic backups
- Real-time monitoring
- Easy scaling

---

## Next Steps

1. ✅ Deploy on Railway (complete this first)
2. 📊 Monitor logs for 24 hours
3. 🔄 Test file transfers thoroughly
4. 🚀 Tell users about the bot
5. 📈 Scale if needed

---

## Useful Links

- **Railway Docs:** https://docs.railway.app
- **Discord.py Docs:** https://discordpy.readthedocs.io
- **Python Docs:** https://docs.python.org/3.11

---

## Need Help?

1. Check `README.md` for full documentation
2. Review logs in Railway dashboard
3. Search error message in Google
4. Ask in Discord.py community

---

**🎉 Congratulations! Your bot is deployed and running on Railway!**
