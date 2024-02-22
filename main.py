import re


class SystemBlock:
    def __init__(self, motherboard, processor, power_supply):
        self.set_motherboard(motherboard)
        self.set_processor(processor)
        self.set_power_supply(power_supply)

    def get_motherboard(self):
        return self._motherboard

    def set_motherboard(self, new_motherboard):
        if 20 <= len(new_motherboard) <= 150:
            self._motherboard = new_motherboard
        else:
            raise ValueError("Наименование материнской платы должно содержать не менее 20 и не более 150 символов")

    def get_processor(self):
        return self._processor

    def set_processor(self, new_processor):
        if re.match("^[A-Za-z0-9\-.;]+$", new_processor):
            self._processor = new_processor
        else:
            raise ValueError(
                "Название процессора может состоять из символов: буквы, цифры, тире, точка, точка с запятой")

    def get_power_supply(self):
        return self._power_supply

    def set_power_supply(self, new_power_supply):
        if re.search(r'\d+W', new_power_supply):
            self._power_supply = new_power_supply
        else:
            raise ValueError("В наименовании блока питания должно присутствовать значение напряжения, например, '500W'")

    def __str__(self):
        return f"Материнская плата: {self.get_motherboard()}\nПроцессор: {self.get_processor()}\nБлок питания: {self.get_power_supply()}"


class VideoCard(SystemBlock):
    def __init__(self, motherboard, processor, power_supply, video_memory):
        super().__init__(motherboard, processor, power_supply)
        self.set_video_memory(video_memory)

    def get_video_memory(self):
        return self._video_memory

    def set_video_memory(self, new_video_memory):
        if 2 <= new_video_memory <= 512:
            self._video_memory = new_video_memory
        else:
            raise ValueError("Объем видеопамяти должен быть не менее 2 ГБ и не более 512 ГБ")

    def __str__(self):
        return f"{super().__str__()}\nОбъем видеопамяти: {self.get_video_memory()} ГБ"


# Создаем экземпляр класса VideoCard
try:
    video_card = VideoCard("ASUSROGStrixZ390-EGamingawdawdawd", "awdoawdoawdoawduawdpojawdawd", "22W", 4)
except ValueError as e:
    print("Ошибка при создании видеокарты:", e)
else:
    # Выводим значения свойств объекта VideoCard
    print("Свойства видеокарты:")
    print(str(video_card))

# Создаем экземпляры класса SystemBlock
try:
    block1 = SystemBlock("ASUSROGStrixZ390-EGamingawdawdawd", "awdoawdoawdoawduawdpojawdawd", "22W")
    block2 = SystemBlock("GigabyteB450AORUSMddddddd", "awdoawdoawdoawduawdpojawdawd", "500W")
except ValueError as e:
    print("Ошибка при создании системного блока:", e)
else:
    # Выводим значения свойств объектов
    print("Свойства системного блока 1:")
    print(str(block1))

    print("\nСвойства системного блока 2:")
    print(str(block2))
