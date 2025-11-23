from tkinter.ttk import Label
from tkinter.ttk import Button
import tkinter as tk 
from loguru import logger as log

# 配置日志系统
log.remove()
log.add("sysuidebug.log")
log.info("系统主题应用程序日志系统已初始化")

class CreateApp:
    """
    应用程序创建类，负责初始化窗口、设置标题和主循环。
    """
    def __init__(self, app_name:str, app_version:str, hight:int, width:int):
        log.info(f"正在初始化系统主题应用程序: {app_name} v{app_version}, 尺寸: {width}x{hight}")
        # 保存应用信息到字典
        self.app_dict = {"name": app_name, "version": app_version,
                         "hight": str(hight), "width": str(width)}
        log.debug(f"app_dict: {self.app_dict}")
        
        try:
            self.app = tk.Tk()
            log.debug("系统主题Tk实例创建成功")
            self.app.title(f"{self.app_dict['name']} v{self.app_dict['version']}")
            # geometry 需要字符串格式 "宽x高"
            self.app.geometry(f"{self.app_dict['hight']}x{self.app_dict['width']}")  # width x height
        except Exception as e:
            log.error(f"初始化系统主题应用程序时出错: {str(e)}")
            raise

    def run(self):
        log.info("正在启动系统主题应用程序主循环")
        try:
            self.app.mainloop()
            log.info("系统主题应用程序主循环已结束")
        except Exception as e:
            log.error(f"运行系统主题应用程序时出错: {str(e)}")
            raise

    def addLabel(self, text:str,row:int,column:int):
        log.debug(f"正在添加系统主题标签: 文本='{text}', 位置=({row},{column})")
        try:
            self.label = Label(self.app, text=text)
            self.label.grid(row=row, column=column)
            log.debug("系统主题标签添加成功")
        except Exception as e:
            log.error(f"添加系统主题标签时出错: {str(e)}")
            raise

    def addButton(self, text:str ,command,row:int,column:int):
        log.debug(f"正在添加系统主题按钮: 文本='{text}', 位置=({row},{column})")
        try:
            self.button = Button(self.app,text=text, command=command)
            self.button.grid(row=row, column=column)
            log.debug("系统主题按钮添加成功")
        except Exception as e:
            log.error(f"添加系统主题按钮时出错: {str(e)}")
            raise

# test code
# only run in this file , add to the github need delete lines below
if __name__ == "__main__":
    log.info("开始执行系统主题测试代码")
    def pt():
        log.info("系统主题按钮被点击!")
        print("Button Clicked!")
    try:
        test_app = CreateApp("Test App", "1.0",600,480)
        test_app.addLabel("Welcome to Test App!", 0, 0)
        test_app.addButton("Click Me", pt, 1, 0)
        test_app.run()
    except Exception as e:
        log.error(f"系统主题测试代码执行出错: {str(e)}")
        raise
    log.info("系统主题测试代码执行完成")
