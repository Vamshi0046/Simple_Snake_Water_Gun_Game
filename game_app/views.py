from django.shortcuts import render, redirect
from random import choice

# from rembg import remove

# # Specify the input and output file paths
# input_image_path = 'game_app\static\images\snake.png'
# output_image_path = 'game_app\static\images\output_snake_img.png'

# # Perform the background removal
# with open(input_image_path, "rb") as input_file:
#     output_data = remove(input_file.read())

# with open(output_image_path, "wb") as output_file:
#     output_file.write(output_data)



def game_view(request):
    if request.method == 'POST':
        user_choice = request.POST.get('user_choice')
        computer_choices = ["snake", "water", "gun"]
        computer_choice = choice(computer_choices)

        result = determine_result(user_choice, computer_choice)

        # Update the session for results tracking
                # Update the session for results tracking
        if 'results' not in request.session:
            request.session['results'] = {'wins': 0, 'losses': 0, 'draws': 0, 'history':[]}

        results = request.session['results']

        if result.startswith("You Won"):
            results['wins'] += 1
        elif result.startswith("You Lost"):
            results['losses'] += 1
        else:
            results['draws'] += 1
        history_item = {'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result}
        results['history'].append(history_item)
        request.session['results'] = results

        context = {
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result,
            'wins': results['wins'],
            'losses': results['losses'],
            'draws': results['draws'],
            'history': results['history'],  # Pass the history to the template
        }

        return render(request, 'game.html', context)

    # Reset the session when starting a new game
    request.session.pop('results', None)

    return render(request, 'game.html')


def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Match Draw!" # Computer chose {computer_choice}

    if user_choice == "snake":
        if computer_choice == "gun":
            return f"You Lost!" # Computer chose {computer_choice}
        elif computer_choice == "water":
            return f"You Won!"

    if user_choice == "water":
        if computer_choice == "snake":
            return f"You Lost!" # Computer chose {computer_choice}
        elif computer_choice == "gun":
            return f"You Won!"

    if user_choice == "gun":
        if computer_choice == "water":
            return f"You Lost!" # Computer chose {computer_choice}
        elif computer_choice == "snake":
            return f"You Won!"

    return "Invalid option!"
