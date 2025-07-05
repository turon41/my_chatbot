from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer


bot = ChatBot('chatbot',read_only = False,logic_adapters = ['chatterbot.logic.BestMatch'])

list_to_train = [

     "hi", #QUESTION
     "hi, there", #ANSWER
     "what's your name?", #QUESTION
     "I'm just a chatbot", #ANSWER
     "Do you know abu sayem rony?",
     "Yes, He is a nice coder",


]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    num = 55
    return HttpResponse(num)

 

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

