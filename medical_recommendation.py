import csv
import io


class Consultation:
    SYMPTOMS = ['высокая температура', 'головная боль',
                'боль мышцах', 'озноб', 'усталость', 'кашель',
                'насморк', 'боль в горле']

    def __init__(self):
        self.recommendation = self.import_data()
        self.user_data = self.get_user_data()

    @classmethod
    def import_data(cls):
        recommendation = {}
        with io.open('data.csv', encoding='utf-8') as file:
            file = csv.reader(file)
            title = None
            for row in file:
                if row[0] == 'название':
                    title = list(row)
                    continue
                res = dict(zip(title, row))
                for key, value in res.items():
                    if value.isdigit():
                        res[key] = True if value == '1' else False
                del res['название']
                for key, value in res.copy().items():
                    if not value:
                        del res[key]
                recommendation[row[0]] = res
        return recommendation

    @classmethod
    def get_user_data(cls):
        user_symptoms = {}
        for symptom in cls.SYMPTOMS:
            while True:
                print(f'У вас есть симптом - {symptom}?\n'
                      f'1 - Да\n'
                      f'0 - Нет', end=': ')
                try:
                    user_symptom = int(input())
                    if user_symptom not in [1, 0]:
                        print('Некорректный ввод')
                        continue
                    if bool(user_symptom):
                        user_symptoms[symptom] = True
                    else:
                        user_symptoms[symptom] = False
                    break
                except TypeError:
                    print('Некорректный ввод')
        for key, value in user_symptoms.copy().items():
            if not value:
                del user_symptoms[key]
        return user_symptoms

    def get_recommendation(self):
        result = []
        print(set(self.user_data.keys()))
        for medication, symptoms in self.recommendation.items():
            for symptom in symptoms:
                if symptom in self.user_data:
                    result.append(medication)
        result = list(set(result))
        text = ('Учитывая ваши симптомы система рекомендует следующие лекарства: \n'
                + '\n'.join(result))
        if {'озноб', 'усталость'} & set(self.user_data.keys()):
            text += '\n\nТак же мы рекомендуем вам обратиться в врачу!'
        return text


tmp = Consultation()
print(tmp.get_recommendation())
