#Imports here:
import os.path
import csv
	
#Code begins
def info():
        question_begin =  input("Would you like to ask me a question?\n")
        REC_Q = 0
        REC_A = 1
        if question_begin == "Yes" or "yes" or "y" or "Y":
                while question_begin == "Yes" or "yes" or "y" or "Y":
                        #Questions asked here!
                        question = input("What is your question?\n")
	
                        reader = csv.reader(open("answers.csv"))
                        #Search here
                        for rec in reader:
                                if question == rec[REC_Q]:
                                        answer = rec[REC_A]
                                        print(answer)
      

                        try:
                                answer
                        except NameError:
                                answer = None

                        if answer == None:
                                definition = input("I don't know how to respond to that! Can you tell me how to?\n")
                                myfile = open("answers.csv", "a")
                                
                                myfile.write(question + "," + definition + "\n")
                                myfile.close()
                        


                                

        else:
                quit()


info()
#Copyright Jake Mortimer 2015
