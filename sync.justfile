# ============== Data Sync Recipes ==============
# Sync external data from Google Drive using rclone
#
# First time setup: just rclone-setup

# Variables (RUN inherited from project.justfile)
GDRIVE_FOLDER_ID := "1kVAT9WZDETF8pwrzCAMQ74GG-ge7TriU"
REMOTE_NAME := "lambda-ber-gdrive"
EXTERNAL_DIR := "assets/external"

# Download files from Google Drive (one-way, read-only)
[group('data sync')]
sync-gdrive:
    mkdir -p {{EXTERNAL_DIR}}
    rclone copy {{REMOTE_NAME}}:/ {{EXTERNAL_DIR}} --progress

# List remote files
[group('data sync')]
list-remote:
    rclone ls {{REMOTE_NAME}}:/

# Setup rclone remote for this Google Drive folder
[group('data sync')]
rclone-setup:
    @echo "Setting up rclone remote '{{REMOTE_NAME}}' for Google Drive folder..."
    rclone config create {{REMOTE_NAME}} drive root_folder_id {{GDRIVE_FOLDER_ID}}
    @echo ""
    @echo "If browser auth didn't work, run: rclone config reconnect {{REMOTE_NAME}}:"

# List contents of external data directory
[group('data sync')]
list-external:
    ls {{EXTERNAL_DIR}}

# Clean external data directory
[group('data sync')]
clean-external:
    rm -rf {{EXTERNAL_DIR}}
    @echo "Cleaned {{EXTERNAL_DIR}}"

# Check rclone is available and remote is configured
[group('data sync')]
check-deps:
    @rclone version | head -1
    @rclone listremotes | grep -q "{{REMOTE_NAME}}:" && echo "Remote '{{REMOTE_NAME}}' configured" || echo "Run 'just rclone-setup' first"
