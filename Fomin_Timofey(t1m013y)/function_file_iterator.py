def listpaths(readdir: str, writedir: str):
    import os
    supported_formats = [
        ".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2", ".png", ".pbm", ".pgm", ".ppm",
        ".sr", ".ras", ".tiff", ".tif"
    ]
    dirlist = os.listdir(readdir)
    dirfiles = [f for f in dirlist
                if os.path.isfile(os.path.join(readdir, f)) and
                os.path.splitext(f)[1].lower() in supported_formats]
    paths = [(os.path.join(readdir, filename), os.path.join(writedir, filename))
             for filename in dirfiles]
    return paths
  
