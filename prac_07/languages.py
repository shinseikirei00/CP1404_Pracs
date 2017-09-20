from prac_07.ProgrammingLanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    for language in languages:
        if language.is_dynamic():
            print(language.name)


    print(ruby)
    print(python)
    print(visual_basic)



main()