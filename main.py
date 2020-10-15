import os

def createifnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
    
    files = os.listdir()
    files.remove("main.py")

    # print(files)

    createifnotexist('Images')
    createifnotexist('Music')
    createifnotexist('Documents')
    createifnotexist('Video')
    createifnotexist('Programs')
    createifnotexist('Compressed')
    createifnotexist('Other')

    imgexts = [".png ", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgexts]

    docsexts = [".txt", ".doc", ".docx", ".pdf", ".xlsx", ".pptx"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docsexts]

    musicexts = [".mp3"]
    music = [file for file in files if os.path.splitext(file)[1].lower() in musicexts]

    videoexts = [".mp4", ".mkv"]
    video = [file for file in files if os.path.splitext(file)[1].lower() in videoexts]

    compexts = [".zip", ".rar"]
    compressed = [file for file in files if os.path.splitext(file)[1].lower() in compexts]

    programexts = [".exe"]
    programs = [file for file in files if os.path.splitext(file)[1].lower() in programexts]

    # print(images)
    other = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgexts) and (ext not in docsexts) and (ext not in musicexts) and (ext not in videoexts) and (ext not in compexts) and (ext not in programexts) and os.path.isfile(file):
            other.append(file)

    # print(other)

    move("Images", images)
    move("Documents", docs)
    move("Music", music)
    move("Video", video)
    move("Compressed", compressed)
    move("Programs", programs)
    move("Other", other)

