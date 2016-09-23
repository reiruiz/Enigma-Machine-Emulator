print "Enigma Simulator"

#   Open the init.txt file:
initfile=open('init.txt', 'r')

#   Read the first line:
alphabet=initfile.readline()
alphabet=alphabet[0:38]

#   Read the second line:
rotor1=initfile.readline()
rotor1=rotor1[0:38]

#   Read the third line:
rotor2=initfile.readline()
rotor2=rotor2[0:38]

#   Read the starting positions:
startpos=initfile.readline()
startpos=startpos[0:5]
startlist=startpos.split()

print "\nSimulator initialized:"
print "Alphabet:","["+alphabet+"]"
print "Rotor 1:","["+rotor1+"]; starting position",startlist[0]
print "Rotor 2:","["+rotor2+"]; starting position",startlist[1]

command=raw_input("\nCommand? ")

poscountrot1=0
poscountrot2=0

while command != 'q' and command != 'Q':

#   Encodes the input:
    if command == 'e' or command == 'E':
        n=0
        torotor2=''
        rotor1=rotor1[int(startlist[0]):]+rotor1[0:int(startlist[0])]       #   Moves the starting position of Rotor 1 to that of the init.txt
        rotor2=rotor2[int(startlist[1]):]+rotor2[0:int(startlist[1])]       #   Moves the starting position of Rotor 2 to that of the init.txt
        passnum=0
        poscountrot1=0
        poscountrot2=0

        print "\nRotors stepped and configured:"
        print "Rotor 1:","["+rotor1+"]"
        print "Rotor 2:","["+rotor2+"]"

        encode=raw_input("\nENCODING: Please enter plaintext: ")
    
        while n < len(encode):
            alpha=encode[n]
            findalpha=alphabet.find(alpha)      #   Finds the offset of the first character of the input in the alphabet.
            if  findalpha == -1:                #   If the character is not in the valid alphabet, it will not encode it.
                torotor2=torotor2+alpha
                n=n+1
            else:
                torotor1=rotor1[findalpha]      #   Uses the offset to convert it to the character of the same offset in Rotor 1.
                rotor1toalpha=alphabet.find(torotor1)       #   Finds the same character of Rotor 1 in the alphabet and records its offset.
                torotor2=torotor2+rotor2[rotor1toalpha]       #   Adds the results.
                if passnum == 38:        #   Rotates Rotor 2 if the number of passes exceed 38.
                    rotor1=rotor1[1:]+rotor1[0]
                    rotor2=rotor2[1:]+rotor2[0]
                    poscountrot2=poscountrot2+1
                    poscountrot1=poscountrot1+1
                    passnum=0
                else:       #   If the number of passes doesn't exceed 38, it rotates Rotor 1.
                    rotor1=rotor1[1:]+rotor1[0]
                    poscountrot1=poscountrot1+1
                passnum=passnum+1
                n=n+1
        print "Encoded message is:",torotor2
        command=raw_input("\nCommand? ")


#   Decodes the input:
    if command == 'd' or command == 'D':
        n=0
        rotor1toalpha=''
        rotor1=rotor1[int(startlist[0]):]+rotor1[0:int(startlist[0])]       #   Moves the starting position of Rotor 1 to that of the init.txt
        rotor2=rotor2[int(startlist[1]):]+rotor2[0:int(startlist[1])]       #   Moves the starting position of Rotor 2 to that of the init.txt
        passnum=0
        poscountrot1=0
        poscountrot2=0

        print "\nRotors stepped and configured:"
        print "Rotor 1:","["+rotor1+"]"
        print "Rotor 2:","["+rotor2+"]"

        decode=raw_input("\nDECODING: Please enter plaintext: ")

        while n < len(decode):
            torot2=decode[n]
            findrotor2=rotor2.find(torot2)      #   Finds the offset of the first character of the input in Rotor 2.
            if findrotor2 == -1:        #   If the character is not in Rotor1, it will not decode it.
                rotor1toalpha=rotor1toalpha+torot2
                n=n+1
            else:
                toalpha=alphabet[findrotor2]     #   Uses the offset to convert it to the character of the same offset in the alpabet.
                alphatorotor1=rotor1.find(toalpha)        #   Finds the same character of the alphabet in Rotor 1 and records its offset.
                rotor1toalpha=rotor1toalpha+alphabet[alphatorotor1]        #   Adds the results.
                if passnum == 38:        #   Rotates Rotor 2 in the opposite direction if the number of passes exceed 38.
                    rotor1=rotor1[1:]+rotor1[0]
                    rotor2=rotor2[1:]+rotor2[0]
                    poscountrot2=poscountrot2+1
                    poscountrot1=poscountrot1+1
                    passnum=0
                else:       #   If the number of passes doesn't exceed 38, it rotates Rotor 1.
                    rotor1=rotor1[1:]+rotor1[0]
                    poscountrot1=poscountrot1+1
                passnum=passnum+1
                n=n+1
        print "Decoded message is:",rotor1toalpha
        command=raw_input("\nCommand? ")

#   Re-initializes the rotors:
    if command == 'i' or command == 'I':
        initfile=open('init.txt','r')

        alphabet=initfile.readline()
        alphabet=alphabet[0:38]

        rotor1=initfile.readline()
        rotor1=rotor1[0:38]

        rotor2=initfile.readline()
        rotor2=rotor2[0:38]

        startpos=initfile.readline()
        startpos=startpos[0:5]
        startlist=startpos.split()
        print "\nSimulator re-initialized."
        print "Alphabet:","["+alphabet+"]"
        print "Rotor 1:","["+rotor1+"]; starting position",startlist[0]
        print "Rotor 2:","["+rotor2+"]; starting position",startlist[1]
        command=raw_input("\nCommand? ")

#   Checks the status of the rotors:
    if command == 's' or command == 'S':
        print "Rotor 1:","["+rotor1+"]"
        print "Rotor 2:","["+rotor2+"]"
        print "\nNumber of times Rotor 1 has moved:",poscountrot1
        print "Number of times Rotor 2 has moved:",poscountrot2
        command=raw_input("\nCommand? ")

initfile.close()
print "\nGoodbye!"
