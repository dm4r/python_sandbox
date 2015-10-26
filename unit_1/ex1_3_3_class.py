class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
            print ""

class Bassist(Musician): # arent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Drummer, self).__init__(["Boom", "Boom", "Boom"])

    def count(self):
        print "And a One, Two, Three, Four!"

    def combust(self):
        print "The Drummer has combusted into a rock flame!"

class Band(object):
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def hire(self, musician):
        self.members.append(musician)

    def fire(self, musician):
        self.members.remove(musician)

def main():
    bob = Guitarist()
    print bob.tune()

    nigel = Bassist()
    slash = Drummer()

if __name__ == '__main__':
  main()
