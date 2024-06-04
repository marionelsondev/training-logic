print("Hello, welcome to the semi-annual performance evaluation system for programmers!");

def get_valid_input(prompt, validate, error_message):
    while True:
        value = input(prompt)
        if validate(value):
            return value
        else:
            print(error_message)

def is_valid_name(name):
    return name.isalpha()

def is_valid_score(score):
    try:
        score = float(score)
        return 0 <= score <= 10
    except ValueError:
        return False

name = get_valid_input("Enter the programmer's name: ", is_valid_name, "Invalid input. The name should only contain letters. Please ty again.")
langProgram = get_valid_input("Enter the main programming language the programmer uses: ", is_valid_name, "Invalid input. The programming language should only contain letters. Please try again.")
scoreTechSkills = float(get_valid_input("Enter the programmmer's technical skills rating on a scale of 0 to 10 :\n" , is_valid_score, "Invalid input. The rating should be a number between 0 and 10. Please try again."))
scoreCommunSkills = float(get_valid_input("Enter the programmer's communication skills rating on a scale of 0 to 10: ", is_valid_score, "Invalid input. The rating should be a number between 0 and 10. Please try again."))
scoreEffort = float(get_valid_input("To finish, enter the programmer's effort rating on a scale of 0 to 10: ", is_valid_score, "Invalid input. The rating should be a number between 0 and 10. Please try again."))
averageEvaluation = (scoreTechSkills + scoreCommunSkills + scoreEffort) / 3

print(f"The programmer {name}, who is proficient in {langProgram}, had an average score of {averageEvaluation} points in his semi-annual evaluation.")