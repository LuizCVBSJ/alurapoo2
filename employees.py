class Employee:
    def register_hours(self, horas):
        print('Hours registered.')

    def show_tasks(self):
        print('Done a lot...')


class Caelum(Employee):
    def show_tasks(self):
        print('Done a lot, Caelumer')

    def search_monthly_courses(self, mes=None):
        print(f'Showing courses - {mes}' if mes else 'Showing courses of this month')


class Alura(Employee):
    def show_tasks(self):
        print('Fez muita coisa, Alurete!')

    def search_unanswered_questions(self):
        print('Showing unanswered questions from the forums')
