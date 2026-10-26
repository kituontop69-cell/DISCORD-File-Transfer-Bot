import discord
from discord.ext import commands
from utils.logger import setup_logger

logger = setup_logger(__name__)

class MessageEvents(commands.Cog):
    """Handle message events"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Handle messages"""
        
        # Ignore bot's own messages
        if message.author == self.bot.user:
            return
        
        # Ignore DMs for automatic processing (optional)
        if isinstance(message.channel, discord.DMChannel):
            logger.info(f"DM from {message.author}: {message.content}")
            return
        
        logger.debug(f"Message from {message.author}: {message.content}")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle command errors"""
        
        logger.error(f"Command error: {str(error)}")
        
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="❌ Missing argument",
                description=f"Please provide: `{error.param.name}`",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="❌ Bad argument",
                description="Invalid argument provided",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        
        elif isinstance(error, commands.CommandNotFound):
            logger.warning(f"Unknown command from {ctx.author}")
            return
        
        else:
            embed = discord.Embed(
                title="❌ Error",
                description=f"An error occurred: {str(error)}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    """Setup the MessageEvents cog"""
    await bot.add_cog(MessageEvents(bot))
    logger.info("MessageEvents cog loaded")
