"""
Wizard Mode
Final Project
Author: Nhu Quynh Duong
"""
from dataclasses import dataclass
import turtle as t


@dataclass
class Tags:
    title = str
    backcolor = str
    font = str
    headcolor = str
    fontcolor = str


def check_hex(color):
    """
    This function checks if the hex color is valid.
    :param color: color from user's input
    :return: boolean of whether the color is a valid hex
    """
    if len(color) != 7:
        return False
    elif color[0] != "#":
        return False
    else:
        for i in range(1, len(color)):
            if 0 < i and i > 16:
                return False
        return True


def get_color(color):
    """
    This function checks if the color from the user's input is valid.
    :param color: the color from the user's input
    :return: the color
    """
    color_list = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
                  'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen',
                  'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat',
                  'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred', 'antiquewhite',
                  'royalblue', 'yellow', 'indigo', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray',
                  'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise',
                  'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise',
                  'coral', 'forestgreen', 'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum',
                  'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon',
                  'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray',
                  'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown',
                  'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod',
                  'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine',
                  'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple',
                  'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon',
                  'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua',
                  'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle',
                  'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise',
                  'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite',
                  'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}
    if color in color_list:
        return color
    elif color[0] == "#":
        check = check_hex(color)
        if not check:
            color = str(input("Please enter a valid color. "))
        else:
            return color
    else:
        color = str(input("Please enter a valid color. "))


def init():
    """
    Initialize the turtle window
    :return: None
    """
    t.ht()
    t.up()
    t.setup(200, 200)
    t.setpos(0, 60)
    t.title("Font Options")


def next_ine():
    """
    This function move the turtle to the next line
    :return: None
    """
    t.up()
    t.right(90)
    t.forward(15)
    t.left(90)


def font_window():
    """
    This function draws the turtle window of the different font style options.
    :return: None
    """
    init()
    t.write("Arial", False, 'center', ('Arial', 12, 'normal'))
    next_ine()
    t.write("Comic Sans MS", False, 'center', ('Comic Sans MS', 12, 'normal'))
    next_ine()
    t.write("Lucida Grande", False, 'center', ('Lucida Grande', 12, 'normal'))
    next_ine()
    t.write("Tahoma", False, 'center', ('Tahoma', 12, 'normal'))
    next_ine()
    t.write("Verdana", False, 'center', ('Verdana', 12, 'normal'))
    next_ine()
    t.write("Helvetica", False, 'center', ('Helvetica', 12, 'normal'))
    next_ine()
    t.write("Times New Roman", False, 'center', ('Times New Roman', 12, 'normal'))
    t.done()


def create_file(title, color, headcolor, font, color_text, paragraph_titles, url):
    """
    This function creates the html file from all the infomation in file and user input
    :param title: website title
    :param color: color of background
    :param headcolor: head color
    :param font: the fontstyle
    :param color_text: the text color
    :param paragraph_titles: the paragraph html syntax
    :param url: the image url
    :return: None
    """
    file = open("style_template.txt")
    f = open("index2.html", "a")
    html_head = "<!DOCTYPE html>\n" \
                "<html>\n" \
                "<head>\n" \
                "<title>" + title + "\n</title>"

    html_body = "\n</head>\n" \
                "<body>\n" \
                "<h1>" + title + "\n</h1>" \
                "\n<hr/>\n" + paragraph_titles + url + "</body>\n" \
                "</html><style>"

    acc = ""
    for line in file:
        if '@BACKCOLOR' in line:
            acc += line.replace('@BACKCOLOR', color)
        elif '@HEADCOLOR' in line:
            acc += line.replace('@HEADCOLOR', headcolor)
        elif '@FONTSTYLE' in line:
            acc += line.replace('@FONTSTYLE', font)
        elif '@FONTCOLOR' in line:
            acc += line.replace('@FONTCOLOR', color_text)
        else:
            acc += line
    f.write(html_head + acc + html_body)


def get_font(font):
    """
    This function returns the font style
    :param font: the number that represent the font
    :return: the font style
    """
    if font > 6 or font < 0:
        return print("Not a valid font")
    else:
        fonts = {0: 'Arial', 1: 'Comic Sans MS', 2: 'Lucida Grande', 3: 'Tahoma', 4: 'Verdana', 5: 'Helvetica',
                 6: 'Times New Roman'}
        return fonts[font]


def get_paragraph_info(paragraph_titles, content):
    """
    This function returns the paragraph syntax
    :param paragraph_titles: list of paragraph_titles
    :param content: list of paragraph content
    :return: paragraph info
    """
    paragraph = ""
    for i in range(0, len(content)):
        paragraph += "<h2>" + paragraph_titles[i] + "\n</h2>\n"
        paragraph += "<p>" + content[i] + "\n</p>\n"
    return paragraph


def get_image_url(image_lst):
    """
    This function creates the html syntax for the image url
    :param image_lst: list of image url
    :return: the image url
    """
    the_image = ""
    for i in image_lst:
        the_image += "<img src=" + i + ' class="center">\n'
    return the_image


def get_user_input():
    """
    This function take in all user input
    create html files from the given information
    :return: None
    """
    paragraph_flag = True
    image_lst = []
    paragraph_title_lst = []
    content_lst = []

    title = str(input("What is the title of your website? "))
    color = str(input("Choose the name of a color, or in format '#XXXXXX': "))
    back_color = get_color(color)
    print("You will now choose a font.")
    font = str(input("Do you want to see what the fonts look like? [yes] "))
    if font == "yes":
        font_window()
        print("Choose a font by its number.")
        print(" 0: Arial, size 14 \n 1: Comic Sans MS, size 14 \n 2: Lucida Grande, size 14 \n 3: "
              "Tahoma, size 14 "
              "\n 4: Verdana, size 14 \n 5: Helvetica, size 14 \n 6: Times New Roman, size 14 \n")

    else:
        print("Choose a font by its number.")
        print(" 0: Arial, size 14 \n 1: Comic Sans MS, size 14 \n 2: Lucida Grande, size 14 \n 3: "
              "Tahoma, size 14 "
              "\n 4: Verdana, size 14 \n 5: Helvetica, size 14 \n 6: Times New Roman, size 14 \n")

    choose_font = int(input("Choose a number: "))
    the_font = get_font(choose_font)
    print("Paragraph Text Color")
    color_text = str(input("Choose the name of a color, or in format '#XXXXXX': "))
    text_color = get_color(color_text)
    print("Heading Color")
    color_head = str(input("Choose the name of a color, or in format '#XXXXXX': "))
    head_color = get_color(color_head)
    while paragraph_flag:
        images_flag = True
        paragraph_title = str(input("Title of your paragraph"))
        paragraph_title_lst.append(paragraph_title)
        print("Content of your paragraph (single line)")
        content = str(input(""))
        content_lst.append(content)
        add_images = str(input("Do you want to add images? [yes]"))
        if add_images != "yes":
            images_flag = False
        while images_flag:
            img_url = str(input("Image file name: "))
            second_answer = str(input("Do you want to add another image? [yes]"))
            image_lst.append(img_url)
            if second_answer != "yes":
                images_flag = False
        second_paragraph = str(input("Do you want to add another paragraph to your website? [yes]"))
        if second_paragraph != "yes":
            paragraph_flag = False
            print("Your web page has been saved as index.html")

    paragraph_titles = get_paragraph_info(paragraph_title_lst, content_lst)
    url = get_image_url(image_lst)
    create_file(title, back_color, head_color, the_font, text_color, paragraph_titles, url)


def main():
    """
    Runs the wizard mode
    :return: None
    """
    get_user_input()


if __name__ == '__main__':
    main()
