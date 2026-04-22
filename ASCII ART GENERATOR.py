# Make a shape artwork with a repeating word, the * get replaced
import sys
import random
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

smile = """
...................................................................
                  ****                 ****                                                
                 ******               ******                                              
                  ****                 ****                                                
                                                                                                                                                      
         **                                    **                                    
         ****                                ****                                    
           *****                           *****                                      
                ******               ******                                                
                      ****************                                                          
..................................................................."""

peace = """
...................................................................
                                                                          
                    *******                  
                   **     **                  
                  **      **                  
                  **      **      
                  **      **                  
                  **      **                  
                  **      **                  
                  **      **                  
                 ***      ***                  
                 ***      ***                 
           *********       ***                    
          ***    **        ******               
         ***      *        ***    ***             
      ****        *        *       **           
   ******         *        *       *****             
  **    *         *        *       **  ***
***    **        **       **       **    **
**     **                          **     ***
*      **                           **      **
**     **                                    **
****                                         **
 ****                                       ***
   ****                                    ***
     ****                                ***
       *****                           ****
          *****                       ***                 
            ***                      ***                 
             **                      **                 
             **                     **                 
             **                     **                 
             *************************                 
                                                                          
..................................................................."""


sass = ["EXCUSE ME??", "Thank god ur not a moron...oh wait.", "This shit can't be serious", "Bro...not cool.", "DUDE COME ON!", "If this was real I would be so mad"]
question = ("Would you like to try 'map', 'smile' or 'peace' ?")
choices = ["map", "smile", "peace"]


#8================================================================================


while True:

    print ('Create artwork with a word, shitpost potential ahead.')
    print (question)
    
    answer = input('>').lower()
    if answer not in choices:
        print (random.choice(sass))

    if answer == "map":
        print ('Enter the message to display with the bitmap NOW!')
        message = input('>')
        if message == '':
            sys.exit()

        for line in bitmap.splitlines():
            for i, bit in enumerate(line):
                if bit == ' ':
                    print (' ', end='')
                else:
                    print(message[i % len(message)], end='')
            print()

    if answer == "smile":
        print ('Enter the message to display with the smile NOW!')
        message = input('>')
        if message == '':
            sys.exit()

        for line in smile.splitlines():
            for i, bit in enumerate(line):
                if bit == ' ':
                    print (' ', end='')
                else:
                    print(message[i % len(message)], end='')
            print()

    if answer == "peace":
        print ('Enter the message to display with the peace NOW!')
        message = input('>')
        if message == '':
            sys.exit()

        for line in peace.splitlines():
            for i, bit in enumerate(line):
                if bit == ' ':
                    print (' ', end='')
                else:
                    print(message[i % len(message)], end='')
            print()

#8================================================================================

    while True:
        choice = input ("Play again? (y/n): ").lower()

        if choice in ["y", "n"]:
            break
        print("Please enter 'y' or 'n', moron.")

    if choice == "n":
        print("GET OUTTA HERE!")
        break
