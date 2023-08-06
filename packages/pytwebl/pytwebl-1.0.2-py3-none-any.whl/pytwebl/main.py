from . import COLORS

LOREM = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis nobis doloremque exercitationem eveniet nesciunt at. Voluptates provident vero amet vel oue deleniti quia explicabo?'


def disableColours():
    COLORS.BLACK = ""
    COLORS.RED = ""
    COLORS.GREEN = ""
    COLORS.YELLOW = ""
    COLORS.BLUE = ""
    COLORS.MAGENTA = ""
    COLORS.CYAN = ""
    COLORS.WHITE = ""
    COLORS.RESET = ""


def insert(bas, add, ini):
    add = add[::-1]
    for i in add:
        bas.insert(bas.index(ini)+1, i)


def fileWriter(tags, file, css_bas):
    try:
        css_bas.insert(0, tags)
        file.writelines(css_bas)
        css_bas.remove(tags)
    except:
        pass


def p_(bas, ini, f2, css_bas):
    add = ['<p>\n', LOREM, '</p>\n']
    insert(bas, add, ini)
    ini = '</p>\n'
    fileWriter('p\n', f2, css_bas)


def img_(bas, ini, f2, css_bas):
    src = input(
        f"\t{COLORS.BLUE}[*]{COLORS.RESET} ENTER THE IMAGE'S FILENAME WITH RELATIVE PATH : ")
    height = input(
        f"\t{COLORS.BLUE}[*]{COLORS.RESET} ENTER THE HEIGHT OF THE IMAGE : ")
    width = input(
        f"\t{COLORS.BLUE}[*]{COLORS.RESET} ENTER THE WIDTH OF THE IMAGE : ")
    alt = input(
        f"\t{COLORS.BLUE}[*]{COLORS.RESET} ENTER THE ALTERNATING MESSAGE INCASE IF IMAGE ISN'T DISPLAYED : ")
    add = [
        f'<img src="{src}" height="{height}" width="{width}" alt="{alt}">\n']
    insert(bas, add, ini)
    ini = add[0]
    fileWriter('img\n', f2, css_bas)


def hx_(bas, ini, f2, css_bas):
    add = ['<h1>\n', "Heading", '</h1>\n']
    insert(bas, add, ini)
    ini = '</h1>\n'
    fileWriter('h1\n', f2, css_bas)


def sup_(bas, ini, sup, f2, css_bas):
    if (sup == '<sub>'):
        add = ['<sub>\n', 'Sample Text Starts here............\n', '</sub>\n']
        insert(bas, add, ini)
        ini = '</sub>\n'
        fileWriter('sub\n', f2, css_bas)
    elif (sup == '<sup>'):
        add = ['<sup>\n', 'Sample Text Starts here............\n', '</sup>\n']
        insert(bas, add, ini)
        ini = '</sup>\n'
        fileWriter('sup\n', f2, css_bas)


def ol_(bas, ini, f2, css_bas):
    add = ['<ol>\n', '<li>\n', LOREM, '\n', '</li>\n', '</ol>\n']
    insert(bas, add, ini)
    ini = '<ol>\n'
    fileWriter('ol\n', f2, css_bas)


def ul_(bas, ini, f2, css_bas):
    add = ['<ul>\n', '<li>\n', LOREM, '\n', '</li>\n', '</ul>\n']
    insert(bas, add, ini)
    ini = '<ul>\n'
    fileWriter('ul\n', f2, css_bas)


def help():
    print("Usage: [--help] [--disable-colours] [--enable-colours]")
    print("Help: Creates template for web-development from shell, includes : html, css and js")
    print()
    print(f"Options:\n\t{'--help':20}Opens man page\n\t{'--disable-colours':20}Disable coloured output\n\t{'--enable-colours':20}Enable coloured output\n> NOTE : Colours are disabled in output by default in Windows only, enabled by default in Linux-based OS.")


