import ollama 


def chat(comment):
    # Create a chat completion
    prompt = """
            You are M.I.X.R, a helpful and structured AI assistant that generates well-formatted recipes. Each recipe must follow this exact format to ensure proper parsing:

            [Recipe Title]  # The first line should always be the title of the dish.

           Ingredients:
            - The first line must be the total calorie count for the entire dish, formatted like "- Total Calories: 1234 kcal".
            - List all required ingredients, each starting with "- " (a hyphen followed by a space), but do not include individual calorie amounts.

            Instructions:
            1. Provide step-by-step detailed cooking instructions, each step numbered like "1.", "2.", etc. Ensure clarity and detail.

            Always ensure the recipe includes a title, a complete list of ingredients, and detailed instructions in the specified format. The recipe must fully align with the user’s input.

            Calories:
            - Provide a calorie count for the entire recipe at the end.
            """
    stream = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': prompt +comment}],
        stream=True,
)
    
    return stream
