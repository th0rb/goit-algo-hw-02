from queue import PriorityQueue
import time
import random

def generate_request(request_queue: PriorityQueue, request_id: int):
    priority = random.randint(1, 10)  # Пріоритет заявки
    request_data = f"Заявка №{request_id} з пріоритетом {priority}"
    request_queue.put((priority, request_data))
    print(f"Сгенеровано нову заявку: {request_data}")

def process_request(request_queue: PriorityQueue):
    if not request_queue.empty():
        _, request_data = request_queue.get()
        print(f"Обробка заявки: {request_data}")
        # Симуляція обробки
        time.sleep(random.uniform(0.5, 1.5))
    else:
        print("Черга пуста.")

def main():
    request_queue = PriorityQueue()
    request_id = 0

    try:
        while True:
            # Генерування нових заявок з імовірністю 50%
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            # Обробка заявок з імовірністю 33%
            if random.choice([True, False, False]):
                process_request(request_queue)


    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем")

if __name__ == "__main__":
    main()
