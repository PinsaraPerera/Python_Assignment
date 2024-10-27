
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """add item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """remove item from the front of the queue"""
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0 # this return boolean value


def ticketing_system(customers):
    queue = Queue() # create a queue object

    for customer in customers:
        queue.enqueue(customer) # add customer to the queue
        print(f"{customer} has been added to the queue.")

    print("\nServing customers in the following order:\n")

    while not queue.is_empty():
        customer = queue.dequeue()

        print(f"{customer} is being served.")


customers = ["Pawan", "Sahan", "Kavindu", "Pinsara", "Saman"]
ticketing_system(customers)
