import os
from config.config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def validate_file(attachment):
    """
    Validate if file meets requirements
    
    Args:
        attachment: Discord attachment object
    
    Returns:
        tuple: (is_valid, error_message)
    """
    
    # Check file extension
    file_extension = os.path.splitext(attachment.filename)[1].lower()
    
    if file_extension not in Config.ALLOWED_FILE_EXTENSIONS:
        error_msg = (
            f"❌ **File type not allowed!**\n"
            f"Allowed extensions: {', '.join(Config.ALLOWED_FILE_EXTENSIONS)}\n"
            f"Your file: `{file_extension}`"
        )
        return False, error_msg
    
    # Check file size
    if attachment.size > Config.MAX_FILE_SIZE:
        size_mb = Config.MAX_FILE_SIZE / (1024 * 1024)
        actual_mb = attachment.size / (1024 * 1024)
        error_msg = (
            f"❌ **File too large!**\n"
            f"Maximum size: `{size_mb:.1f}MB`\n"
            f"Your file: `{actual_mb:.1f}MB`"
        )
        return False, error_msg
    
    return True, None

async def send_file_to_dm(user, attachment):
    """
    Send file to user's DM
    
    Args:
        user: Discord user object
        attachment: Discord attachment object
    
    Returns:
        tuple: (success, message)
    """
    try:
        # Validate file
        is_valid, error_msg = await validate_file(attachment)
        
        if not is_valid:
            return False, error_msg
        
        # Open DM channel
        dm_channel = await user.create_dm()
        
        # Download and send file
        file_data = await attachment.read()
        
        # Send file in DM
        with open(f"temp_{attachment.filename}", "wb") as f:
            f.write(file_data)
        
        with open(f"temp_{attachment.filename}", "rb") as f:
            await dm_channel.send(
                f"📁 **File from {attachment.filename}**",
                file=__import__('discord').File(f, filename=attachment.filename)
            )
        
        # Clean up temp file
        os.remove(f"temp_{attachment.filename}")
        
        logger.info(f"File '{attachment.filename}' sent to {user} successfully")
        return True, f"✅ File sent to {user.mention}'s DM"
    
    except Exception as e:
        logger.error(f"Error sending file to DM: {str(e)}")
        return False, f"❌ Error sending file: {str(e)}"
