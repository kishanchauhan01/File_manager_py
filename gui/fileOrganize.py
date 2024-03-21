import os
import shutil

class FileManager:
    def __init__(self, main_path):
        self.main_path = main_path

    def check_extension(self, file_name):
        """
        This function checks if an extension is valid and belongs to a certain category.

        parameter: file_name: The file name to check.
        return: The category of the extension, or None if it's not valid.
        """
        image_extension = ['.webp', '.jpg', '.jpeg', '.svg', '.psd', '.gif', '.png']
        video_extension = ['.mp4', '.mkv', '.webm', '.flv', '.avi', '.mpeg']
        audio_extension = ['.mp3', '.wav', '.flac', '.aac']
        document_extension = ['.pdf', '.pptx', '.docx', '.xlsx', '.txt', '.html', '.css', '.map', '.json', '.js', '.ipynb']
        compressed_extension = ['.zip', '.rar', '.7z', '.tar.gz', '.tgz', '.tar', '.tar.xz', '.deb']
        software_extension = ['.EXE', '.exe']

        for ext in image_extension:
            if file_name.endswith(ext):
                return 'image'
        for ext in video_extension:
            if file_name.endswith(ext):
                return 'video'
        for ext in audio_extension:
            if file_name.endswith(ext):
                return 'audio'
        for ext in document_extension:
            if file_name.endswith(ext):
                return 'document'
        for ext in compressed_extension:
            if file_name.endswith(ext):
                return 'compressed'
        for ext in software_extension:
            if file_name.endswith(ext):
                return 'software'
        return None

    def organize_files(self):
        """
        This function organizes files into their respective categories.
        """
        for file_name in os.listdir(self.main_path):
            file_path = os.path.join(self.main_path, file_name)
            if os.path.isfile(file_path):
                category = self.check_extension(file_name)
                if category:
                    new_path = os.path.join(self.main_path, category)
                    if not os.path.exists(new_path):
                        os.mkdir(new_path)
                    shutil.move(file_path, new_path)

if __name__ == "__main__":
    file_manager = FileManager('/home/kishan/Downloads/')
    file_manager.organize_files()