from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, SmallInteger
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# relationship, Mapped # новая штука наверное как создавать таблицы в sqlalchemy
# from typing import List

from dotenv import load_dotenv, dotenv_values


# Создаём базовый класс для наших моделей
class Base(DeclarativeBase):
    pass


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String(15), unique=True)

    # products = relationship('Product', back_populates='brand')

    def __repr__(self):
        return f'Brand id={self.id}, name={self.name}'


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True) # поменять на смолл инт
    name = Column(String(15), unique=True)

    # product = relationship('Product', back_populates='city')

    def __repr__(self):
        return f'City id={self.id}, name={self.name}'


class Section(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    # product = relationship('Product', back_populates='section')

    def __repr__(self):
        return f'Brand(id={self.id}, name={self.name}'


# class Unit(Base):
#     __tablename__ = 'unit'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(15), unique=True)
#
#     def __repr__(self):
#         return f'Brand(id={self.id}, name={self.name}'


class Product(Base):
    __tablename__ = 'product_dodo_pizza'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))
    new_price = Column(SmallInteger)
    old_price = Column(SmallInteger)
    brand_id = Column(Integer, ForeignKey('brand.id'))  # сериал2
    city_id = Column(Integer, ForeignKey('city.id'))  # сериал2
    section_id = Column(Integer, ForeignKey('section.id')) # сериал2

    # children: Mapped[List["Child"]] = relationship(back_populates="parent")

    # city: Mapped[List['City']] = relationship(back_populates='product_dodo_pizza')
    # brand: Mapped[List['Brand']] = relationship(back_populates='product_dodo_pizza')
    # section: Mapped[List['Section']] = relationship(back_populates='product_dodo_pizza')

    # city = relationship('City', back_populates='product_dodo_pizza')
    # brand = relationship('Brand', back_populates='product_dodo_pizza')
    # section = relationship('Section', back_populates='product_dodo_pizza')

    def __repr__(self):
        return f'Product(id={self.id}, name={self.name}, description={self.description}, new_price={self.new_price}'


config = dotenv_values(".env")

USERNAME = config.get('USERNAME')
PASSWORD = config.get('PASSWORD')
HOST = config.get('HOST')
PORT = config.get('PORT')
DATABASE = config.get('DATABASE')


# Создаем подключение к базе данных PostgreSQL
engine = create_engine(
    f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
)

# Создаём таблицы
Base.metadata.create_all(engine)

# Создаём сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()
