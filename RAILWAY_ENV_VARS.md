# Railway Environment Variables Configuration

This file documents the environment variables needed for Railway deployment.

## Required Environment Variables

### 1. DISCORD_TOKEN
**Purpose:** Authenticates your bot with Discord servers

**How to get it:**
1. Go to https://discord.com/developers/applications
2. Select your application
3. Go to "Bot" tab on the left
4. Click "Reset Token" button (since your previous token was exposed)
5. Copy the newly generated token
6. Paste this token as the value in Railway

**Example value format:** 
```
(Your unique Discord bot token - starts with MTQ... and is ~70 characters)
```

**Security:** Keep this token secret. Never share it or commit it to version control.

---

### 2. COMMAND_PREFIX
**Purpose:** Sets the character(s) that trigger bot commands

**Common options:**
- `!` - Most popular
- `?` - Alternative
- `.` - Minimal
- `$` - Clean
- `>` - Angular

**Recommended value:**
```
!
```

**How it works:**
- With `!` as prefix, users would type: `!help`, `!ping`, etc.

---

### 3. LOG_LEVEL
**Purpose:** Controls how much detail is logged from the bot

**Available levels (from most to least verbose):**
- `DEBUG` - Most detailed, shows everything (good for development/troubleshooting)
- `INFO` - Standard information (recommended for production)
- `WARNING` - Only warnings and errors
- `ERROR` - Only critical errors

**Recommended value:**
```
INFO
```

**Why INFO is recommended:**
- Provides useful operational information
- Doesn't spam logs with debug details
- Still captures important warnings and errors

---

## How to Add Variables to Railway

1. Log in to https://railway.app
2. Go to your project dashboard
3. Click on your deployment
4. Find "Environment" or "Variables" section
5. For each variable below, click "Add Variable"
6. Enter the key and value
7. Save/Deploy

---

## Quick Reference Table

| Variable | Recommended Value | Required? |
|----------|-------------------|-----------|
| DISCORD_TOKEN | (Your bot token) | ✅ YES |
| COMMAND_PREFIX | ! | ⭕ Optional* |
| LOG_LEVEL | INFO | ⭕ Optional* |

*Optional but recommended - bot will use defaults if not set

---

## Next Steps

1. ✅ Get your new Discord bot token
2. ✅ Decide on a command prefix (or use `!`)
3. ✅ Choose a log level (or use `INFO`)
4. ✅ Add all three variables to Railway
5. ✅ Deploy the application

Your bot will start running on Railway once deployed!
