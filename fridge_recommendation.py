import csv
import io


class FridgeSelector:
    PROPERTIES = ['встраиваемость', 'большой объём', 'наличие морозильной камеры', 'наличие no frost',
                  'экономичность']

    def __init__(self):
        self.recommendation = self.import_data()
        self.user_data = self.get_user_data()

    @classmethod
    def import_data(cls):
        recommendation = {}
        with io.open('file.csv', encoding='utf-8') as file:
            file = csv.reader(file)
            for row in file:
                if row[0] == 'модель':
                    model = list(row)
                    continue
                res = dict(zip(model, row))
                for key, value in res.items():
                    if value.isdigit():
                        res[key] = True if value == '1' else False

                del res['модель']
                recommendation[row[0]] = res
        return recommendation

    @classmethod
    def get_user_data(cls):
        user_properties = {}
        for property in cls.PROPERTIES:
            while True:
                print(f'Вам необходима характеристика "{property}"?\n'
                      f'0 - Нет\n'
                      f'1 - Да')
                print('Введите ответ: ', end='')
                try:
                    user_property = int(input())
                    if user_property not in [0, 1]:
                        print('Некорректный ввод! Попробуйте ещё раз.')
                        continue
                    user_properties[property] = bool(user_property)
                    break
                except TypeError:
                    print('Некорректный ввод! Попробуйте ещё раз.')
        return user_properties

    def get_fridge_recommendation(self):
        result = []
        user_values = list(self.user_data.values())
        for result_model, properties in self.recommendation.items():
            model_values = list(properties.values())
            if model_values == user_values:
                result.append(result_model)
        result = list(set(result))
        return ('Вашим пожеланиям соответствует следующая модель холодильника: \n'
                + '\n'.join(sorted(result)))


tmp = FridgeSelector()
print(tmp.get_fridge_recommendation())
