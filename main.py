from kivy.uix.actionbar import Button
from kivy.uix.dropdown import ScrollView
from kivy.uix.filechooser import Screen
from kivy.uix.codeinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import Label
from kivy.uix.actionbar import BoxLayout
from kivy.app import App
from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.lang import Builder

def round_robin(processes:list[str], arrival_times:list[int], burst_times:list[int], quantum:int):
    n:int = len(processes)
    remaining_burst_time = burst_times.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    time = 0
    schedule = []

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                    schedule.append(processes[i])
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - burst_times[i] - arrival_times[i]
                    turnaround_time[i] = time - arrival_times[i]
                    total_waiting_time += waiting_time[i]
                    total_turnaround_time += turnaround_time[i]
                    remaining_burst_time[i] = 0
                    schedule.append(processes[i])
        
        if done:
            break
    
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    context_switches = len(schedule) - n

    return schedule, average_waiting_time, average_turnaround_time, context_switches


class ManagerScreen(ScreenManager):
    ...
class NumProcesses(Screen):
    num_processes = 0
    processes = []
    arrival_times = []
    screens = None
    def press(self,screen):
        if self.ids.processes_input.text == "":
            self.ids.processes_input.background_color = (252/255,197/255,197/255,1)
        else:
            self.ids.processes_input.background_color = (1,1,1,1)
            self.manager.current = 'second'
            self.manager.transition.direction = 'left'
            NumProcesses.num_processes = int(self.ids.processes_input.text)
            view = ScrollView(do_scroll_x=False,do_scroll_y=True)
            main = GridLayout(cols=2,size_hint_y=None,spacing=20,padding=50)
            
            NumProcesses.screens = screen
            value = screen[1]
            
            
            for num in range(NumProcesses.num_processes):
                NumProcesses.processes.append(f"P{num}")
                main.add_widget(Label(font_size=32,markup=True,text= f'[b]P[color=#8eff69]{num}[/color][/b]',size_hint_y=None,height=60,size_hint_x=.1))
                NumProcesses.arrival_times.append(TextInput(input_filter ='int',halign='right',font_size=40))
                main.add_widget(NumProcesses.arrival_times[num])

            main.bind(minimum_height=main.setter('height'))
            view.add_widget(main)
            
            layout = BoxLayout(orientation ='vertical',padding=20)
            layout.add_widget(Label(markup=True,
            text= "[b]Enter [size=40][color=#8eff69]Arrival Times[/color][/size]:[/b]",
            size_hint_y=.1,font_size = 30,pos_hint={"center_x":.33}))
            layout.add_widget(view)
            layout.add_widget(Button(text='Next Screen',size_hint_y= .1,font_size=32,on_press=Processes.press),)

            value.add_widget(layout)
        
class Processes(Screen):
    burst_times = []
    num_arrival = []
    def press(self):

        num_error = 0
        Processes.num_arrival = []

        for arrival in NumProcesses.arrival_times:
            if arrival.text == '':
                arrival.background_color = (252/255,197/255,197/255,1)
                num_error += 1
            else:
                arrival.background_color = (1,1,1,1)
                Processes.num_arrival.append(int(arrival.text))

        if  0 < num_error:
            pass
        else:
            print(Processes.num_arrival)
            third = NumProcesses.screens[1]
            third.manager.current = "third"

            view = ScrollView(do_scroll_x=False,do_scroll_y=True)
            main = GridLayout(cols=2,size_hint_y=None,spacing=20,padding=50)
            
            value = NumProcesses.screens[2]
            for num in range(NumProcesses.num_processes):
                main.add_widget(Label(font_size=32,markup=True,text= f'[b]P[color=#f3ff12]{num}[/color][/b]',size_hint_y=None,height=60,size_hint_x=.1))
                Processes.burst_times.append(TextInput(input_filter ='int',halign='right',font_size=40))
                main.add_widget(Processes.burst_times[num])

            main.bind(minimum_height=main.setter('height'))
            view.add_widget(main)
            
            layout = BoxLayout(orientation ='vertical',padding=20)
            layout.add_widget(Label(markup=True,
            text= "[b]Enter [size=40][color=#f3ff12]Request Times[/color][/size]:[/b]",
            size_hint_y=.1,font_size = 30,pos_hint={"center_x":.33}))
            layout.add_widget(view)
            layout.add_widget(Button(text='Next Screen',size_hint_y= .1,font_size=32,on_press=RequestTimes.press),)

            value.add_widget(layout)     

