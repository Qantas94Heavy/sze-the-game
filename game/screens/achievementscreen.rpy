screen achievementscreen(achievements=achievements):
# ensures other menu screens are replaced
    tag menu

    # Include the navigation menu
    use navigation
    add "Quests.jpg"

    # Give title of page
    frame:
        area (0, 0, 500, 50)
        text "Achievements": 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"
    
    default currentAchieveType = achievements.currentAchieveType
    
    # Create hbox to select achivement type to display
    hbox:
        style "achieve_select"
        frame:
            has hbox
            for achieveType in achievements.displayableAchieveTypes:
                textbutton unicode.title(achieveType):
                    action [
                        SetScreenVariable("currentAchieveType", achieveType),
                        Hide("achieve_description")
                    ]
    # Left vertical box for ongoing quests
    use achieve_info(currentAchieveType, achievements)
    use achieve_description
    


# Quest info
screen achieve_info(achieveType, achievements):
    default achieveColour = {
        "hidden":       "#b30000",
        "available":    "#e6ac00",
        "completed":    "#009933"
    }
    $ currentAchievements = getattr(achievements, achieveType)
    $ colour = achieveColour[achieveType]
    vbox:
        style "achieve_info"
        frame:          # The frame window is used for dialogue, which has a maroon color
            xsize 625
            has vbox    # Give it the size of the vbox
            text "{b}" + "{0} achievements".format(unicode.title(achieveType)) + "{/b}"
            if currentAchievements:
                # Grid and scroll bar
                side "c r":
                    # Create a grid of 1 column, and n rows
                    $ _vpgrid_name = "achievement_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 20
                        draggable True
                        mousewheel True
                        style "achieve_vpgrid"
                        # Show each quest in the dictionary
                        for achieveID, achievement in currentAchievements.iteritems():
                            use achieve_entry(achieveID, achievement, colour)
                    # Add scrollbar
                    vbar value YScrollValue(_vpgrid_name)
            # If there are no achievements, show a message
            else:
                text "No achievements are currently {0}".format(achieveType)

#Quest entry
screen achieve_entry(achieveID, achievement, colour):
    default achieveInfo = ["title", "brief"]
    vbox:
        style "achieve_entry"
        frame:
            xsize 600
            ymaximum 100
            background Solid(colour)
            has vbox
            text "{b}" + "Achievement: {0}".format(achieveID) + "{/b}"
            for option in achieveInfo:
                $ msg = "{b}" + "{0}: ".format(unicode.title(option)) + "{/b}"
                if not achievement[option]:
                    $ msg += "None"
                else:
                    $ msg += achievement[option] 
                text msg
            textbutton "Show description":
                action [
                    Show("achieve_description", achievement=achievement)
                ]

# Longer description
screen achieve_description(achievement=None):
    default achieveInfo = ["description", "dependencies"]
    vbox:
        style "achieve_description"
        frame:          # The frame window is used for dialogue, which has a maroon color
            xsize 625
            ymaximum 200
            has vbox    # Give it the size of the vbox
            if achievement:
                for option in achieveInfo:
                    text "{b}" + "{0}".format(unicode.title(option)) + "{/b}"
                    if not achievement[option]:
                        text "None"
                    else:
                        text achievement[option]           
            else:
                text "{b}An achievement has not been selected{/b}"


##############################################


style achieve_info:  # Used for the quests info
    xsize 625
    ysize 450
    xoffset 720
    yoffset 95

style achieve_vpgrid: # Used to display a list of quests
    xsize 600
    ysize 415

style achieve_entry:  # Used for easy quest entry in the list
    xsize 600
    ysize 40

style achieve_description:  # Used for the quests info
    xsize 625
    ysize 200
    xoffset 720
    yoffset 565
    
style achieve_select: # Used to describe the quest type selection menu
    xmaximum 625
    xoffset 700
    ysize 20
    yoffset 45
# alpha = transparency for images