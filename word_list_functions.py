
def make_plain_text(text):
#Converts raw text input including linebreaks and punctuation and converts into plain text. 
#Preserves any accented letters. 
   text = text.lower()
   text = text.replace("\n", " ").replace("\r", " ").replace("  ", " ")
   text = "".join(character for character in text if character.isalpha() or character.isspace())
   return text
   
def transliterate_diacritics(text):
#Replaces letters with diacritics with a latin alphabet transliteration. 
#This is to follow convention in English language crossword construction, where accents are not included. 
#Let's not get into linguistic ethics here. I know they're not really equivalent. We're just making a crossword. 
#This is never going to be a complete list but should cover most instances occuring in English text sources. 
   diacritic_dictionary = {'dž': 'dzs', 'i': 'i', 'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'a', 'å': 'a', 'æ': 'ae', 'ç': 'c', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i', 'ñ': 'n', 'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ø': 'oe', 'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 'ý': 'y', 'ÿ': 'y', 'ā': 'a', 'ć': 'c', 'ĉ': 'c', 'č': 'c', 'ď': 'd', 'đ': 'd', 'ē': 'e', 'ĝ': 'g', 'ğ': 'g', 'ģ': 'g', 'ĥ': 'h', 'ī': 'i', 'ĵ': 'j', 'ķ': 'k', 'ĺ': 'l', 'ļ': 'l', 'ľ': 'l', 'ņ': 'n', 'ň': 'n', 'ŉ': 'n', 'ō': 'o', 'ŕ': 'r', 'ŗ': 'r', 'ŝ': 's', 'ş': 's', 'š': 's', 'ť': 't', 'ū': 'u', 'ŭ': 'u', 'ŵ': 'w', 'ŷ': 'y', 'ž': 'z', 'ǟ': 'a', 'ț': 't', 'ȭ': 'o', 'ȯ': 'o', 'ȱ': 'o', 'ḑ': 'd', 'ẁ': 'w', 'ẃ': 'w', 'ẅ': 'w', 'ỳ': 'y'}
   for diacritic, plain in diacritic_dictionary.items():
    text = text.replace(diacritic, plain)
   return text 
   

def make_clean_list(text):
#Converts processed text into an ordered list with no duplicates.
   text = text.split()
   text = list(set(text))
   text.sort()
   return text

def censor_list(list):
#Removes words from list which are found in specificed censorship list. They are replaced by nothing. 
#Have not produced censor list yet. Feels awkward!
    censorship_list = ["testtesttest"]
    censored_list = [word for word in list if word not in censorship_list]
    return censored_list
 

def fully_process_text(text):
#Fully processes raw text into a clean word list. In order, it is:
#Made into plain text. 
#Diacritics are transliterated into latin characters. 
#Text string is converted into ordered list and duplicates removed. 
#List is censored as per specification. 
    text = censor_list(make_clean_list(transliterate_diacritics(make_plain_text(text))))
    return text
    

def remove_existing_words(new_list, reference_list):
#Compares list to reference list and removes any word which occurs in reference/
#Leaving you with only the new unique words!
    return [word for word in new_list if word not in reference_list]



#                        .
#                       -|-
#                        |
#                    .-'~~~`-.
#                  .'         `.
#                  |  R  I  P  |
#                  |           |
#                  |           |
#                \\|           |//
#--------------------GRAVEYARD-------------------#   
#things that i don't need but might be useful to reference later
   
#diacritic_characters = ['dž', 'i', 'à', 'á', 'â', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'ÿ', 'ā', 'ć', 'ĉ', 'č', 'ď', 'đ', 'ē', 'ĝ', 'ğ', 'ģ', 'ĥ', 'ī', 'ĵ', 'ķ', 'ĺ', 'ļ', 'ľ', 'ņ', 'ň', 'ŉ', 'ō', 'ŕ', 'ŗ', 'ŝ', 'ş', 'š', 'ť', 'ū', 'ŭ', 'ŵ', 'ŷ', 'ž', 'ǟ', 'ț', 'ȭ', 'ȯ', 'ȱ', 'ḑ', 'ẁ', 'ẃ', 'ẅ', 'ỳ']
#plain_characters = ['dzs', 'i', 'a', 'a', 'a', 'a', 'a', 'ae', 'c', 'e', 'e', 'e', 'e', 'i', 'i', 'i', 'i', 'n', 'o', 'o', 'o', 'o', 'o', 'oe', 'u', 'u', 'u', 'u', 'y', 'y', 'a', 'c', 'c', 'c', 'd', 'd', 'e', 'g', 'g', 'g', 'h', 'i', 'j', 'k', 'l', 'l', 'l', 'n', 'n', 'n', 'o', 'r', 'r', 's', 's', 's', 't', 'u', 'u', 'w', 'y', 'z', 'a', 't', 'o', 'o', 'o', 'd', 'w', 'w', 'w', 'y']
#diacritic_dictionary = {diacritic_characters[i]: plain_characters[i] for i in range(len(diacritic_characters))}