class RequestTimes(Screen):
    num_request = []

    def press(self):
        num_error = 0
        RequestTimes.num_request = []

        for request in Processes.burst_times:
            if request.text == '':
                request.background_color = (252/255,197/255,197/255,1)
                num_error += 1
            else:
                request.background_color = (1,1,1,1)
                RequestTimes.num_request.append(int(request.text))

        if  0 < num_error:
            pass
        else:
            fourth = NumProcesses.screens[2]
            fourth.manager.current = "fourth"

class Quantum(Screen):
    quantum = 0
    def press(self):
        if self.ids.quantum_input.text == "":
            self.ids.quantum_input.background_color = (252/255,197/255,197/255,1)
        else:
            self.ids.quantum_input.background_color = (1,1,1,1)
            Quantum.quantum = int(self.ids.quantum_input.text)
            fourth = NumProcesses.screens[3]
            fourth.manager.current = "fifth"

            value = NumProcesses.screens[4]
            layout = BoxLayout(orientation ='vertical',padding=10)
            layout.add_widget(Label(markup=True,
            text= "[b][size=40][color=#8eff69]Scheduling [/color][/size]order:[/b]",
            size_hint_y=.02,font_size = 30,pos_hint={"center_x":.33}))

            schedule, avg_wait_time, avg_turnaround_time, context_switches = round_robin(NumProcesses.processes, Processes.num_arrival, RequestTimes.num_request, Quantum.quantum)

            view = ScrollView(do_scroll_x=True,do_scroll_y=False,size_hint_y=.1)
            p0layout = BoxLayout(orientation ='horizontal',padding=20,spacing=40,size_hint_x=None)
            for sch in schedule:
                p0:Button = Button(markup=True,text=f'[b][color=#8eff69]{sch}[/color][/b]',background_color=(142/255,255/255,105/255,1),size_hint_y=.1,size_hint_x=.5,
                font_size=25)
                p0layout.add_widget(p0)
            
            view.add_widget(p0layout)
            p0layout.bind(minimum_width=p0layout.setter('width'))

            layout.add_widget(view)
            layout.add_widget(Label(markup=True,text=f'[b]Average wait time = [color=#8eff69]{avg_wait_time}[/color][/b]',
            size_hint_y=.1,font_size = 30))
            
            layout.add_widget(Label(markup=True,text=f'[b]Average turn-around time = [color=#8eff69]{avg_turnaround_time}[/color][/b]',
            size_hint_y=.1,font_size = 30))
            
            layout.add_widget(Label(markup=True,text=f'[b]Context Switching = [color=#8eff69]{context_switches}[/color][/b]',
            size_hint_y=.1,font_size = 30))
            
            value.add_widget(layout)
     
class Result(Screen):
    ...

kv = Builder.load_string("""
ManagerScreen:
    NumProcesses:
    Processes:
    RequestTimes:
    Quantum:
    Result:

<NumProcesses>
    name: "first"
    BoxLayout:
        orientation: 'vertical' 
        size: root.width , root.height

        padding: 20

        Label:
            pos_hint: {"center_x":.33}
            size_hint_y:.1
            markup: True
            
            text: "[b]Enter Number Of [size=40][color=#a12a2a]Processes[/color][/size]:[/b]"
            font_size: 30
            
        TextInput:
            id: processes_input
            multiline: False 
            input_filter: 'int'
            pos_hint: {"center_x":.5}
            size_hint_y:.11
            size_hint_x:.9
            font_size: 40
            halign: 'right'
        
        Label:
            text: ''
            
        Button:
            text: 'Next Screen'
            font_size: 32
            size_hint_y: .1
            on_press: root.press(app.root.screens)
            
<Processes>
    name: 'second'
    GridLayout:
        cols: 1
        
<RequestTimes>
    name: "third"
    GridLayout:
        cols: 1

<Quantum>
    name: "fourth"
    BoxLayout:
        orientation: 'vertical'
        size: root.width , root.height

        padding: 20

        Label:
            pos_hint: {"center_x":.33}
            size_hint_y:.1
            markup: True
            
            text: "[b]Enter Time [size=40][color=#f712ff]Quantum[/color][/size]:[/b]"
            font_size: 30
            
        TextInput:
            id: quantum_input
            multiline: False 
            input_filter: 'int'
            pos_hint: {"center_x":.5}
            size_hint_y:.11
            size_hint_x:.9
            font_size: 40
            halign: 'right'
        
        Label:
            text: ''
            
        Button:
            text: 'Next Screen'
            font_size: 32
            size_hint_y: .1
            on_press: root.press()

<Result>
    name: "fifth"
    GridLayout:
        cols: 1    
""")

class MyApp(App):
    def build(self):
        return kv

if '__main__' == __name__:
    MyApp().run()
