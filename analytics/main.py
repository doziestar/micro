import json

import typer
from kafka import KafkaConsumer


def product_consumer(topic: str, bootstrap_servers: str):
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
    for message in consumer:
        print(f"sending message to user with id: {json.loads(message.value)['id']}")
        print(f"message: {json.loads(message.value)}")
        print("calculating the total price of the orders")
        total_price = 0
        total_price += json.loads(message.value)["product_price"]
        for i in range(int(total_price)):
            print("processing order")
        print(f"total price: {total_price}")
        print("sending the total price to the user")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")


if __name__ == "__main__":
    typer.run(product_consumer("products", "localhost:9092"), auto_envvar_prefix="KAFKA")
