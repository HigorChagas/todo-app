from tasks import *
    
def main():
    show_menu()
    while True:
        try:
            options = input("Escolha uma opção: ")
            match options:
                case "1":
                    task_title = input("Digite o titulo da tarefa: ")
                    tasks = load_tasks()
                    add_tasks(task_title, tasks)
                    save_tasks(tasks)
                case "2":
                    list_tasks(load_tasks())
                    show_menu()
                case "3":
                    complete_task()
                case "4":
                    delete_task()
                case "5":
                    edit_task()
                case "6":
                    filter_tasks()
                case "7":
                    print("Saindo...")
                    break
                case _:
                    raise ValueError("Opção inválida")
        except ValueError as e:
            print(f"Erro: {e}")   

main()

        