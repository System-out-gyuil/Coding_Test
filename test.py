import time
import threading
import keyboard
import pygame

# MP3 파일 경로를 여기에 입력하세요
MP3_FILE_PATH = "quack.mp3"  # 다운로드한 MP3 파일의 경로로 변경하세요

# 볼륨 설정 (0.0 ~ 1.0, 0.5 = 50% 볼륨)
VOLUME = 0.1  # 원하는 볼륨으로 조절하세요 (0.0 = 무음, 1.0 = 최대 볼륨)

# pygame 초기화
pygame.mixer.init()

def start_single_timer():
    time.sleep(57)
    pygame.mixer.music.load(MP3_FILE_PATH)
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.play()

if __name__ == "__main__":
    
    # F1을 누르면 하나의 타이머 스레드 실행
    # keyboard.on_press_key("f1", lambda _: threading.Thread(target=start_single_timer, daemon=True).start())
    keyboard.on_press_key("1", lambda _: threading.Thread(target=start_single_timer, daemon=True).start())

    # 프로그램을 계속 실행 상태로 유지
    keyboard.wait()
