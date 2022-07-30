import json

import faker
import typer
from kafka import KafkaProducer


def product_producer():
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092", value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    for i in range(10000):
        # use faker to generate fake data
        fake = faker.Faker()
        data = {
            "id": i,
            "product_name": fake.name(),
            "product_price": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        }
        producer.send("products", data)
        typer.echo(f"{i} - {data}")
        producer.flush()


if __name__ == "__main__":
    typer.run(product_producer())
    print("Products sent to Kafka")
    print("Press Ctrl+C to stop")
