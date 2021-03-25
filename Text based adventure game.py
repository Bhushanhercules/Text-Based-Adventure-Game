global health 
health = 10
try:
    name=str(input('Enter your name: '))
    age=int(input('Enter your age: '))

    if age>=12:
        print('Great!, Your eligible to play this game')
        ask=int(input('Shall we start the game?\n1.Yes.\n2.No\n-> '))

        if ask == 1:
            print('So your on the way to an adventures Life')
            print('And the road is dividing into Left and Right')
            choice1=int(input('Which path you will chose?\n1.Left\n2.Right\n-> '))

            if choice1==1:
                print("Now there is a House and a Strange Pond , So what will you chose? house or pond")
                choice2=int(input('Enter your choice\n1.House\n2.Pond\n-> '))

                if choice2==1:
                    newhealth=health-5
                    print('There was gang of bad guys\n You had a fight with them and you lose your health.')
                    print('Your recent health is %s' % newhealth)
                        
                elif choice2 == 2:
                    print("You have a happy life now. \nYou live by fishing in the Pond.")
                    wlcm=str(input('Write thankyou to me for saving you: '))
                    print("Your Welcome")
                else:
                    print('You entered wrong value')
                    
            elif choice1==2:
                print("You encounter a Monster near a cave, would you like to Run or Attack")
                choice3=int(input('Enter your decision.\n1.Run\n2.Attack\n-> '))

                if choice3== 1:
                    print("You run but the monster grabed you from behind and you lost your life")
                    print("Better Luck Next Time!")
                        
                elif choice3== 2:
                    print("You found two weapons nearby a Flamethrower or a Sword")
                    choice4=int(input('which one would you choose?\n1.Flamethrower.\n2.Sword\n-> '))

                    if choice4==1:
                        print("You burned that monster with flamethrower")
                        print("As you entered in the cave you found treasure in it")
                        print("And you lived a happy life")
                        wlcm1=str(input('Write thankyou to me for saving you: '))
                        print("Your Welcome")
                            
                    elif choice4==2:
                        new_health = health - 7
                        print("You barely survived with that Sword and somehow you managed to escaped")
                        print('Your recent health is %s' % new_health)
                            
                    else:
                        print('You entered wrong value')
                        
                else:
                    print('You entered wrong value')
                    
                    
            else:
                print('You entered wrong value')
                
        elif age == 2:
            print('As you wish')
        else:
            print('You entered wrong vlaue')
            
    else:
        print('Sorry, This game is only for thoes who are 12 or above 12')
except ValueError:
    print('You entered invalid value, Please enter valid value')
except NameError:
    print('You entered invalid words, Please enter from the words from given options')
except KeyError:
    print('You used wrong keys, plz try againg')

