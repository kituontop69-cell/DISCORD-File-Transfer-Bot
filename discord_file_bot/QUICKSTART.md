# Quick Start Guide

## Local Setup (5 minutes)

### 1. Get Discord Bot Token

1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Go to "Bot" tab → "Add Bot"
4. Copy your bot token

### 2. Create .env File

```bash
# Copy the example
copy .env.example .env

# Edit .env and add your token:
# DISCORD_TOKEN=your_token_here
```

### 3. Install & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
```

You should see: `✅ Bot logged in as YourBotName`

### 4. Invite Bot to Server

1. In Discord Developer Portal, go to OAuth2 > URL Generator
2. Select scopes: `bot`
3. Select permissions: `Send Messages`, `Read Message History`, `Attach Files`, `Read Messages/View Channels`
4. Copy URL and open in browser
5. Select server and authorize

---

## Railway Deployment (5 minutes)

### Prerequisites
- GitHub account
- Railway account (free tier available at railway.app)

### Step 1: Setup GitHub Repository

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial Discord bot setup"

# Add your GitHub repo as remote
git remote add origin https://github.com/YOUR_USERNAME/discord-file-bot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Railway

1. **Go to Railway Dashboard**
   - Visit https://railway.app
   - Sign in with GitHub

2. **Create New Project**
   - Click "+ New Project"
   - Select "Deploy from GitHub repo"
   - Choose your discord-file-bot repository
   - Authorize GitHub access

3. **Add Environment Variables**
   - In Railway dashboard, go to your project
   - Click on the service
   - Go to "Variables" tab
   - Add these variables:
     ```
     DISCORD_TOKEN=your_bot_token_here
     COMMAND_PREFIX=!
     LOG_LEVEL=INFO
     ```

4. **Deploy**
   - Railway auto-deploys when you push to GitHub
   - Check "Deployments" tab for status
   - Wait for "✅ Success" status

5. **View Logs**
   - Go to "Logs" tab
   - You should see: `✅ Bot logged in as YourBotName`
   - And: `✅ Bot is ready and online!`

---

## Testing the Bot

### Test 1: Check If Bot is Online

In your Discord server:
```
!fileinfo
```

You should see a message with allowed file types and limits.

### Test 2: Send a File

1. Upload a `.rar`, `.msg`, or `.apk` file to Discord
2. Use command:
   ```
   !sendfile @username
   ```
3. File should appear in user's DM

### Test 3: Check Logs

**Local:**
```
# Check logs folder
logs/bot_2024-XX-XX.log
```

**Railway:**
- Go to project → Logs tab
- Real-time logs shown here

---

## Common Issues & Solutions

### Bot not responding
```
❌ Problem: Bot doesn't respond to commands

✅ Solution:
1. Check token in .env is correct
2. Verify bot has permissions in server
3. Check bot prefix (!sendfile not !sendfile)
4. Restart bot
```

### File not sending
```
❌ Problem: File not delivered to user DM

✅ Solution:
1. Check file size (max 25MB)
2. Check file extension (.rar, .msg, .apk, etc)
3. Verify user hasn't blocked DMs
4. Check logs for error messages
```

### Railway deployment failed
```
❌ Problem: Deployment shows error

✅ Solution:
1. Check DISCORD_TOKEN in variables
2. Verify token is current (not revoked)
3. Check logs for error details
4. Ensure requirements.txt is correct
5. Try redeploying (push commit to GitHub)
```

### Bot keeps crashing
```
❌ Problem: Bot crashes repeatedly

✅ Solution:
1. Check logs for error
2. Verify all imports in code
3. Check .env variables are set
4. Ensure Python version is 3.11+
```

---

## Useful Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run bot locally
python main.py

# Stop bot (in terminal)
Ctrl+C

# Check Python version
python --version

# View logs (local)
type logs/bot_*.log
```

---

## Next Steps

After deployment:

1. **Monitor** - Keep an eye on Railway logs
2. **Scale** - Add more features if needed
3. **Backup** - Keep your .env token safe
4. **Update** - Push improvements to GitHub (auto-deploys)

---

## Support

**Check these files for help:**
- `README.md` - Full documentation
- `logs/bot_*.log` - Detailed error logs
- `.env.example` - Configuration template

🎉 **Your bot is ready!**
