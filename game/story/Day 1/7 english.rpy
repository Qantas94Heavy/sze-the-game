# first english class testing
label english1:
    "You arrive at {s}base camp{/s} ground floor of Wilkins"
    "You look up at the stairs, into the gaping maws of the infinite abyss"
    sze "Am I even bothered enough for this?"
    menu:
        "Fuck this shit, I'm out":
            $ sze.loss("fort")
            sze "I don't want to risk a heart attack"
            "You start turning around"
            "And stop before the forboding form of Moxham"
            mox "\"Well, well, well\""
            mox "\"You wouldn't happen to be turning away from your class, now, would you?\""
            menu:
                "I would":
                    sze "\"Yea, so what?\""
                    mox "\"So I'll extend to you an invitation to visit my {s}secret dungeon{/s} office after school\""
                    sze "\"Oh...\""
                    mox "\"But you were being honest, so if you turn around now, I might forgive you, just this once\""
                    sze "Damn, that was close"
                    jump eng1ascension
                "I wouldn't":
                    sze "\"N-n-no\""
                    mox "\"You lie\""
                    sze "\"ah, I, uh, wuz just, ah, going to go t-to the t-toilet... yeah, that's what I was doing\""
                    mox "\"Well, you do like you are about to piss yourself\""
                    $ sze.loss("strength")
                    mox "\"I expect you to be back here in 5 minutes, otherwise there will be consequences\""
                    sze "\"erm...'kay\""
                    "You have no choice but to comply"
                    jump eng1ascension
        "I actually need to pass":
            "You take a deep breath and {s}gather your qi{/s} mentally prepare yourself for the brutal climb"
            sze "I need to be {b}smart{/b} about this and {b}strong{/b} enough to make it successfully"
            jump eng1ascension

