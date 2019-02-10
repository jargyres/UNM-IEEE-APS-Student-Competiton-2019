import tkinter as tk
import Graph

master = tk.Tk()

master.title("Live Graphing")


graph = tk.Button(master, text = "Turn on live graphing", command = Graph.graph)

quit = tk.Button(master, text = "Quit", command = quit)
def _quit():
    master.quit()     # stops mainloop
    master.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



graph.pack()
quit.pack()

master.mainloop()