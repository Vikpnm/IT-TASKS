import random

def calculate_conveyor_load():
    print("\nРозрахунок навантаження на конвеєрні лінії")
    print("=" * 50)
    
    LINES_COUNT = 3
    WORKERS_PER_LINE = 5
    MIN_FRUIT_MASS = 0.1 
    MAX_FRUIT_MASS = 0.5 
    

    production_lines = []
    

    for line_num in range(LINES_COUNT):
        line_load = 0
        worker_loads = []
        

        for worker in range(WORKERS_PER_LINE):

            fruits_count = random.randint(10, 20)
            worker_total = 0
            

            fruits = [round(random.uniform(MIN_FRUIT_MASS, MAX_FRUIT_MASS), 2) 
                     for _ in range(fruits_count)]
            worker_total = sum(fruits)
            worker_loads.append((fruits_count, worker_total))
            line_load += worker_total
            
        production_lines.append((worker_loads, line_load))

    total_load = 0
    
    print("\nДЕТАЛЬНИЙ ЗВІТ ПО ЛІНІЯХ:")
    print("-" * 50)
    
    for line_num, (worker_loads, line_load) in enumerate(production_lines, 1):
        print(f"\nЛінія {line_num}:")
        print("-" * 20)
        
        for worker_num, (fruits_count, worker_load) in enumerate(worker_loads, 1):
            print(f"Робітник {worker_num}:")
            print(f"  Кількість фруктів: {fruits_count} шт.")
            print(f"  Загальна маса: {worker_load:.2f} кг")
        
        print(f"\nЗагальне навантаження на лінію {line_num}: {line_load:.2f} кг")
        total_load += line_load
    
    print("\n" + "=" * 50)
    print("ПІДСУМОК:")
    print(f"Сумарне навантаження на всі лінії: {total_load:.2f} кг")
    print(f"Середнє навантаження на одну лінію: {(total_load/LINES_COUNT):.2f} кг")
    print("=" * 50)

if __name__ == "__main__":
    calculate_conveyor_load() 