label eng1ascension:
            sze "Can't be too hard, just put one foot in front of the other"
            "..."
            sze "\"Just keep swimmin'\""
            "You notice Dean walk past you"
            dea "\"man, these steps are pretty stupid. We should just use rockets\""
            "..."
            sze "\"One flight down, three to go\""
            "..."
            sze "\"I can do this\""
            if sze.intellect > 5:
                "You notice Richard walk past you"
                sze "\"If Pheidippides of Athens could run from Marathon to Greece, I can get up these steps\""
                dik "\"Quite so, my good fellow! Persevere but a few seconds longer, then \"Joy to you, we've won\"!\""
                $ dik.gain()

            else:
                "You notice Richard walk past you"
                sze "\"if that greek guy could do that mara thing, then I can do these stairs too\""
                "You notice Richard shaking his head"
                dik "\"I almost pity thee. Thine incompetence is but a miracle beholden to few\""
                $ dik.loss()

            "..."
            "The second flight was down, half way"
            "You find yourself at the first floor, and allow yourself one second of respite"
            "Gary/Jitian staggers past"
            jit "\"Phew, good thing I have Strauss for English. This is as high as I need to go; sucks to be everyone else\""
            sze "\"lucky\""
            "..."
            "You pass by Chao, who, despite his girth, appears to be doing rather well"
            if cha.friendship > 1:
                cha "\"Hey Arthur, how's it going?\""
                sze "\"im fking dying\""
                cha "\"Y'know, since you had my back earlier on, I reckon I'll help you out. Aren't I a great guy?\""
                menu:
                    "\"im fking ded, halp me plz\"":
                        cha "\"Alright then, just stay put and I'll get you to the top in no time.\""
                        "Chao suddenly grabs you by the back of your shirt and dangles you over the edge of the building"
                        "He gets into a lopsided shotput pose"
                        $ sze.loss("strength")
                        cha "\"3\""
                        cha "\"2\""
                        cha "\"1\""
                        $ _englishstairs1rngthrow = renpy.random.randint(0, 6)
                        if _englishstairs1rngthrow > 4:
                            sze "\"Wait stop, let me down!!!!!\""
                            "You get launched through the air, rapidly reaching the top floor of the stairs" with vpunch
                            "However, you find yourself shooting past it"
                            "You continue going upwards"
                            "..."
                            "You have already expelled your bowel and bladder contents"
                            "..."
                            "The air is becoming rather thin, making it less easy to constantly scream"
                            "..."
                            "You are unsure if you are starting to drop or still continuing into the infinite blue expanse"
                            "..."
                            "You close your eyes and give up on life"
                            jump dead
                        elif _englishstairs1rngthrow >2:
                            sze "\"Wait stop, let me down!!!!!\""
                            "You get launched through the air, rapidly reaching the top floor of the stairs" with vpunch
                            "Despite the unusual and potentially dangerous method of travel, you do feel quite thankful to Chao."
                            "You lean over the edge and shout a few words to him"
                            sze "\"I don't know if I could've done the rest without a heart attack\""
                            cha "\"Oops I didn't let you down\""
                            sze "\"Thanks Chao, you are truly a great man\""
                            cha "\"Awww thanks Arthur\""
                            sze "\"Your heart is as big as you are\""
                            cha "\"...\""
                            cha "\"k\""
                            $ cha.gain()
                            jump english1top
                        elif _englishstairs1rngthrow <= 2:
                            "You get launched through the air, rapidly reaching the top floor of the stairs{nw}"
                            "But Chao didn't throw hard enough"
                            "Your fingers desperately grasp at, first, the metal railings, then, the concrete wall beneath it, then, anything at all"
                            "But your flailing attempts, like your chances with Serena, slip from your failing hands"
                            sze "\"Fuuuuuuuuuuuuuuucccckkk yooooooouuuuuuuuu chhaaaaaaaaaaaaoooooooo\""
                            cha "\"Fuuuuuuuuuuuuuuucccckkk yooooooouuuuuuuuu toooooooooooooooooooooo\""
                            rik "\"{i}He hit the ground, the sound was "SPLAT", his blood went spurting high{/i}\""
                            rik "\"{i}His comrades, they were heard to say "A HELL OF A WAY TO DIE!"{/i}\""
                            rik "\"{i}He lay there, rolling 'round in the welter of his gore,{/i}\""
                            rik "\"{i}And he ain't gonna jump no more.{/i}\""
                            jump dead
                    "\"thanks but nah\"":
                        sze "\"thanks for the offer\""
                        sze "\"but nah\""
                        sze "\"I\""
                        sze "\"must\""
                        sze "\"overcome\""
                        $ sze.gain("strength")
                        cha "\"gotta respect\""
                        cha "\"strength of body and of character\""
                        cha "\"and strong of body odour too...\""
                        $ sze.loss("charm")
                        cha "\"anyway, cya\""
                        jump english1flight3
            else:
                cha "\"Oh look who it is\""
                sze "\"uhh...hi chao\""
                cha "\"I'm tired\""
                sze "\"...\""
                sze "\"yeh so? aren't we all?\""
                cha "\"So i think i'll ride you\""
                "Before you can reply, he has hurled himself onto your back"
                if sze.strength >= 2:
                    "Somehow you manage to stay upright"
                    cha "\"giddyup horsie\""
                    sze "\"Urghgerroffyoufuglypoofter\""
                    cha "\"Save your energy, don't speak, just climb\""
                    "..."
                    "You get to the top of the third flight and decide to throw Chao off"
                    cha "\"Oi slave, what do you think you're doing?!\""
                    sze "\"You know you aren't cool doing that, right?\""
                    cha "\"Oh, tell me, why not?\""
                    menu:
                        "Exacerbate his insecurities":
                            sze "\"Cos all you're doing is proving that you're a chubby ass mofo\""
                            "You notice Dean and Richard nearby"
                            dea "\"Oh shit, good burn\""
                            dik "\"I doth doff my hat at thee, twas a well placed blow\""
                            $ sze.gain("charm")
                            cha "\"...\""
                            cha "\"gotta admit that was a good burn\""
                            cha "\"But perhaps you might be the one to help me make peace with my weight\""
                            cha "\"mebe you truly are The Chosen One\""
