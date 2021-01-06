from time import sleep


class TrafficLights:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print('Светофор переключается\n' f'{TrafficLights.__color[i]}')
            if i == 0:
                sleep(5)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(2)
            i += 1


TrafficLights = TrafficLights()
TrafficLights.running()
