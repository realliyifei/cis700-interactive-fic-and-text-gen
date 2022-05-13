from game_classes import * 

def build_game():
    #  # Locations
    nowhere = Location("nowhere", "")
    
    # cottage = Location("Cottage", "You are standing in a small cottage.")
    # garden_path = Location("Garden Path", "You are standing on a lush garden path. There is a cottage here.")
    # cliff = Location("Cliff", "There is a steep cliff here. You fall off the cliff and lose the game. THE END.")
    # cliff.set_property('end_game', True)
    # fishing_pond = Location("Fishing Pond", "You are at the edge of a small fishing pond.")
    
    top_of_building_aug = Location("Top of Building August 21st",
                                  "You are standing on the roof. Your watch shows Aug 21.")
    lab = Location("Lab", "A lab, a foundation")
    time_machine = Location("Time machine", "The time machine invented by your lab partner in the future.")
    top_of_building_jul = Location("Top of Building July 28th",
                                  "You are standing on the roof. Your watch shows Jul 28.")
    stair_case = Location("Stair Case", "You're walking in the stair. It's a bit dark here.")
    floor_7 = Location("Floor 7", "You are in the 7th floor.")
    floor_8 = Location("Floor 8", "You are in the 8th floor.")
    storage_room = Location("Storage Room", "A storage room, dark and wet. "
                                            "Kurisu's dad pushs Kurisu and grabs a folder that contains Kurisu's paper about time machine from her.\n"
                                            "You can see a metal upa (a small metal toy) in the folder.\n"
                                            "He waves a knife and threatens to kill Kurisu.")

    
    # Connections
    # cottage.add_connection("out", garden_path)
    # garden_path.add_connection("west", cliff)
    # garden_path.add_connection("south", fishing_pond)
    
    top_of_building_aug.add_connection("down", lab)
    lab.add_connection("up", top_of_building_aug)
    top_of_building_aug.add_connection("get into time machine", time_machine)
    time_machine.add_connection("time travel to august", top_of_building_aug)
    time_machine.add_connection("time travel to july", top_of_building_jul)
    top_of_building_jul.add_connection("get into time machine", time_machine)
    top_of_building_jul.add_connection("in", stair_case)
    stair_case.add_connection("down", floor_8)
    floor_8.add_connection("down", floor_7)
    floor_8.add_connection("east", storage_room)
    
    # Items that you can pick up
    # fishing_pole = Item("pole", "a fishing pole", "A SIMPLE FISHING POLE.", start_at=cottage)
    # potion = Item("potion", "a poisonous potion", "IT'S BRIGHT GREEN AND STEAMING.", start_at=cottage, take_text='As you near the potion, the fumes cause you to faint and lose the game. THE END.')
    # potion.set_property('end_game', True)
    # rose = Item("rose", "a red rose", "IT SMELLS GOOD.",  start_at=None)
    # fish = Item("fish", "a dead fish", "IT SMELLS TERRIBLE.", start_at=None)
    
    phone = Item("phone", "a phone",
                 "ON THE PHONE, YOU CAN SEE A NEWS PLAYING. A MIDDLE-AGE TIME MACHINE SCIENTIST SURVIVED AN AIRPLANE CRASH.\n "
                 "HIS TIME MACHINE PAPER LUCKILY SURVIVED BECAUSE A METAL UPA (A SMALL TOY FROM GASHAPON MACHINE) IN HIS FOLDER WAS DETECTED AT THE SECURITY CHECK.",
                 start_at=top_of_building_aug)
    one_dollar = Item("dollar", "a dollar", "A DOLLAR COIN", start_at=top_of_building_aug)  # need to take it to use it at the gashapon machine
    two_dollar = Item("another dollar", "another dollar", "ANOTHER DOLLAR COIN", start_at=top_of_building_aug)  # need to take it to use it at the gashapon machine
    lightsaber = Item("lightsaber", "a lightsaber", "A LIGHTSABER FILLED WITH RED FLUID", start_at=lab)
    empty_lightsaber = Item("empty lightsaber", "an empty lightsaber", "AN EMPTY LIGHTSABER WITH NO LIQUID INSIDE",
                            start_at=None)
    stun_gun = Item("stun gun", "a stun gun", "A STUN GUN THAT CAN BE USED TO PUT PEOPLE INTO COMA", start_at=lab)  # need to consider other cases when the stun gun is used against other people
    key = Item("key", "a key", "THE KEY TO OPEN THE DOOR TO THE STAIR CASE", start_at=lab)  # need to consider other cases when the stun gun is used against other people

    plastic_upa = Item("plastic upa", "a green plastic upa",
                      "A SMALL GREEN TOY FROM GACHAPON MACHINE THAT IS MADE OF PLASTIC.", start_at=None)
    metal_upa = Item("metal upa", "a metal upa", "A SMALL TOY FROM GACHAPON MACHINE THAT IS MADE OF METAL.",
                     start_at=None)
    metal_upa2 = Item("kurisu's dad's metal upa", "a metal upa from kurisu's dad's folder",
                      "A SMALL TOY FROM GACHAPON MACHINE THAT IS MADE OF METAL.", start_at=None)
    knife = Item("knife", "a knife", "A KNIFE THAT CAN HARM PEOPLE", start_at=None)
    saved_kurisu_event = Item("saved kurisu", "You have saved kurisu", "THE EVENT THAT YOU HAVE SAVED KURISU",
                              start_at=None)  # this is to be put in inventory and trigger the happing end of the game
    swapped_upa_event = Item("swapped upa", "You have swapped upa", "THE EVENT THAT YOU HAVE SWAPPED UPA",
                             start_at=None)  # this is to be put in inventory and trigger the happing end of the game
    timeline_checker = Item("time line checker", "a time line checker",
                            "A TIME LINE CHECKER THAT CHECK THE TIME LINE DESITATION", start_at=time_machine)
    
    # Sceneary (not things that you can pick up)
    # pond = Item("pond", "a small fishing pond", "THERE ARE FISH IN THE POND.", start_at=fishing_pond)
    # pond.set_property("gettable", False)
    # rosebush = Item("rosebush", "a rosebush", "THE ROSEBUSH CONTAINS A SINGLE RED ROSE.  IT IS BEAUTIFUL.", start_at=garden_path)
    # rosebush.set_property("gettable", False)
    
    gashapon_machine_which_next_upa_metal = Item("gashapon machine whose next upa is metal",
                                                 "a gashapon machine whose next upa is metal",
                                                 "A GASHAPON MACHINE FILLED WITH SMALL TOYS. YOU CAN PAY 2 DOLLAR TO GET THE METAL UPA" \
                                                 "TO USE THE MACHINE AND GET ONE TOY RANDOMLY. SOME ARE METAL AND SOME ARE PLASTIC.",
                                                 start_at=floor_7)
    gashapon_machine_which_next_upa_metal.set_property("gettable", False)
    gashapon_machine_which_next_upa_plastic = Item("gashapon machine whose next upa is plastic",
                                                  "a gashapon machine whose next upa is plastic",
                                                  "A GASHAPON MACHINE FILLED WITH SMALL TOYS.\n YOU CAN PAY 1 DOLLAR TO GET THE PLASTIC UPA" \
                                                  "TO USE THE MACHINE AND GET ONE TOY RANDOMLY.\n SOME ARE METAL AND SOME ARE PLASTIC.",
                                                  start_at=None)
    gashapon_machine_which_next_upa_plastic.set_property("gettable", False)
    door = Item("door", "a locked door", "A HUGE AND TOUGH DOOR IN THE MIDDLE.", start_at=top_of_building_jul)
    door.set_property("gettable", False)
    unlocked_door = Item("unlocked door", "an unlocked door", "THE DOOR IS UNLOCKED!", start_at=None)
    unlocked_door.set_property("gettable", False)
    kurisu = Item("kurisu", "Kurisu Makise",
                  "A 17-YEAR-OLD RED HAIR GIRL WHO IS A SCIENTIST AND THE TIME MACHINE INVENTOR IN THE FUTURE",
                  start_at=storage_room)
    kurisu.set_property("gettable", False)
    kurisu_dad = Item("dad", "Kurisu's dad",
                      "A TIME MACHINE SCIENTIST WHO STOLE TIME MACHINE PAPER FROM HIS DAUGHTER. YOU CAN SEE THAT A METAL UPA IS IN HIS FOLDER THAT CONTAINS THE TIME MACHINE PAPER.",
                      start_at=storage_room)
    kurisu_dad.set_property("gettable", False)
    unconscious_kurisu = Item("unconscious kurisu", "Unconscious Kurisu is lying on the floor",
                              "SHE HAS BEEN PUT INTO A COMA WITH A STUN GUN", start_at=None)
    unconscious_kurisu.set_property("gettable", False)
    fake_blood_kurisu = Item("fake blood kurisu", "Kurisu soaked in fake blood is lying on the floor",
                             "SHE HAS BEEN PUT INTO A COMA WITH A STUN GUN AND POURED FAKE BLOOD ONTO", start_at=None)
    fake_blood_kurisu.set_property("gettable", False)
    stabbed_kurisu = Item("stabbed kurisu", "Stabbed Kurisu is lying on the floor", "SHE HAS BEEN STABBED BY A KNIFE",
                          start_at=None)
    stabbed_kurisu.set_property("gettable", False)
    suzuha = Item("suzuha", "Suzuha Amane", "TIME TRAVELER FROM THE FUTURE.", start_at=top_of_building_aug)
    suzuha.set_property("gettable", False)
    
    # Add special functions to your items
    # rosebush.add_action("pick rose",  add_item_to_inventory, (rose, "You pick the lone rose from the rosebush.", "You already picked the rose."))
    # rose.add_action("smell rose",  describe_something, ("It smells sweet."))
    # pond.add_action("catch fish",  describe_something, ("You reach into the pond and try to catch a fish with your hands, but they are too fast."))
    # pond.add_action("catch fish with pole",  add_item_to_inventory, (fish, "You dip your hook into the pond and catch a fish.","You weren't able to catch another fish."), preconditions={"inventory_contains":fishing_pole})
    # fish.add_action("eat fish",  end_game, ("That's disgusting! It's raw! And definitely not sashimi-grade! But you've won this version of the game. THE END."))
    
    suzuha.add_action("talk to suzuha", describe_something,
                      ("Suzuha says, 'Kurisu is a genius scientist. You saw her in a blood pool on July 28th.\n"
                       "If you want to save her and change what has happened, you need to save her without changing what you yourself saw on that day.\n"
                       "Or else you will fail.\n"
                       "Remember how much you love her? Go back in time to deceive the world and save her!\n"
                       "Also, her dad uses the theory from her paper to invent the time machine and triggered WWIII.\n"
                       "To avoid WWIII, you need to destroy the paper. Now go!'"))
    door.add_action("unlock door", perform_multiple_actions,
                    ([(destroy_item, (door, "You unlock the door with the key.")),
                      (create_item, (unlocked_door, "The door opens into a landing with a few more stairs."))]),
                    preconditions={"inventory_contains": key, "location_has_item": door})
    gashapon_machine_which_next_upa_metal.add_action("use gashapon machine", perform_multiple_actions,
                                                     ([(destroy_item, (one_dollar, "You paid one dollar.")),
                                                      (destroy_item, (gashapon_machine_which_next_upa_metal,
                                                                      "The next upa in the machine is metal")),
                                                      # The gashapon machine gives your a plastic upa.
                                                      #  (create_item, (metal_upa, ""))]),
                                                      #  (create_item, (metal_upa, "")),
                                                      (add_item_to_inventory, (metal_upa, "Now you have metal upa.",
                                                                                "You already got metal upa")),
                                                      (create_item, (gashapon_machine_which_next_upa_plastic,
                                                                      "The next upa in the machine is plastic"))]),
                                                     preconditions={"inventory_contains_any": [one_dollar, two_dollar]})
    # preconditions = {"inventory_contains": two_dollar, "location_has_item": metal_upa})
    gashapon_machine_which_next_upa_plastic.add_action("use gashapon machine", perform_multiple_actions,
                                                      ([(destroy_item, (two_dollar, "You paid one dollar.")),
                                                         #  (create_item, (plastic_upa, "")),
                                                         (add_item_to_inventory, (
                                                         plastic_upa, "Now you have plastic upa.",
                                                         "You already got plastic upa")), ]),
                                                      preconditions={
                                                          "inventory_contains_any": [one_dollar, two_dollar]})

    kurisu_dad.add_action("hit kurisu's dad", create_item, (knife,
                                                            "You hit Kurisu's dad and his knife drops. You want to take the knife. \nAfter you have the knife, you can STAB KURISU'S DAD or SCARE KURISU'S DAD AWAY."))
    knife.add_action("take knife", add_item_to_inventory, (
    knife, "You pick the knife. Kurisu's dad looks crazy. You can STAB KURISU'S DAD or SCARE KURISU'S DAD AWAY",
    "You already picked the knife."))
    kurisu_dad.add_action("stab kurisu's dad", end_game,
                          ("Kurisu sees that you're going to stab her dad and rushes forward in front of her dad. \n"
                          "The knife doesn't go into Kurisu's dad's heart but instead Kurisu's. \n"
                          "She falls into your arm and the blood drips down and soaks your shirt. \n"
                          "Kurisu is still killed. This time not by her father but by you yourself. You fail to change what happened."),
                          preconditions={"inventory_contains": knife, "location_has_item": kurisu_dad})
    kurisu_dad.add_action("scare kurisu's dad away", destroy_item,
                          (kurisu_dad, "You waves the knife towards Kurisu's dad and he runs away."),
                          preconditions={"inventory_contains": knife, "location_has_item": kurisu_dad})
    kurisu_dad.add_action("swap upa", perform_multiple_actions,
                          ([(destroy_item, (plastic_upa, "You put your plastic upa in his folder.")),
                            (add_item_to_inventory, (swapped_upa_event, "", "")),
                            (add_item_to_inventory,
                             (metal_upa2, "You put the metal upa taken from the folder into your pocket.", ""))]),
                          preconditions={"inventory_contains": plastic_upa})
    kurisu.add_action("talk to kurisu", describe_something,
                      ("Kurisu replies, 'You're the person I saw just now. Why are you here?'"))
    kurisu_dad.add_action("talk to kurisu's dad", describe_something,
                          ("Kurisu's dad replies, 'Oh the two of you are trying to conspire something against me!'"))
    kurisu.add_action("stun kurisu", perform_multiple_actions,
                      ([(destroy_item, (kurisu, "'Hmmm....'")),
                        (create_item, (unconscious_kurisu, "Kurisu lies down on the floor."))]),
                      preconditions={"inventory_contains": stun_gun, "location_has_item": kurisu,
                                     "location_does_not_have_item": kurisu_dad})
    kurisu.add_action("use lightsaber", describe_something,
                      ("You want to poar the fake blood from lightsaber onto Kurisu to fake her death, "
                      "but she's confused about what you're trying to do and pushes you away."),
                      preconditions={"inventory_contains": lightsaber, "location_has_item": kurisu})
    unconscious_kurisu.add_action("use lightsaber", perform_multiple_actions,
                                  ([(destroy_item, (
                                  unconscious_kurisu, "You open the lightsaber and pour red liquid inside onto her.")),
                                    (create_item, (fake_blood_kurisu,
                                                  "Kurisu soaks in the red liquid, as if she is soaked in blood.")),
                                    (add_item_to_inventory, (
                                    saved_kurisu_event, "You fake Kurisu's death and save her!",
                                    "You already faked Kurisu's death.")),
                                    (destroy_item, (lightsaber, "")),
                                    (create_item, (empty_lightsaber, ""))]),
                                  preconditions={"inventory_contains": lightsaber,
                                                 "location_has_item": unconscious_kurisu})

    # timeline_checker.add_action_if("check timeline (end game)", [end_game, end_game, end_game, end_game],
    #                               [("You activate the Steins Gate Timeline successfully! El Psy Kongroo!"),
    #                                 (
    #                                     "You saved Kurisu but the time machine paper didn't get destroyed, so time machine was still invented and the third world war will happen."),
    #                                 (
    #                                     "You swapped the upa in Kurisu's dad's folder, so the time machine paper passed the airplane's security check and got destroyed. \n"
    #                                     "The third world war won't happen. But you didn't save Kurisu your love."),
    #                                 (
    #                                     "You didn't save Kurisu and didn't stop WWIII from happening. You live rest of your life in regret.")],
    #                               preconditions=[{"inventory_contains_all": [saved_kurisu_event, swapped_upa_event]},
    #                                               {"inventory_contains": saved_kurisu_event},
    #                                               {"inventory_contains": swapped_upa_event},
    #                                               {}])
    timeline_checker.add_action("check timeline (end game)", end_game,
                                ("You activate the Steins Gate Timeline successfully! El Psy Kongroo!"),
                                preconditions={"inventory_contains_all": [saved_kurisu_event, swapped_upa_event]})

    
    
     # Blocks
    top_of_building_jul.add_block("in", "There is a locked door here.",
                                  preconditions={"location_does_not_have_item": door})
    
    return Game(lab)
            
            