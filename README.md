# Discord File Transfer Bot

A professional Discord bot that securely handles file transfers by forwarding files to users' DMs.

## Features

✅ **Secure File Transfer** - Send files directly to user DMs  
✅ **File Validation** - Validates file types and sizes  
✅ **Supported Formats** - .rar, .msg, .apk, .zip, .7z, .exe, .bin  
✅ **Error Handling** - Comprehensive error handling and logging  
✅ **Professional Logging** - Detailed logs for debugging  
✅ **Production Ready** - Clean, well-documented code  
✅ **Railway Compatible** - Ready for Railway deployment  

## Installation

### Prerequisites
- Python 3.11+
- Discord Bot Token

### Step 1: Clone/Setup
```bash
cd discord_file_bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment
```bash
# Copy example env file
copy .env.example .env

# Edit .env and add your Discord bot token
# DISCORD_TOKEN=your_token_here
```

### Step 4: Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" section and click "Add Bot"
4. Copy the token and paste it in `.env` file
5. Enable these intents:
   - Message Content Intent
   - Server Members Intent
   - Direct Messages

6. Go to OAuth2 > URL Generator
7. Select scopes: `bot`
8. Select permissions: `Send Messages`, `Read Messages`
9. Use the generated URL to invite bot to your server

### Step 5: Run Locally
```bash
python main.py
```

## Commands

| Command | Aliases | Description | Usage |
|---------|---------|-------------|-------|
| `sendfile` | `sf`, `send` | Send file to user DM | `!sendfile @user` (attach file) |
| `fileinfo` | `finfo`, `info` | Show file info | `!fileinfo` |
| `help` | - | Show help | `!help` |

## File Specifications

| Property | Value |
|----------|-------|
| Allowed Types | .rar, .msg, .apk, .zip, .7z, .exe, .bin |
| Max Size | 25 MB |
| Max Per Guild | Unlimited |

## Project Structure

```
discord_file_bot/
├── config/
│   └── config.py          # Configuration settings
├── commands/
│   └── file_handler.py    # File transfer commands
├── events/
│   ├── bot_events.py      # Bot lifecycle events
│   └── message_events.py  # Message event handlers
├── utils/
│   ├── logger.py          # Logging setup
│   └── file_utils.py      # File utilities
├── logs/                  # Bot logs directory
├── main.py                # Main bot file
├── requirements.txt       # Python dependencies
├── .env.example           # Example env file
├── .env                   # Your env file (create from example)
├── Procfile               # Railway deployment config
├── runtime.txt            # Python version for Railway
└── README.md              # This file
```

## Error Handling

The bot includes comprehensive error handling:
- File validation (type & size)
- Command error handling
- DM sending error handling
- Detailed logging of all operations

## Logging

Logs are stored in the `logs/` directory with the format:
- Filename: `bot_YYYY-MM-DD.log`
- Contains: Timestamps, log levels, messages, and errors

## Deployment on Railway

### Prerequisites
- Railway account ([railway.app](https://railway.app))
- GitHub account with bot code

### Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Railway Project**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub"
   - Choose your repository

3. **Add Environment Variables**
   - Go to Project Settings
   - Add variable: `DISCORD_TOKEN` with your bot token
   - Add variable: `COMMAND_PREFIX` (optional, default: !)
   - Add variable: `LOG_LEVEL` (optional, default: INFO)

4. **Deploy**
   - Railway will automatically deploy when you push to GitHub
   - Check deployment status in Railway dashboard

5. **Keep Bot Running**
   - Railway will keep the bot running continuously
   - Use Railway's monitoring to check logs

## Troubleshooting

### Bot doesn't respond
- Check if token is correct in `.env`
- Verify bot has permissions in server
- Check logs for errors

### File not sending
- Check file size (max 25MB)
- Check file extension (must be in allowed list)
- Verify user is not blocking DMs

### Railway deployment fails
- Check all environment variables are set
- Verify token is correct
- Check Python version is 3.11+
- Review deployment logs

## Security Notes

⚠️ **NEVER** share your Discord bot token  
⚠️ Keep `.env` file private  
⚠️ Use environment variables for secrets  
⚠️ Don't commit `.env` to version control  

## Support

For issues or questions:
1. Check the logs in `logs/` directory
2. Review command usage
3. Verify configuration

## License

This bot is provided as-is for educational and commercial use.

---

**Version:** 1.0.0  
**Last Updated:** 2024
