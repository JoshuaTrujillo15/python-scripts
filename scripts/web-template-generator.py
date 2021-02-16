# web template maker

import os

# templates

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!--HEADER-->
    <header>

    </header>

    <!--MAIN-->
    <main>

    </main>

    <!--FOOTER-->
    <footer>

    </footer>
</body>
</html>
"""

SCSS_TEMPLATE = """
$primary: #000;
$secondary: #000;
$shadow: rgba(0,0,0,0.5);
$white: #fff;
$gray: #888;

* {
    margin: 0;
    padding: 0;
}

body {

}

header {

}

main {

}

footer {
    
}
"""
def scssWatcher(root):
    cmd = "sass --watch {0}/scss/index.scss {0}/css/index.css".format(root)
    print("[issuing command] " + cmd + "\nLeave the terminal open ...")
    os.system(cmd)

def writeFile(ext, root):
    root = root[2:]
    print(root)
    if ext == "css":
        fileName = root + "/" + ext + "/index." + ext
        os.system("touch " + fileName)
        print(fileName + " created.")
        return
    elif ext == "html":
        fileName = root + "/index." + ext
        fileTemplate = HTML_TEMPLATE
    elif ext == "scss":
        fileName = root + "/" + ext + "/index." + ext
        fileTemplate = SCSS_TEMPLATE
    
    with open(fileName, "w") as f:
        f.write(fileTemplate)
        print(fileName + " template generated.")

def createTemplate(dirName):
    root = "~/documents/github/{}".format(dirName)
    scss = "/scss"
    css = "/css"
    htmlExt = "html"
    scssExt = "scss"
    cssExt = "css"

    print("Creating directories ...")

    os.system("mkdir " + root)
    print(root)

    os.system("mkdir " + root + scss)
    print(root + scss)

    os.system("mkdir " + root + css)
    print(root + css)

    print("\nDirectories created.\nGenerating file templates ...")

    writeFile(htmlExt, root)
    writeFile(scssExt, root)
    writeFile(cssExt, root)
    print("\nTemplate generated ...\n")

    scssWatcher(root)




def main():
    while True:
        dirName = input("Enter root directory name...\n")
        if os.path.isfile("~/documents/github/" + dirName):
            print("Directory already exists ...")
            continue
        break

    createTemplate(dirName)





if __name__ == "__main__":
    main()