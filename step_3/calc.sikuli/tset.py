__author__ = 'Wladislaw'

from sikuli import Screen
from sikuli import App
from sikuli import Region
from sikuli import addImagePath
from sikuli import Key
from org.sikuli.script.Key import DELETE
from sikuli import KeyModifier

s = Screen()
addImagePath("images")


def start_app():
    explorer = App("Dieser PC")
    if not explorer.window():
        App.open("explorer")
        s.wait(1)
    explorer.focus()
    s.wait(1)
    return explorer


def close_app():
    App.close("Downloads")


def do(*args):
    # default timeout value
    print "timeout is %i" % args[3]

    # action can be click, doubleclick, rightclick, dragdrop, etc.
    action = args[0]
    if args[0] == 'click':
        action = s.click
    elif args[0] == 'doubleclick':
        action = s.doubleClick
    elif args[0] == 'rightclick':
        action = s.rightClick

    # perform action e.g.
    # click image ... check ... condition until end of timeout
    action((args[1])); check_post_condition((args[2]), (args[3]))


def click_gui_element(image, condition, timeout = 5):
    s.click(image)
    check_post_condition(condition, timeout)


def doubleclick_gui_element(image):
    s.doubleClick(image)


def press_key(key):
    s.type(key)
    # s.type(Key.DELETE)


def check_post_condition(condition, timeout=5):
    if s.exists(condition, timeout):
        pass
        # return timeout
    else:
        print "FAIL! Wrong post condition!"


def type_text(text):
    s.paste(text)
    s.type(Key.ENTER)


# PRE CONDITION
start_app()

# TEST START
print "1. Select Downloads Folder"
# click_gui_element("tset/downloads.png", "tset/downloads_folder_selected.png")
# check_post_condition("tset/downloads_folder_selected.png")

do('click', "tset/downloads.png", "tset/downloads_folder_selected.png", 7)

print "2. Click the 'New Folder' Button"
# click_gui_element("tset/new_folder.png", "tset/ready_to_create_new_folder.png")
# check_post_condition("tset/ready_to_create_new_folder.png")

do('click', "tset/new_folder.png", "tset/ready_to_create_new_folder.png", 6)

print "3. Give the New Folder a Name"
type_text("aaa tset sikuli test")
check_post_condition("tset/new_folder_created.png")

print "4. Open the New Folder"
doubleclick_gui_element("tset/new_folder_created.png")
check_post_condition("tset/new_folder_opened.png")

print "5. Go Back to the Previous Folder"
click_gui_element("tset/gui_back.png", "tset/returned_from_new_folder.png")
# check_post_condition("tset/returned_from_new_folder.png")

print "6. Delete the Created Folder"
press_key(Key.DELETE)
check_post_condition("tset/downloads_folder_selected.png")

print "7. Close Explorer Window"
close_app()
# TEST END

# POST CONDITION
# Browser Closed
###############################################################



###############################################################

# # ACTION: Navigate to Downloads Folder
# print "1. Select Downloads Folder"
# s.click("tset/downloads.png")
#
# # CHECK Post Condition
# if s.exists("tset/downloads_folder_selected.png", 5):
#     pass
# else:
#     print "FAIL! Wrong post condition!"
#     print "downloads_folder_selected.png NOT FOUND"
#
# # ACTION: Click Button "New Folder"
# print "2. Click the 'New Folder' Button"
# s.click("tset/new_folder.png")
#
# # CHECK Post Condition
# if s.exists("tset/ready_to_create_new_folder.png"):
#     pass
# else:
#     print "FAIL! Wrong post condition!"
#     print "ready_to_create_new_folder.png NOT FOUND"
#
# # ACTION: Give The New Folder a Name
# print "3. Give The New Folder a Name"
# s.paste('aaa tset sikuli test')
# s.type(Key.ENTER)
#
# # CHECK Post Conditon
# if s.exists("tset/new_folder_created.png"):
#     pass
# else:
#     print "FAIL! Wrong post condition!"
#     print "new_folder_created.png NOT FOUND"
#
# # ACTION: Open The New Folder with a Double Click
# print "4. Open New Folder"
# s.doubleClick("tset/new_folder_created.png")
#
# # CHECK post condition
# if s.exists("tset/new_folder_opened.png"):
#     pass
# else:
#     print "FAIL! Wrong post condition!"
#
# # ACTION + post CHECK: Go back in explorer
# print "5. Go Back"
# s.click("tset/gui_back.png")
#
# if s.exists("tset/returned_from_new_folder.png"):
#     pass
# else:
#     print "FAIL! Wrong post condition!"
#     print "returned_from_new_folder.png NOT FOUND"
#
# # ACTION + post CHECK
# print "6. Delete the created folder"
# s.type(Key.DELETE)
#
# if s.exists("tset/downloads_folder_selected.png"):
#     pass
# else:
#     print "FAIL! Wrong post condition!"
#     print "downloads_folder_selected.png NOT FOUND"
#
# # ACTION + post CHECK
# print "7. Close Explorer Window"
# App.close("Downloads")
# # s.click("tset/gui_close.png")

