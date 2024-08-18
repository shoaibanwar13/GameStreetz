from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def LandingPage(request):
    if request.method=="POST":
        email=request.POST.get('email')
        check=Player.objects.filter(email=email).exists()
        if check:
            messages.warning(request,"Email Already Exist")
            return redirect("/")
        else:
            create=Player.objects.create(email=email)
            request.session['player_email'] = email
            create.save()
            return redirect("rules")

    return render(request,"landing.html")
def rules(request):
    player_email = request.session.get('player_email')
    check=Score.objects.filter(email=player_email).exists()
    if check:
        return HttpResponse("You are not Eligible for Playing This Game.You Already Play This Game")
    if not player_email:
         
        return redirect("/")
    
    return render(request,"rules.html")
def gamearea(request):
    player_email = request.session.get('player_email')
    check=Score.objects.filter(email=player_email).exists()
    if check:
        return HttpResponse("You are not Eligible for Playing This Game.You Already Play This Game")
    if not player_email:
        return redirect("/")
    return render(request,"game.html")

def send_winning_email(player_email, score):
    subject = 'Congratulations! You Won the Game!'
    message = f'Dear Player,\n\nCongratulations on reaching a score of {score}! You have won a ticket of streetzfestival .\n\nPlease reply to this email with your contact details to claim your streetzfestival ticket.\n\nBest regards,\nThe streetzfestival Team'
    from_email = 'shoaib4311859@gmail.com.com'  # Replace with your email
    recipient_list = [player_email]
    
    send_mail(subject, message, from_email, recipient_list)
@csrf_exempt
def submit_score(request):
   
    if request.method == 'POST':
        # Assuming you have stored the player's email in the session
        player_email = request.session.get('player_email')
        score = int(request.POST.get('score'))
        check=Score.objects.filter(email=player_email).exists()
        if check:
            return redirect("/")
        else:
            # Here you can save the score to the database, for example:
           store=Score.objects.create(email=player_email, score=score)
           store.save()

        print(store)
        if score>=30:
            send_winning_email(player_email, score)
            return redirect("gamewin")
        # For now, we'll just print it out to the console
        print(f"Player: {player_email}, Score: {score}")
        return redirect("gameover")

        

    return redirect("gameover")
def gameover(request):
    return render(request,"Gameover.html")
def gamewin(request):
    return render(request,"Gamewin.html")