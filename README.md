# TactilePi

## Описание проекта
TactilePi — это проект, созданный для школьной олимпиады в области робототехники. Его цель — разработка системы тактильного восприятия окружающего пространства для незрячих людей. Проект использует стереокамеру для измерения расстояний до объектов и передачи этой информации через тактильные сигналы.

Проект основан на репозитории [StereoPi](https://github.com/realizator/stereopi-tutorial) и адаптирован для реализации задачи обеспечения безопасной навигации для незрячих людей. Система адаптирована для работы с Raspberry Pi 5 и библиотекой picamera2, что делает её более современной и гибкой по сравнению с использованием CM3/3+ и picamera.

**English version below.**

## Функциональность проекта
TactilePi предоставляет следующий функционал:
- Измерение расстояния до объектов с использованием стереокамеры.
- Обработка данных для определения препятствий.
- Передача информации о расстоянии через тактильные сигналы.

## Структура файлов
1. **1_test.py**  
   Тестирование базовой функциональности системы.  
   [Видеоинструкция](https://www.youtube.com/watch?v=wllLrNUw3SE)

2. **2_chess_cycle.py**  
   Калибровка стереокамеры с использованием шахматной доски.  
   [Видеоинструкция](https://youtu.be/1XCAlU3k-xs)

3. **3_pairs_cut.py**  
   Работа с парными изображениями для стереоанализа.  
   [Видеоинструкция](https://youtu.be/95DWmPECbDc)

4. **4_calibration.py**  
   Настройка параметров калибровки камеры.  
   [Видеоинструкция](https://youtu.be/vtPhu23tKGo)

5. **5_dm_tune.py**  
   Тонкая настройка диспарити карты.  
   [Видеоинструкция](https://youtu.be/Z4j3NrMyeGE)

6. **6_dm_video.py**  
   Генерация диспарити карты в режиме реального времени.  
   [Видеоинструкция](https://youtu.be/f29arVstfZA)  
   

## Как начать работу
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/твой_пользователь/tactilepi.git
   ```
2. Установите необходимые зависимости (например, OpenCV, NumPy):
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите нужный скрипт в соответствии с задачей.

## Благодарности
Спасибо проекту [StereoPi](https://github.com/realizator/stereopi-tutorial) за предоставленную базу для реализации данной идеи.

---

# TactilePi (English Version)

## Project Description
TactilePi is a project created for a school robotics competition. Its goal is to develop a tactile perception system for visually impaired individuals, enabling them to perceive their surroundings through touch. The project uses a stereo camera to measure distances to objects and conveys this information through tactile signals.

The project is based on the [StereoPi](https://github.com/realizator/stereopi-tutorial) repository and adapted to meet the needs of safe navigation for visually impaired individuals. The system has been upgraded to work with Raspberry Pi 5 and the picamera2 library, providing a more modern and flexible solution compared to the older CM3/3+ and picamera setup.

## Features
- Distance measurement to objects using a stereo camera.
- Data processing for obstacle detection.
- Tactile signal transmission of distance information.

## File Structure
1. **1_test.py**  
   Basic functionality testing of the system.  
   [Video Guide](https://www.youtube.com/watch?v=wllLrNUw3SE)

2. **2_chess_cycle.py**  
   Stereo camera calibration using a chessboard pattern.  
   [Video Guide](https://youtu.be/1XCAlU3k-xs)

3. **3_pairs_cut.py**  
   just cuts all captured photos to left and right images.
   [Video Guide](https://youtu.be/95DWmPECbDc)

4. **4_calibration.py**  
   Adjusting calibration parameters for the camera.  
   [Video Guide](https://youtu.be/vtPhu23tKGo)

5. **5_dm_tune.py**  
   Fine-tuning disparity maps.  
   [Video Guide](https://youtu.be/Z4j3NrMyeGE)

6. **6_dm_video.py**  
   Real-time disparity map generation.  
   [Video Guide](https://youtu.be/f29arVstfZA)

## How to Get Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your_user/tactilepi.git
   ```
2. Install the required dependencies (e.g., OpenCV, NumPy):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the desired script based on your task.

## Acknowledgments
Thanks to the [StereoPi](https://github.com/realizator/stereopi-tutorial) project for providing the foundation for this idea.