#                           include new quest - help chao lose his weight, pt.1 -> making peace with his weight
                            cha "\"Until next time, cya\""
                            $ cha.gain()
                            jump english1flight3
                        "Destroy his dignity":
                            if sze.intellect > 3:
                                sze "\"Clearly, ur desire to make me carry u is due to a desire to dominate\""
                                sze "\"This must be cos you get dominated by other people, but clearly not at school\""
                                cha "\"...\""
                                sze "\"Therefore, it must be in home environment\""
                                sze "\"So either ur gf dominates you or ur family does\""
                                sze "\"well?\""
                                sze "\"r u getting dominated by a LG?\""
                                sze "\"r u getting rekt by ur daddy?\""
                                sze "\"or is mummy expressing her desire for Oedipus complex by whipping ur ass?\""
                                cha "\"stfu, I'll remember this\""
                                sze "\"All of the above?\""
                                $ cha.loss()
                                "The people around you go quiet"
                                dea "\"That was fucking savage. Dunno, man, but you might've gone too far\""
                                dea "\"Still, those are good burns\""
                                $ sze.gain("charm")
                                jump english1flight3
                            elif sze.strength > 2:
                                sze "I would try something witty, but I'm probs not smart enough to do that this quickly"
                                sze "Looks like all I can do is use my fists then"
                                cha "\"Well?\""
                                sze "\"i'll let my fist explain\""
                                "You only have one shot at this"
                                "You feel time slowing down as you pull your elbow back"
                                sze "This is gonna be hard; I'll need to punch Chao for a combat score of 12, to do anything"
                                $ _english1stairspunchchao = renpy.random.randint(0, 6) + int(sze.strength)*2 + int(sze.intellect)
                                "Your fist flies forward, with a combat score of [_english1stairspunchchao]"
                                if _english1stairspunchchao > 11:
                                    "!!!"
                                    $ playsfx("hpunch.ogg")
                                    with hpunch
                                    sze "shit"
                                    "Chao has caught your fist"
                                    sze "\"welp\""
                                    sze "\"Do what you will\""
                                    cha "\"You tried\""
                                    cha "\"Gotta respect\""
                                    "He releases your fist, and extends his hand"
                                    sze "\"Ok\""
                                    $ cha.gain()
                                    jump english1flight3
                                else:
                                    "!!!"
                                    $ playsfx("hpunch.ogg")
                                    with hpunch
                                    "Chao stumbles back, holding his jaw"
                                    cha "\"You...\""
                                    "He jabs you a few times"
                                    cha "\"Omae Wa Mou Shindeiru\""
                                    sze "\"{i}N-Nani{/i}?!\""
                                    "You explode"
                                    jump dead
                            else:
                                sze "shit"
                                sze "so...how am I supposed to destroy his dignity"
                                sze "Would dignity even exist outside of society and social interaction?"
                                sze "Why must we have the inalienable right to be valued and respected?"
                                $ sze.gain("intellect")
                                sze "Do we deserve it?"
                                cha "\"Well?\""
                                sze "\"umm\""
                                sze "\"You're a dumbfuck\""
                                cha "\"lol\""
                                cha "\"Nice try\""
                                cha "\"Pretty sure you're more lacking in the mental department\""
                                sze "\"eh?\""
                                cha "\"I think I should put you out of your misery\""
                                sze "\"So you'll make me happy then?\""
                                "He jabs you a few times"
                                cha "\"Omae Wa Mou Shindeiru\""
                                sze "\"what?!\""
                                "You explode"
                                jump dead
                else:
                    "Unfortunately, your knees are weak, palms are sweaty"
                    $ playmusic("VarienThroneOfRavens.ogg")
                    "You are instantly flattened"
                    sze "\"gluuurrg-\""
                    "Your breath is pushed out of you, but Chao's mass prevents you from taking another"
                    "Your ribs are almost certainly shattered, your sternum faring no better"
                    "Even if you could take a breath, both of your lungs have already collapsed due to the multiple punctures"
                    "You feel blood filling your thoracic cavity, with each weakening pulse"
                    "In some distant space, through the fading light, you can hear Chao"
                    cha "\"Hey Arthur, cool prank, you can get up now\""
                    sze "i would if i could you fking fgt"
                    jump dead
