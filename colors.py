import os


def load_gmt_colors():
    if os.path.exists("gmt_colors"):
        fid = open("gmt_colors","r")
        colors = fid.read()
        fid.close()
        colors = colors.split("\n")
        return colors
    else:
        print("File not found!")
        return -1

    

    
                          

