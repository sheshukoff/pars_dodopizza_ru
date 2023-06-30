from create_table_sql import Brand, City, Section, Product
from create_table_sql import session
from sqlalchemy import insert
from parser import get_data_from_locality


def int_price(price):
    if price is None:
        return None

    new_price = ''

    for element in price:
        if element.isdigit():
            new_price += element

    return int(new_price)


def load_table_brand(brand):

    insert_brand = [
        {'name': brand},
    ]

    insert_value = session.scalars(insert(Brand).returning(Brand), insert_brand)
    result = insert_value.all()
    print(result)

    session.commit()


def load_table_city(name_city):

    insert_city = [
        {'name': name_city},
    ]

    insert_value = session.scalars(insert(City).returning(City), insert_city)
    result = insert_value.all()
    print(result)

    session.commit()


def load_table_section(name_section):

    insert_section = [
        {'name': name_section},
    ]

    insert_value = session.scalars(insert(Section).returning(Section), insert_section)
    result = insert_value.all()
    print(result)

    session.commit()


def load_database_description_product_card(data_from_locality, brand_id, city_id):

    section_id = 1

    for section, elements in data_from_locality.items():
        # section_id = definition_section_id(section)
        print(section_id, section)
        # print(section_id, section, len(elements))
        for product_card in elements:
            name = product_card.get('name')
            description = product_card.get('description')
            new_price = product_card.get('new_price')
            new_price = int_price(new_price)
            old_price = product_card.get('old_price')
            old_price = int_price(old_price)

            insert_product_card = [
                {'name': name,
                 'description': description,
                 'new_price': new_price,
                 'old_price': old_price,
                 'brand_id': brand_id,
                 'city_id': city_id,
                 'section_id': section_id},
            ]

            insert_value = session.scalars(insert(Product).returning(Product), insert_product_card)
            result = insert_value.all()
            print(result)

        section_id += 1

    session.commit()


session.close()
