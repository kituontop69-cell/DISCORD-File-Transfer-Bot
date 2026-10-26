import discord
from discord.ext import commands
from utils.logger import setup_logger
from config.config import Config

logger = setup_logger(__name__)

class BotEvents(commands.Cog):
    """Handle bot events"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Called when bot is ready"""
        
        logger.info(f"✅ Bot logged in as {self.bot.user}")
        logger.info(f"Bot ID: {self.bot.user.id}")
        logger.info(f"Bot name: {Config.BOT_NAME} v{Config.BOT_VERSION}")
        
        # Set bot status
        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name=f"files | {Config.PREFIX}fileinfo"
        )
        await self.bot.change_presence(activity=activity)
        
        logger.info("✅ Bot is ready and online!")
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Called when bot joins a guild"""
        
        logger.info(f"Bot joined guild: {guild.name} (ID: {guild.id})")
        logger.info(f"Guild members: {guild.member_count}")
    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """Called when bot is removed from a guild"""
        
        logger.warning(f"Bot removed from guild: {guild.name} (ID: {guild.id})")

async def setup(bot):
    """Setup the BotEvents cog"""
    await bot.add_cog(BotEvents(bot))
    logger.info("BotEvents cog loaded")
