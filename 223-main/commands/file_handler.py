import discord
from discord.ext import commands
from config.config import Config
from utils.logger import setup_logger
from utils.file_utils import send_file_to_dm, validate_file

logger = setup_logger(__name__)

class FileHandler(commands.Cog):
    """File handling commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name='sendfile',
        aliases=['sf', 'send'],
        help='Send a file to a user\'s DM'
    )
    async def send_file(self, ctx, user: discord.User = None):
        """
        Send file to user DM
        Usage: !sendfile @user (with file attachment)
        """
        
        # Check if file is attached
        if not ctx.message.attachments:
            embed = discord.Embed(
                title="❌ No file attached",
                description="Please attach a file to send with this command",
                color=discord.Color.red()
            )
            embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
            await ctx.send(embed=embed)
            logger.warning(f"{ctx.author} used sendfile without attachment")
            return
        
        # Check if user is specified
        if not user:
            embed = discord.Embed(
                title="❌ User not specified",
                description="Please mention a user or provide a user ID",
                color=discord.Color.red()
            )
            embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
            await ctx.send(embed=embed)
            logger.warning(f"{ctx.author} used sendfile without specifying user")
            return
        
        # Process each attachment
        attachment = ctx.message.attachments[0]
        
        try:
            # Validate file
            is_valid, error_msg = await validate_file(attachment)
            
            if not is_valid:
                embed = discord.Embed(
                    title="❌ Invalid file",
                    description=error_msg,
                    color=discord.Color.red()
                )
                embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
                await ctx.send(embed=embed)
                logger.warning(f"File rejected: {attachment.filename} from {ctx.author}")
                return
            
            # Send file to user
            success, message = await send_file_to_dm(user, attachment)
            
            if success:
                embed = discord.Embed(
                    title="✅ File sent successfully",
                    description=f"📁 **File:** `{attachment.filename}`\n👤 **Recipient:** {user.mention}\n💾 **Size:** `{attachment.size / 1024:.2f}KB`",
                    color=discord.Color.green()
                )
                embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
                await ctx.send(embed=embed)
                logger.info(f"File '{attachment.filename}' sent to {user} by {ctx.author}")
            else:
                embed = discord.Embed(
                    title="❌ Error sending file",
                    description=message,
                    color=discord.Color.red()
                )
                embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
                await ctx.send(embed=embed)
                logger.error(f"Failed to send file: {message}")
        
        except Exception as e:
            logger.error(f"Error in send_file command: {str(e)}")
            embed = discord.Embed(
                title="❌ Unexpected error",
                description=f"Error: {str(e)}",
                color=discord.Color.red()
            )
            embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
            await ctx.send(embed=embed)
    
    @commands.command(
        name='fileinfo',
        aliases=['finfo', 'info'],
        help='Show file information'
    )
    async def file_info(self, ctx):
        """Show allowed file types and limits"""
        
        max_size_mb = Config.MAX_FILE_SIZE / (1024 * 1024)
        allowed_types = ', '.join(Config.ALLOWED_FILE_EXTENSIONS)
        
        embed = discord.Embed(
            title="📋 File Transfer Bot Information",
            description="Here are the file transfer settings",
            color=discord.Color.blue()
        )
        embed.add_field(
            name="✅ Allowed file types",
            value=f"`{allowed_types}`",
            inline=False
        )
        embed.add_field(
            name="💾 Maximum file size",
            value=f"`{max_size_mb:.1f}MB`",
            inline=False
        )
        embed.add_field(
            name="📝 How to use",
            value="`!sendfile @user` (attach file)",
            inline=False
        )
        embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
        
        await ctx.send(embed=embed)
        logger.info(f"{ctx.author} requested file info")

async def setup(bot):
    """Setup the FileHandler cog"""
    await bot.add_cog(FileHandler(bot))
    logger.info("FileHandler cog loaded")
