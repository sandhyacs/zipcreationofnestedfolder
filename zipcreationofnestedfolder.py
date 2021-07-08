import os
# import zipfile
# def zipdir(path):
#     # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         print(root, dirs, files)
#         for file in files:
#             zipf = zipfile.ZipFile("./sourcezip"+"/"+file + '.zip', 'w', zipfile.ZIP_DEFLATED)
#             # ziph.write(os.path.join(root, file))
# # zipf = zipfile.ZipFile(file + '.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir('./Source')
# # zipf.close()


import shutil
dir_list = os.listdir("./Source/")
for idx, dirs in enumerate(dir_list):
    print(dirs)
    dirsl="./Source/"+dirs
    shutil.make_archive("./sourcezip/"+dirs, 'zip', dirsl)
