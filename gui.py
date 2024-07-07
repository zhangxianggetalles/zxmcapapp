import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("简单GUI示例")

# 创建标签
label = tk.Label(root, text="欢迎使用GUI程序")
label.pack()

# 创建按钮
button = tk.Button(root, text="点击我")
button.pack()

# 运行主循环
root.mainloop()