label english1flight3:
    sze "3 out of 4"
    sze "75 percent"
    sze "I can do this"
    sze "\"arrggfuqtootired\""
    sze "\"One foot\""
    sze "\"in front\""
    sze "\"of the\""
    sze "\"other\""
    "As you trudge along, you see her"
    "Her radiant form inspires and stimulates you"
    $ sze.gain("thirst")
    "And gives you strength"
    $ sze.gain("strength")
    "Your heart is pumping, freshly oxygenated blood coursing through your body"
    if sze.thirst > 3:
        "You surge forward, with surefooted and steady steps, despite your nausea"
        "Your heart is racing"
        "You reach out, hoping to say something, anything to her. You have a pressure in your chest that you just need to get rid of."
        "The sound of your blood rapidly throbbing in your ears is all you hear"
        "You know, in this moment, you are no longer paralyzed by fear. You can talk to her, tell her how you feel {nw}"
        "Your heart rate, so fast, it simply quivers"
        sze "\"gaaa-\""
        "Your heart stops"
        if wil.friendship > 40:
            wil "\"lol, you idiot, you've overexerted yourself\""
            wil "\"I still need you around, so I can't let you die of a heart attack\""
            "Your consciousness is fading"
            "You hear Will say something vaguely"
            "There appears to be something going on in the background"
            wil "\"Well, here goes\""
            wil "\"Clear\""
            $ playsfx("vpunch.ogg")
            with vpunch
            sze "\"-aargh\""
            wil "\"Surprised that worked\""
            "Your blurry vision makes out a few battery shaped objects, connected to a big spring shaped thing"
            "Wires join the otherwise disconnected bits and pieces, with two leading to two accupuncture needles sticking near your right shoulder and left armpit"
#           can include random advanced quiz question
            wil "\"Well, you should be good to go\""
            wil "\"cya around\""
            jump english1top
        elif pra.friendship > 1:
            pra "\"Whoa, Arthur are you dead?\""
            sze "\"-aargh\""
            pra "\"Is that a yes or a no?\""
            sze "\"Huurgh\""
            pra "\"I think that's a yes\""
            "You aren't too sure what's going on, but you think you see Pragash deliberately prick his own finger"
            pra "\"Ouch\""
            pra "\"{i}Kuchiyose: Karegyangu{/i}\""
            sze "I must be dreaming"
            "{s}Curries{/s} People clearly of sub-continental descent appear around Pragash"
            pra "\"Thanks for appearing on such short notice, my dudes\""
            "Your consciousness fades"
            "..."
            sze "I'm taking a long time to die"
            sze "But is this dying?"
            sze "I feel too energetic"
            "..."
            "You can sense a form of life energy flowing into you"
            sze "I blink"
            sze "I sze"
            sze "\"Errm...why is there a bunch of guys putting there hands on me?\""
            pra "\"Brothers, it seems our work here is done\""
            pra "\"{i}kai{/i}\""
            "All the {s}Curries{/s} people of sub-continental descent disappear, as you blink"
            pra "\"I'll explain some other time, for now, I do believe we have English\""
            jump english1top
        else:
            wil "\"Lol, you look kinda funny\""
            sze "\"-rgh\""
            pra "\"Whoa, shit it moved\""
            pra "\"Dead bodies shouldn't move\""
            pra "\"Kill it dead\""
            jump dead
    else:
        "But you control your heart, and decide to approach some other time"
        $ sze.gain("thirst")
        "..."
        jump english1top
label english1top:
    "Captain's report, {s}February 4th, 2531{/s} January 28th, 2015"
    "{s}Five year, five long years.{/s} 5 minutes, 5 long minutes. That's how long it took to get {s}Harvest back{/s} to the top."
    "At first it was going well...{s}then setback after setback, loss after loss...{/s} step after step, sweat after sweat..."
    "Made what was going to be a {s}quick and decisive win{/s} normal journey to class..."
    "Into five minutes of hell..."
    "..."
    sze "I'm here"
    sze "On time"
    sze "Now who are my classmates?"
    "You aren't too familiar with a lot of the people"
    "However there are some who you do recognise"
    sze "Roy is pulling off fancy tricks with his yoyo, occasionally messing up"
    sze "Andrew is talking to someone you remember from a while ago..."
    sze "whatshisname?"
    sze "crap"
    sze "I think he's waving to me?"
    sze "\"Hi...uh...?\""
    menu:
        "Stefan":
            sze "\"Hi Stefan\""
            dng "\"lol, when did you get a lisp?\""
        "Steven":
            sze "\"Hi Steven\""
            dng "\"Hey Arthur\""
        "Stevo":
            sze "\"G'day Stevo\""
            dng "\"lmao when did you get so ozzie?\""
    sze "\"Bullshittery at its finest\""
    jump mthext1day1
