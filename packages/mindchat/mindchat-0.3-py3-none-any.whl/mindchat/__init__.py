import openai as ai

class enter_key:
    def __init__(self):
        print("Please enter a key below")
        self.key = input()
        print('Key entered is : ',self.key)
    def show(self): 
        return self.key

class set_parameters:
    def __init__(self):
        self.model_engine = 'davinci'
        self.temp = 0.2
        print("Please enter a model engine:")
        self.model_engine = input()
        print("Please set the accuracy temperature :")
        self.temp = float(input())
    def show_parameters(self):
        print(self.model_engine,self.temp)
class qna(enter_key,set_parameters):
    def __init__(self):
        self.key = enter_key().show()
        self.show_parameters = set_parameters().show_parameters()
    def question(self):
        if self.key == "":
            print("You have not entered the API key!")
        self.key = "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"
        print(self.show_parameters[0],self.show_parameters[1],self.key)
        ai.api_key = self.key
        while True:
            print("Enter question below : ")
            self.question = input()
            if self.question == 'Exit' or self.question == 'exit':
                print('Thanks! for using our application. Do visit us again')
                break
            prompt = f"Question: {self.question}\nAnswer:"
            response = ai.Completion.create(
                engine=self.show_parameters[0],
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=self.show_parameters[1],
            )
            answer = response.choices[0].text
            s = ''
            for i in answer:
                if i == 'Q':
                    break
                else:
                    s+=i
            answer = s 
            print('Answer to your above query is : ',answer)