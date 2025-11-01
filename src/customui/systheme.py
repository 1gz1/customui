from tkinter.ttk import *  # 导入 tkinter 库
import tkinter as tk 

class CreateApp:
    """
    应用程序创建类，负责初始化窗口、设置标题和主循环。
    """
    def __init__(self, app_name:str, app_version:str, hight:str, width:str):
        # 保存应用信息到字典
        self.app_dict = {"name": app_name, "version": app_version,
                         "hight": hight, "width": width}
        self.app = tk.Tk()
        self.app.title(f"{self.app_dict['name']} v{self.app_dict['version']}")
        # geometry 需要字符串格式 "宽x高"
        self.app.geometry(f"{self.app_dict['hight']}x{self.app_dict['width']}")  # width x height

    def run(self):
        self.app.mainloop()

    def addLabel(self, text,row,column):
        self.label = Label(self.app, text=text)
        self.label.grid(row=row, column=column)

    def addButton(self, text ,command,row,column):
        self.button = Button(self.app,text=text, command=command)
        self.button.grid(row=row, column=column)

# test code
# only run in this file , add to the github need delete lines below
if __name__ == "__main__":
    def pt():
        print("Button Clicked!")
    test_app = CreateApp("Test App", "1.0","600","480")
    test_app.addLabel("Welcome to Test App!", 0, 0)
    test_app.addButton("Click Me", pt, 1, 0)
    test_app.run()