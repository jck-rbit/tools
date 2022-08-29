# activity suggestion based on mood

# intro

state = input( "hey felicia :) you're not feeling so good? could you pick which one is the closest? I'm feeling: agitated, heavy, dizzy " )

why = input( "do you know why? " )

if 'y' in why:
    print(" that's great :D! whether you can or can't control it, take a breather. try to let go if it's something you can't control, and do what you can if it's something you can. life is full of randomness, and something that is bad right now might come out to be good later. godspeed and good night :)" )

else:
    if state == 'agitated':
        print("you know what to do! let's rock out to some banging tunes >:), could be here, could be outside. get yourself some physical activity! if you feel like you might hurt yourself though, call eldrin. this is serious and you need support. godspeed and have fun <3" )
    
    elif state == 'heavy':
        to_do = input("do you have anything you need to do right now? ")
        if 'y' in to_do:
            print("set an alarm for you to just sit up. nothing else. the follow on with an alarm to get up. if the next step feels too hard, set an alarm for that next step. clean yourself up and take a shower maybe. hopefully after all of that you'll feel a bit better. godspeed and good luck :)")
        else:
            print("let's take care of ourselves then! it's ok to be a bit lazy <3. why not call eldrin? if that's too hard, or he's not available, we can watch some nice fun videos like: rossboomsocks, cute animal videos, any tv show you like (saiki?). godspeed and good night :)")
    elif state == 'dizzy':
        print("oh dear! i think it's time for you to eat something or drink something! sit down a bit and take it easy :) hope you feel better soon!")
