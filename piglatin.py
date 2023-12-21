#####################################################################################
#Joti Gokaraju
#CS20 P5 S1
#20/12/2023
#Pig Latin Converter
#Purpose: To Build a Streamlit App that Converts Regular Text to Pig Latin
#####################################################################################


#Import Streamlit
import streamlit as st

#Preset Values
vowels = 'aeiouy'
numbers = '1234567890'
letters = 'abcdefghijklmnopqrstuvwxyz'
capitol_letters = letters.upper()
punctuation = ':;,.-!?'

#Headers
st.title("Pig Latin Converter")
st.header("*Joti Gokaraju CS20 P5 12/20/2023*")
st.divider()

start_word = st.text_input("Text to Translate", placeholder="Type the Text...")
st.write("You Entered:", start_word)

#Adjust Start_Word to Append Words into List one at a time
start_word = str(start_word).split()


def punctuation_check(word, punctuation, character_num, vowel_start):
    ''' Checks if Punctuation Exists and Keeps Punctation after translated_word '''
    last_word = len(word)-1
    if vowel_start == True:
        if any(character in punctuation for character in word):
            return word[:last_word] + "yay" + word[last_word] + " "
        else:
            return word + "yay" + " "
            
    else:
        if any(character in punctuation for character in word):
            return word[character_num:last_word] + word[:character_num] + "ay" + word[last_word] + " "
        else:
            return word[character_num:] + word[:character_num] + "ay" + " "


def capitol_check(translated_word, character, capitol_letters, word):
    ''' if the original word contained a capital, it will capitalize the first letter of the new word '''
    if any(character in capitol_letters for character in word):
        
        if len(translated_word)-len(word)-3 > 1:
            capitolize_word = len(translated_word)-len(word)-3
        else:
            capitolize_word = 0
        
        return translated_word[:capitolize_word] + translated_word[capitolize_word:].capitalize()
    else:
        return translated_word


def translate(phrase, numbers, letters, capitol_letters, punctuation):
    ''' Translate Phrase to Pig Latin With Capitolization and Proper Punctuation '''
    translated_word = ""
    
    for word in phrase:
        character_num = -1
        
        if all(character not in letters for character in word) and all(character not in capitol_letters for character in word):
            translated_word += word + " "
        else:
            for character in word:
                character_num += 1
                
                if character in vowels or character in vowels.upper():

                    if character_num == 0:
                        translated_word += punctuation_check(word, punctuation, character_num, True)
                        #Capitol Check is unneeded here because if the vowel is the first word, the word is the same so capitals are preserved regardless. 
                    else:
                        translated_word += punctuation_check(word, punctuation, character_num, False)
                        translated_word = capitol_check(translated_word, character, capitol_letters, word)
                    
                    break
    
    return translated_word


#Run The Program on Button Click
if st.button("Convert!", type="primary"):
    phrase = start_word
    st.write(translate(phrase, numbers, letters, capitol_letters, punctuation))
    
