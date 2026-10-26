import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Discord bot"""
    
    # Bot Token
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    # Bot Prefix
    PREFIX = os.getenv('COMMAND_PREFIX', '!')
    
    # Allowed file extensions
    ALLOWED_FILE_EXTENSIONS = ['.rar', '.msg', '.apk', '.zip', '.7z', '.exe', '.bin']
    
    # Maximum file size (in bytes) - Discord's limit is ~25MB per file
    MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB
    
    # Bot settings
    BOT_NAME = "File Transfer Bot"
    BOT_VERSION = "1.0.0"
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_DIR = 'logs'
    
    @staticmethod
    def validate():
        """Validate configuration"""
        if not Config.TOKEN:
            raise ValueError("DISCORD_TOKEN environment variable is not set!")
        return True
