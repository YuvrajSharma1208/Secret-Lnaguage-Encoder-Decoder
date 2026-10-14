import random
import string



def encode_word(word):
   if (len(word)>= 3):
      modified = word[1:] + word[0]

      star_charac = ''.join(random.choices(string.ascii_lowercase,k=3))
      end_charac = ''.join(random.choices(string.ascii_lowercase,k=3))

      return star_charac + modified +end_charac
   else:
      return word[::-1]

   
def decode_word(secret_word):

   if (len(secret_word)<3):
      return secret_word[::-1]
   else:
      stripped = secret_word[3:-3]

      original = stripped[-1]+stripped[:-1]

      return original
def secret_language():
   
   choices= input("Enter '1' for Coding (Encrypt) and '0' for Decoding (Decrypt) : " ).strip()

   

   if (choices =='1'):

      sentence = input("Enter Your Sentence: ")
      
      
      words = sentence.split()

      encode_words = [encode_word(w) for w in words]

      print("Encoded Message is : ", ' '.join(encode_words))

   elif (choices == '0'):

      sentence = input("Enter Your Sentence: ")
      
      
      words = sentence.split()

      decode_words = [ decode_word(w) for w in words]

      print("Decoded Message is : ", ' '.join(decode_words))

   else:
      print("Invalid Choice! Please enter 1 or 0.")


secret_language()
   

