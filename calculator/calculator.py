# tkinter는 파이썬 기본 GUI 툴킷. UI를 만들 수 있게 해줌
import tkinter as tk

# 계산기 클래스 정의
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("파이썬 계산기")  # 창 제목 설정
        self.expression = ""  # 사용자가 입력하는 수식 저장할 변수

        # Entry 위젯: 사용자에게 수식/결과를 보여주는 화면
        self.entry = tk.Entry(root, width=25, font=('Arial', 18), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 버튼 정의 (숫자와 연산자)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # 버튼을 하나씩 만들어서 grid에 배치
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 16),
                      command=lambda b=button: self.on_click(b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear 버튼 추가
        tk.Button(root, text="C", width=22, height=2, font=('Arial', 16),
                  command=self.clear).grid(row=row, column=0, columnspan=4, padx=5, pady=5)

    # 버튼 클릭 시 호출되는 함수
    def on_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))  # eval 함수로 수식 계산
                self.entry.delete(0, tk.END)         # 기존 입력 지움
                self.entry.insert(tk.END, result)    # 결과 입력
                self.expression = result             # 결과를 다음 계산에 이어서 사용
            except Exception as e:
                print("에러 발생:", e)  # 콘솔에 에러 출력
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "오류")
                self.expression = ""
        else:
            self.expression += str(char)            # 버튼 입력을 수식에 추가
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    # C(초기화) 버튼 눌렀을 때
    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

# 프로그램 실행
root = tk.Tk()
calc = Calculator(root)
root.mainloop()