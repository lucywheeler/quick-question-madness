#!/usr/bin/python

print "Hello. What is your name?"
name = raw_input()

print "Hello, " + name + ". It's nice to meet you."
print " my name is Alexa I am a girl "

print "What is your brother's name, " + name + "?"
brother_name = raw_input()

print "your brother's name is " +  brother_name + "."

print "What is your favorite food?"
favorite_food = raw_input()

print  "your favorite food is " + favorite_food + "."

if favorite_food.lower() == "dumplings":
    print "that is mine too"
else:
    print "That is awesome!"

print "What is your favorite color?"
color = raw_input()

print "my favorite color is purple"

print "what is your favorite sport"
sport = raw_input()

print "that is very cool"

if sport.lower() == "soccer":
    print "that is mine too"
else:
    print  "mine is soccer"

print "what is your favorite kind of pet?"
pet = raw_input()

if pet.lower() == "dog":
    print "that is mine"
else:
    print "mine is a dog"

print "when you were little what was the most embarrising thing that happened to you ?"
embarrising_thing = raw_input()

print "hahahahaha!"

print "Please play Quick Question Madness again bye hope to see you soon!"
