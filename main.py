import os
import discord
from discord.ext import commands
from config.config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix=Config.PREFIX,
    intents=intents,
    help_command=commands.DefaultHelpCommand()
)

# Store loaded cogs
loaded_cogs = []

async def load_cogs():
    """Load all cogs from commands and events directories"""
    
    cogs_dir = [
        ('commands', 'commands'),
        ('events', 'events')
    ]
    
    for directory, prefix in cogs_dir:
        for filename in os.listdir(directory):
            if filename.endswith('.py') and not filename.startswith('_'):
                cog_name = filename[:-3]
                module_name = f"{prefix}.{cog_name}"
                
                try:
                    await bot.load_extension(module_name)
                    loaded_cogs.append(module_name)
                    logger.info(f"✅ Loaded cog: {module_name}")
                except Exception as e:
                    logger.error(f"❌ Failed to load cog {module_name}: {str(e)}")

@bot.event
async def on_ready():
    """Called when bot is ready - sync commands"""
    
    try:
        synced = await bot.tree.sync()
        logger.info(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {str(e)}")

async def main():
    """Main function"""
    
    try:
        # Validate configuration
        Config.validate()
        logger.info("✅ Configuration validated")
        
        # Load cogs
        await load_cogs()
        logger.info(f"✅ Loaded {len(loaded_cogs)} cog(s)")
        
        # Start bot
        logger.info("🚀 Starting bot...")
        await bot.start(Config.TOKEN)
    
    except ValueError as e:
        logger.error(f"❌ Configuration error: {str(e)}")
        exit(1)
    except Exception as e:
        logger.error(f"❌ Fatal error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
