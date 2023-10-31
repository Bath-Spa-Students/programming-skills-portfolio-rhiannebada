## Exercise 3: Glossary 2 

#assigning value to key
#source: https://www.indeed.com/career-advice/career-development/coding-terminology
#and https://www.idtech.com/blog/coding-terminology-list 
glossary = {"BIT /bɪt/" : "the individual 1's and 0's you see in binary",
            "FUNCTION /ˈfʌŋ(k)ʃn/" : "a block of code that can be referenced by name to run the code it contains",
            "INPUT /ˈɪnpʊt/" : "any interaction from the user to the program",
            "STRING /strɪŋ/" : "reffered as variables holding words",
            "VARIABLE /ˈvɛːrɪəbl/" : "a container that holds a single number, word, or other information that you can use throughout a program",
            "STATEMENT /ˈsteɪtm(ə)nt/" : "instructions that explain to a computer what action to perform", #adding 5 more Python terms
            "BINARY NUMBER /ˈbʌɪn(ə)ri ˈnʌmbə/" : "(0 and 1) a computer's way to represent information",
            "ASSIGNMENT OPERATOR /əˈsʌɪnm(ə)nt ˈɒpəreɪtə/" : "(+=, -=, *=, /=) are operators that combine variable assignments (=) with arithmetic operators",
            "ALGORITHM /ˈalɡərɪð(ə)m/" : "a set of instructions that are followed to solve a problem",
            "BUG /bʌɡ/" : "a broken code with a fault or flaw that cause a program crash or send an error message"} 

sorted_glossary = sorted(glossary.items()) #to display all words with their definitions alphabetically, including newly added ones

for word, definition in sorted_glossary:
    print (word + "\n" + "\t:" + definition + "\n")  #use of \n to add blank line and \t for indention, in every word&definition
