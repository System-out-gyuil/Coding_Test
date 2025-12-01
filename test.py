import time
import winsound
import threading
import keyboard

def start_single_timer():
    time.sleep(55)
    winsound.Beep(1000, 500)

if __name__ == "__main__":
    
    # F1을 누르면 하나의 타이머 스레드 실행
    keyboard.on_press_key("f1", lambda _: threading.Thread(target=start_single_timer, daemon=True).start())

    # 프로그램을 계속 실행 상태로 유지
    keyboard.wait()
