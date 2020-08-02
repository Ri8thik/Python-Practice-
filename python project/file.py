import os , shutil
dict_extentions ={
        
       ' audio_extentensions' :('.mp3','.m4a','.wav','.flac'),
        'vedio_extentensions ':('.mp4','.mkv','.MKV','.flv','.mpeg'),
        'documents_extentions' :('.doc','.pdf','.txt')
}
folderpath =input("enter folder path: ")
def file_finder(folder_path, file_extentions):
        files=[]
        for file in os.listdir(folder_path):
                for extention in file_extentions:
                        if file.endswith(extention):
                                files.append(file)

        return files
#print(file_finder(folderpath,vedio_extentensions))
for extension_type, extension_tuple in dict_extentions.items():
        folder_name = extension_type.split("_")[0] +'files'
        folder_path = os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in file_finder(folderpath, extension_tuple):
                item_path = os.path.join(folderpath,item)
                item_new_path= os.path.join(folder_path, item)
                shutil.move(item_path,item_new_path)
        #print("calling file finder")
        # print(file_finder(folderpath, extension_tuple))
