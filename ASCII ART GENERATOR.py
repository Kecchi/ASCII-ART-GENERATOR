# Make a shape artwork with a repeating word, the * get replaced
import sys
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

#smile """
#...................................................................
#                  ****                 ****                        
#                *******               ******                       
#                  ****                 ****                        
#                                                                   
#         **                                    **                  
#         ****                                ****                  
#           *****                           *****                   
#                ******               ******                        
#                      ****************                             
#..................................................................."""

#
while True:

    print ('Create artwork with a word, shitpost potential ahead.')
#    print ("Would you like to try 'map', 'smile' or 'alpha' ?")

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

    while True:
        choice = input("Play again? (y/n): ").lower()

        if choice in ["y", "n"]:
            break
        print("Please enter 'y' or 'n', moron.")

    if choice == "n":
        print("GET OUTTA HERE!")
        break