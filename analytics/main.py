import typer
from kafka import KafkaConsumer


def product_consumer(topic: str, bootstrap_servers: str):
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
    for message in consumer:
        print(message.value)


if __name__ == "__main__":
    typer.run(product_consumer("products", "localhost:9092"), auto_envvar_prefix="KAFKA")
