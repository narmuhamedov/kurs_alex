class Junior_Development:
    def __init__(self, laptop, salary, prog_lang):
        self.laptop = laptop
        self.salary = salary
        self.prog_lang = prog_lang

    def copy_paste(self, resourse):
        return f'can copy past from - {resourse}'

    def __str__(self):
        return f'Ноутбук:{self.laptop}\n' \
               f'ЗП: {self.salary}$\n' \
               f'Язык программирования:{self.prog_lang}'

proger = Junior_Development(laptop=True, salary=800, prog_lang='Python')
print(proger.copy_paste('Forum Prog'))
print(proger)
print('-'*50)

class Middle_Development(Junior_Development):
    def __init__(self, laptop, salary, prog_lang, experience,responsibility):
        super().__init__(laptop, salary, prog_lang)
        self.ex = experience
        self.respob = responsibility

    def can_be_mentor(self):
        return f'Can be mentor{proger}'

    def __str__(self):
        return super(Middle_Development, self).__str__()+f'\nОпыт:{self.ex}\n' \
                                                         f'Обязанности: {self.respob}'

mid_prog = Middle_Development(laptop=True, salary=1200, prog_lang='Python, PHP', experience=2.5,
                              responsibility='Good write code!')
print(mid_prog.can_be_mentor())
print('-'*50)
print(mid_prog)
print('-'*50)

class Senior_Development(Middle_Development):
    def __init__(self, laptop, salary, prog_lang, experience, responsibility, team_lead):
        super().__init__(laptop, salary, prog_lang, experience, responsibility)
        self.team_lead = team_lead

    def advanced_skill(self, lang):
        if lang == 'Python':
            return 'You are Good Proger'
        elif lang == 'PHP':
            return 'You are Boss'
        elif lang == 'Java':
            return 'You are not our dude'


    def __str__(self):
        return super(Senior_Development, self).__str__()+f'\nТим Лидер:{self.team_lead}'

print('-'*50)
sen_prog = Senior_Development(laptop=True, salary=3000, prog_lang='Python', experience=5.0, responsibility='Lead Command',
                              team_lead=True)
print(sen_prog.advanced_skill('PHP'))
print(sen_prog)

