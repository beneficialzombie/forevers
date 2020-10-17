# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Piers")
define i = Character("Ivy")
define o = Character("Oliver")
define v = Character("Verity")
define f = Character("Finnegan")
define n = Character("noemi")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    scene bg ocean
    "The cold spray blasts against my face as I stand at the water’s edge, watching the burly vessel on the horizon slowly traverse the grey waters on its never-ending journey ferrying goods and passengers from the mainland to Mont-Desert Island and back."
    "The wind ruffles my overcoat, and I feel the slightest tinge of numbness creep into my fingertips."
    "As the ferry slips over the horizon, my attention remains fixed on the waves pounding against the walls of the harbour."
    "The temperature has hovered just below ten degrees centigrade for several days, but I don’t mind it."
    "If there ever was a reason to be bothered by the cold, the siege took away my ability to see it."
    "My hand rises to my throat, as it often does in moments of solitude, my fingers slipping beneath my collar. As always, it’s there."
    scene bg seawall
    "My hand drops to my side as I hear voices approach me. I spin around, my oversized coat billowing around my willow frame."
    "Two figures, one about my height, the other a head shorter, approach."
    "The taller of the two immediately catches my attention. Judging by the gait, it’s a man, somewhere in his mid-twenties."
    "His body is wrapped in a long grey coat, and he carries a large umbrella, shielding himself and his companion from the rain."
    "His face is entirely concealed behind a crimson mask, featureless except for small depressions through which a pair of brown eyes are visible."
    "The shorter figure is a girl, perhaps a little younger than me. Her blonde hair, swept aside by the wind, is untied, and her rosy face is uncovered."
    "She has something of a natural bounce to her step, and almost seems to glow despite the unpleasant weather. Her unusual eyes, one green, one blue, sparkle with excitement as she flashes me a welcoming smile."
    
    
    show ivy happy

    # These display lines of dialogue.
    
    i "HI-hi-hi! You're Meiss Piers, Right?"
    i "Welcome to Seawall! I'm Ivy, Ivy summers, from Dominic Academy!"
    i "How was the Ferry? Are you tired? Do you-"
    hide ivy
    show ivy happy at left
    "The masked man raises his hand, and the girl takes a step back, her face flushing."
    show oliver happy
    o "Blessings! I’m Brother Oliver. Please forgive our Meiss Summers, she tends to get excited when new residents arrive. Are you the only one today?"
    "His mask betrays no emotion, but his words are touched with warmth. I nod hesitantly, before bowing slightly, as I was instructed to do around civilians."
    show piers happy at right
    hide ivy
    p "Blessings, Meiss. And yes, I was alone on the ferry."
    hide oliver
    show oliver happy
    o "It’s good to have you among us."
    p "Thank you."
    "I bow my head slightly, causing the masked man to chuckle."
    o "No need to be so formal."
    "The girl shakes her head disbelievingly."
    hide oliver
    show ivy happy
    i "I heard you’re from the capital! Do you have news for us? What are people saying about the-"
    hide ivy
    show oliver happy
    o "Shhh, calm down! I’m sure Piers must be exhausted. Why don’t you bring him to his aeg? Just... don’t ask him too many questions, alright?"
    hide oliver
    show ivy happy
    i "I won’t be a bother!"
    "The blonde girl begins down the pathway, gesturing energetically for me to follow."
    "The trees quickly give way to a neat lane dotted on both sides with the towering domes of the local aegs."
    "Ivy turns a corner and stops in front of one of the houses, rifling through a ring of large brass keys. She unclips one and hands it to me."
    i "This is your place, number one-thirty-five! I live right across the road, so if you need anything at all, just knock! Number one-thirty-two, I’m usually at home!"
    p "Thank you, Meiss."
    i "Oh, it’s alright, just call me Ivy!"
    p "Your first name? I don’t think it would be proper for me to-"
    i "Don’t worry about it! We’re going to be great friends, I can feel it!"
    hide ivy
    hide piers
    "Without waiting for an answer, she spins around and gleefully skips off in the direction of her house."
    "I stand there for a moment, my head spinning. I’d never met anyone so… obnoxiously cheerful."
    "My hand reaches up to my neck again."
    "I decide to do a quick sweep of the lane."
    "The buildings are all identical in make, with any unique features most likely put in place by individual residents."
    "I take note of the dimensions of my lot, and check the integrity of the wrought-iron fence that borders it."
    "The strength seems acceptable, and as I close the gate behind me, I confirm that the lock is sufficiently new."
    "I take a stroll around the building, examining it from all angles."
    "The windows are mostly small and high off the ground, and each is fitted with wrought-iron bars."
    "Satisfied, I unlock the door and step inside."
    "The house is furnished, but not over-cluttered."
    "I flick the light switch, and quickly examine the furnishings:"
    " simple wooden table and chairs, rocket stove, icebox, air-con. Luxury by my standards."
    "I move upstairs, surveying the bathroom and bedroom."
    "Certainly an improvement over portable outhouses."
    "I clamber up the ladder and open a trapdoor, peering into the attic."
    "Like the rest of the house, it’s swept and dusted."
    "Thankfully, I won’t have much cleaning-up to do."
    "I wander back to the bedroom, and seat myself on the empty mattress, staring into space."
    show bg city
    with dissolve
    
    
    # This ends the game.

    return
