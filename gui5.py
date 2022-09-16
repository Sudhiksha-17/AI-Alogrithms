import tkinter as tk
import math
import time
from tkinter import Canvas
from tkinter import *

class Graph:
    node = []
    nd=[]
    edges = []
    flag = 0
    prev = -1
    s=1
    n=1
    d = []
    cost=0
    INF = 10**9
    
    def __Root_Window(self):
        self.root = tk.Tk() #first line
        self.root.title("Graph ADT")
        
        self.leftframe = LabelFrame(self.root, padx=50, pady=500, height=500)
        self.leftframe.pack(padx=10, pady=10,side=LEFT)
        
        l = Label(self.root, text = "Visited")
        
        def set_start():
            self.s=self.menu.get()  
        
        def set_goal():
            self.n=self.menu1.get()
            visited_label =Label(self.leftframe, text = 'Visited:', font=('calibre',10, 'bold'))
            visited_label.grid(row=2, column=0)
            cost_label =Label(self.leftframe, text = 'Cost:', font=('calibre',10, 'bold'))
            cost_label.grid(row=3, column=0)    
               

            
        self.menu=StringVar()
        self.menu1=StringVar()
        
        
   
        self.b1 = Button(self.leftframe, text="Set Start",width=10,command=set_start)
        self.b1.grid(row=0, column=0)
        
        self.b2 = Button(self.leftframe, text="Set Goal",width=10, command=set_goal)
        self.b2.grid(row=1, column=0)
        
        self.e=OptionMenu(self.leftframe, self.menu,-1)
        self.e.grid(row=0, column=1)
        
        self.e1=OptionMenu(self.leftframe, self.menu1,-1)
        self.e1.grid(row=1, column=1)
        
       
        
        #Code to align Window in the middle of the screen irrespective of the screen dimention 
        self.window_width = 1000
        self.window_height = 700
        
        #self.screen_width = self.root.winfo_screenwidth()
        #self.screen_height = self.root.winfo_screenheight()
        
        #self.center_x = int(self.screen_width/2 - self.window_width/2)
        #self.center_y = int(self.screen_height/2 - self.window_height/2)
        
        #self.root.geometry('{0}x{1}+{2}+{3}'.format(self.window_width,self.window_height,self.center_x,self.center_y)) #Window Dimension 
        
        #self.root.resizable(False,False) #Resizability of the Window is restricted
        
    
    def __canva(self):
        #canva is where nodes and edges are displayed
        self.canva_width = 700
        self.canva_height = 700
        
        self.canva = Canvas(self.root,width = self.canva_width, height = self.canva_height)
        
        self.canva.create_rectangle(5,5,self.canva_width,self.canva_height-5,width = 3)
        self.canva.pack(side = "right")
    
    def __draw(self):
        def add_node(event):
            node_id = len(self.node) + 1
            x = event.x
            y = event.y
            r = 30
            self.node.append([node_id,x,y])
            self.nd.append(node_id)
            self.canva.create_oval(x-r,y-r,x+r,y+r,tags = 'del',width = 3)
            self.canva.create_text(x,y,text = "{0}".format(node_id),fill = "black",tags = "del",font=('Helvetica 25 bold'))
        
            self.e=OptionMenu(self.leftframe, self.menu,*self.nd)
            self.e.grid(row=0, column=1)
            
            self.e1=OptionMenu(self.leftframe, self.menu1,*self.nd)
            self.e1.grid(row=1, column=1)
        
        def add_edge(event):
            
            if(len(self.node) == 0):
                return
            
            x = event.x
            y = event.y
            
            closest_node = -1
            closest_dist = self.INF 
            
            for i in self.node:
                dist = math.sqrt((x-i[1])**2 + (y-i[2])**2)
                if(dist < closest_dist):
                    closest_node = i[0]
                    closest_dist = dist
            
            if(self.flag == 0):
                self.prev = closest_node
                
                x1,y1 = self.node[closest_node-1][1],self.node[closest_node-1][2]
                self.canva.create_text(x1,y1,text = "{0}".format(closest_node),fill = "red",tags = "del",font=('Helvetica 25 bold'))
                
                self.flag = 1
            else:
                x1,y1 = self.node[self.prev-1][1],self.node[self.prev-1][2]
                x2,y2 = self.node[closest_node-1][1],self.node[closest_node-1][2]
                
                dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                #d0=dist//10
                #self.d.append(d0)
                if(self.prev != closest_node):
                    self.edges.append([self.prev,closest_node,dist//10])
                    print(self.edges)
                    self.edges.append([closest_node,self.prev,dist//10])
                    print(self.edges)
                    self.canva.create_line(x1,y1,x2,y2,width = 5,tags = "del",fill='#999999')
                    
                    self.canva.create_text(x1,y1,text = "{0}".format(self.prev),fill = "black",tags = "del",font=('Helvetica 25 bold'))
                    self.canva.create_text(x2,y2,text = "{0}".format(closest_node),fill = "black",tags = "del",font=('Helvetica 25 bold'))
                    self.canva.create_text((x1+x2)/2,(y1+y2)/2,text = "{0}".format(dist//10),fill = "red",tags = "del",font=('Helvetica 15 bold'))
                    self.flag = 0
                    
        def clear(event):
            self.node = []
            self.edges = []
            self.flag = 0
            self.prev = -1
            self.canva.delete('del')
            
        self.canva.bind('<Button-1>',add_node)
        self.canva.bind('<Button-3>',add_edge)
        self.root.bind('<x>',clear)
        
    def path(self,n1,n2,c,tag): #Node_1 Node_2 colour tags
        x1,y1 = self.node[n1-1][1],self.node[n1-1][2]
        x2,y2 = self.node[n2-1][1],self.node[n2-1][2]
        
        self.canva.create_line(x1,y1,x2,y2,
                               width = 5,tags = tag, fill = c)
        self.canva.update()
    
    def __algo(self):
        def DFS(event):
            
            adj_list = {}
            for i in self.node:
                adj_list[str(i[0])] = []
            
            for i in self.edges:
                if(str(i[0]) not in adj_list[str(i[1])]):
                    adj_list[str(i[0])] += [str(i[1])]
                    adj_list[str(i[1])] += [str(i[0])]
            
            
            #start = 0, source = n
            cost=0
            vis = []
            n=str(self.n)
            s=str(self.s)
            def dfs(s,n):
                
                if(s == n):
                    time.sleep(5)
                    return
                i=0
                vis.append(s)
                visited_label =Label(self.leftframe, text = 'Visited: '+str(vis[(len(vis)-1)]), font=('calibre',10, 'bold'))
                visited_label.grid(row=2, column=0)
                print(vis)
                #print(self.d)
                for i in range(len(self.edges)):
                    if len(vis)!=1:
                        if vis[len(vis)-2]==self.edges[i][0] and vis[len(vis)-1]==self.edges[i][1]:
                            self.cost=self.cost+int(self.edges[i][3])
                            print("cost : ",self.cost)
                cost_label =Label(self.leftframe, text = 'Cost: '+str(self.cost), font=('calibre',10, 'bold'))
                cost_label.grid(row=3, column=0)
                adj_list[s].sort()
                for i in adj_list[s]:
                    if(i not in vis):
                        self.path(int(s),int(i),"red","algo")
                        time.sleep(0.5)
                        dfs(i,n)
                        self.path(int(s),int(i),"#999999","algo")
                        time.sleep(0.2)
                         
                        
              
            dfs(s,n)            
            
            self.canva.delete("algo")
        self.root.bind("1",DFS)

        def BFS(event):
            
            adj_list = {}
            for i in self.node:
                adj_list[str(i[0])] = []
            print(adj_list)
            for i in self.edges:
                if(str(i[0]) not in adj_list[str(i[1])]):
                    adj_list[str(i[0])] += [str(i[1])]
                    adj_list[str(i[1])] += [str(i[0])]
            
            print(adj_list)
            #start = 0, source = n
            n = str(len(self.node))
            s = '1'
            vis = []
            que = []
            def bfs(s,n):
                
                vis.append(s)
                que.append(s)

                while (que):
                    m = que.pop(0)
                    for i in adj_list[m]:
                        if i not in vis :
                            if n in vis:
                                time.sleep(5)
                                break
                            self.path(int(m),int(i),"red","algo")
                            time.sleep(0.5)
                            vis.append(i)
                            que.append(i)
                            
            bfs(s,n)

            self.canva.delete("algo")
        self.root.bind("2",BFS) 
    
    def __init__(self):
        self.__Root_Window()
        self.__canva()
        self.__draw()        
        self.__algo()
        self.root.mainloop() #Last line
        
g = Graph()