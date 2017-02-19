# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:18:16 2017

@author: Joseph Lowman
Algorithmic Music Generator
"""
# https://www.reddit.com/r/dailyprogrammer/comments/5q9cll/20170126_challenge_300_easyintermediate_lets_make/

import winsound, time, pprint

def beep(freq, duration):
  freq= int(round(freq))
  duration = int(round(duration))
  winsound.Beep(freq, duration)
  
def solfege(starting_frequency): # e.g. do-re-mi-fa-sol-la-ti
  notes = [("do",starting_frequency), ("re",get_new_note(starting_frequency, 2)), 
  ("mi",get_new_note(starting_frequency, 4)), ("fa",get_new_note(starting_frequency, 5)),
  ("sol",get_new_note(starting_frequency, 7)), ("la",get_new_note(starting_frequency, 9)), 
  ("ti",get_new_note(starting_frequency, 11))]
  for note, f in notes:
    time.sleep(.25)
    print("playing note ",note, "at frequency ", int(round(f)), "Hz")
    beep(int(round(f)), 500)
   
  
def get_new_note(note, num_half_steps):
  half_step = 2.0**(1.0/12)
  new_note = note*(half_step)**num_half_steps
  return new_note  

def get_next_gen(current_gen, rule_number):
  binary_rule = (bin(rule_number)[2:]).zfill(8) #convert rule_number to binary
  combinations = [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)]
  rule = {}
  for j, combo in enumerate(combinations):
    rule[combo]= int(binary_rule[j])
      
  next_gen = [0]*len(current_gen)
  for i in range(1, len(next_gen)-1):
    for r in list(rule.keys()):
      if (current_gen[i-1], current_gen[i], current_gen[i+1])==r: 
        next_gen[i]=rule[r]
  
  return tuple(next_gen)
    
def cellular_auto(size, number_rows_output, rule_number): 
  first_gen = [0]*size   
  first_gen[size//2]=1
  first_gen = tuple(first_gen)
  all_gen = [(first_gen[:])]
  current_gen = first_gen
  for i in range(number_rows_output):
    next_gen = get_next_gen(current_gen, rule_number)
    all_gen.append(next_gen)
    current_gen = next_gen[:]
  return all_gen

def display(all_generations):
  for gen in all_generations:
    print("".join(str(gen)))    

def play_matrix(all_generations, freq, duration):
  for generation in all_generations:
    i=0
    for g in generation:
      if g: i+=1
    beep(get_new_note(freq, i), duration)

def main():
  middle_c = 261.625565
  #solfege(middle_c)
  all_generations = (cellular_auto(43, 50, 182))
  formatted_gen = display(all_generations)
  play_matrix(all_generations, 262, 200)
  
main()