from time import sleep

class TrafficLight:
    color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 3}

    @staticmethod
    def running():
        for key, value in TrafficLight.color.items():
            print(f'На светофоре {key} свет')
            sleep(value)

TrafficLight.running()