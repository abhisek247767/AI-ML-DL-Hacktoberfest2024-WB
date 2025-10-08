import hashlib
import os
import shutil

class OptimizedFileTransfer:
    def __init__(self):
        self.transferred_files = []

    def hash_file(self, filepath):
        """Generate SHA-256 hash for a given file."""
        try:
            hasher = hashlib.sha256()
            with open(filepath, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None

    def transfer_files(self, source_dir, dest_dir):
        """Transfer files from source to destination based on hash comparison."""
        
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory not found: {source_dir}")
            return
        
        # Create destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f"Destination directory created: {dest_dir}")
        
        # Loop through files in source directory
        for filename in os.listdir(source_dir):
            src_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)

            print(f"Processing file: {src_file}")  # Debug statement

            src_hash = self.hash_file(src_file)
            dest_hash = self.hash_file(dest_file) if os.path.exists(dest_file) else None

            print(f"Source hash: {src_hash}, Destination hash: {dest_hash}")  # Debug statement

            if src_hash and src_hash != dest_hash:
                shutil.copy2(src_file, dest_file)
                self.transferred_files.append(filename)
                print(f"Transferred file: {filename}")
            else:
                print(f"File unchanged: {filename}")

    def get_transferred_files(self):
        """Return the list of transferred files."""
        return self.transferred_files

# Test Cases
file_transfer = OptimizedFileTransfer()

# Use the absolute paths for your directories here
source_directory = "C:/Users/ASUS/Desktop/Rsp/AI-ML-DL-Hacktoberfest2024-WB/source_folder"
destination_directory = "C:/Users/ASUS/Desktop/Rsp/AI-ML-DL-Hacktoberfest2024-WB/destination_folder"

# Transfer files and handle directories
file_transfer.transfer_files(source_directory, destination_directory)

# List transferred files
print("Transferred Files:", file_transfer.get_transferred_files())
