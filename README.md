![](https://github.com/Poyamohamadi/Python_Kivy_Round_Robin/blob/main/Kivy_Round_Robin.gif)
### **Project Description**

This project is a Python-based application that implements the **Round Robin Scheduling Algorithm** with a user-friendly graphical interface built using the Kivy library. The program allows users to input process details, arrival times, burst times, and a time quantum, and then calculates key metrics such as average waiting time, average turnaround time, and the scheduling sequence.

#### **Key Features:**
1. **Round Robin Scheduling Algorithm:**
   - Implements the Round Robin algorithm, a widely used CPU scheduling method in operating systems.
   - Users can specify the time quantum (`quantum`) for process execution.

2. **Performance Metrics Calculation:**
   - Computes **waiting time** and **turnaround time** for each process.
   - Calculates the **average waiting time** and **average turnaround time** across all processes.

3. **Scheduling Sequence:**
   - Generates a detailed schedule showing the order of process execution.

4. **Context Switch Count:**
   - Calculates and displays the total number of context switches during the scheduling process.

5. **Graphical User Interface (GUI) with Kivy:**
   - Provides an intuitive GUI for users to input data and view results.
   - Input fields for processes, arrival times, burst times, and quantum.
   - Buttons and labels for executing the algorithm and displaying results.
   - 
---

#### **Example Input and Output**

**Input:**
- Processes: `["P1", "P2", "P3"]`
- Arrival Times: `[0, 1, 2]`
- Burst Times: `[5, 4, 2]`
- Quantum: `3`

**Output:**
- Schedule: `["P1", "P2", "P3", "P1", "P2"]`
- Average Waiting Time: `X.XX`
- Average Turnaround Time: `Y.YY`
- Context Switches: `Z`

---

### **توضیحات پروژه**

این پروژه شامل یک برنامه به زبان پایتون است که الگوریتم زمان‌بندی **Round Robin** را پیاده‌سازی می‌کند و از کتابخانه **Kivy** برای ایجاد رابط کاربری گرافیکی استفاده می‌کند. این برنامه به کاربر اجازه می‌دهد تا جزئیات فرآیندها، زمان‌های ورود، زمان‌های اجرا و مقدار کوانتوم زمان را وارد کند و سپس معیارهای کلیدی مانند زمان انتظار میانگین، زمان بازگشت میانگین و ترتیب اجرای فرآیندها را محاسبه کند.

#### **ویژگی‌های اصلی:**
1. **الگوریتم Round Robin:**
   - پیاده‌سازی الگوریتم Round Robin، یکی از روش‌های معروف زمان‌بندی در سیستم‌عامل‌ها.
   - کاربر می‌تواند مقدار کوانتوم زمان (`quantum`) را مشخص کند.

2. **محاسبه معیارهای عملکرد:**
   - محاسبه **زمان انتظار** و **زمان بازگشت** برای هر فرآیند.
   - محاسبه **زمان انتظار میانگین** و **زمان بازگشت میانگین** برای تمام فرآیندها.

3. **ترتیب اجرای فرآیندها:**
   - تولید جدولی که ترتیب اجرای فرآیندها را نشان می‌دهد.

4. **تعداد تعویض زمینه:**
   - محاسبه و نمایش تعداد تعویض‌های زمینه در طول زمان‌بندی.

5. **رابط کاربری گرافیکی با Kivy:**
   - ارائه یک رابط کاربری شهودی برای ورود داده‌ها و مشاهده نتایج.
   - فیلدهای ورودی متن برای نام فرآیندها، زمان‌های ورود، زمان‌های اجرا و کوانتوم زمان.
   - دکمه‌ها و برچسب‌ها برای اجرای الگوریتم و نمایش نتایج.

---

#### **مثال ورودی و خروجی**

**ورودی:**
- فرآیندها: `["P1", "P2", "P3"]`
- زمان‌های ورود: `[0, 1, 2]`
- زمان‌های اجرا: `[5, 4, 2]`
- کوانتوم: `3`

**خروجی:**
- ترتیب اجرا: `["P1", "P2", "P3", "P1", "P2"]`
- زمان انتظار میانگین: `X.XX`
- زمان بازگشت میانگین: `Y.YY`
- تعداد تعویض‌های زمینه: `Z`

