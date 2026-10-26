# Testing Checklist

Use this checklist to ensure everything works before deployment.

## Pre-Deployment Testing

### ✅ Local Setup (Before Running)
- [ ] Python 3.11+ installed (`python --version`)
- [ ] `.env` file created from `.env.example`
- [ ] Discord bot token added to `.env`
- [ ] All files created successfully
- [ ] Project structure is correct

### ✅ Local Runtime (Start Bot)
- [ ] `pip install -r requirements.txt` completed
- [ ] `python main.py` starts without errors
- [ ] See "✅ Bot logged in as YourBotName"
- [ ] See "✅ Bot is ready and online!"
- [ ] No errors in console

### ✅ Bot Permissions (Discord Server)
- [ ] Bot joined the server
- [ ] Bot appears in member list
- [ ] Bot has "Administrator" or these permissions:
  - Send Messages
  - Read Messages/View Channels
  - Attach Files
  - Read Message History

### ✅ Command Tests (Local)

**Test 1: Help Command**
```
Input: !help
Expected: List of commands
Status: ✅ Pass / ❌ Fail
```

**Test 2: File Info**
```
Input: !fileinfo
Expected: Shows allowed file types and limits
Status: ✅ Pass / ❌ Fail
```

**Test 3: Send Invalid File**
```
Input: !sendfile @user (with .txt file)
Expected: ❌ File type not allowed
Status: ✅ Pass / ❌ Fail
```

**Test 4: Send Valid File - RAR**
```
Input: !sendfile @user (with .rar file)
Expected: ✅ File sent to user's DM
Status: ✅ Pass / ❌ Fail
Details: Check user's DM for file
```

**Test 5: Send Valid File - APK**
```
Input: !sendfile @user (with .apk file)
Expected: ✅ File sent to user's DM
Status: ✅ Pass / ❌ Fail
Details: Check user's DM for file
```

**Test 6: Send Valid File - MSG**
```
Input: !sendfile @user (with .msg file)
Expected: ✅ File sent to user's DM
Status: ✅ Pass / ❌ Fail
Details: Check user's DM for file
```

**Test 7: Send File - No User**
```
Input: !sendfile (no @user mention)
Expected: ❌ User not specified
Status: ✅ Pass / ❌ Fail
```

**Test 8: Send File - No Attachment**
```
Input: !sendfile @user (no file attached)
Expected: ❌ No file attached
Status: ✅ Pass / ❌ Fail
```

**Test 9: File Too Large**
```
Input: !sendfile @user (with 30MB file)
Expected: ❌ File too large
Status: ✅ Pass / ❌ Fail
```

### ✅ Error Handling
- [ ] Graceful error messages shown
- [ ] No bot crashes on errors
- [ ] Logs capture all errors
- [ ] User receives helpful feedback

### ✅ Logging
- [ ] `logs/` folder created
- [ ] `logs/bot_YYYY-MM-DD.log` file created
- [ ] Logs contain timestamps
- [ ] Successful operations logged
- [ ] Errors logged with details

---

## Pre-Deployment Railway Checks

### ✅ Code Ready
- [ ] No local `.env` committed to GitHub
- [ ] `.gitignore` includes `.env`
- [ ] `.gitignore` includes `__pycache__/`
- [ ] `.gitignore` includes `logs/`
- [ ] `requirements.txt` has all dependencies
- [ ] `Procfile` is correct (`worker: python main.py`)
- [ ] `runtime.txt` specifies Python 3.11

### ✅ GitHub Setup
- [ ] Repository created on GitHub
- [ ] All files pushed to GitHub
- [ ] `main` branch is default
- [ ] No `.env` file in repository

### ✅ Railway Setup
- [ ] Railway account created
- [ ] Project created in Railway
- [ ] GitHub repository connected
- [ ] `DISCORD_TOKEN` variable added
- [ ] Token value is correct (no spaces)
- [ ] `COMMAND_PREFIX` set to `!` (optional)
- [ ] `LOG_LEVEL` set to `INFO` (optional)

---

## Post-Deployment Testing (On Railway)

### ✅ Deployment Status
- [ ] Deployment shows "✅ Success"
- [ ] Green checkmark on deployment
- [ ] No red error messages

### ✅ Bot Online
- [ ] Check Railway logs see "Bot logged in"
- [ ] See "Bot is ready and online!"
- [ ] No error messages in logs

### ✅ Commands Work
- [ ] `!fileinfo` works
- [ ] `!help` works
- [ ] Bot responds in real-time

### ✅ File Transfer Works (Railway)
- [ ] Send `.rar` file to user DM
- [ ] Send `.apk` file to user DM
- [ ] Send `.msg` file to user DM
- [ ] User receives files successfully

### ✅ Logs Working
- [ ] View real-time logs in Railway
- [ ] Logs show command usage
- [ ] Logs show file transfers
- [ ] No error spam in logs

### ✅ Bot Resilience
- [ ] Leave bot running for 1 hour
- [ ] No crashes or errors
- [ ] Bot responds consistently
- [ ] Logs accumulate normally

---

## Test Results Summary

**Local Testing:** ✅ Pass / ❌ Fail
**Railway Deployment:** ✅ Pass / ❌ Fail
**Production Ready:** ✅ Yes / ❌ No

---

## Issues Found

If any tests fail, document here:

```
Test Name: [specify test]
Issue: [describe problem]
Solution: [how you fixed it]
Status: ✅ Fixed / ⏳ Pending
```

### Issue #1
- Test Name: 
- Issue: 
- Solution: 
- Status: 

---

## Sign-Off

- [ ] All tests passed
- [ ] No known issues
- [ ] Ready for production
- [ ] Bot is professional-grade

**Date Tested:** ___________
**Tested By:** ___________
**Status:** ✅ APPROVED / ⏳ NEEDS WORK

---

## Continuous Testing

After deployment, periodically:
- [ ] Test bot weekly
- [ ] Monitor Railway logs
- [ ] Check for errors
- [ ] Verify file transfers work
- [ ] Update bot if needed
