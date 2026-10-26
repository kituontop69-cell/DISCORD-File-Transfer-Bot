# Getting Started Checklist

Complete these steps in order to get your bot running.

## Step 1: Discord Developer Setup (5 minutes)

- [ ] Go to https://discord.com/developers/applications
- [ ] Click "New Application"
- [ ] Name it (e.g., "File Transfer Bot")
- [ ] Go to "Bot" tab
- [ ] Click "Add Bot"
- [ ] Under "TOKEN", click "Copy"
- [ ] Save token somewhere safe
- [ ] Go to "Intents" section
- [ ] Enable: "Message Content Intent"
- [ ] Enable: "Server Members Intent"
- [ ] Click "Save Changes"
- [ ] Go to OAuth2 > URL Generator
- [ ] Select scopes: `bot`
- [ ] Select permissions: `Send Messages`, `Read Message History`, `Attach Files`, `Read Messages/View Channels`
- [ ] Copy generated URL
- [ ] Paste URL in browser
- [ ] Select your test server
- [ ] Click "Authorize"

**Result:** Bot should appear in your server's member list ✅

---

## Step 2: Local Setup (5 minutes)

### 2.1 Configure Environment

```bash
# Navigate to bot folder
cd discord_file_bot

# Copy example .env file
copy .env.example .env

# Edit .env file and paste your token:
# DISCORD_TOKEN=paste_your_token_here
```

### 2.2 Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed discord.py-2.4.0 python-dotenv-1.0.0
```

### 2.3 Run Bot Locally

```bash
python main.py
```

**Expected output:**
```
✅ Bot logged in as YourBotName
✅ Configuration validated
✅ Loaded 3 cog(s)
✅ Bot is ready and online!
```

- [ ] Bot starts without errors
- [ ] See "Bot is ready and online!"
- [ ] No error messages

**Result:** Bot is running locally ✅

---

## Step 3: Test Bot Locally (5 minutes)

In your Discord server, test each command:

### Test Command 1: File Info
```
!fileinfo
```
- [ ] Bot responds with file specifications
- [ ] Shows allowed file types
- [ ] Shows maximum file size

### Test Command 2: Send Valid File
```
!sendfile @your_username
```
Then attach a `.rar` file

- [ ] Bot accepts the file
- [ ] Shows success message
- [ ] File appears in your DM

### Test Command 3: Send Invalid File
```
!sendfile @username
```
Then attach a `.txt` file

- [ ] Bot rejects the file
- [ ] Shows error message explaining why

### Test Command 4: Help
```
!help
```
- [ ] Shows command list
- [ ] Shows command descriptions

**Result:** All commands work locally ✅

---

## Step 4: Prepare for Railway (5 minutes)

### 4.1 Create GitHub Repository

- [ ] Go to https://github.com/new
- [ ] Create repository named `discord-file-bot`
- [ ] Do NOT add README, .gitignore, or license
- [ ] Click "Create repository"

### 4.2 Initialize Git

```bash
cd discord_file_bot

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Discord file bot - production ready"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/discord-file-bot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

- [ ] Code pushed to GitHub
- [ ] No `.env` file in repository (should be ignored)
- [ ] All other files present

**Result:** Code is on GitHub ✅

---

## Step 5: Deploy on Railway (5 minutes)

### 5.1 Connect Railway

- [ ] Go to https://railway.app
- [ ] Sign in with GitHub
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Authorize GitHub
- [ ] Select `discord-file-bot` repository

### 5.2 Configure Environment Variables

- [ ] Railway shows "Environment Variables" tab
- [ ] Add variable: `DISCORD_TOKEN` = `your_token_here`
- [ ] Add variable: `COMMAND_PREFIX` = `!`
- [ ] Add variable: `LOG_LEVEL` = `INFO`
- [ ] Save variables

### 5.3 Deploy

- [ ] Click "Deploy" button
- [ ] Wait for deployment to complete (1-2 minutes)
- [ ] Look for green checkmark ✅

### 5.4 Verify Deployment

- [ ] Go to "Logs" tab
- [ ] Look for: "✅ Bot logged in as YourBotName"
- [ ] Look for: "✅ Bot is ready and online!"
- [ ] No error messages

**Result:** Bot deployed on Railway ✅

---

## Step 6: Test on Railway (5 minutes)

In your Discord server, test commands:

- [ ] `!fileinfo` - Bot responds
- [ ] `!sendfile @user` with .rar file - File sent to DM
- [ ] `!sendfile @user` with .apk file - File sent to DM
- [ ] Check Railway logs - All operations logged

**Result:** Bot works on Railway ✅

---

## Final Checklist

### ✅ Setup Complete When:
- [ ] Bot token generated
- [ ] .env file configured
- [ ] Dependencies installed
- [ ] Bot runs locally without errors
- [ ] All local tests pass
- [ ] Code pushed to GitHub
- [ ] Railway deployment successful
- [ ] All Railway tests pass
- [ ] Logs show bot online

### ✅ Troubleshooting Needed If:
- [ ] Bot doesn't run locally
- [ ] Commands don't respond
- [ ] Files not sending
- [ ] Railway deployment fails
- [ ] Logs show errors

**Refer to:**
- Local issues → `QUICKSTART.md`
- Railway issues → `DEPLOYMENT.md`
- Test issues → `TESTING.md`
- General help → `README.md`

---

## Success! 🎉

Your Discord file transfer bot is now:
- ✅ Running locally
- ✅ Deployed on Railway
- ✅ Tested and working
- ✅ Production ready

### What's Next?

1. **Monitor** - Check Railway logs daily
2. **Test** - Run file transfers weekly
3. **Update** - Push improvements to GitHub (auto-deploys)
4. **Scale** - Add more features if needed

---

## Important Notes

⚠️ **SECURITY:**
- Never share your bot token
- Keep `.env` file private
- Don't commit `.env` to GitHub
- Use environment variables for secrets

✅ **BEST PRACTICES:**
- Keep bot token safe
- Monitor logs regularly
- Test before deploying updates
- Update dependencies periodically

📞 **NEED HELP?**
- Check relevant guide (.md files)
- Review logs for error details
- Try restarting bot/deployment
- Search error message online

---

**Congratulations! Your bot is production-ready! 🚀**