def main():
    import platform
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        help()
        return
    if platform.system() == "Windows" and len(sys.argv) == 1:
        disableColours()
    elif (platform.system() == "Windows" and sys.argv()[1] == "--enable-colours") or (len(sys.argv) > 1 and sys.argv[1] == "--enable-colours"):
        pass
    elif (len(sys.argv) > 1 and sys.argv[1] == "--disable-colours"):
        disableColours()
    elif (len(sys.argv) > 1):
        print(f"Unknown command {sys.argv[1]}")
        return

    try:
        import os
        print(f"""{COLORS.GREEN}
    ____       _______       __     __    __ 
   / __ \__  _/_  __/ |     / /__  / /_  / / 
  / /_/ / / / // /  | | /| / / _ \/ __ \/ /  
 / ____/ /_/ // /   | |/ |/ /  __/ /_/ / /___
/_/    \__, //_/    |__/|__/\___/_.___/_____/
      /____/                                 
{COLORS.RESET}""")

        dir = "./"+input(
            f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.CYAN}ENTER THE DIRECTORY NAME : {COLORS.RESET}").strip()
        if not os.path.exists(dir):
            os.mkdir(dir)
        file_html = input(
            f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.CYAN}ENTER THE FILENAME FOR THE HTML TEMPLATE : {COLORS.RESET}").strip()
        file_css = input(
            f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.CYAN}ENTER THE FILENAME FOR THE CSS TEMPLATE : {COLORS.RESET}").strip()
        file_js = input(
            f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.CYAN}ENTER THE FILENAME FOR THE JAVASCRIPT FILE : {COLORS.RESET}").strip()
        global LOREM
        f2 = None
        f3 = None
        if (file_css != '' and len(file_css.split(".")) == 2 and file_css.split(".")[1].strip() == "css"):
            f2 = open("./"+dir+"/"+file_css, 'w+')
        elif (file_css != ''):
            print(f"{COLORS.RED}INVALID FILENAME OR EXTENSION iN CSS{COLORS.RESET}")
            return
        if (file_js != '' and len(file_js.split(".")) == 2 and file_js.split(".")[1].strip() == "js"):
            f3 = open("./"+dir+"/"+file_js, 'w+')
        elif (file_js != ''):
            print(f"{COLORS.RED}INVALID FILENAME OR EXTENSION iN JS{COLORS.RESET}")
            return
        if (file_html != '' and len(file_html.split(".")) == 2 and file_html.split(".")[1].strip() == "html"):
            with open("./"+dir+"/"+file_html, 'w+') as f1:
                title_ = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}ENTER THE TITLE OF THE DOCUMENT : {COLORS.RESET}")
                p = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}DO YOU WANT TO ADD PARAGRAPH TAG : Y/N : {COLORS.RESET}").upper()
                img = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}DO YOU WANT TO ADD IMAGE TAG : Y/N : {COLORS.RESET}").upper()
                H = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}DO YOU WANT TO ADD HEADER  TAG : Y/N : {COLORS.RESET}").upper()
                sup = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}DO YOU WANT TO ADD SUPERSCRIPT/SUBSCRIPT TAG , enter the tag name in the tag format : {COLORS.RESET}")
                ol = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}DO YOU WANT TO ADD ORDER LISTS : Y/N : {COLORS.RESET}").upper()
                ul = input(
                    f"{COLORS.BLUE}[*]{COLORS.RESET} {COLORS.GREEN}DO YOU WANT TO ADD UNORDER LISTS : Y/N : {COLORS.RESET}").upper()
                ini = '<body>\n'
                bas = ['<!DOCTYPE html>\n', '<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n',
                       '    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n',
                       '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n', f'    <title>{title_}</title>\n', f'<link rel="stylesheet" href="{file_css}"></head>\n',
                       '<body>\n', '</body>\n', '</html>']
                css_bas = ["{\n", "color : Blue;\n", "font-size : 20px;\n", "font-family : 'Times New Roman',Times,Serif;\n",
                           "background-size : 300px 100px;\n", "background-repeat : no-repeat;\n", "}\n"]

                if (p == 'Y'):
                    p_(bas, ini, f2, css_bas)

                if (img == 'Y'):
                    img_(bas, ini, f2, css_bas)

                if (sup == '<sup>' or sup == '<sub>'):
                    sup_(bas, ini, sup, f2, css_bas)
                if (ol == 'Y'):
                    ol_(bas, ini, f2, css_bas)
                    ini = '</ol>\n'
                if (ul == 'Y'):
                    ul_(bas, ini, f2, css_bas)
                    ini = '</ul>\n'

                if (H == 'Y'):
                    hx_(bas, ini, f2, css_bas)

                f1.writelines(bas)
            print(
                f"{COLORS.GREEN}Succesfully Created {file_html}{f', {file_css}' if f2 != None else ''}{f', {file_js}' if f3!=None else ''}{COLORS.RESET}")
        else:
            print(
                f"{COLORS.RED}PLEASE ENTER A VALID FILE NAME FOR HTML.{COLORS.RESET}")
    except:
        pass


if __name__ == "__main__":
    main()
