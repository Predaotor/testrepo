class Todolist:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_task(self):
        if not self.tasks:
          print("No tasks added yet.")
        else:
          print("Tasks:")
          for i, task in enumerate(self.tasks,1):
            print(f"{i}. {task}")
    def mark_task_completed(self,index):
       if 1<=index<=len(self.tasks):
          self.tasks.pop(index-1)
          print("Task marked as completed")
       else:
          print("Invalid task index.")
def main():
          todo_list=Todolist()
        
          while True:
             print("\n1.Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Exit")
             choice=input("Enter your choice: ")

             if choice=="1":
                task=input("Enter task: ")
                todo_list.add_task(task)
             elif choice=="2":
                todo_list.view_task()
             elif choice=="3":
                index=int(input("Enter task index to mark as completed: "))
                todo_list.mark_task_completed(index)
             elif choice=="4":
                print("Exiting...")
                break
             else:
                print("Invalid choice. Please try again.")

if __name__=="__main__":
   main()
             
          