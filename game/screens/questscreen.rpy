##############################################
screen questscreen(quests=quests):
    use navigation 
    add "Quests.jpg"
    # Used to keep track of the quest types, and which one to show
    default currentQuestType = quests.currentQuestType
    default currentQuests = getattr(quests, currentQuestType)
    default currentQuestID = None
    # Used for decoration of the quest menu
    default questColour = {
        "unavailable":  "#b30000",
        "available":    "#e6ac00",
        "completed":    "#009933"
    }
    # Used to determine what info gets displayed on the left and right panels
    default questInfo = ["title", "brief"]
    
    # Name of page
    # Give title of page
    frame:
        area (0, 0, 500, 50)
        text "Quests": 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"


    # Create hbox to select quest type to display
    hbox:
        style "quest_select"
        frame:
            has hbox
            for questType in quests.displayableQuestTypes:
                textbutton unicode.title(questType):
                    action [
                        SetScreenVariable("currentQuestType", questType),   # Local copy for easier access
                        SetField(quests, "currentQuestType", questType),    # Object field which will retain value over intialisations
                        SetScreenVariable("currentQuests", getattr(quests, questType)),
                        SetScreenVariable("currentQuestID", None),            # Reset the current quest to show
                    ]
    # Left vertical box for ongoing quests
    vbox:
        style "quest_panel"
        frame:          # The frame window is used for dialogue, which has a maroon color
            has vbox    # Give it the size of the vbox
            text "{b}" + "{0} quests".format(unicode.title(currentQuestType)) + "{/b}"
            if currentQuests:
                # Grid and scroll bar
                side "c r":
                    # Create a grid of 1 column, and n rows
                    $ _vpgrid_name = "quest_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 20
                        draggable True
                        mousewheel True
                        style "quest_vpgrid"
                        # Show each quest in the dictionary
                        for questID in currentQuests:
                            # Create horizontal boxes with style "quest_entry" for each grid box
                            frame:
                                style "quest_entry"
                                background Solid(questColour[currentQuestType])
                                vbox:
                                    # Description of the quest
                                    $ currentQuest = currentQuests[questID]
                                    text "{b}" + "Quest: {0}".format(questID) + "{/b}"
                                    for infoKey in questInfo:
                                        $ _info_string = ""
                                        $ _info_string += "{b}" + "{0}: ".format(unicode.title(infoKey)) + "{/b}"
                                        if currentQuest[infoKey]:
                                            $ _info_string += currentQuest[infoKey]
                                        else:
                                            $ _info_string += "None"
                                        text _info_string
                                    # Show the description when clicked upon
                                    textbutton "Show description":
                                        action SetScreenVariable("currentQuestID", questID)
                                    # Depending on the quest type, have different options
                                    if currentQuestType == "available":
                                        textbutton "Start quest":
                                            action [
                                                Function(quests.startQuest, questID),
                                            ]
                    # Add scrollbar
                    vbar value YScrollValue(_vpgrid_name)
            # If there are no quests, show a message
            else:
                text "No quests are currently {0}".format(currentQuestType)
    use quest_info(currentQuestID, currentQuests)

# Longer description
screen quest_info(currentQuestID, currentQuests):
    default longQuestInfo = ["description", "dependencies"]
    vbox:
        style "quest_info"
        frame:          # The frame window is used for dialogue, which has a maroon color
            xsize 625
            ymaximum 200
            has vbox    # Give it the size of the vbox
            if currentQuestID not in currentQuests:
                text "{b}A quest has not been selected{/b}"
            else:
                $ currentQuest = currentQuests[currentQuestID]
                text "{b}" + "Quest: {0}".format(currentQuestID) + "{/b}"
                for infoKey in longQuestInfo:
                    text "{b}" + "{0}".format(unicode.title(infoKey)) + "{/b}"
                    if currentQuest[infoKey]:
                        if infoKey != "dependencies":
                            text "{0}".format(currentQuest[infoKey])
                        else:
                            text quests._getDependencyString(currentQuestID)
                    else:
                        text "None"


##############################################
style quest_entry:  # Used for easy quest entry in the list
    xsize 650
    ysize 40

style quest_panel:  # Used for the top quests
    xsize 650
    ysize 450
    xoffset 720
    yoffset 95

style quest_info:  # Used for the quests info
    xsize 625
    ysize 20
    xoffset 720
    yoffset 565
    

style quest_vpgrid: # Used to display a list of quests
    xsize 600
    ysize 415

style quest_select: # Used to describe the quest type selection menu
    xmaximum 625
    xoffset 700
    ysize 20
    yoffset 45
# alpha = transparency for images