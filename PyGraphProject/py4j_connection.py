from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))


def add_friend(tx, name, friend_name, age01, age02):
    tx.run("merge (a:Person {name: $name, age: $p_age}) "
           "merge (a)-[:KNOWS]->(friend:Person {name: $friend_name, age: $f_age})",
           name=name,
           friend_name=friend_name,
           p_age=age01,
           f_age=age02)

def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record['friend.name'])


def add_traffic(tx, sip, dip, ):
    pass


with driver.session() as session:
    for i in range(1000):
        session.write_transaction(add_friend, "David", str(i)+":TEST", 32, i)

    session.read_transaction(print_friends, "David")
