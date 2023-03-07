""" игра Угадай число - компьютер сам загадывает и угадывает число
"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number  = np.random.randint(1,101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла 
    return(count)

def score_game(random_predict) -> int:
    """за какое количество подходов в среднем из 1000 попыток наш алгоритм угадывает 

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток 
        """
        
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))  # находим среднее количество попыток
    
    print(f'ваш алгоритм угадывает число в среднем за : {score} попыток')
    return(score)

# RUN  
if _name_ == '_main_':
score_game(random_predict)
        