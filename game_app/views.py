from django.shortcuts import render
from random import choice

# Initialize win, draw, and loss counts
wins = 0
draws = 0
losses = 0

def game_view(request):
    global wins, draws, losses

    if request.method == 'POST':
        user_choice = request.POST.get('user_choice')
        computer_choices = ["snake", "water", "gun"]
        computer_choice = choice(computer_choices)

        result = determine_result(user_choice, computer_choice)

        if result.startswith("You Won"):
            wins += 1
        elif result.startswith("You Lost"):
            losses += 1
        else:
            draws += 1

        context = {
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result,
            'wins': wins,
            'losses': losses,
            'draws': draws,
        }

        return render(request, 'game.html', context)

    return render(request, 'game.html')

def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Match Draw!"

    if user_choice == "snake":
        if computer_choice == "gun":
            return f"You Lost!"
        elif computer_choice == "water":
            return f"You Won!"

    if user_choice == "water":
        if computer_choice == "snake":
            return f"You Lost!"
        elif computer_choice == "gun":
            return f"You Won!"

    if user_choice == "gun":
        if computer_choice == "water":
            return f"You Lost!"
        elif computer_choice == "snake":
            return f"You Won!"

    return "Invalid option!"
